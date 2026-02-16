# React State Management Reset: From Weak Spot to Competitive Edge

I used to answer React state questions with broad confidence and thin precision.
That works until someone asks for boundaries.
Then the confidence evaporates.

So I rebuilt this area from first principles.
Not to pass trivia.
To make better production decisions under time pressure.

Here is the model I now use in both interviews and live projects.

Local UI state handles interaction that belongs to one feature surface.
Global client state handles cross-screen UI concerns.
Server state handles remote truth, cache policy, retries, and synchronization.
Derived state is computed, not duplicated.

If these four concerns are mixed, complexity rises quietly.
If they are separated, defects become debuggable.

I run five questions before I write any state code:

1. Who owns the truth?
2. Who reads this data?
3. How often does it change?
4. How stale can it be before users notice?
5. What is the graceful behaviour when network calls fail?

That five-question pass removes most accidental architecture.

A practical mapping helps.
I keep this in my head during implementation:

- Modal open/close, hovered row, form dirty flag → local `useState`.
- Theme, auth token, user UI preferences → small global store.
- Product list, profile data, invoices, notifications feed → React Query server state.
- `filteredProducts`, `isSubmitEnabled`, totals → derived via selectors or memoized computation.

I’m not convinced by “one store for everything.”
It sounds tidy.
It ages badly.

## Practical example 1: Local state done cleanly

A filter panel does not need Redux by default.
It needs predictable local behaviour:

```tsx
const [filters, setFilters] = useState({ search: '', status: 'all' });

const onSearchChange = (search: string) =>
  setFilters((prev) => ({ ...prev, search }));

const onStatusChange = (status: 'all' | 'open' | 'closed') =>
  setFilters((prev) => ({ ...prev, status }));
```

That stays inside one component boundary.
No global coupling.
No ceremony tax.

## Practical example 2: Server state with React Query

Server state is where many teams still overuse `useEffect`.
I’d avoid that.

```tsx
const { data, isLoading, isError, refetch } = useQuery({
  queryKey: ['tickets', filters],
  queryFn: () => api.tickets.list(filters),
  staleTime: 30_000,
  retry: 2,
});
```

Now cache, loading, retries, and refetching are explicit.
And importantly, they are standard.
The team can reason about behaviour quickly.

## Practical example 3: Global state when it is truly global

I keep global state small and obvious.
For instance, UI preferences:

```tsx
import { create } from 'zustand';

type UiState = {
  density: 'compact' | 'comfortable';
  setDensity: (v: UiState['density']) => void;
};

export const useUiStore = create<UiState>((set) => ({
  density: 'comfortable',
  setDensity: (density) => set({ density }),
}));
```

Simple state.
Clear ownership.
Minimal surface area.

If the domain grows and transitions become more complex, Redux Toolkit is usually the better fit.
Not because it is fashionable.
Because explicit reducers and action flow improve team-scale maintenance.

## Practical example 4: Redux Toolkit for auditable transitions

```tsx
const cartSlice = createSlice({
  name: 'cart',
  initialState: { items: [] as Array<{ id: string; qty: number }> },
  reducers: {
    addItem: (state, action: PayloadAction<{ id: string }>) => {
      const existing = state.items.find((x) => x.id === action.payload.id);
      if (existing) existing.qty += 1;
      else state.items.push({ id: action.payload.id, qty: 1 });
    },
  },
});
```

For carts, permissions matrices, and multi-step workflows, this explicitness pays for itself.

## Two anti-patterns I now flag immediately

First, mirrored state.
If API data is copied into multiple stores “for convenience,” divergence appears.
Sooner or later, one view renders stale truth.

Second, effect-driven orchestration.
If business logic depends on interlocked `useEffect` chains, timing bugs appear under load.
I’d advise against it.
Move business decisions closer to event handlers or dedicated domain functions.

## Interview-safe answer template

When asked, “How do you choose between Redux, Zustand, and React Query?”, I answer like this:

“By ownership and lifecycle.
React Query for server truth and caching.
Local state for isolated interaction.
Global store only for shared client concerns.
Redux Toolkit when transitions and auditability matter.
If we mix these concerns, complexity grows and defect triage slows.”

Short.
Defensible.
Senior.

## Real scenario I can tell in 60–90 seconds

We had a dashboard with polling, table filters, and cross-page preferences.
Originally, the team had stored API collections in Redux and also copied them into component state.
Hydration and stale-data bugs followed.

I proposed a reset.
Server collections moved to React Query.
Filters stayed local.
User preferences stayed global.
We removed mirrored state and replaced ad-hoc effects with explicit query invalidation.

Trade-off: the refactor took longer than a patch.
Result: stale-data bugs dropped, re-render noise decreased, and onboarding for new engineers improved because the architecture became legible.

## Testing strategy that sounds practical, not academic

I separate tests by risk:

- Reducers/selectors: deterministic unit tests.
- Query hooks: integration tests with mocked network timing and failure edges.
- Critical user path: one or two end-to-end flows.

Time. Cost. Risk.
That triad keeps the test plan honest.

The core shift is psychological.
I no longer defend a toolkit identity.
I defend data ownership, failure behaviour, and maintainability under real constraints.
That is usually what interviewers are really measuring.


For adjacent framing, I keep one principle visible: quality comes from short evaluation loops with explicit checks, not from one clever first attempt.
And when failures appear, I debug with models by narrowing scope, testing assumptions, and isolating one variable at a time—the same discipline we use for state regressions.
If you want deeper background, see [evaluation loops in AI-assisted engineering](../ai_about_ai/05_prompt_engineering_evaluation_loops.md) and [debugging with models](../ai_about_ai/08_vibe_coding_debugging_with_models.md).
