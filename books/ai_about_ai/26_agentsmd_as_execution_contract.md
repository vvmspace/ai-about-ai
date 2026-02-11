# AGENTS.md as an Execution Contract

Most teams treat `AGENTS.md` as a note.
Then they wonder why the agent behaves like a tourist.

Let’s be clear:
if your agent has no local contract,
it improvises policy from vibes.

That is not an option.

## What `AGENTS.md` really is

`AGENTS.md` is operational law for a directory scope.
Not philosophy. Not aspiration.

A strong file answers five things, quickly:

- what outcomes matter,
- what is forbidden,
- how quality is verified,
- how changes are documented,
- how escalation works.

If one of these is missing,
you have ambiguity.
Ambiguity becomes cost.

## Scope first, then style

The useful move is not “write better prose.”
It is scope control.

Define which tree the file governs.
Then define local standards for that tree only.

Why this matters:

- broad rules become noise,
- local rules become executable,
- nested rules resolve edge cases.

You are building jurisdiction, not literature.

## The minimum contract skeleton

Use this baseline:

1. **Mission** — one paragraph, concrete business outcome.
2. **Boundaries** — explicit “never do” list.
3. **Workflow** — preferred sequence for edits, checks, and delivery.
4. **Tests and gates** — required commands and pass criteria.
5. **Output format** — commit style, PR style, reporting style.

Anything longer must earn its keep.

## A practical pattern: status -> boundary -> consequence

When writing constraints, avoid fluffy warnings.
Use hard lines.

Example:

- Status: `docs/` is customer-facing.
- Boundary: no speculative claims without source.
- Consequence: remove claim or block commit.

Short, decisive, and machine-followable.

## Failure modes you can predict

### 1) Policy in people’s heads

If rules live only in senior engineers,
new contributors and agents produce random quality.

### 2) Conflicting instruction layers

Root says “run full tests.”
Subfolder says “run smoke only.”
No precedence rule means guaranteed friction.

### 3) Unverifiable quality

“Write clearly” is not a gate.
“Run `npm test` and no failing snapshots” is a gate.

### 4) Process theatre

A giant `AGENTS.md` that nobody reads is not governance.
It is décor.

## What high-performing teams do differently

They version control operational behaviour.

When incidents happen, they patch instructions,
not just code.

When onboarding happens, they point to the file,
not a 45-minute oral tradition.

When velocity drops, they remove stale rules,
not pile on new ones.

## A 30-minute upgrade exercise

Pick one active directory.

- Write a 12-line `AGENTS.md` draft.
- Add two hard boundaries.
- Add two mandatory checks.
- Add one escalation trigger.
- Run three real tasks through it.

Then trim anything no one used.

I’m curious how often this reveals the real issue:
not model quality,
but missing local law.

## The core idea

Treat `AGENTS.md` as an execution contract.

Not “nice to have.”
Not later.

Here’s what’s going to happen when you do:
less rework,
faster handoffs,
and far fewer polite disasters.
