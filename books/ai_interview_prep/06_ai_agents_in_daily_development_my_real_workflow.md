# AI Agents in Daily Development: My Real Workflow

People often ask whether AI agents “replace engineering effort.”
I’m not convinced.
They replace low-leverage toil.
Judgement remains my job.

So I describe my workflow as a controlled pipeline.
Context in.
Draft out.
Verification loop.
Ship or stop.

If one stage is weak, the whole system degrades.

## Stage 1: Context packaging before prompts

Most weak outputs come from vague context.
Not weak models.

Before I ask for code, I provide five blocks:

1. Task objective in one sentence.
2. Constraints (stack, style, performance, security).
3. Existing code boundaries (files/modules to touch).
4. Acceptance criteria.
5. Non-goals.

My practical prompt skeleton:

```text
Goal: Add bulk invite endpoint for workspace admins.
Stack: NestJS, PostgreSQL, Redis queue.
Constraints: Keep existing auth guards, no schema-breaking changes.
Touch only: invites.module.ts, invites.service.ts, invites.controller.ts.
Acceptance: handles CSV up to 5k rows, idempotent by email+workspace.
Non-goals: no UI changes, no new third-party provider.
```

That structure reduces drift immediately.

## Stage 2: Agent role split

I do not use one chat for everything.
I split roles to reduce confusion:

- Architect agent: module shape, contracts, migration strategy.
- Implementer agent: concrete code changes.
- Reviewer agent: risk, edge cases, regression scan.
- Test agent: test plan and missing-case detection.

In practice, this can be separate sessions or explicit role prompts in one tool.
The principle is the same.
Separation improves reasoning quality.

## Stage 3: Controlled generation and patching

I ask for small, reviewable deltas.
Not giant rewrites.

Bad request: “Refactor this service for performance.”
Better request: “Optimize `getWorkspaceMembers` for pagination and N+1 reduction without API contract changes.”

My standard rule:
If diff size is too large to review confidently in one pass, split it.
Speed without review is theatre.

## Stage 4: Verification loop I never skip

AI output is draft code.
Never final code.

I run four checks before merge:

1. Compile/type check.
2. Unit/integration tests for touched paths.
3. Static analysis/lint rules.
4. Manual edge-case walkthrough.

Then one question:
What could silently fail in production?
If I can’t answer, I haven’t finished.

## Practical example: bug triage with an agent

Scenario: intermittent duplicate notifications.

My first prompt:

```text
You are a senior backend reviewer.
Given this service and worker code, identify top 3 causes of duplicate delivery.
Prioritize by production likelihood.
For each cause: evidence in code, minimal fix, regression test idea.
```

The model suggested three causes.
Only one was correct.
That is normal.

Correct root cause:
Retry behaviour existed in both API layer and queue consumer with no idempotency key.

Fix we shipped:

- Add idempotency key per notification event.
- Store processed keys with TTL.
- Enforce dedupe in consumer before sending.

Agent value was not “perfect diagnosis.”
It accelerated hypothesis generation.
I still owned truth.

## Prompt patterns I reuse

For feature scaffolding:

```text
Generate a minimal implementation plan for [feature].
Output:
1) module boundaries,
2) API contract,
3) data model changes,
4) risk list,
5) test plan.
Keep it under 30 lines.
```

For code review:

```text
Review this diff as staff engineer.
Find correctness, performance, security, and maintainability risks.
Label each issue: Critical / Major / Minor.
Suggest concrete patch snippets only where necessary.
```

For refactor safety:

```text
Propose a no-behavior-change refactor for this file.
List invariants that must hold.
Then provide incremental commits, each with rollback step.
```

## Failure modes I watch carefully

- Context window overflow leading to hallucinated assumptions.
- Tool calls suggested without environment reality.
- Confident but wrong API usage.
- Loss of domain constraints across long sessions.

Mitigations are simple:
Reset context.
Restate invariants.
Anchor to source files.
Require citations to specific code lines when possible.

## Interview answer template

If asked, “How do you use AI agents daily?”, I answer plainly:

“I use them as force multipliers, not decision replacements.
I package context, split tasks by role, request small deltas, and run strict verification loops.
They reduce cycle time for drafting and triage.
I keep architecture and production-risk judgement with the engineering team.”

That answer tends to land.
It sounds practical because it is.

For related depth, I connect this with [multi-agent workflows](../ai_about_ai/12_agents_multi_agent_workflows.md) and [agents as execution contracts](../ai_about_ai/26_agentsmd_as_execution_contract.md), because reliability in AI-assisted engineering depends on explicit boundaries and verification discipline.
