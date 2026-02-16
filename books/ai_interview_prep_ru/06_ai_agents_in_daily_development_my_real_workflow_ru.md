# AI-агенты в ежедневной разработке: мой реальный workflow

Меня часто спрашивают, «заменяют» ли AI-агенты инженерную работу.
“I’m not convinced.” [Я в этом не убеждён.]
Они убирают low-leverage рутину.
Инженерное суждение остаётся моей ответственностью.

Поэтому я описываю workflow как управляемый конвейер.
Контекст на входе.
Черновик на выходе.
Цикл верификации.
Ship или stop.

Если один этап слабый, деградирует вся система.

## Этап 1: упаковка контекста до промпта

Большинство слабых ответов идут из размытого контекста.
Не из слабой модели.

До запроса кода я даю пять блоков:

1. Цель задачи в одном предложении.
2. Ограничения (stack, style, performance, security).
3. Границы существующего кода (какие файлы/модули трогаем).
4. Acceptance criteria.
5. Non-goals.

Мой практический skeleton промпта:

```text
Goal: Add bulk invite endpoint for workspace admins.
Stack: NestJS, PostgreSQL, Redis queue.
Constraints: Keep existing auth guards, no schema-breaking changes.
Touch only: invites.module.ts, invites.service.ts, invites.controller.ts.
Acceptance: handles CSV up to 5k rows, idempotent by email+workspace.
Non-goals: no UI changes, no new third-party provider.
```

Эта структура сразу снижает drift.

## Этап 2: разделение ролей агентов

Я не использую один чат для всего.
Я разделяю роли, чтобы уменьшить путаницу:

- Architect agent: форма модулей, контракты, стратегия миграции.
- Implementer agent: конкретные изменения в коде.
- Reviewer agent: риски, edge-cases, скан регрессий.
- Test agent: план тестирования и поиск пропущенных сценариев.

На практике это могут быть отдельные сессии или явные role-промпты в одном инструменте.
Принцип тот же.
Разделение повышает качество рассуждений.

## Этап 3: контролируемая генерация и патчинг

Я прошу небольшие, проверяемые дельты.
Не гигантские переписывания.

Плохой запрос: “Refactor this service for performance.” [Сделай рефакторинг сервиса ради производительности.]
Лучший запрос: “Optimize `getWorkspaceMembers` for pagination and N+1 reduction without API contract changes.”
[Оптимизируй `getWorkspaceMembers` под пагинацию и снижение N+1 без изменений API-контракта.]

Моё стандартное правило:
Если размер diff слишком большой, чтобы уверенно проверить за один проход, я делю задачу.
Скорость без review — это театр.

## Этап 4: цикл верификации, который я не пропускаю

AI-вывод — это черновой код.
Никогда не финальный.

Перед merge я прогоняю четыре проверки:

1. Compile/type check.
2. Unit/integration tests для затронутых участков.
3. Static analysis/lint.
4. Ручной проход по edge-cases.

Потом один вопрос:
Что может молча упасть в продакшене?
Если я не могу ответить, работа не закончена.

## Практический пример: bug triage с агентом

Сценарий: периодические дубли уведомлений.

Мой первый промпт:

```text
You are a senior backend reviewer.
Given this service and worker code, identify top 3 causes of duplicate delivery.
Prioritize by production likelihood.
For each cause: evidence in code, minimal fix, regression test idea.
```

Модель предложила три причины.
Верной оказалась только одна.
Это нормально.

Корневой дефект:
Retry-логика существовала и в API-слое, и в queue-consumer без idempotency key.

Что мы выпустили:

- Добавили idempotency key на событие уведомления.
- Сохраняли обработанные ключи с TTL.
- Ввели dedupe в consumer до отправки.

Ценность агента была не в «идеальном диагнозе».
Он ускорил генерацию гипотез.
Истина всё равно оставалась на моей стороне.

## Промпт-паттерны, которые я переиспользую

Для feature scaffolding:

```text
Generate a minimal implementation plan for [feature].
Output:
1) module boundaries,
2) API contract,
3) data model changes,
4) risk list,
5) test plan.
Keep it under 30 lines.
```

Для code review:

```text
Review this diff as staff engineer.
Find correctness, performance, security, and maintainability risks.
Label each issue: Critical / Major / Minor.
Suggest concrete patch snippets only where necessary.
```

Для безопасного refactor:

```text
Propose a no-behavior-change refactor for this file.
List invariants that must hold.
Then provide incremental commits, each with rollback step.
```

## Режимы отказа, за которыми я слежу особенно внимательно

- Переполнение context window и «галлюцинированные» допущения.
- Предложения tool calls без учёта реальной среды.
- Уверенное, но неверное использование API.
- Потеря доменных ограничений в длинных сессиях.

Митигации простые:
Сброс контекста.
Повторная фиксация инвариантов.
Привязка к исходным файлам.
Требование ссылок на конкретные строки кода, когда это возможно.

## Шаблон ответа для интервью

Если спрашивают: “How do you use AI agents daily?” [Как вы ежедневно используете AI-агентов?], я отвечаю прямо:

“I use them as force multipliers, not decision replacements.
I package context, split tasks by role, request small deltas, and run strict verification loops.
They reduce cycle time for drafting and triage.
I keep architecture and production-risk judgement with the engineering team.”
[Я использую их как усилители, а не как замену решений.
Я упаковываю контекст, делю задачи по ролям, прошу небольшие дельты и прогоняю строгие циклы верификации.
Они сокращают цикл черновой разработки и triage.
Архитектурные решения и оценку продакшен-рисков я оставляю за инженерной командой.]

Такой ответ обычно «садится» хорошо.
Он практичный, потому что так и работает.


Для связанной глубины я формулирую ключевую мысль прямо: multi-agent workflow полезен, потому что архитектура, реализация и review требуют разных режимов мышления и не должны сливаться в один неразделённый поток.
И инструкции агенту работают только как execution contracts — scope, ограничения и acceptance criteria должны быть явными до начала генерации.
Если нужен расширенный контекст, это естественно связать с [multi-agent workflows](../ai_about_ai/12_agents_multi_agent_workflows.md) и [agents as execution contracts](../ai_about_ai/26_agentsmd_as_execution_contract.md): надёжность AI-assisted разработки стоит на явных границах и дисциплине верификации.

Английская версия главы: [AI Agents in Daily Development: My Real Workflow](../ai_interview_prep/06_ai_agents_in_daily_development_my_real_workflow.md).
