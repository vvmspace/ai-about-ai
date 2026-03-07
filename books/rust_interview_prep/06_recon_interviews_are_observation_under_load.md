# Interviews Are Observation Under Load

I used to think interviews were about answers.
Then I watched a panel ignore a correct answer because the candidate had delivered it like a man escaping a fire.
That was the moment I understood the game.
They were not testing memory.
They were testing behaviour under controlled pressure.

A production system is judged in peak traffic, not idle mode.
Interviewers do the same with engineers.
They add uncertainty, shorten time, and watch whether your reasoning remains stable.
Quite manageable, if you prepare for the mechanism rather than the theatre.

My model is simple.
Every question has two channels:
- technical correctness;
- cognitive posture.

Most candidates rehearse channel one.
Strong candidates rehearse both.

Cognitive posture sounds abstract, so I reduce it to observable signals:
- Do I clarify constraints before coding?
- Do I state trade-offs instead of pretending certainty?
- Do I recover cleanly after a mistake?
- Do I keep the conversation structured under interruption?

I use a three-step speaking loop in technical rounds.

First: frame.
“I’ll start with correctness, then optimise for latency once behaviour is deterministic.”

Second: expose reasoning.
“I’m choosing a bounded channel here to enforce backpressure and avoid silent queue growth.”

Third: verify.
“Before we move on, I want to confirm ordering guarantees and failure policy.”

That loop makes panic difficult.
Panic thrives in silence.
Structure kills it.

Before each interview, I run a two-minute composure routine:
- 30 seconds: define the round objective in one line;
- 60 seconds: breathe and slow speech cadence deliberately;
- 30 seconds: rehearse one honest uncertainty phrase.

My preferred uncertainty line is this:
“I haven’t used that exact approach in production, so I’d test it in layers: correctness, throughput, then p99 latency.”

No drama, no bluffing, no collapse.
Just professional control.

When I do get stuck, I narrate the boundary.
“That design creates lock contention on the hot path; I’m stepping back to reduce shared mutable state.”

Interviewers rarely punish temporary blockage.
They punish invisible blockage.

If you remember one thing, keep this: an interview is a simulation of production pressure with polite lighting.
If you stay clear-headed while observed, you are already answering the real question.
And yes, that question arrives before the code does.
