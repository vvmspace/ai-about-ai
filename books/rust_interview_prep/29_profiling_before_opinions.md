# Profiling Before Opinions

The most expensive sentence in performance work is, “I think the bottleneck is…”
Sometimes it is correct.
Often it is merely confident.

In interviews, I state my rule early.
No optimisation without evidence.
No architectural rewrite without baseline metrics.
Opinion may start the search.
Measurement ends the argument.

My profiling loop is disciplined:
- define workload and success metric;
- capture baseline (throughput, p95/p99, CPU, allocation rate);
- isolate hotspot with profiler traces;
- change one variable at a time;
- rerun under comparable load;
- keep or revert based on data.

This sounds obvious.
Under deadline pressure, teams skip half of it.
Then they optimise symptoms.

I also separate micro and macro evidence.
A microbenchmark can validate a local improvement.
Only end-to-end measurement proves user-visible impact.
Interviewers usually appreciate that distinction.

When asked about tools, I avoid fan club behaviour.
Flamegraphs, tracing spans, allocator stats, and runtime metrics are all useful.
Tool choice is secondary to method quality.

A small interview phrase that works well:
“I’d like to see where wall time accumulates before selecting an optimisation strategy.”
It signals patience and control.

This chapter naturally extends [Networking on the Hot Path](./28_networking_on_the_hot_path.md): once network, parsing, and queueing are separated in traces, tuning decisions become far less theatrical.

If you optimise before profiling, you may improve code and worsen the system.
If you profile first, you may fix less code and improve the business metric.
I prefer the second arrangement.
