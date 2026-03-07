# Next.js for Backend Engineers

The first time I entered a frontend round for a trading role, I made the classic mistake.
I spoke flawlessly about backend throughput and almost nothing about what traders actually see.
That was the moment I understood their game.
If the UI lies for even three seconds, the whole platform is lying.

So I learned to treat Next.js as part of the reliability surface.
Not decoration.
Not marketing.
A decision interface for people moving real capital.

I begin with rendering strategy.
Server-side rendering, static generation, and client rendering are not ideological camps.
They are latency and freshness choices.
For a trading dashboard, static generation suits reference pages.
Server rendering helps controlled initial state.
Client updates carry the live edge once the session is active.

Interviewers often ask, “How would you structure data fetching?”
I answer by boundary.
Initial snapshot comes from a stable API call.
Real-time deltas arrive through websocket or streaming channels.
The client reconciles snapshot plus deltas using deterministic update rules.
If I can explain reconciliation clearly, they usually relax.

Then I discuss state without romanticism.
Global state is expensive if you make everything global.
Local state is fragile if shared truths fragment across components.
I keep critical trading state centralized and typed.
Derived presentation state remains local.
This avoids duplicate truth while preserving component clarity.

A curious trap appears in fast-moving UIs.
Developers optimise for average render speed and ignore outliers.
Traders experience outliers.
So I mention frame drops, event burst handling, and render throttling.
When market bursts arrive, the interface must degrade gracefully, not freeze theatrically.

I also talk about error surfaces.
Frontend errors should carry structured context: request id, symbol, account scope, timestamp.
A blank toast saying “Something went wrong” is not operationally useful.
I prefer explicit states: stale, reconnecting, partial, blocked.
People can handle bad news when it is precise.

Security and permissions are part of the conversation as well.
Role-based controls are enforced on the backend first.
Frontend visibility mirrors those rules but never replaces them.
If someone can toggle a hidden button and place an order, we are not doing engineering.
We are doing theatre.

Because this role is full stack, I connect UI decisions back to Rust services.
Batching, pagination, and schema stability determine frontend complexity.
When backend contracts are noisy, frontend code becomes defensive and slow.
When contracts are crisp, frontend remains calm even under pressure.

For interview practicality, I carry a mini checklist.
What is rendered where?
How is live data merged?
What is the stale-data policy?
What is the reconnect strategy?
What telemetry proves the UI stayed useful during burst load?
Five questions, and suddenly the round becomes much more manageable.

I also keep one story from my CV ready.
In one project, we had optimised API latency but ignored browser memory growth.
After two hours of live updates, sessions had degraded badly.
We fixed it with bounded in-memory windows, selective virtualization, and tighter event schemas.
The lesson was simple: low latency at the server is only half the journey.

This chapter follows [SQL Beyond CRUD](./36_sql_beyond_crud.md) and leads directly to [API Contracts Between Rust and Frontend](./38_api_contracts_between_rust_and_frontend.md).
A trading UI is not where performance work ends.
It is where performance becomes visible.
