# Интеграция LLM API и RAG: от прототипа к продакшену

Прототип может впечатлить на демо и провалиться в продакшене уже к понедельнику.
Я видел это не раз.
Проблема редко только в качестве модели.
Проблема в системной дисциплине.

Поэтому я объясняю LLM-интеграцию как инженерную систему.
Inputs.
Retrieval.
Generation.
Evaluation.
Guardrails.
Cost control.

Если один слой слаб, качество ответа становится нестабильным.

## Выбор модели: практично, а не идеологично

Я выбираю модели по профилю задачи:

- пути, где нужна high-precision логика,
- high-throughput классификация/извлечение,
- latency-чувствительные пользовательские взаимодействия,
- cost-constrained фоновые процессы.

Я избегаю разговоров о “best model overall.” [лучшей модели вообще.]
В продакшене такого нет.
Есть только best fit под набор ограничений.

## RAG-конвейер, который я могу защитить

Мой базовый RAG-поток простой:

1. Chunk и normalize исходные документы.
2. Создать embeddings с versioned metadata.
3. Сохранить vectors с source pointers.
4. Достать top-k через semantic + опционально lexical hybrid.
5. Re-rank, где это требуется.
6. Сгенерировать ответ с citations на извлечённый контекст.

Ключевая мысль:
Если retrieval слаб, качеству generation доверять нельзя.

## Решения по chunking и metadata

Большинство проблем retrieval-качества начинается именно здесь.

Я держу chunk-и цельными по идее, а не по случайному числу символов.
Потом добавляю metadata, которая нужна для фильтрации:

- источник документа,
- секция/тема,
- access scope,
- version timestamp,
- язык.

Без metadata governance и debugging очень быстро становятся болезненными.

## Практический prompt-contract для grounded answers

Для продакшен-генерации ответов я использую строгие prompt-контракты:

```text
You are an assistant for internal engineering docs.
Answer ONLY from provided context.
If evidence is insufficient, say: "I don't have enough context to answer safely."
Cite source IDs for each claim.
Do not invent APIs, versions, or policies.
```

Звучит строго.
Материально снижает hallucinated confidence.

## Evaluation loop перед запуском

RAG-систему я оцениваю на фиксированном тест-сете.
Не на разрозненных впечатлениях.

Минимальный evaluation pack включает:

- answer correctness,
- citation faithfulness,
- retrieval hit rate,
- качество отказа на неизвестных вопросах,
- latency и cost на запрос.

Если качество отказа слабое, риск высокий.
Неправильный уверенный ответ обычно хуже, чем ясное “insufficient context.” [недостаточно контекста.]

## Сценарий: от демо к стабильной фиче

У нас был прототип support-assistant, который выглядел отлично в контролируемых демо.
В живом использовании качество «поплыло».

Сбои были предсказуемы:

- устаревшие документы оставались в vector index,
- не было metadata filters для tenant boundaries,
- промпты позволяли слишком широкие спекулятивные ответы,
- отсутствовал regression benchmark перед model updates.

Последовательность исправлений:

1. Добавили document versioning и политику re-index.
2. Добавили tenant и access-scope фильтры на retrieval.
3. Зафиксировали grounded-answer contract с явным refusal behaviour.
4. Ввели regression suite с еженедельным score-tracking.

Результат:
Жалобы на hallucinations снизились.
Доверие поддержки выросло.
Обновления модели стали контролируемыми событиями, а не рулеткой.

## Контроль cost и latency, который я использую

LLM-системы, если их не контролировать, финансово падают раньше, чем технически.
Поэтому я включаю:

- cache для повторяющихся детерминированных запросов,
- request shaping и token budgets,
- tiered model routing по критичности задачи,
- async processing для неинтерактивных задач,
- cost-dashboards по каждому feature-flow.

Если неизвестна стоимость успешного результата, фича не готова к продакшену.

## Шаблон ответа для интервью

Если спрашивают: “How do you productionize RAG?” [Как вы выводите RAG в продакшен?], я отвечаю:

“I treat it as a retrieval-and-evaluation system, not a prompt trick.
I version content, enforce scoped retrieval, require grounded citations, and benchmark quality before and after changes.
I track latency and cost per successful answer, and I keep refusal behaviour explicit when context is insufficient.”
[Я рассматриваю это как retrieval-and-evaluation систему, а не как трюк с промптом.
Я версионирую контент, требую scoped retrieval, grounded citations и сравниваю качество до/после изменений.
Я отслеживаю latency и cost на успешный ответ и делаю refusal behaviour явным, когда контекста недостаточно.]

Такой ответ обычно сигнализирует реальный delivery-опыт.


Для родственного фрейминга я формулирую практическое правило прямо: сильные AI-фичи требуют мышления maintained knowledge graph, где источники, связи и версия остаются явными по мере эволюции системы.
И дисциплина «meeting-to-memory» критична, потому что сырая беседа не становится памятью, пока она не дистиллирована, не размечена и не сделана извлекаемой с ясным ownership.
Если полезно, связываю эту главу с [personal knowledge graph](../ai_about_ai/16_knowledge_systems_personal_knowledge_graph.md) и [meeting to memory](../ai_about_ai/19_knowledge_systems_meeting_to_memory.md): устойчивая AI-ценность зависит от качественной памяти и трассируемого retrieval.

Английская версия главы: [LLM API Integration and RAG: From Prototype to Production](../ai_interview_prep/10_llm_api_integration_and_rag_from_prototype_to_production.md).
