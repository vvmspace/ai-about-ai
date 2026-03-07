# Locking, Contention, and Throughput

I once reviewed a service that looked perfectly thread-safe and performed like wet cement.
No data races.
Plenty of latency spikes.
The culprit was ordinary: lock contention in the hot path.

Locks are not bad.
Unexamined lock scope is bad.
I keep this distinction precise in interviews.

When I introduce a lock, I ask:
- what data truly requires mutual exclusion;
- how many threads compete for it;
- how long the critical section can run.

If I cannot answer quickly, I am probably locking too much.

`Mutex` is simple and often correct.
`RwLock` can help read-heavy workloads, but write starvation and coordination overhead are real.
I do not promise miracles.
I promise measurements.

My default throughput tactics are practical:
- shrink critical sections;
- move expensive work outside lock guards;
- shard state by key where contention is systematic;
- prefer ownership transfer to shared mutation when architecture allows.

A classic mistake in async code is holding a lock across `.await`.
That can deadlock progress or amplify tail latency.
I call it out early and redesign boundaries.

In interview rounds, I narrate contention detection as an observability problem.
I want lock wait-time metrics, queue depth, and stage latency distributions.
Without these, optimisation is guesswork in a respectable jacket.

If asked for a concise heuristic, I give one.
Correctness first.
Then minimise time spent inside shared mutable territory.
Then verify with p99 outcomes.

This chapter pairs naturally with [Channels and Backpressure](./24_channels_and_backpressure.md): when contention dominates, rethinking coordination model is often better than micro-optimising lock usage.

Locking is a tool, not a personality.
Use it where the invariants demand it.
And keep the contested space as small as professional pride allows.
