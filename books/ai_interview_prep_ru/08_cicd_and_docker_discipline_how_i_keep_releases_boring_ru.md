# CI/CD и Docker-дисциплина: как я делаю релизы скучными

Лучший релиз — скучный.
Без героизма.
Без праздничной паники.
Просто предсказуемое исполнение.

Поэтому, когда на интервью спрашивают про CI/CD, я начинаю не с инструментов.
Я начинаю с поведенческой надёжности.

Мой базовый принцип релиза прост.
Каждое изменение должно быть легко валидировать, легко трассировать и легко откатить.
Если чего-то из этого нет, deployment-risk растёт заметно.

## Дизайн pipeline, которому я доверяю

Я держу pipeline явным и поэтапным:

1. Install и cache зависимостей.
2. Lint и type-check.
3. Unit tests.
4. Integration tests для затронутых модулей.
5. Build artifact/container.
6. Security scan зависимостей и образа.
7. Deploy в staging + smoke tests.
8. Контролируемый rollout в production.

Ни один этап не экзотический.
В этом и смысл.
Последовательность сильнее новизны.

## Docker-дисциплина, которая убирает drift

Я использую Docker прежде всего для parity окружений.
Не ради модной сложности.

Мои стандартные правила образов:

- Multi-stage builds.
- Небольшой runtime image.
- Явные версии base images.
- Non-root runtime user.
- Healthcheck endpoint.

Практичный паттерн Dockerfile:

```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./
RUN npm ci --omit=dev
USER node
CMD ["node", "dist/main.js"]
```

Просто.
Воспроизводимо.
Деплоебельно.

## Стратегия rollback, на которой я настаиваю

For the avoidance of doubt, I do not accept “we’ll fix forward” as the only strategy. [Во избежание двусмысленности: я не принимаю «починим вперёд» как единственную стратегию.]
Иногда это работает.
Часто это выдача желаемого за действительное.

Мои базовые варианты отката:

- Blue/green или canary с управлением трафиком.
- Предыдущий artifact сохранён и быстро переиспользуем.
- Feature flags для рискованных путей.
- DB migrations с обратной совместимостью, где это возможно.

Если rollback занимает часы, это не rollback-план.
Это надежда.

## Сценарий: как избежать плохого релиза

У нас был high-risk релиз с изменениями queue processing и billing events.
Исторически такие релизы заканчивались длинными инцидентными звонками.

Я изменил дизайн rollout:

- Добавили contract tests между producer и consumer.
- Добавили canary-release для одного tenant-сегмента.
- Добавили idempotency-проверки в billing events до полного rollout.
- Добавили dashboard-gate: если метрика duplicate-charge растёт, rollout останавливается автоматически.

Итог:
Нет billing-инцидента.
Нет emergency rollback.
И особенно важно: тревожность стейкхолдеров снизилась, потому что прозрачность выросла.

## CI-метрики, по которым я управляю улучшениями

Я еженедельно отслеживаю четыре числа:

- Lead time for changes.
- Deployment frequency.
- Change failure rate.
- Mean time to recovery.

Да, классика DORA.
Потому что именно она показывает, где доставка хрупкая.

Если растёт failure rate — уменьшаю batch size.
Если растёт lead time — ищу bottleneck в approvals и тестах.
Если MTTR высокий — слабые observability или rollback design.

## Шаблон ответа для интервью

Если спрашивают: “How do you keep releases stable?” [Как вы удерживаете стабильность релизов?], я отвечаю:

“I keep pipelines strict and boring.
Every change passes build, tests, and staged rollout gates.
Artifacts are reproducible, containers are minimal, and rollback paths are tested.
I monitor delivery metrics and tune process where risk concentrates.
The goal is not fast deployment alone.
It is fast, reversible, observable deployment.”
[Я держу pipeline строгим и скучным.
Каждое изменение проходит build, тесты и этапные rollout-gates.
Артефакты воспроизводимы, контейнеры минимальны, а пути отката проверены.
Я мониторю метрики поставки и улучшаю процесс там, где концентрируется риск.
Цель не просто быстрый деплой.
Цель — быстрый, обратимый и наблюдаемый деплой.]

Обычно это звучит по-senior, потому что опирается на операционную практику.


Для соседнего чтения я фиксирую две идеи: надёжность релизов растёт, когда команды поставляют маленькими обратимыми партиями, а не крупными рискованными пакетами.
И операционные документы должны быть спроектированы для ясности, чтобы runbooks, шаги rollback и ownership были применимы мгновенно под давлением.
Если полезно, связываю это с [ship small daily](../ai_about_ai/10_vibe_coding_ship_small_daily.md) и [document design for clarity](../ai_about_ai/18_knowledge_systems_document_design.md): качество релизов растёт, когда изменения малы, а операционные предпосылки описаны ясно.

Английская версия главы: [CI/CD and Docker Discipline: How I Keep Releases Boring](../ai_interview_prep/08_cicd_and_docker_discipline_how_i_keep_releases_boring.md).
