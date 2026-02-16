# Next.js Frontend Scenarios: Hydration, Caching, and UI Stability

I learned this the expensive way.
A frontend can look fast in staging and still fail under real traffic.
Usually not because React is weak.
Because state, rendering mode, and caching policy had been chosen without a failure model.

So for Next.js interview questions, I keep one structure.
Context.
Constraint.
Choice.
Consequence.

If I skip one of those, the answer sounds polished and hollow.

The first decision is rendering strategy.
I map it directly to business requirements:

- SSR when data must be fresh on each request and SEO matters.
- ISR when pages can be stale for a controlled window.
- Static generation when data rarely changes and delivery speed dominates.
- Client-side fetching when personalization is high and indexability is not the primary concern.

That’s the clean theory.
In production, pages are mixed.
One page often needs static shell, server-fetched critical data, and client updates for live widgets.
I’m not convinced by ideological purity here.
A hybrid is often the practical answer.

## Hydration mismatches: what I check first

When hydration breaks, teams often chase symptoms.
I start with deterministic rendering.
Server and client must produce the same initial tree.

My quick checklist:

1. Are we using non-deterministic values during render (`Date.now()`, random IDs, locale-dependent formatting)?
2. Are browser-only APIs called before mount (`window`, `localStorage`, media queries)?
3. Is conditional rendering dependent on client-only context at first paint?
4. Are async boundaries creating different fallback trees on server and client?

Practical fix pattern:

```tsx
const [mounted, setMounted] = useState(false);

useEffect(() => {
  setMounted(true);
}, []);

if (!mounted) return null; // or deterministic skeleton

return <ThemeSensitiveWidget />;
```

This is not a silver bullet.
It is a controlled trade-off.
You protect hydration integrity, then optimize perceived loading with stable placeholders.

## Caching decisions I can defend in an interview

I treat caching as a product decision, not just a framework flag.
Three questions matter:

- How stale is acceptable for users?
- What is the cost of stale data?
- What is the cost of recompute on each request?

In App Router terms, I usually explain choices like this:

```ts
// example: product catalogue can be slightly stale
fetch('https://api.example.com/products', {
  next: { revalidate: 60 },
});
```

Or for truly dynamic endpoints:

```ts
fetch('https://api.example.com/account', {
  cache: 'no-store',
});
```

Interviewers care less about syntax memorization.
They care whether I can explain why one route has `revalidate: 60` and another has no cache at all.

## UI stability under load

A page that shifts during interaction feels broken, even if metrics look acceptable.
So I design for stable surfaces.

What I do in practice:

- Reserve space for async components to reduce layout shift.
- Keep skeleton dimensions close to final content.
- Avoid re-mounting large trees when only filters change.
- Debounce noisy interactions and cancel stale requests.

For lists, I keep expensive computations memoized only after profiling shows pressure.
Premature memoization is a tax.
Measured memoization is a tool.

## Scenario I use in interviews

We had a Next.js page with three pain points:
Hydration warnings, stale widgets, and visible layout jumps.

Root causes were straightforward.
Theme logic depended on `localStorage` at render.
Multiple widgets used ad-hoc client fetch with inconsistent caching.
Skeletons had different dimensions from final cards.

I led a cleanup in three passes.

Pass one: hydration correctness.
Client-only logic moved behind mount guards.
Server render became deterministic.
Warnings dropped to zero.

Pass two: cache policy.
Catalog data moved to controlled revalidation.
Account-specific panels used no-store.
“Sometimes stale” behaviour became intentional and documented.

Pass three: layout stability.
Shared skeleton primitives replaced ad-hoc placeholders.
CLS improved, but more importantly user complaints stopped.

Trade-off: we spent one sprint on plumbing instead of visible features.
Outcome: incident noise dropped, frontend confidence rose, and release reviews got faster.
That is usually worth it.

## Interview answer template: SSR vs ISR vs CSR

If asked quickly, I answer in one breath:

“I choose by freshness, personalization, and indexability.
If data must be fresh per request, SSR.
If slight staleness is acceptable, ISR with explicit revalidate windows.
If content is highly user-specific and SEO is secondary, client fetching.
Then I verify hydration stability and cache invalidation paths before scaling traffic.”

Calm.
Specific.
Operational.


For adjacent depth, I keep two principles explicit: context quality determines frontend decisions, so rendering mode and cache policy must match real user constraints, not framework fashion.
And steady delivery cadence matters—small, frequent releases expose hydration and stability regressions early, before they become expensive incidents.
If you want the longer framing, see [context as operating currency](../ai_about_ai/02_prompt_engineering_context_is_the_new_currency.md) and [ship small daily](../ai_about_ai/10_vibe_coding_ship_small_daily.md), because frontend reliability improves when decision context and delivery cadence are both explicit.
