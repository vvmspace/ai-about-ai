# The Rust Live-Coding Round

The live-coding round is where confidence gets audited.
The editor is shared.
The clock is impolite.
And the borrow checker waits with perfect memory.

I do not walk in trying to look brilliant.
I walk in trying to look reliable.
Brilliance is optional.
Control is not.

My first move is always scope negotiation.
"I’ll start with a correct baseline, then optimize if time allows."
That sentence buys room for trade-offs.
It also signals production instincts.

When the prompt appears, I narrate constraints before writing code.
Input size.
Ordering guarantees.
Error semantics.
Latency sensitivity.
Mutability boundaries.
A curious question can save ten minutes.
"Do we prefer allocation minimization over API ergonomics here?"

Then I sketch structure in comments.
Data model.
Function signatures.
Failure cases.
Tests I would write.
This prevents frantic rewrites.
It also gives the interviewer a map of my reasoning.

In Rust rounds, the common failure is fighting ownership mid-flight.
I avoid that by deciding ownership at boundaries.
Who owns the buffer?
Who borrows slices?
Where do we clone intentionally?
If I cannot answer those early, I simplify design.

I prefer plain types first.
`Vec`, `HashMap`, `Result`, enums.
No decorative abstractions.
Interview code is not a framework launch.
It is a proof of judgment.

When the compiler protests, I stay calm and read the message aloud.
Not performatively.
Operationally.
"We moved `order`, then attempted to borrow `order.id` in the log path."
That shows I can debug under observation.

If stuck on lifetime knots, I use three escapes.
Own the value instead of borrowing.
Split the function to shorten borrow scope.
Replace nested references with indices or IDs.
Purity is lovely.
Shipping is lovelier.

I also mark optimization hooks without prematurely optimizing.
"This clone is intentional for clarity; in production I’d benchmark an arena-backed variant."
Interviewers care that I see the cost model.
They do not require micro-optimizing toy input on minute twelve.

Testing during live coding is a force multiplier.
I add one happy-path case.
One edge case.
One failure case.
Even pseudo-tests, stated clearly, demonstrate completeness.
In this role, deterministic behavior under burst load matters as much as syntax.

Sometimes they ask for async in the same round.
I keep it elegant.
Bounded channel.
Explicit cancellation path.
Timeout with decision.
No hidden unbounded queues.
I reference the backpressure patterns from [Channels and Backpressure](./24_channels_and_backpressure.md).

If time runs short, I do not panic-polish.
I summarize.
What works now.
What invariants are enforced.
What I would improve next with measurement.
A clean partial solution beats a chaotic near-complete one.

The last minute matters disproportionately.
I restate trade-offs in plain language.
"I prioritized correctness and ownership clarity; next step is reducing allocation churn on the hot loop."
Now they can remember my reasoning, not just my typos.

Live coding in Rust is not a duel with syntax.
It is a demonstration that I can make careful decisions while being watched.
Once I accepted that, the round became quite manageable.
