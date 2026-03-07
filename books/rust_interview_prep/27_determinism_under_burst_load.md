# Determinism Under Burst Load

Calm systems are easy to design at 10% load.
Interviews about trading infrastructure are not about 10% load.
They are about what happens when the market behaves badly and your service must remain polite.

Determinism under burst means two things.
First, bounded behaviour when input spikes.
Second, predictable policy when capacity is exceeded.
Without both, latency charts become fiction.

I define deterministic posture through explicit rules:
- queue limits per stage;
- ordering guarantees per message type;
- timeout and retry boundaries;
- load-shedding policy with clear precedence.

If these are implicit, they will be inconsistent.
If they are inconsistent, incidents will choose the policy for you.

In interviews, I narrate burst handling as a sequence:
1. detect pressure early via queue depth and lag metrics;
2. preserve critical flows first;
3. shed or defer non-critical work;
4. recover gradually to avoid oscillation.

A common mistake is treating all messages equally.
I’m not convinced that helps.
Market data snapshots, heartbeats, and execution acknowledgements have different business value.
The system should admit that truth in code.

I also defend bounded work per tick.
Unbounded loops may maximise short-term throughput while destroying latency predictability.
In production trading systems, predictability usually outranks peak vanity metrics.

This chapter connects naturally to [Channels and Backpressure](./24_channels_and_backpressure.md).
Backpressure gives the mechanism.
Determinism gives the policy objective.

If asked for one interview line, I use this:
“I optimise for controlled degradation before I optimise for perfect throughput.”

Burst load is where architecture reveals character.
Design your rules in advance, and the system behaves like a professional.
Leave them vague, and panic becomes your runtime.
