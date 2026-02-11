# AGENTS.md in Agentic Repos: Scope, Precedence, and Control

Most teams discover `AGENTS.md` at exactly the wrong moment:
after an agent has edited the wrong file with total confidence.

Am I missing something, or do we still call this a “model error”
when it was clearly an instruction error?

For the avoidance of doubt:
`AGENTS.md` is not decorative documentation.
It is runtime control.

## What this file is (and is not)

In agentic workflows, `AGENTS.md` defines local operating rules for an AI agent.

Treat it as:

- a scoped instruction layer,
- loaded during execution,
- designed to constrain behaviour in that subtree.

It is not a wiki page.
It is governance in plain text.

## The key mechanic: directory scope

The file governs the directory where it lives,
and every directory beneath it.

That gives you policy layers:

- repository root: universal defaults,
- subsystem folder: domain constraints,
- feature folder: narrow exceptions.

Location is policy.
Simple as that.

## Precedence rules that actually matter

A reliable instruction stack usually works like this:

1. system / developer / user instructions,
2. nearest applicable `AGENTS.md`,
3. broader parent `AGENTS.md` files,
4. agent defaults.

Nested files override broader files when they conflict.
If that boundary is vague, output becomes non-reproducible.

## What to put inside: minimum viable contract

A high-signal `AGENTS.md` should define:

- **mission**: what success means in this subtree,
- **boundaries**: what must never happen,
- **workflow**: preferred sequence of work,
- **validation**: exact checks and commands,
- **delivery rules**: commit/PR/report format,
- **escalation triggers**: when to stop and surface risk.

No prose theatre.
Only behaviour-changing lines.

## Weak vs strong instruction style

Weak:
“Please keep code clean and well-tested.”

Strong:

- run `pnpm test --filter api` after edits in `services/api/`,
- do not edit generated files under `src/gen/`,
- if schema changes, run migration checks and include output in PR.

Specificity narrows improvisation.
That is precisely the point.

## Real failure pattern: instruction shadowing

Typical incident:

- root file says “run full test suite,”
- nested file says “run package-local tests only,”
- override intent is never stated.

Result: inconsistent execution,
then long debates about why “it passed on my run.”

Fix: declare override intent explicitly.
No subtlety required.

## Design pattern: status -> boundary -> consequence

Use control lines with sharp edges:

- Status: `docs/public/` is customer-facing.
- Boundary: no unverifiable claims.
- Consequence: remove claim or block commit.

Calm tone.
Firm limits.
Predictable outcomes.

## AGENTS.md as incident memory

When a failure happens, update instructions,
not only code.

If incidents never produce instruction diffs,
your system has not learned.
It has merely forgotten politely.

## 20-minute hardening pass

For one active repository:

1. map instruction layers,
2. remove contradictions,
3. add explicit override notes,
4. replace vague quality language with executable checks,
5. add one escalation trigger with clear threshold.

Then run three tasks and compare rework.

## The core idea

`AGENTS.md` is a control surface for agent execution.

Treat it seriously, and this is what happens next:
more predictable runs,
cleaner handoffs,
and fewer expensive surprises disguised as intelligence limits.
