# Prompt Engineering for Engineers: Patterns That Cut Rework

Most prompt advice is too theatrical.
In engineering, prompts are not poetry.
They are structured task specifications.

When prompts are weak, rework rises.
When prompts are precise, review cycles shrink.

So I treat prompts as mini design docs.
Short.
Constrained.
Testable.

## The baseline prompt format I use

I keep one reliable structure:

- Role: who the model should behave as.
- Objective: what outcome we need.
- Context: relevant system details.
- Constraints: what must not be violated.
- Output format: what shape the answer must have.
- Acceptance checks: how we validate success.

Example for an API feature:

```text
Role: Senior NestJS engineer.
Objective: Add endpoint to archive project without deleting data.
Context: Monolith, PostgreSQL, soft-delete pattern already exists for tasks.
Constraints: No breaking API changes, preserve audit trail, update tests only in touched module.
Output: 1) plan, 2) code diff by file, 3) test additions, 4) rollback notes.
Acceptance: endpoint archives project, tasks remain queryable by admin, existing clients unaffected.
```

This is neither long nor fancy.
It is just unambiguous.

## Pattern 1: Bug triage prompt

When production issues appear, speed matters.
But so does diagnostic quality.

My triage prompt:

```text
Act as incident reviewer.
Given logs + service code, produce:
1) likely root causes ranked,
2) confidence level,
3) evidence in code/logs,
4) minimal safe fix,
5) one regression test per root cause.
Do not suggest infra changes unless evidence requires it.
```

Why it works:
It forces ranked hypotheses and evidence.
Not generic brainstorming.

## Pattern 2: Feature scaffolding prompt

I use this before coding starts:

```text
Design implementation skeleton for [feature].
Include module boundaries, data flow, error handling, and test strategy.
Keep architecture aligned with existing patterns.
Flag unknowns explicitly.
```

This gives me a structured first draft to critique.
Not final truth.
Still useful.

## Pattern 3: Refactor prompt with invariants

Refactors fail when invariants are implied rather than written.
So I pin them.

```text
Propose incremental refactor for this file.
Invariants:
- API contract unchanged.
- Error codes unchanged.
- Latency not worse than current baseline.
Return step-by-step commits and how to verify each step.
```

Now the model cannot “improve” behaviour accidentally without detection.

## Pattern 4: Code-review prompt for senior signal

```text
Review this diff as principal engineer.
Report issues under: Correctness, Security, Performance, Maintainability, Observability.
For each issue include severity and concrete patch suggestion.
Do not comment on naming/style unless it impacts readability materially.
```

This is practical.
It aligns with how teams actually review code.

## Anti-patterns that create rework

I avoid these with discipline:

- Vague goals (“make it better”).
- Missing constraints.
- Multi-feature prompts with no boundaries.
- No output format.
- No acceptance criteria.

If prompt quality drops, output entropy rises.
That is predictable.

## Practical before/after

Weak prompt:

“Add caching to improve performance.”

Result:
Random cache layer, unclear invalidation, high regression risk.

Strong prompt:

“Add read-through caching for `GET /projects/:id` only.
Use existing Redis client.
TTL 60s.
Cache key must include tenant ID.
Do not cache 4xx/5xx.
Include invalidation on project update.
Return exact files changed and tests.”

Result:
Smaller diff.
Clear invalidation logic.
Reviewable risk.

## Interview answer template

If asked, “How do prompts reduce rework?”, I say:

“By turning ambiguous requests into constrained execution.
I define objective, boundaries, and acceptance checks up front.
That improves first-pass accuracy and shortens review loops.
The gain is not magical intelligence.
It is structured communication.”

That usually resonates with engineering leads.


For adjacent context, I make the principle explicit first: instruction stacks keep complex tasks coherent by separating intent, constraints, and output format so the model does not improvise critical assumptions.
And rework only drops when prompts are paired with evaluation loops—clear checks, fast feedback, and correction before merge.
If you want deeper background, I connect this chapter to [instruction stacks](../ai_about_ai/03_prompt_engineering_instruction_stacks.md) and [evaluation loops](../ai_about_ai/05_prompt_engineering_evaluation_loops.md), because strong prompts only matter when paired with consistent verification.
