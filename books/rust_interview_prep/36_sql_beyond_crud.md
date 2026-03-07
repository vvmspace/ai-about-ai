# SQL Beyond CRUD

I once sat down for what had been advertised as a Rust systems interview.
Forty minutes later, we were discussing why a query had scanned fifty million rows before breakfast.
Quite manageable, if you had prepared for the ambush.

When a trading company says “full stack,” SQL is rarely a side quest.
It is part of the execution path, the risk dashboard, and the post-trade truth ledger.
If you treat it as simple CRUD, they will treat you as simple CRUD.

My rule is straightforward.
I never describe queries first.
I describe workload shape first.
Reads versus writes.
Hot symbols versus cold history.
Latency-sensitive paths versus analytical paths.
By the time I discuss `SELECT`, the interviewer already knows I think in systems.

Then I draw the tables with intent.
Orders, fills, positions, risk snapshots, user actions.
I mark primary keys and show how access patterns map to indexes.
If a table is queried by `(account_id, ts DESC)`, I say that index explicitly.
If a dashboard filters by `(symbol, venue, status)`, I design for that filter, not for aesthetic purity.

A curious question interviewers love is, “How do you choose indexes?”
I answer with a sequence.
First, identify the top three critical queries.
Second, run `EXPLAIN` and check estimated versus actual rows.
Third, add or reshape composite indexes based on predicates and sort order.
Fourth, verify write overhead and memory pressure.
Fifth, remove decorative indexes that flatter no real query.

In trading systems, time is a first-class citizen.
So I discuss partitioning early.
Recent data remains hot and tightly indexed.
Historical partitions are cheaper, compressed, and queried differently.
This prevents one month-end report from poisoning daily execution latency.

I also separate operational truth from analytical convenience.
The operational database stores state transitions with strict constraints.
Analytical views may denormalize for speed.
If someone asks whether I prefer normalization or denormalization, I’m not convinced by the framing.
I prefer correctness where money moves, and speed where people explore.

Naturally, lock behavior appears next.
I mention transaction boundaries in plain language.
Keep them short.
Touch rows in consistent order.
Avoid “chatty” transactions that hold locks while application code hesitates.
Under burst load, one long transaction can become a polite catastrophe.

Then I move to failure posture.
What happens when replication lags?
What happens when a migration runs long?
What happens when a query plan regresses after data distribution shifts?
I explain guardrails: query timeouts, statement budgets, migration playbooks, and rollback paths.
Production readiness is not a slogan; it is a list of unpleasant events you rehearsed in advance.

Because this role spans Rust and Next.js, I also discuss interface discipline.
Frontend screens should not issue accidental N+1 storms.
Backend handlers should expose query-friendly endpoints and stable pagination.
I prefer cursor pagination for live feeds and keyset semantics for deep history.
Offset pagination is convenient until page 900 becomes an apology letter.

If the interviewer asks for optimisation priorities, I keep this elegant.
Measure with realistic data.
Fix the heaviest query first.
Reduce cardinality where possible.
Cache carefully, invalidate honestly, and never let cache correctness become folklore.

This chapter extends [Trading Pipeline End-to-End](./35_trading_pipeline_end_to_end.md) and prepares the contract discussion in [API Contracts Between Rust and Frontend](./38_api_contracts_between_rust_and_frontend.md).
SQL performance is not wizardry.
It is disciplined respect for access patterns under pressure.
