# Benchmark Design That Interviewers Trust

Anyone can produce a fast benchmark number.
Producing a trustworthy one is a different profession.
Interviewers in performance-critical roles know the difference instantly.

When I discuss benchmarking, I focus on credibility.
A result is only useful if workload, environment, and interpretation are explicit.
Otherwise we are comparing theatre props.

My benchmark checklist is practical:
- define the question (what decision will this benchmark inform?);
- use representative input distributions;
- include warmup and sufficient sample size;
- control noisy variables where possible;
- report percentile latency, not just average;
- compare against a clear baseline.

Average latency can flatter broken systems.
Tail latency tells the operational truth.
For trading paths, p95 and p99 are often the lines that matter.

I also separate benchmark types in interviews.
Microbenchmarks test local mechanics.
Scenario benchmarks test integrated behaviour.
Load tests reveal failure policy and saturation shape.
Each answers a different question.

A common anti-pattern is benchmark-driven overfitting.
Code gets brilliant at one synthetic case and fragile everywhere else.
I’d advise against it.
Benchmarks should constrain decisions, not replace judgement.

When panelists ask, “How would you prove this optimisation helps?” I answer with structure:
- establish baseline;
- apply minimal change;
- rerun same workload;
- compare percentile improvements and variance;
- verify no regressions in correctness or resource profile.

This chapter follows directly from [Profiling Before Opinions](./29_profiling_before_opinions.md).
Profiling finds candidates.
Benchmark design validates outcomes.

Trustworthy benchmarks do not just show speed.
They show that speed survives scrutiny.
And scrutiny is exactly what interview rooms simulate.
