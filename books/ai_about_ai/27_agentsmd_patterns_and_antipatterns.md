# AGENTS.md Patterns for Real Repositories

You do not need a perfect instruction system.
You need one that survives deadlines and new contributors.

This chapter covers practical `AGENTS.md` patterns for active repositories.

## Pattern 1: layered files, limited depth

In most projects, three layers are enough:

- root defaults,
- domain overrides,
- local feature exceptions.

Too flat gives poor local precision.
Too deep destroys precedence clarity.

## Pattern 2: command-level checks

If quality gates are vague, they will be skipped.

Prefer:

- exact command,
- expected pass signal,
- explicit scope.

Example:

- in `frontend/`: run `pnpm lint && pnpm test`,
- in `infra/`: run `terraform validate`,
- in `docs/`: run link-check script.

This turns quality from intention into execution.

## Pattern 3: explicit no-touch zones

Agents are fast.
They are also literal.

Declare protected areas clearly:

- generated code,
- migration history,
- vendor snapshots,
- legal text blocks.

If a file is fragile, say so directly.

## Pattern 4: fallback rules under tool failure

Tools fail.
That is normal.
Silence is not.

Define fallback behaviour:

- if e2e is unavailable, run unit + integration,
- mark the result as conditional,
- include the warning in the final report.

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

## Anti-pattern 1: policy novel mode

Long motivational instruction files are ignored.

Rule of thumb:
if a line cannot be tested or observed,
it probably does not belong.

## Anti-pattern 2: contradictory instructions

“Move fast” plus “always run full monorepo checks” for every tiny edit
is not rigour.
It is latency theatre.

Match checks to risk and scope.

## Anti-pattern 3: hidden precedence

If nested overrides exist but remain undocumented,
agents and humans will apply rules inconsistently.

State overrides plainly:

“Rules in this folder replace root test requirements for local doc-only changes.”

## Anti-pattern 4: no feedback from incidents

A defect occurs.
A retro happens.
`AGENTS.md` remains unchanged.

That does not work.
It is managed amnesia.

## Quick audit checklist

For each `AGENTS.md` layer, ask:

- Is scope obvious from location?
- Are commands executable as written?
- Are protected paths explicit?
- Are overrides documented?
- Are escalation triggers present?

If two or more answers are “no”,
expect inconsistent agent behaviour.

## Minimal template you can reuse

- **Scope**: this directory tree.
- **Must do**: required checks and sequence.
- **Must not do**: explicit prohibitions.
- **When unsure**: escalation conditions.
- **Deliver as**: final output format.

One page.
High signal.
No decorative language.

## The core idea

In agentic repositories, `AGENTS.md` quality determines execution quality.

Not model branding.
Not louder prompts.

Better local instructions,
better local outcomes.
