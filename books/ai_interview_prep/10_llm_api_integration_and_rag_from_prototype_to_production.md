# LLM API Integration and RAG: From Prototype to Production

A prototype can impress in a demo and still fail in production by Monday.
I’ve seen that repeatedly.
The missing piece is rarely model quality alone.
It is system discipline.

So I explain LLM integration as an engineering system.
Inputs.
Retrieval.
Generation.
Evaluation.
Guardrails.
Cost control.

If one layer is weak, output quality becomes unstable.

## Model selection: practical, not ideological

I choose models by task profile:

- high-precision reasoning paths,
- high-throughput classification/extraction,
- latency-sensitive user interactions,
- cost-constrained background processing.

I avoid “best model overall” conversations.
There is no such thing in production.
There is only best fit for constraint set.

## RAG pipeline I can defend

My baseline RAG flow is simple:

1. Chunk and normalize source documents.
2. Create embeddings with versioned metadata.
3. Store vectors with source pointers.
4. Retrieve top-k by semantic + optional lexical hybrid.
5. Re-rank where required.
6. Generate answer with citations to retrieved context.

Key point:
If retrieval is weak, generation quality cannot be trusted.

## Chunking and metadata decisions

Most retrieval quality problems begin here.

I keep chunks coherent by idea, not by arbitrary character count.
Then I attach metadata that supports filtering later:

- document source,
- section/topic,
- access scope,
- version timestamp,
- language.

Without metadata, governance and debugging become painful quickly.

## Practical prompt contract for grounded answers

I use strict prompt contracts for production answer generation:

```text
You are an assistant for internal engineering docs.
Answer ONLY from provided context.
If evidence is insufficient, say: "I don't have enough context to answer safely."
Cite source IDs for each claim.
Do not invent APIs, versions, or policies.
```

This sounds strict.
It reduces hallucinated confidence materially.

## Evaluation loop I run before launch

I evaluate RAG systems with a fixed test set.
Not ad-hoc impressions.

My minimal evaluation pack includes:

- answer correctness,
- citation faithfulness,
- retrieval hit rate,
- refusal quality for unknown questions,
- latency and cost per query.

If refusal quality is poor, risk is high.
A wrong confident answer is usually worse than a clear “insufficient context.”

## Scenario: from demo to stable feature

We had a support assistant prototype that looked excellent in controlled demos.
In live usage, quality drifted.

Failures were predictable:

- stale documents remained in vector index,
- no metadata filters for tenant boundaries,
- prompts allowed broad speculative responses,
- no regression benchmark before model updates.

Fix sequence:

1. Add document versioning and re-index policy.
2. Add tenant and access-scope filters at retrieval.
3. Enforce grounded-answer contract with explicit refusal behaviour.
4. Introduce regression suite with weekly score tracking.

Outcome:
Hallucination complaints dropped.
Support trust improved.
Model updates became controlled events, not roulette.

## Cost and latency controls I use

LLM systems fail financially before they fail technically, if unmanaged.
So I include:

- caching for repeated deterministic queries,
- request shaping and token budgets,
- tiered model routing by task criticality,
- async processing for non-interactive tasks,
- cost dashboards per feature flow.

If cost per successful outcome is unknown, the feature is not production-ready.

## Interview answer template

If asked, “How do you productionize RAG?”, I answer:

“I treat it as a retrieval-and-evaluation system, not a prompt trick.
I version content, enforce scoped retrieval, require grounded citations, and benchmark quality before and after changes.
I track latency and cost per successful answer, and I keep refusal behaviour explicit when context is insufficient.”

That usually signals real delivery experience.


For related framing, I state the practical rule directly: strong AI features need a maintained knowledge graph mindset, where sources, relationships, and version history stay explicit as systems evolve.
And meeting-to-memory discipline matters because raw conversation is not usable memory until it is distilled, tagged, and made retrievable with clear ownership.
If useful, I connect this chapter with [personal knowledge graph](../ai_about_ai/16_knowledge_systems_personal_knowledge_graph.md) and [meeting to memory](../ai_about_ai/19_knowledge_systems_meeting_to_memory.md), because durable AI value depends on high-quality memory and traceable retrieval.
