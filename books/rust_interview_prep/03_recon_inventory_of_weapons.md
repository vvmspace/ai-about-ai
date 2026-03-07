# Inventory of Weapons

I never begin preparation by pretending I am stronger than I am.
That approach feels good for an hour and fails spectacularly in round two.
I prefer an honest inventory.

So I split my skill map into three zones: green, yellow, red.

Green: production backend architecture, distributed services, monitoring discipline, SQL tuning, and pragmatic frontend delivery in Next.js.

Yellow: Rust fluency in interview conditions, especially writing clean code fast while narrating ownership decisions.

Red: edge-case confidence in lifetime-heavy API design and nuanced runtime behaviour under extreme burst scenarios.

This classification is not self-criticism.
It is resource allocation.
If I have less than 48 hours, ego is a luxury item.

I then attach evidence to each green area.
For instance, I can discuss systems where I had improved throughput, reduced instability, or established observability loops with Grafana and Prometheus.
That gives me reliable material for behavioural and systems rounds.

For yellow and red zones, I define conversion goals.
Not “master Rust”.
That is fantasy.
Instead:
- eliminate beginner mistakes in ownership and borrowing explanations;
- practise two or three idiomatic patterns for async pipelines;
- prepare clear language for memory and allocation trade-offs;
- memorise a small set of debugging narratives tied to measurable outcomes.

I am curious when candidates say they have “strong Rust” but cannot explain why `Arc<Mutex<T>>` is both useful and dangerous in low-latency code.
Interviewers are curious too.
So I rehearse answers at two depths:
- a short executive version for time pressure;
- a deeper technical version if they probe.

Then I run the CV stress test.
Every bullet gets four attachments:
1. context;
2. concrete technical decision;
3. metric or operational result;
4. what I would improve now.

If I cannot fill all four, the bullet is fragile.
Fragile bullets become trapdoors during interviews.
I remove ambiguity before they find it.

There is also psychological value in this process.
When I see gaps clearly, they stop being monsters.
They become tasks.
And tasks can be scheduled.

I finish the inventory with a risk ledger:
- likely weak-question areas;
- fallback explanation strategies;
- bridging phrases to keep structure when surprised.

Example:
“Good question. I’d separate correctness from optimisation first, then choose between shared state and message passing based on contention profile.”

That line buys clarity and time.
In interviews, time is often the rarest currency.

By evening, the inventory had done its work.
I knew exactly where I was dangerous, where I was exposed, and what would change by tomorrow.
A calm operator does not need perfect coverage.
He needs deliberate positioning.
