# Channels and Backpressure

The easiest way to crash a fast system is success.
Input grows, dashboards glow, and somewhere a queue becomes a denial letter written in memory.
I had seen that script before.

Channels are excellent for decoupling producers and consumers.
But decoupling without flow control is optimism, not engineering.
Backpressure is the policy that keeps optimism solvent.

In interview designs, I state queue policy early.
Unbounded by default is rarely acceptable on market-data paths.
Bounded queues force explicit decisions when load exceeds capacity.
That discomfort is healthy.

When the queue is full, only four honest options exist:
- block producer;
- drop newest;
- drop oldest;
- shed upstream load with signalling.

Each option has business consequences.
Trading systems do not get to pretend otherwise.

I often choose bounded `mpsc` channels with instrumented depth and drop counters.
Then I explain behaviour under burst load in plain language.
“If consumers lag, we either apply controlled shedding or slow producers according to policy.”

Interviewers appreciate explicit failure semantics.
They distrust queues described as “it should be fine.”
Rightly so.

I also avoid hidden multi-hop pipelines where ownership and ordering guarantees become unclear.
If I need multiple stages, I define per-stage SLA and queue limits.
Design clarity beats accidental throughput.

A practical check I use in mocks:
- what is max queue depth per stage?
- what metric triggers protective action?
- what action fires first?
- how do we recover normal mode?

If you need conceptual continuity, this chapter extends [Concurrency Mental Models](./21_concurrency_mental_models.md): channels are not merely communication primitives; they are control surfaces for overload.

Backpressure is not pessimism.
It is respect for finite resources.
And systems that respect limits survive their busiest days.
