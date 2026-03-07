# Reading the Terrain, Not the Brochure

Whenever I read a job description, I assume two documents exist.
The first is the one written for candidates.
The second, invisible one, is written by production incidents.
My task is to reconstruct the second.

On paper, this role sounded broad: strategy to processing to network to order execution to trading UI.
Many candidates read that and think, “impressive scope.”
I read it and think, “they have coupling risk and they need an adult in the room.”

So I translated every headline into operational meaning.

“High market data throughput” means queues, backpressure, bounded memory growth, and data-shape discipline.

“Deterministic behaviour under burst load” means no hand-wavy concurrency, no accidental lock amplification, and very careful scheduling assumptions.

“Minimise latency and latency variability” means p99 and p999 thinking, not average latency theatre.

“Stable under real production pressure” means incident ownership, rollback judgement, and boring recovery paths.

By the time I finished annotation, I had a competency matrix with four columns:
- what they say;
- what it really means technically;
- what proof I can provide from experience;
- what gap I must close before interview day.

This is where most preparation either sharpens or collapses.
If I leave statements unparsed, I prepare abstractly.
If I decode them into failure modes, I prepare for the actual conversation.

I also map the *question archetypes* each line will generate.
For example, if they mention Tokio and concurrent architecture, I should expect at least one of these:
- explain task scheduling and cooperative yielding;
- compare channel-based design with shared mutable state;
- describe a contention bug I found and how I proved the fix.

Likewise for frontend.
If the role includes trading-facing Next.js applications, I should be able to discuss:
- UI consistency under real-time updates;
- safe polling vs websocket stream handling;
- preserving responsiveness while high-frequency data arrives.

The elegant part is that this analysis reduces anxiety.
Ambiguity causes panic.
Structure creates control.

I then write three interview theses I want them to remember:
1. I make performance claims only with measurements.
2. I design for predictability first, then speed.
3. I can own the whole path, including user-facing consequences.

Those theses become a filter.
Every story from my CV, every technical explanation, every answer to “tell me about yourself” should reinforce at least one of them.

Naturally, I do not recite these lines like a slogan.
I demonstrate them through examples, trade-offs, and post-mortem style clarity.

There is a pleasant side effect.
When I read the terrain properly, I stop trying to look impressive in general.
I start looking specifically useful for their risks.

And interviews tend to reward that precision.
Brochures attract applicants.
Terrain selects operators.
