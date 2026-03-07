# Testing Strategy Across the Stack

I used to think test strategy questions were gentle warm-up.
Then I watched an interviewer spend thirty minutes probing exactly where my confidence exceeded my evidence.
Quite educational.

In performance-critical systems, testing is not about vanity coverage.
It is about risk control under constrained time.
When I have less than two days to prepare, I speak in priorities.
What must never break?
What fails silently?
What would lose money if wrong for five minutes?

I begin with unit tests in Rust.
They guard pure logic: risk checks, state transitions, parsing rules, deterministic calculations.
Fast, focused, and numerous.
If an enum transition is invalid, I want a test to say so before reviewers need to squint.

Then integration tests.
I wire realistic components: ingestion, validation, routing, persistence, outbound events.
The goal is contract truth, not microscopic perfection.
Can an order travel the expected path with coherent IDs and timestamps?
Can a reject propagate with the right reason and severity?
If not, architecture diagrams are fiction.

For async systems, I highlight deterministic test harnesses.
Bounded queues.
Controlled clocks when possible.
Explicit timeout assertions.
Unbounded concurrency in tests creates charming flakes and no confidence.

Property-based testing is my tactical advantage for interview conversation.
I use it where input space is broad: parsers, normalizers, risk limit math, idempotent handlers.
Instead of writing fifty examples, I define invariants and let generators hunt edge cases.
Interviewers tend to remember that because it sounds like engineering, not ritual.

Load and performance tests come next.
I separate microbenchmarks from scenario load tests.
Microbenchmarks isolate code-path costs.
Scenario tests model bursts, reconnect storms, and backlog recovery.
Both matter, but they answer different questions.

On the frontend side, I stay practical.
Component tests for critical widgets.
Integration tests for data flow and reconnect behavior.
A thin end-to-end slice for the most valuable workflows.
I’m not convinced by massive brittle E2E suites that fail because a button moved two pixels.

Observability validation is often ignored, so I mention it explicitly.
Tests should verify metrics emission, structured logs, and trace continuity on key flows.
If the system fails and telemetry goes dark, incident response becomes guesswork.
That is not on the table.

I also show how I would phase automation under deadline.
Phase one: correctness on critical path.
Phase two: contract and regression guards.
Phase three: resilience and load behaviour.
Interviewers appreciate sequencing, because real teams always face trade-offs.

To defend the CV, I keep one story prepared.
In a prior system, we had excellent unit coverage and still shipped a queue overflow bug.
Why?
No burst-load scenario tests had existed.
We added bounded-load simulations and explicit drop policies.
The same class of incident did not return.

Finally, I explain failure policy.
A failing test on the hot path blocks release.
A flaky non-critical test is quarantined with owner and deadline, not ignored indefinitely.
Discipline is not severity theatre.
It is consistent consequence.

This chapter builds on [API Contracts Between Rust and Frontend](./38_api_contracts_between_rust_and_frontend.md) and prepares [Debugging Stories They Actually Remember](./40_debugging_stories_they_actually_remember.md).
Good tests do not guarantee safety.
They guarantee that surprises arrive early enough to be useful.
