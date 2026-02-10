# Evaluation Loops Beat Clever Prompts

Prompt edits without evaluation are mostly guesswork.

The core mistake: teams optimise wording before they optimise measurement.

## What an evaluation loop is

A practical weekly cycle:

1. Define a small rubric (3–5 criteria)
2. Sample real production-like tasks
3. Score outputs consistently
4. Tag failure categories
5. Ship one targeted change
6. Re-score and compare against baseline

Repeat.

## Rubrics must map to business impact

Beyond text quality, include operational risk:

- factual accuracy,
- policy compliance,
- decision clarity,
- escalation correctness (if applicable).

## Track why failures happen

“Good vs bad” is too coarse.
Use a failure taxonomy, e.g.:

- missing context,
- ambiguous instruction,
- stale source,
- schema violation,
- hallucinated claim,
- tone mismatch.

Once causes are visible, fixes become surgical.

## Common anti-patterns

- “Looks good to me” scoring
- No historical baseline
- Many edits shipped at once
- Testing only easy cases

## 7-day sprint template

Day 1 rubric → Day 2 sample set → Day 3 scoring → Day 4 pick top failure → Day 5 one fix → Day 6 re-test → Day 7 keep/revert.

The key idea:

**Prompting creates possibilities; evaluation creates reliability.**

---

Continue in depth: [Evaluation Loops](../ai_about_ai/05_prompt_engineering_evaluation_loops.md).
