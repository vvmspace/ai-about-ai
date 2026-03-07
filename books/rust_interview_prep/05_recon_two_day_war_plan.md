# Two-Day War Plan

With less than two days, preparation is no longer a study programme.
It is an operation with timing, scope, and acceptable risk.
I plan it the way I would plan a production migration: clear objectives, bounded tasks, and checkpoints.

I use six blocks across two days.
No block exceeds three hours without a break, because cognitive quality collapses before ambition does.

## Day 1 — Build Technical Control

### Block 1 (2h): Rust Core Refresh
I review ownership, borrowing, `Result`/`Option`, pattern matching, traits, and collections.
Not by passive reading.
I write short snippets and explain each decision aloud.
Goal: remove hesitation in fundamentals.

### Block 2 (2.5h): Async and Concurrency Reality
I focus on Tokio mental model, channels, task cancellation, lock scope, and backpressure.
I compare two small designs: shared state with locks vs message-passing pipeline.
Goal: answer architecture questions with trade-off language, not slogans.

### Block 3 (2h): Performance and Observability
I rehearse profiling logic: establish baseline, locate hotspot, change one variable, re-measure.
I prepare crisp definitions for throughput, latency, p99, jitter, and contention.
Goal: sound like someone who measures before he optimises.

## Day 2 — Convert Knowledge Into Interview Output

### Block 4 (2h): CV Cross-Examination
I run through every major CV bullet.
For each, I speak one 90-second answer with metric, technical detail, and lesson.
Goal: eliminate vague narratives.

### Block 5 (2h): Full-Stack Scenarios
I practise questions that bridge backend and trading UI:
- market data bursts and UI consistency;
- degraded backend modes and frontend fallbacks;
- API design choices affecting user trust.
Goal: prove cross-stack ownership.

### Block 6 (2h): Mock Interview and Recovery Drills
I simulate pressure: rapid technical questions, one system design prompt, one behavioural round.
I deliberately include questions I may not answer perfectly.
Goal: maintain composure and structured reasoning under uncertainty.

Between blocks, I keep short resets:
- 10 minutes walk;
- zero doom-scrolling;
- quick note of what improved and what remains risky.

I also keep a “last-mile” sheet for interview day:
- 12 Rust truths I can explain cleanly;
- 5 CV stories with metrics;
- 6 questions to ask interviewer about latency budget, incident ownership, and success criteria;
- 3 phrases for honest uncertainty.

Example phrase: “I haven’t used that exact approach in production, so I’d validate it in stages: correctness, load profile, then latency impact.”

The plan looks strict because it is.
Pressure rewards structure.

By the final evening, I do not aim to feel invincible.
I aim to feel prepared, bounded, and dangerous in the right places.
That is more than enough.
In interview operations, elegant discipline beats heroic improvisation.
