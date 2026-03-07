# Concurrency Mental Models

The interview question sounded innocent: “How would you process market data concurrently?”
I had seen that line before.
It never asks for syntax first.
It asks whether your mental model collapses under load.

Concurrency decisions are architecture decisions with latency consequences.
If I confuse concurrency with parallelism, I design noise.
If I separate them, I design control.

My baseline map has four tools:
- threads for OS-level parallel execution;
- async tasks for high-concurrency I/O workflows;
- message passing for ownership transfer;
- shared state for truly shared mutable data.

I do not treat these as rival religions.
They are trade-offs.
Question first, mechanism second.

In a trading path, I usually begin with pipeline thinking.
Ingest, normalise, risk-check, route, confirm.
Each stage has bounded responsibility.
Ownership moves forward.
Backpressure is explicit.

That style scales reasoning.
It also reduces lock-heavy spaghetti, which is the usual source of performance regret.

When shared state is unavoidable, I ask three blunt questions:
- who writes;
- who reads;
- how long the critical section lives.

If those answers are vague, contention is already scheduled.

Interviewers often probe with, “Channel or lock?”
My answer is operational.
Channels are excellent when ownership transfer and queue policy are primary.
Locks are acceptable when state must remain central and contention is bounded.
I benchmark both where it matters.

I also narrate failure modes early.
What happens when producers outrun consumers?
What happens when one stage stalls?
If I cannot answer those, the design is decorative.

For continuity with earlier chapters, this builds directly on [Smart Pointers in the Real World](./18_rust_smart_pointers_in_the_real_world.md): shared ownership primitives are only half the story; workload shape decides the rest.

Concurrency is not about looking sophisticated.
It is about preserving determinism while work arrives faster than comfort allows.
If your model stays clear under pressure, your system usually does too.
