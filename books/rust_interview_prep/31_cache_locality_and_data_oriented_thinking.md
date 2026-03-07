# Cache Locality and Data-Oriented Thinking

I once watched a candidate explain an elegant O(n) algorithm, then wonder why it still felt slow.
The answer was not in big-O.
It was hiding in cache misses.

In low-latency systems, memory access patterns are often the real plot.
The CPU can execute arithmetic very quickly.
It slows down when data arrives in unpredictable fragments from deeper cache levels or main memory.
That is why two O(n) solutions can have very different latency profiles.

When interviewers ask about optimisation, I mention data layout early.
Quite manageable, if you keep three principles in view:
- keep hot data contiguous;
- reduce pointer chasing;
- separate hot and cold fields.

For market-data paths, I prefer structures that help sequential reads.
A `Vec<Tick>` with compact `Tick` fields often beats scattered heap objects.
If one verbose field is rarely used, I move it out of the hot struct.
I want the common path to fit comfortably in cache lines.

I also discuss *data-oriented design* in plain language.
Instead of modelling objects first, I model access patterns first.
What is read every microsecond?
What is updated occasionally?
What can be batched?
That approach usually reduces both average latency and jitter.

A curious question interviewers like is: “Would you choose struct-of-arrays or array-of-structs?”
My answer is conditional, not doctrinal.
If processing touches one or two fields across many items, struct-of-arrays can be faster.
If processing needs most fields per item, array-of-structs is often clearer and still efficient.
I explain expected access patterns, then choose.

In practice, I validate with measurement.
Locality intuition is useful, but cache behaviour can still surprise.
So I benchmark both layouts under representative bursts, then keep the simpler version unless data says otherwise.

If you want to sound credible in this round, connect layout to outcomes: fewer cache misses, tighter p99, steadier throughput.
Interviewers hear that and realise you are not merely chasing syntax.
You are designing for silicon reality.

The sequence matters: [Benchmark Design That Interviewers Trust](./30_benchmark_design_that_interviewers_trust.md) gives measurement discipline, and [Failure Modes in Real-Time Pipelines](./32_failure_modes_in_real_time_pipelines.md) shows what happens when throughput assumptions collapse.

In this business, performance is not only about clever code.
It is about putting the right bytes in the right place before the clock notices.
