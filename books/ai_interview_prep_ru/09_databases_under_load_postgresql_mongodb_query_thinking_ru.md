# Базы данных под нагрузкой: PostgreSQL, MongoDB и query-thinking

Интервью по базам данных часто уходит в спор брендов.
Я этого избегаю.
Движок важен.
Поведение запросов важнее.

Поэтому любой ответ по database-дизайну я строю вокруг формы нагрузки.
Read/write ratio.
Требования к consistency.
Latency targets.
Терпимость к отказам.

Если это не определено, выбор технологии в основном гадание.

## Как я выбираю PostgreSQL vs MongoDB на практике

Держу это без лишней романтики.

PostgreSQL — мой дефолт, когда:

- правила целостности данных строгие,
- транзакции центральны,
- join-ы являются нормальной частью продукта,
- отчётность и реляционные запросы будут расти.

MongoDB практична, когда:

- форма документа быстро эволюционирует,
- вложенные агрегаты естественно совпадают с сущностями продукта,
- гибкость записи важнее межсущностных ограничений,
- мы допускаем denormalization с ясным ownership.

“I’m not convinced by ‘one database for everything.’” [Меня не убеждает подход «одна база данных для всего».]
Это упрощает закупку.
Операции обычно не упрощает.

## Query-thinking до споров о схеме

Когда я тюню систему, начинаю с путей запросов.
Не с ER-диаграмм.

Я спрашиваю:

1. Какие запросы критичны для пользователя?
2. Какие запросы выполняются чаще всего?
3. Какие записи дорогие и почему?
4. Для каких access path нужен предсказуемый p95 latency?
5. Какие запросы можно precompute или cache?

Потом индексирую под реальный трафик.
Не под гипотетическую «элегантность».

## PostgreSQL-паттерны, на которые я опираюсь

Несколько привычек многократно окупались:

- Composite indexes, выровненные по порядку фильтров.
- Partial indexes для селективных частых предикатов.
- `EXPLAIN (ANALYZE, BUFFERS)` до и после оптимизации.
- Отказ от `SELECT *` на hot-path.
- Пагинация через keyset, когда стоимость offset растёт.

Пример сдвига:

```sql
-- дорого на масштабе
SELECT * FROM events
WHERE workspace_id = $1
ORDER BY created_at DESC
LIMIT 50 OFFSET 50000;

-- стабильно при росте
SELECT id, type, created_at
FROM events
WHERE workspace_id = $1
  AND created_at < $2
ORDER BY created_at DESC
LIMIT 50;
```

Это не модно.
Это просто удерживает latency стабильным.

## MongoDB-паттерны, которые я внимательно контролирую

Mongo работает очень хорошо, когда дизайн запроса и документа согласован.
Она деградирует, когда мы делаем вид, будто это «неограниченный реляционный store».

Мои рабочие правила:

- Проектировать документы от read-pattern.
- Держать индексы явными и регулярно аудировать.
- Следить за неограниченным ростом массивов.
- Использовать TTL indexes для эфемерных данных, где это уместно.
- Не ставить ad-hoc aggregation pipelines в latency-критичные пути без benchmark.

Если endpoint зависит от огромного aggregation pipeline, для меня это сигнал.
Либо precompute.
Либо cache.
Либо redesign read model.

## Сценарий, который я использую на интервью

У нас был feed endpoint, который выглядел безобидно.
Трафик вырос.
Latency стала «плавать».

Симптомы:

- PostgreSQL p95 вырос в пиковые окна.
- Query plan переключался под нагрузкой.
- API timeout росли при достаточном запасе CPU.

Что нашли:

- Offset pagination на глубоких страницах.
- Non-covering index для доминирующей формы запроса.
- Лишние колонки в выборке, которые UI не использовал.

Последовательность исправлений:

1. Перешли на keyset pagination.
2. Добавили composite index под `workspace_id + created_at`.
3. Оставили в SELECT только нужные поля.
4. Добавили cache для повторных чтений верхних страниц.

Результат:
p95 заметно снизился.
Timeout вернулись к норме.
Нагрузка базы стала предсказуемой.

Компромисс:
Keyset pagination потребовала изменить cursor-handling на клиенте.
Оно того стоило.

## Шаблон ответа для интервью

Если спрашивают: “How do you optimize database performance?” [Как вы оптимизируете производительность базы данных?], я отвечаю:

“I start from workload and critical query paths.
I inspect actual execution plans, then align indexes and query shape.
I reduce payload, remove deep-offset patterns, and cache only where access is repetitive.
Then I measure p95 and error rate before calling the change successful.”
[Я начинаю с нагрузки и критичных путей запросов.
Смотрю реальные execution plans, затем выравниваю индексы и форму запросов.
Уменьшаю payload, убираю глубокие offset-паттерны и кеширую только повторяющиеся access path.
Потом измеряю p95 и error rate, и только после этого считаю изменение успешным.]

Звучит не слишком «гламурно».
Зато деплоебельно.

## Тестирование и observability, которые я всегда добавляю

Изменения в БД без измерений — это сторителлинг.
Поэтому я добавляю:

- Дашборды query-level latency.
- Slow-query logs с пороговыми алертами.
- Regression tests для пагинации и корректности фильтров.
- Снимки load tests до и после индексов/переписывания запросов.

Time.
Cost.
Risk.
Тот же рабочий каркас.


Для соседнего контекста я фиксирую ядро прямо: качество поиска и retrieval зависит от чистой структуры, стабильного именования и предсказуемых access path, а не только от «индексов побольше» или более быстрого железа.
И RAG-системы проваливаются по той же причине, по которой проваливаются многие database-системы — размытый query intent, слабая гигиена данных и не измеренное retrieval-поведение.
Если нужен более глубокий фон, эта глава хорошо сочетается с [searchability and clarity](../ai_about_ai/20_knowledge_systems_searchability_and_clarity.md) и [RAG without fantasy](../ai_about_ai/17_knowledge_systems_rag_without_fantasy.md): и query design, и retrieval quality ломаются, когда пути доступа расплывчаты.

Английская версия главы: [Databases Under Load: PostgreSQL, MongoDB, and Query Thinking](../ai_interview_prep/09_databases_under_load_postgresql_mongodb_query_thinking.md).
