# Node.js and NestJS: How I Structure Backends That Survive Change

Most backend failures are not algorithmic.
They are structural.
A service works for six months, requirements shift, and every change becomes surgery.

So my answer to backend interview questions is straightforward.
I optimise for changeability under pressure.
Not elegance for a conference slide.

My default architecture rule is simple.
Keep business logic in domain services.
Keep transport concerns at the edge.
Never bury core rules inside controllers.

In NestJS terms, that means:

- Controllers validate and orchestrate request flow.
- Services contain use-case logic.
- Repositories hide storage details.
- Events/messages model cross-module communication.

If those boundaries hold, replacing REST with GraphQL, or PostgreSQL with another store, is work.
Not disaster.

## Module boundaries that age well

I design modules around business capabilities.
Not around technical layers alone.

Bad split: `users-controller`, `users-service`, `users-repo` as a giant everything bucket.
Better split: `identity`, `billing`, `notifications`, each with clear responsibility and interface.

A practical contract looks like this:

```ts
export interface InvoiceService {
  issueInvoice(input: IssueInvoiceInput): Promise<InvoiceResult>;
}
```

Small interface.
Clear language.
No transport leakage.

## Validation and error handling without drama

I never trust boundary inputs.
Validation should be explicit and repeatable.

In NestJS this is ordinary work:

- DTO validation for incoming payloads.
- Domain-level guards for business invariants.
- Consistent error mapping to HTTP/GraphQL responses.

I avoid “catch everything, return 500” behaviour.
It destroys observability.

Example boundary discipline:

```ts
@Post()
async create(@Body() dto: CreateOrderDto) {
  const result = await this.orderService.create(dto);
  return toOrderResponse(result);
}
```

If `create` fails, we map known domain failures to clear status codes.
Unknown failures are logged with correlation IDs and traced.

## Observability as a design requirement

If I cannot see it, I cannot fix it.
So I include observability from day one:

- Structured logs with request and correlation IDs.
- Latency and error-rate metrics per endpoint/use case.
- Tracing across async boundaries where possible.
- Alert thresholds tied to user-impact metrics.

This keeps on-call discussions factual.
Not emotional.

## REST vs GraphQL: how I answer

I’m not ideological here.
REST is excellent for clear resource-oriented APIs and predictable caching paths.
GraphQL is excellent when clients need flexible composition across many entities.

The core issue is operational complexity.
GraphQL can reduce over-fetching.
It can also hide expensive resolver behaviour.
So if we choose GraphQL, we need query cost controls, persisted queries, and resolver observability.

That is usually the answer interviewers trust.
Balanced and experience-based.

## Scenario: production bug without theatrics

We had intermittent checkout failures in a service mesh.
Not catastrophic.
Quite expensive.

Symptoms were noisy timeouts and duplicate order attempts.
Initial diagnosis blamed infrastructure.
That seemed optimistic.

I traced request flow with correlation IDs and found two problems.
First, retries happened at multiple layers with no idempotency key.
Second, one downstream dependency had spiky latency and no circuit breaker policy.

Fix plan:

1. Add idempotency key at order-creation boundary.
2. Consolidate retry policy into one layer with bounded backoff.
3. Add timeout budgets and circuit-breaker rules for the unstable dependency.
4. Publish dashboard panels tied to checkout success rate and p95 latency.

Result: duplicate orders disappeared.
Timeout incidents dropped sharply.
Most importantly, future failures became diagnosable within minutes.

## How I explain trade-offs in interviews

I use one sentence pattern:

“We chose X because constraint Y mattered more than benefit Z, and we accepted cost C.”

Example:

“We kept a modular monolith for the first stage because team size and delivery speed mattered more than independent service scaling, and we accepted tighter deploy coupling until domain boundaries stabilized.”

That language signals ownership.
Not cargo-cult architecture.

For related reading, I often bridge to [single-agent myth](../ai_about_ai/11_agents_single_agent_myth.md) and [tools, permissions, safety](../ai_about_ai/13_agents_tools_permissions_safety.md), because backend stability and AI-assisted development both depend on explicit boundaries.
