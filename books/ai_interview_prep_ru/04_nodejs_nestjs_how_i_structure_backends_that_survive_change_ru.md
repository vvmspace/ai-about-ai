# Node.js и NestJS: как я строю backend, который переживает изменения

Большинство backend-сбоев — не алгоритмические.
Они структурные.
Сервис работает полгода, требования сдвигаются, и каждое изменение превращается в операцию на открытом сердце.

Поэтому на backend-вопросы в интервью я отвечаю прямо.
Я оптимизирую под изменяемость под давлением.
Не под «красоту» для конференционного слайда.

Моё базовое архитектурное правило простое.
Бизнес-логику держать в domain services.
Транспортные детали — на краю.
Никогда не прятать ключевые правила внутри controllers.

В терминах NestJS это означает:

- Controllers валидируют и оркестрируют поток запроса.
- Services содержат use-case логику.
- Repositories скрывают детали хранилища.
- Events/messages моделируют связь между модулями.

Если эти границы держатся, замена REST на GraphQL или PostgreSQL на другой store — это работа.
Не катастрофа.

## Границы модулей, которые хорошо стареют

Я проектирую модули вокруг бизнес-возможностей.
Не вокруг технических слоёв как самоцели.

Плохое разбиение: `users-controller`, `users-service`, `users-repo` как огромный «мешок всего».
Лучше: `identity`, `billing`, `notifications` — каждый с ясной ответственностью и интерфейсом.

Практичный контракт выглядит так:

```ts
export interface InvoiceService {
  issueInvoice(input: IssueInvoiceInput): Promise<InvoiceResult>;
}
```

Небольшой интерфейс.
Понятный язык.
Никакой утечки транспорта.

## Валидация и обработка ошибок без драмы

Я никогда не доверяю входу на границе.
Валидация должна быть явной и повторяемой.

В NestJS это обычная инженерная дисциплина:

- DTO validation для входящего payload.
- Domain-level guards для бизнес-инвариантов.
- Единое отображение ошибок в HTTP/GraphQL-ответы.

Я избегаю модели “catch everything, return 500.” [ловим всё, возвращаем 500.]
Она уничтожает observability.

Пример дисциплины на границе:

```ts
@Post()
async create(@Body() dto: CreateOrderDto) {
  const result = await this.orderService.create(dto);
  return toOrderResponse(result);
}
```

Если `create` падает, известные domain-ошибки маппятся в понятные статус-коды.
Неизвестные ошибки логируются с correlation ID и трассируются.

## Observability как требование к дизайну

Если я не вижу проблему, я не могу её исправить.
Поэтому observability закладываю с первого дня:

- Structured logs с request ID и correlation ID.
- Метрики latency и error-rate по endpoint/use case.
- Трассировка через async-границы, где это возможно.
- Пороги алертов, привязанные к пользовательским метрикам влияния.

Это делает on-call-разговоры фактическими.
Не эмоциональными.

## REST vs GraphQL: как я это формулирую

Я не идеологичен в этом вопросе.
REST отлично работает для ресурсных API с предсказуемыми путями кеширования.
GraphQL отлично работает, когда клиенту нужна гибкая композиция по множеству сущностей.

Ключевой вопрос — операционная сложность.
GraphQL может снизить over-fetching.
И одновременно может скрыть дорогие resolver-цепочки.
Поэтому если выбираем GraphQL, нужны query cost controls, persisted queries и observability по resolvers.

Именно такой ответ обычно вызывает доверие на интервью.
Сбалансированно.
С опорой на практику.

## Сценарий: production-баг без театра

У нас были периодические сбои в checkout в service mesh.
Не катастрофа.
Но довольно дорого.

Симптомы: шумные timeout и дублированные попытки создать заказ.
Первичная версия обвиняла инфраструктуру.
“That seemed optimistic.” [Это звучало чрезмерно оптимистично.]

Я прошёл поток запроса по correlation ID и нашёл две проблемы.
Первая: retry срабатывал на нескольких слоях без idempotency key.
Вторая: одна downstream-зависимость имела всплески latency без circuit breaker политики.

План исправления:

1. Добавить idempotency key на границе создания заказа.
2. Свести retry-политику в один слой с ограниченным backoff.
3. Ввести timeout budget и правила circuit breaker для нестабильной зависимости.
4. Вывести dashboard-панели, привязанные к checkout success rate и p95 latency.

Результат: дубли заказов исчезли.
Timeout-инциденты заметно снизились.
И главное — будущие сбои стали диагностироваться за минуты.

## Как я объясняю trade-off на интервью

Я использую один паттерн-фразу:

“We chose X because constraint Y mattered more than benefit Z, and we accepted cost C.”
[Мы выбрали X, потому что ограничение Y было важнее преимущества Z, и приняли цену C.]

Пример:

“We kept a modular monolith for the first stage because team size and delivery speed mattered more than independent service scaling, and we accepted tighter deploy coupling until domain boundaries stabilized.”
[На первом этапе мы оставили modular monolith, потому что размер команды и скорость поставки были важнее независимого масштабирования сервисов, и приняли более тесную связку деплоев, пока границы домена не стабилизировались.]

Такой язык показывает владение решением.
А не архитектурный карго-культ.


Для родственного фрейминга я формулирую ядро прямо: один агент редко качественно закрывает архитектуру, реализацию и верификацию на стабильном продакшен-темпе.
И backend остаётся надёжным только когда доступ к инструментам, границы прав и safety-проверки спроектированы как первоклассные ограничения, а не добавлены в конце.
При необходимости я связываю это с [single-agent myth](../ai_about_ai/11_agents_single_agent_myth.md) и [tools, permissions, safety](../ai_about_ai/13_agents_tools_permissions_safety.md): и backend-стабильность, и AI-assisted разработка держатся на явных границах.

Английская версия главы: [Node.js and NestJS: How I Structure Backends That Survive Change](../ai_interview_prep/04_nodejs_nestjs_how_i_structure_backends_that_survive_change.md).
