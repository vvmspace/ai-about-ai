# Lock-Free and Low-Contention Patterns

I once watched a team replace every lock with atomics and call it progress.
Throughput improved in one benchmark.
Operational clarity collapsed everywhere else.
A memorable trade.

Lock-free is not a badge of honour.
It is a precision tool with a strict invoice attached.
If I cannot explain invariants clearly, I do not deploy cleverness to the hot path.

In interviews, I begin with intent.
The goal is usually lower contention and better tail latency, not ideological purity.
Sometimes a well-scoped lock wins.
Sometimes ownership transfer and batching win by a mile.

Low-contention patterns I trust first:
- shard mutable state by key;
- use single-writer components where possible;
- transfer ownership through channels instead of sharing mutable structures;
- reduce coordination frequency with micro-batching.

When atomics are justified, I keep usage narrow and explicit.
Counters, flags, sequence numbers.
Not sprawling state machines built on optimism.
Memory ordering choices are part of the design, not decoration.

Interviewers often ask, “Would you go lock-free here?”
My answer is cautious.
Only if contention metrics prove locks are the dominant bottleneck, invariants are tractable, and we can test concurrency behaviour under stress.

A practical bridge from [Locking, Contention, and Throughput](./25_locking_contention_and_throughput.md):
start with measurable lock contention,
then decide whether to shrink lock scope, shard, queue, or selectively introduce lock-free primitives.

I also mention ring buffers in producer-consumer scenarios.
They can reduce allocation churn and coordination overhead when workload shape is stable.
But capacity policy and overflow behaviour must be explicit.
Silent overwrite is still failure, simply quieter.

For the avoidance of doubt, “lock-free” does not mean “bug-free.”
It means you moved correctness burden into more subtle territory.
If you step there, step carefully.

Low contention is a business outcome.
The mechanism is negotiable.
The discipline is not.
