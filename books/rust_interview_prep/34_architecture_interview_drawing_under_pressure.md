# Architecture Interview: Drawing Under Pressure

Whiteboards are curious instruments.
They pretend to test diagrams, but they mostly test how I think when the room goes quiet.

Early in my career, I drew boxes too quickly.
The interviewer nodded, then asked where latency budget was spent and how failures were isolated.
That was the moment I understood their game.

Now I follow a strict sequence.
Let’s keep this elegant.

1. Confirm requirements before drawing components.
   I ask for throughput targets, p99 expectations, durability needs, and failure tolerance.
2. Name bottlenecks and critical path explicitly.
   I mark where time is spent, where contention appears, and where queues can explode.
3. Draw minimal architecture first.
   Ingestion, processing, storage, API/UI fan-out.
   Nothing ornamental.
4. Add failure handling and observability.
   Retries, idempotency, timeouts, metrics, alerts, rollback path.
5. Discuss trade-offs and evolution plan.
   What I would ship now, and what I would improve after first production data.

I narrate while drawing.
Silence makes interviewers guess my intent.
Reasoned narration makes trade-offs visible.
If I choose bounded channels, I say why.
If I avoid distributed transactions, I explain the compensation model.

For this specific role, I keep both Rust backend and Next.js frontend in scope.
I describe how execution events become stable API contracts for trading UI.
I separate hot execution flow from analytics paths so noisy workloads do not contaminate latency-critical lanes.

A popular trap is premature detail.
Nobody needs ten database tables in minute three.
They need to see judgment.
So I provide enough depth to prove competence, then wait for prompts.

If challenged, I stay composed.
A curious question is not an attack; it is an invitation to reveal model quality.
I restate constraints, adjust design, and keep moving.

This chapter connects directly to [Production Readiness Checklist](./33_production_readiness_checklist.md) and leads naturally into [Trading Pipeline End-to-End](./35_trading_pipeline_end_to_end.md).
A diagram is only persuasive when it survives operational reality.

Under pressure, architecture is less about drawing beautifully.
It is about thinking in public without losing control.
