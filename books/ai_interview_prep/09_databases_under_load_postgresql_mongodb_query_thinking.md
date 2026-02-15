# Databases Under Load: PostgreSQL, MongoDB, and Query Thinking

Database interviews often drift into brand preference.
I avoid that.
The engine matters.
Query behaviour matters more.

So I frame every database answer around workload shape.
Read/write ratio.
Consistency needs.
Latency targets.
Failure tolerance.

If those are vague, technology choice is mostly guesswork.

## How I choose PostgreSQL vs MongoDB in practice

I keep it plain.

PostgreSQL is my default when:

- data integrity rules are strong,
- transactions are central,
- joins are part of normal product behaviour,
- reporting and relational queries will grow.

MongoDB is practical when:

- document shape evolves quickly,
- nested aggregates map naturally to product entities,
- write flexibility matters more than cross-entity constraints,
- we can tolerate denormalisation with clear ownership.

I’m not convinced by “one database for everything.”
It simplifies procurement.
It rarely simplifies operations.

## Query thinking before schema debates

When I tune systems, I start with query paths.
Not ER diagrams.

I ask:

1. Which queries are user-critical?
2. Which queries run most often?
3. Which writes are expensive and why?
4. Which access paths need predictable p95 latency?
5. Which queries can be precomputed or cached?

Then I index for real traffic.
Not hypothetical elegance.

## PostgreSQL patterns I rely on

A few habits have paid repeatedly:

- Composite indexes aligned with filter order.
- Partial indexes for selective high-frequency predicates.
- `EXPLAIN (ANALYZE, BUFFERS)` before and after tuning.
- Avoid `SELECT *` on hot paths.
- Pagination with keyset strategy where offset cost grows.

Example shift:

```sql
-- expensive at scale
SELECT * FROM events
WHERE workspace_id = $1
ORDER BY created_at DESC
LIMIT 50 OFFSET 50000;

-- stable under growth
SELECT id, type, created_at
FROM events
WHERE workspace_id = $1
  AND created_at < $2
ORDER BY created_at DESC
LIMIT 50;
```

This is not fashionable.
It simply keeps latency stable.

## MongoDB patterns I watch closely

Mongo performs very well when query and document design stay aligned.
It degrades when we pretend it behaves like an unrestricted relational store.

My working rules:

- Design documents around read patterns.
- Keep indexes explicit and audited.
- Watch unbounded array growth.
- Use TTL indexes for ephemeral data where appropriate.
- Avoid ad-hoc aggregation pipelines in latency-critical paths without benchmarking.

If one endpoint depends on a huge aggregation pipeline, I treat it as a signal.
Either precompute, cache, or redesign read model.

## Scenario I use in interviews

We had a feed endpoint that looked harmless.
Traffic grew.
Latency became volatile.

Symptoms:

- PostgreSQL p95 jumped during peak windows.
- Query plan switched under load.
- API timeouts increased despite enough CPU headroom.

What we found:

- Offset pagination on deep pages.
- Non-covering index for dominant query shape.
- Extra columns fetched that UI never used.

Fix sequence:

1. Move to keyset pagination.
2. Add composite index matching `workspace_id + created_at`.
3. Select only required columns.
4. Add cache for repeated top-page reads.

Outcome:
P95 dropped sharply.
Timeouts normalized.
Database load became predictable.

Trade-off:
Keyset pagination changed client cursor handling.
Worth it.

## Interview-safe answer template

If asked, “How do you optimize database performance?”, I answer:

“I start from workload and critical query paths.
I inspect actual execution plans, then align indexes and query shape.
I reduce payload, remove deep-offset patterns, and cache only where access is repetitive.
Then I measure p95 and error rate before calling the change successful.”

That sounds less glamorous.
It sounds deployable.

## Testing and observability I include

Database changes without measurement are storytelling.
So I include:

- Query-level latency dashboards.
- Slow-query logs with threshold alerts.
- Regression tests for pagination and filter correctness.
- Load test snapshots before and after index/query changes.

Time.
Cost.
Risk.
Same framework.

For adjacent context, this chapter pairs with [searchability and clarity](../ai_about_ai/20_knowledge_systems_searchability_and_clarity.md) and [RAG without fantasy](../ai_about_ai/17_knowledge_systems_rag_without_fantasy.md), because query design and retrieval quality both fail when access paths are vague.
