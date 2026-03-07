# API Contracts Between Rust and Frontend

I have watched excellent teams lose weeks to one avoidable mistake.
They treated API schemas as temporary conversation.
Naturally, the conversation changed every sprint.
The systems did not survive the improvisation gracefully.

In interview rounds, I frame API contracts as legal documents for distributed components.
Rust services and Next.js clients are independent actors.
Without explicit contracts, each side invents reality.
That is expensive on quiet days and dangerous on volatile ones.

I start with schema clarity.
Every response should declare stable field names, explicit types, and predictable nullability.
If a field is optional, we say why.
If it may disappear, we version the endpoint.
Surprises belong in novels, not production payloads.

Then I define error envelopes.
Not just HTTP status.
A structured body with code, message, category, and trace identifier.
Frontend logic can then decide whether to retry, degrade, or block user action.
Interviewers notice when you design for operators, not only for happy-path demos.

Versioning usually arrives as the next question.
I keep this elegant and practical.
Backward-compatible additions are fine.
Breaking changes require explicit version boundaries.
Deprecation windows are announced and measured.
Consumers are migrated with telemetry, not optimism.

For streaming workflows, I explain event contracts separately from REST contracts.
Each event has type, sequence semantics, ordering guarantees, and idempotency expectations.
If events can arrive out of order, the client needs deterministic merge logic.
If duplicates are possible, handlers must remain safe by construction.
This is where Rust enum modelling helps both safety and readability.

Pagination is another place where interviews quietly test maturity.
I prefer cursor-based pagination for mutable datasets.
Offsets are acceptable for static or low-churn lists.
In high-frequency domains, offset pages drift while users watch.
Cursor semantics keep continuity under concurrent writes.

I also discuss timestamps with unusual seriousness.
Use one canonical format.
Use UTC.
State precision explicitly.
Distinguish event time from processing time.
By the time you debug cross-service drift in production, you will wish this had been strict earlier.

A curious question I sometimes get is, “How much should frontend know about backend internals?”
I answer with a boundary.
Frontend should know contract semantics, never storage trivia.
If UI logic depends on table structure, the architecture has already leaked.
That doesn’t work for me.

Testing contracts is where many teams grow disciplined.
I mention schema tests in Rust, type-safe client generation where appropriate, and integration checks that replay real payload samples.
Contract drift should fail CI long before it reaches traders.
Live markets are not the place for schema archaeology.

When I tie this to CV defense, I pick one concrete incident.
We once had changed an enum value without deprecation.
The frontend had mapped unknown values to “success,” which was charming until it wasn’t.
We fixed it with strict unknown-case handling, contract snapshots, and release gates.
The interview lesson is memorable because it is painfully real.

This chapter connects [Next.js for Backend Engineers](./37_nextjs_for_backend_engineers.md) to [Testing Strategy Across the Stack](./39_testing_strategy_across_the_stack.md).
In full-stack trading systems, API contracts are not paperwork.
They are the difference between coordinated speed and synchronized confusion.
