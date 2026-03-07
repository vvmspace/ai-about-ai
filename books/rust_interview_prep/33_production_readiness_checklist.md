# Production Readiness Checklist

I have never seen an interviewer object to a checklist that prevents a 3 a.m. incident.
They tend to object to confidence without controls.
Quite right, too.

When a system sits on the execution path, readiness is not a slogan.
It is a gate.
Either we pass it, or we are rehearsing an outage.

My production-readiness checklist is short enough to remember and strict enough to matter.

First: **observability**.
- structured logs with correlation IDs;
- metrics for throughput, error rate, queue depth, and p95/p99 latency;
- traces across service boundaries for critical requests.

Second: **safety controls**.
- bounded queues and backpressure policy;
- rate limits or admission control for burst defense;
- explicit timeout and retry budgets;
- idempotency for externally visible side effects.

Third: **deployment discipline**.
- canary or phased rollout;
- fast rollback path that has been tested, not imagined;
- feature flags for risky behaviour changes;
- clear owner on call for the release window.

Fourth: **failure drills**.
- dependency timeout simulation;
- queue saturation test;
- partial region or service degradation scenario;
- runbook verification with realistic alerts.

In interviews, I present this as an execution sequence.
Before deploy, validate instrumentation and rollback.
During deploy, watch leading indicators.
After deploy, compare new latency and error profile to baseline.
If drift appears, reverse quickly and investigate soberly.

I also connect this checklist to CV stories.
If I claim I improved reliability by 40%, I can explain what changed in alerting, runbooks, and ownership rituals.
Numbers without operating detail sound decorative.

For the avoidance of doubt, I do not frame production readiness as bureaucracy.
I frame it as latency insurance and decision clarity under stress.
In performance-critical teams, that argument is usually well received.

This chapter closes Act III and prepares the design pressure of [Architecture Interview: Drawing Under Pressure](./34_architecture_interview_drawing_under_pressure.md).
Because the architecture that cannot be operated is not architecture yet.
