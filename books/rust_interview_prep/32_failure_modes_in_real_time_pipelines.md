# Failure Modes in Real-Time Pipelines

The most dangerous pipeline is the one that looks healthy right before it fails.
I learned this during a release where dashboards were green, then the queue depth doubled in under a minute.
By the time we had framed the incident, downstream systems had already started timing out.

Interviewers in trading care about this chapter for one reason.
Production does not fail politely.
It fails in combinations.

So I prepare a simple map of likely failure modes:
- upstream burst exceeds processing budget;
- retries amplify load instead of recovering;
- duplicate or out-of-order events corrupt state assumptions;
- one slow dependency causes queue buildup and tail collapse;
- poison messages block forward progress.

When I discuss mitigation, I keep it concrete.
Bound queues.
Explicit backpressure.
Idempotent handlers.
Dead-letter routing for poison payloads.
Timeout budgets that reflect business priority, not optimism.

A common interviewer prompt is: “What would you do when consumers cannot keep up?”
I answer with policy, not panic.
I define drop or degrade rules per message class.
For example, market snapshots may be sampled under pressure, but order acknowledgements are never dropped.
This is what happens next: critical paths get deterministic guarantees; non-critical paths absorb turbulence.

I also mention sequence control.
If ordering matters, I keep partition keys stable and preserve per-key order.
If global order is impossible at scale, I say so directly and design reconciliation logic.
That honesty tends to land well.

Monitoring is part of failure design.
I track queue depth, processing lag, retry rate, timeout rate, and p99 end-to-end latency.
If alerts only trigger after customer impact, the system is not observably safe.

For interview storytelling, I structure one incident clearly: symptom, hypothesis, instrumentation, fix, prevention.
That gives the panel evidence that I can own production-critical systems without melodrama.

This chapter builds on [Channels and Backpressure](./24_channels_and_backpressure.md) and sets up [Production Readiness Checklist](./33_production_readiness_checklist.md).
One teaches control flow.
The other enforces operational discipline.

Real-time engineering is not about pretending failure is rare.
It is about ensuring failure remains bounded when the market is not in a generous mood.
