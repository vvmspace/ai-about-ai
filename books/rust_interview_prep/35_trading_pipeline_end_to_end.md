# Trading Pipeline End-to-End

Whenever interviewers ask me to design a trading system, I start with one sentence.
Orders are promises with a deadline.
Miss the deadline, and the promise is worth less.

So I walk the pipeline end to end, with latency budget in hand.

Signal enters from strategy.
I validate schema and timestamp immediately.
Anything malformed is rejected early, with explicit reason.
This keeps corrupted intent out of the hot path.

Next comes risk.
Pre-trade checks must be deterministic and fast: limits, exposure, symbol state, account permissions.
I keep risk state local or near-local for speed, with controlled refresh from authoritative sources.
If risk lookup depends on a fragile remote call, I treat that as architectural debt.

Then routing.
I choose venue using current market state and policy.
The routing decision is logged with structured context so post-trade analysis is possible.
I avoid expensive allocations and unnecessary copies in this stage; jitter here becomes expensive quickly.

Execution feedback returns asynchronously.
I correlate acknowledgements, fills, rejects, and cancels by stable order IDs.
State transitions are modeled with enums to prevent impossible combinations.
If duplicate messages appear, idempotent handlers keep state coherent.

Finally, UI propagation.
Traders need fast, trustworthy updates, not noisy chatter.
I publish concise event envelopes to frontend services, then fan out to Next.js clients via streaming or websocket channels.
Critical updates are prioritised; analytical enrichments may lag without harming decisions.

When I explain latency budget, I split p99 targets by stage.
For example: risk 20%, routing 25%, exchange/IO 35%, internal fan-out 20%.
Numbers vary by system, but budget ownership must be explicit.
If one stage overruns, everyone sees where and why.

Interviewers often ask about resilience.
I describe bounded queues, load-shedding policy for non-critical streams, replay capability for recovery, and clear incident ownership.
That shows I do not confuse “works in staging” with “safe in production”.

This chapter extends [Architecture Interview: Drawing Under Pressure](./34_architecture_interview_drawing_under_pressure.md) and sets up design conversations around SQL and frontend boundaries in the next rounds.
End-to-end thinking is what turns isolated competence into hiring confidence.

In trading infrastructure, elegance is not decorative.
It is the discipline of making every millisecond accountable.
