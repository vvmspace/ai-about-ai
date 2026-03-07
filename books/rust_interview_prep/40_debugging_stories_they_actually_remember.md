# Debugging Stories They Actually Remember

Every interview eventually reaches the same polite trap.
“Tell me about a difficult bug.”
Most candidates answer with drama.
I answer with structure.

A memorable debugging story is not a confession.
It is evidence of judgment under uncertainty.
Interviewers are not collecting entertainment.
They are measuring how I think when the map is wrong.

I use a five-part sequence.
Symptom.
Hypothesis.
Instrumentation.
Fix.
Prevention.
If I keep that order, my story stays clear even when the incident was chaotic.

Let me show the shape I usually present.
Symptom first: traders reported intermittent stale positions during volatile open.
Not all accounts.
Not reproducible on demand.
High consequence, low clarity.

Then hypothesis framing.
I list plausible classes instead of guessing one villain.
Data ingestion lag.
Out-of-order event handling.
Cache invalidation race.
Frontend reconciliation error.
A curious question guided me: where could truth diverge silently?

Instrumentation came next.
We added correlation IDs across ingestion, risk, position service, and websocket fan-out.
We logged sequence numbers and event-time versus process-time deltas.
We exposed a temporary dashboard for stale-window duration by account.
Within hours, the uncertainty field narrowed sharply.

Root cause was inelegant but precise.
Under burst load, one consumer path had retried with exponential backoff and re-emitted older snapshots after newer deltas.
The frontend had applied updates by arrival order, not sequence order.
Two small assumptions had aligned into one expensive lie.

Fix phase was deliberately boring.
We enforced sequence-aware merge logic client-side.
We added monotonic guards server-side to reject stale replays on critical channels.
We reduced retry jitter range and separated recovery traffic from live delta streams.
Latency barely changed.
Correctness improved immediately.

Prevention is where stories become senior.
We wrote integration tests for out-of-order replay.
We added alerts on sequence regressions.
We documented event ordering guarantees in the API contract.
And we updated incident runbooks so first responders could detect the pattern in minutes, not hours.

When I tell this story, I also state what I had missed initially.
I had trusted arrival order because the system had behaved in calm markets.
Calm markets are generous teachers and terrible validators.
That admission signals honesty without surrendering competence.

Interviewers sometimes ask what I learned personally.
I keep it simple.
I learned to instrument before arguing.
I learned to separate hypotheses from identity.
And I learned that cross-stack bugs do not respect team boundaries.

For CV defense, this format scales.
Pick any project line.
Attach one incident.
Show diagnosis mechanics, trade-offs, and preventive controls.
Suddenly your experience sounds lived, not rehearsed.

If pressed for another example, I keep a shorter backup.
A database plan regression that appeared only after quarterly data rollover.
Symptoms looked like network jitter.
`EXPLAIN ANALYZE` said otherwise.
Index reshaping and partition pruning solved it.
Lesson repeated: measure first, narrate second.

This chapter follows [Testing Strategy Across the Stack](./39_testing_strategy_across_the_stack.md) and closes Act IV with operational credibility.
In interviews, brilliant answers are pleasant.
Controlled debugging stories are persuasive.
