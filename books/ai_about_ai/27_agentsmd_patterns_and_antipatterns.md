# AGENTS.md Patterns for Real Repositories

You do not need a perfect instruction system.
You need one that survives deadlines and new contributors.

This chapter is about practical patterns for `AGENTS.md` in active repos.

If Chapter 26 defined the contract,
this chapter is about operating it under pressure.

## Pattern 1: layered files, limited depth

Use at most three layers in most projects:

- root defaults,
- domain overrides,
- local feature exceptions.

Too flat: no local precision.
Too deep: nobody can reason about precedence.

A simple stack is easier to audit,
and faster to explain during incidents.

## Pattern 2: command-level checks

If quality gates are vague, they will be skipped.

Prefer:

- exact command,
- expected pass signal,
- where it applies.

Example:

- in `frontend/`: run `pnpm lint && pnpm test`,
- in `infra/`: run `terraform validate`,
- in `docs/`: run link check script.

This turns quality from intention into execution.

For *AI coding workflows*, this one habit prevents a surprising number of regressions.

## Pattern 3: explicit no-touch zones

Agents are fast.
They are also literal.

Declare protected areas:

- generated code,
- migration history,
- vendor snapshots,
- legal text blocks.

If files are fragile, say so directly.

## Pattern 4: fallback rules under tool failure

Tooling fails.
That’s normal.
Silence is not.

Define fallback behaviour:

- if e2e is unavailable, run unit + integration,
- mark result as conditional,
- include warning in final report.

Controlled degradation beats fake green builds.

## Pattern 5: output template contracts

Many teams constrain coding,
but forget to constrain reporting.

Specify response format:

- summary bullets,
- changed files,
- tests run,
- known risks,
- citations or evidence format.

Clear output contracts reduce review friction.

They also improve internal knowledge discoverability,
because evidence appears in a stable, searchable shape.

## Anti-pattern 1: policy novel mode

Long files with motivational language are ignored.

Rule:
if a line cannot be tested or observed,
it probably does not belong.

## Anti-pattern 2: contradictory instructions

“Move fast” plus “always run full monorepo checks” for every tiny edit
is not rigor.
It is latency theatre.

Match checks to risk and scope.

## Anti-pattern 3: hidden precedence

If nested overrides exist but are undocumented,
agents and humans will apply rules inconsistently.

State overrides plainly:

“Rules in this folder replace root test requirements for local doc-only changes.”

## Anti-pattern 4: no feedback from incidents

A defect occurs.
A retro happens.
`AGENTS.md` remains unchanged.

That’s not continuous improvement.
That is managed amnesia.

## Quick audit checklist

For each `AGENTS.md` layer, ask:

- Is scope obvious from location?
- Are commands executable as written?
- Are protected paths explicit?
- Are overrides documented?
- Are escalation triggers present?

If two or more answers are “no,”
expect inconsistent agent behaviour.

## Minimal template you can reuse

- **Scope**: this directory tree.
- **Must do**: required checks and sequence.
- **Must not do**: explicit prohibitions.
- **When unsure**: escalation conditions.
- **Deliver as**: final output format.

One page. High signal.
No decorative language.

In agentic repos, `AGENTS.md` quality determines execution quality.

Not model branding.
Not louder prompts.

Better local instructions,
better local outcomes.

Continue with [Agent-to-Agent Interaction Protocols](./28_agent_to_agent_interaction_protocols.md) to design cleaner handoffs on top of these instruction patterns.
