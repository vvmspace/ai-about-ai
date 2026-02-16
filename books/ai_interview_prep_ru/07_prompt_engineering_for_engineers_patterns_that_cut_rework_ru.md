# Prompt Engineering для инженеров: паттерны, которые снижают переделки

Большая часть советов по промптам слишком театральна.
В инженерной работе промпты — не поэзия.
Это структурированные task specifications.

Когда промпты слабые, переделка растёт.
Когда промпты точные, цикл review сокращается.

Поэтому я отношусь к промптам как к mini design docs.
Коротко.
С ограничениями.
Проверяемо.

## Базовый формат промпта, который я использую

Я держу одну надёжную структуру:

- Role: кем модель должна выступать.
- Objective: какой результат нам нужен.
- Context: релевантные детали системы.
- Constraints: что нельзя нарушить.
- Output format: в какой форме нужен ответ.
- Acceptance checks: как валидируем успех.

Пример для API-фичи:

```text
Role: Senior NestJS engineer.
Objective: Add endpoint to archive project without deleting data.
Context: Monolith, PostgreSQL, soft-delete pattern already exists for tasks.
Constraints: No breaking API changes, preserve audit trail, update tests only in touched module.
Output: 1) plan, 2) code diff by file, 3) test additions, 4) rollback notes.
Acceptance: endpoint archives project, tasks remain queryable by admin, existing clients unaffected.
```

Это не длинно и не «красиво».
Это просто однозначно.

## Паттерн 1: промпт для bug triage

Когда в продакшене проблема, скорость важна.
Но и качество диагностики тоже.

Мой triage-промпт:

```text
Act as incident reviewer.
Given logs + service code, produce:
1) likely root causes ranked,
2) confidence level,
3) evidence in code/logs,
4) minimal safe fix,
5) one regression test per root cause.
Do not suggest infra changes unless evidence requires it.
```

Почему это работает:
Он заставляет ранжировать гипотезы и подкреплять их evidence.
А не устраивать общее brainstorming.

## Паттерн 2: промпт для feature scaffolding

Я использую это до старта кодинга:

```text
Design implementation skeleton for [feature].
Include module boundaries, data flow, error handling, and test strategy.
Keep architecture aligned with existing patterns.
Flag unknowns explicitly.
```

Это даёт структурированный первый черновик для критики.
Не финальную истину.
Но полезную отправную точку.

## Паттерн 3: промпт для refactor с инвариантами

Рефакторинг ломается, когда инварианты подразумеваются, а не записываются.
Поэтому я фиксирую их явно.

```text
Propose incremental refactor for this file.
Invariants:
- API contract unchanged.
- Error codes unchanged.
- Latency not worse than current baseline.
Return step-by-step commits and how to verify each step.
```

Теперь модель не может «улучшить» поведение случайно и незаметно.

## Паттерн 4: промпт code review с senior-сигналом

```text
Review this diff as principal engineer.
Report issues under: Correctness, Security, Performance, Maintainability, Observability.
For each issue include severity and concrete patch suggestion.
Do not comment on naming/style unless it impacts readability materially.
```

Это практично.
И совпадает с тем, как команды реально ревьюят код.

## Анти-паттерны, которые создают переделку

Я дисциплинированно избегаю следующих вещей:

- Размытых целей (“make it better”). [сделай лучше.]
- Отсутствующих ограничений.
- Мульти-фича промптов без границ.
- Отсутствия формата вывода.
- Отсутствия acceptance criteria.

Если качество промпта падает, энтропия вывода растёт.
Это предсказуемо.

## Практический before/after

Слабый промпт:

“Add caching to improve performance.” [Добавь кеширование для повышения производительности.]

Результат:
Случайный cache-layer, неясная invalidation-логика, высокий риск регрессий.

Сильный промпт:

“Add read-through caching for `GET /projects/:id` only.
Use existing Redis client.
TTL 60s.
Cache key must include tenant ID.
Do not cache 4xx/5xx.
Include invalidation on project update.
Return exact files changed and tests.”
[Добавь read-through кеширование только для `GET /projects/:id`.
Используй существующий Redis client.
TTL 60 секунд.
Cache key должен включать tenant ID.
Не кешируй 4xx/5xx.
Добавь invalidation при обновлении проекта.
Верни точный список изменённых файлов и тестов.]

Результат:
Меньше diff.
Прозрачная invalidation-логика.
Риски удобно ревьюить.

## Шаблон ответа для интервью

Если спрашивают: “How do prompts reduce rework?” [Как промпты уменьшают объём переделок?], я отвечаю так:

“By turning ambiguous requests into constrained execution.
I define objective, boundaries, and acceptance checks up front.
That improves first-pass accuracy and shortens review loops.
The gain is not magical intelligence.
It is structured communication.”
[Преобразуя неоднозначные запросы в исполнение с ограничениями.
Я заранее фиксирую цель, границы и критерии приёмки.
Это повышает точность первого прохода и сокращает циклы ревью.
Выигрыш не в «магическом интеллекте».
Выигрыш в структурированной коммуникации.]

Обычно это хорошо резонирует с engineering leads.


Для соседнего контекста я сначала фиксирую принцип: instruction stacks удерживают сложные задачи в целостности, разделяя intent, constraints и output format, чтобы модель не импровизировала критические допущения.
И переделка падает только тогда, когда промпты связаны с evaluation loops — чёткие проверки, быстрый feedback и коррекция до merge.
Если нужен более глубокий фон, я связываю эту главу с [instruction stacks](../ai_about_ai/03_prompt_engineering_instruction_stacks.md) и [evaluation loops](../ai_about_ai/05_prompt_engineering_evaluation_loops.md): сильный промпт имеет смысл только в паре с устойчивой верификацией.

Английская версия главы: [Prompt Engineering for Engineers: Patterns That Cut Rework](../ai_interview_prep/07_prompt_engineering_for_engineers_patterns_that_cut_rework.md).
