# Memory and Allocation Behavior

I once watched p99 latency rise while CPU looked respectable.
The culprit was not algorithmic complexity.
It was allocation churn hiding inside innocent-looking code.

Rust gives fine control over memory behaviour, but only if I pay attention.
Interviewers in trading roles care because latency variance often starts here.

I keep four facts close.

First, stack versus heap.
Stack allocation is fast and scoped.
Heap allocation is flexible and costly under pressure.
Not evil, simply expensive when overused.

Second, `Vec` growth policy.
A vector that grows unpredictably may trigger reallocations on hot paths.
If I know expected volume, I reserve capacity.
Predictability is a performance feature.

Third, `String` and cloning discipline.
Unnecessary `clone()` calls are frequently hidden latency tax.
Sometimes cloning is the right trade.
Blind cloning is not.

Fourth, allocation visibility.
If I cannot describe where allocations occur, I am optimising in the dark.
I profile before I speculate.

In interviews, I narrate this as an operational loop:
- identify allocation hotspots;
- reduce temporary objects in critical sections;
- preallocate where workload shape is known;
- remeasure percentile latency, not just mean.

A tiny practical move:

```rust
let mut events = Vec::with_capacity(expected_batch);
```

One line, occasionally a meaningful jitter reduction.

I also discuss ownership choices with memory in mind.
Borrowing can avoid copies.
Owned values can simplify boundaries.
The right answer depends on call frequency and contention profile.

If you need conceptual continuity, [Borrowing Without Bleeding](./11_rust_borrowing_without_bleeding.md) explains how to keep references sane while reducing copy pressure.

Interviewers are rarely impressed by dramatic optimisation claims.
They are impressed by controlled, measurable improvements.
Memory work is exactly that: less folklore, more accounting.
And good accounting keeps trading systems honest.
