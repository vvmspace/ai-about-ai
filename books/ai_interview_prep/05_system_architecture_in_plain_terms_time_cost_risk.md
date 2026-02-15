# System Architecture in Plain Terms: Time, Cost, Risk

Architecture interviews can become performative quickly.
Big diagrams.
Ambitious vocabulary.
Minimal accountability.

I avoid that game.
I frame architecture as controlled trade-offs under constraints.
Time.
Cost.
Risk.

If I can’t state those three clearly, I’m not designing.
I’m decorating.

My opening move in a system design question is always clarification.

“I’m curious—what matters most for this scenario: latency, reliability, or implementation speed?”

That one question sets the negotiation frame.
And it prevents elegant but irrelevant answers.

## My 7-step architecture response flow

1. Clarify product goal and success metric.
2. Identify primary constraint (scale, latency, compliance, team size).
3. Propose baseline architecture, not final perfection.
4. Mark failure points and bottlenecks.
5. Add observability and recovery paths.
6. Explain trade-offs explicitly.
7. Offer phased evolution path.

Interviewers usually relax when they hear phase-based thinking.
It implies realism.

## Modular monolith vs microservices

I answer this without romance.

A modular monolith is often best when:

- Team is small to medium.
- Domain boundaries are still emerging.
- Fast iteration matters more than independent scaling.
- Operational budget is limited.

Microservices become justified when:

- Distinct domains have different scaling profiles.
- Teams can own services end-to-end.
- Operational maturity supports distributed tracing, resilience, and governance.
- Failure isolation is a business requirement, not a preference.

If we split too early, complexity arrives before value.
If we split too late, coupling taxes growth.
Timing matters.

## Data consistency: practical language

I keep consistency decisions explicit.
For critical money movement, strict consistency is usually non-negotiable.
For analytics dashboards, eventual consistency is often acceptable.

I say this directly in interviews:

“Strong consistency where legal or financial correctness is required.
Eventual consistency where user experience tolerates slight lag and throughput matters more.”

Then I add mechanisms.
Outbox pattern.
Idempotent consumers.
Dead-letter queues.
Replay tooling.

That combination sounds less theoretical and more deployable.

## Scenario: designing a matching platform

Suppose we design an AI-assisted matching system with profile ingestion, embedding generation, and ranked recommendations.

I’d start with a modular monolith plus async pipelines:

- API layer for profile CRUD and search requests.
- Worker pipeline for embedding generation.
- Vector store for semantic retrieval.
- Ranking layer combining vector score and business rules.
- Cache layer for hot recommendation paths.

Failure model:

- Embedding service outage should degrade to lexical search, not full outage.
- Queue lag should trigger alerts before SLA breach.
- Partial profile updates should be idempotent and replayable.

Evolution path:

- Keep ranking and ingestion modules isolated from day one.
- Split into services only when throughput or team ownership requires it.

Trade-off statement:

“We accept temporary coupling now to reduce time-to-market, while preserving extraction seams for future service boundaries.”

That is practical architecture.

## Cost control in AI-heavy systems

This comes up often now.
I answer in operating terms:

- Cache frequent prompts and deterministic responses where possible.
- Use tiered model routing by task criticality.
- Track cost per successful workflow, not cost per API call alone.
- Add evaluation gates before expanding model usage.

In any case, architecture without cost visibility is incomplete.

## Reliability posture I insist on

For the avoidance of doubt, I do not call a system “production-ready” without:

- SLO definitions linked to user-facing outcomes.
- Runbooks for top incidents.
- Rollback or feature-flag strategy.
- Load test evidence for expected peaks.
- On-call ownership model.

That might sound strict.
It prevents avoidable chaos.

## Interview answer template for system design

If time is short, I use this script:

“The goal is X.
The main constraint is Y.
I’d start with Z architecture to optimise time-to-value.
Primary risks are A and B, so I’d add observability and fallback paths first.
If growth hits threshold T, I’d split module M into a service.
That gives us a controlled path from speed to scale.”

Clear.
Defensible.
Operational.

For adjacent framing, this chapter pairs naturally with [RAG without fantasy](../ai_about_ai/17_knowledge_systems_rag_without_fantasy.md) and [searchability and clarity](../ai_about_ai/20_knowledge_systems_searchability_and_clarity.md), because architecture quality is mostly a function of explicit constraints and traceable decisions.
