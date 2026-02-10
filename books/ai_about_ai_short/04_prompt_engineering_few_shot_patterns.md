# Few-Shot Patterns That Actually Transfer

Examples are useful only if they teach judgement, not just style mimicry.

Teams often add polished examples, pass rehearsed cases, and then fail on messy real inputs.
That is an example design problem.

## Teach boundaries, not cosmetics

Use three example types:

1. **Gold** — excellent output and why it is excellent
2. **Minimum pass** — acceptable but imperfect output
3. **Reject** — plausible output that fails standards

This teaches both target behaviour and failure boundaries.

## Add reviewer notes

Short notes after each example improve transfer:

- what is strong,
- what is weak,
- why a response is rejected.

These notes often matter more than adding more examples.

## Where few-shot is most valuable

Use it for fuzzy-quality tasks:

- tone-sensitive communication,
- nuanced classification,
- rewriting/simplification,
- policy-safe response drafting.

## Keep examples fresh

Language, market framing, and policy terms change.
Stale examples teach stale judgement.
Set review cadence and expiration dates.

## Common anti-patterns

- Only polished examples
- Too many similar examples
- No failure examples
- Hidden scoring standard across reviewers

The key idea:

**Few-shot works when examples encode decision boundaries.**

---

Continue in depth: [Few-Shot Patterns](../ai_about_ai/04_prompt_engineering_few_shot_patterns.md).
