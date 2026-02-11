# AGENTS.md in Agentic Repos: Scope, Precedence, and Control

Most teams discover `AGENTS.md` in the worst possible way:
after an agent confidently edits the wrong thing.

I’m curious how many “model mistakes” are actually instruction mistakes.

Let’s be clear:
`AGENTS.md` is not team documentation.
It is runtime control.

## What this file is (and is not)

In agentic coding workflows, `AGENTS.md` defines local operating rules for an AI agent.

Think of it as:

- a scoped instruction layer,
- loaded during task execution,
- designed to constrain behaviour in that subtree.

It is **not** a wiki note.
It is executable governance in plain text.

This sits in the heart of **AI agent governance**:
clear instructions, repeatable outcomes, and fewer production incidents.

## The key mechanic: directory scope

The file governs the directory where it lives,
and everything beneath it.

This means you can design policy layers:

- repo root: universal defaults,
- subsystem folder: domain-specific constraints,
- feature folder: narrow exceptions.

Short version:
location is policy.

If scope is ambiguous, execution becomes political.
People debate intent instead of reading the rule.

## Precedence rules that actually matter

A robust stack usually behaves like this:

1. system/developer/user instructions,
2. nearest applicable `AGENTS.md`,
3. broader parent `AGENTS.md` files,
4. agent defaults.

More deeply nested files override broader ones when they conflict.

That’s not optional bookkeeping.
That is the difference between reproducible output and chaos.

When teams skip this order, they often diagnose the wrong thing.
They blame the model, when the failure had begun in governance design.

## What to put inside (minimum viable contract)

A high-signal `AGENTS.md` should define:

- **mission**: what success looks like here,
- **boundaries**: what must never happen,
- **workflow**: preferred order of work,
- **validation**: exact checks/commands,
- **delivery rules**: commit/PR/report format,
- **escalation triggers**: when to stop and surface risk.

No prose theatre.
Only behaviour-changing instructions.

If a line cannot change an agent decision,
it should probably be removed.

## Bad vs good instruction style

Weak:
“Please keep code clean and well-tested.”

Strong:

- run `pnpm test --filter api` after edits in `services/api/`,
- do not edit generated files under `src/gen/`,
- if schema changes, run migration check and include output in PR.

Specificity gives the agent less room to hallucinate process.

## Real failure pattern: instruction shadowing

A common incident:

- root file says “run full test suite,”
- nested file says “run package-local tests only,”
- no explicit override language.

Result: inconsistent behaviour across tasks,
and endless “but it passed for me” conversations.

Fix:
state override intent explicitly.

For the avoidance of doubt, phrase it as a replacement, not a suggestion:
“Rules in this folder replace root test requirements for docs-only edits.”

## Design pattern: status -> boundary -> consequence

Use crisp control lines:

- Status: `docs/public/` is customer-facing.
- Boundary: no unverifiable claims.
- Consequence: remove claim or block commit.

Calm language.
Hard edge.
Clear outcome.

## AGENTS.md as incident memory

When a failure happens, update instructions,
not just code.

If incidents do not produce instruction diffs,
your system does not learn.
It merely forgets politely.

This is the practical route from “postmortem culture” to *operational memory*.

## 20-minute hardening pass

For one active repository:

1. map current instruction layers,
2. remove contradictory commands,
3. add explicit override notes for nested scopes,
4. replace vague quality lines with exact checks,
5. add one clear escalation trigger.

Then run three tasks and compare rework.

Most teams are surprised by how quickly rework drops once boundary text is precise.

`AGENTS.md` is a control surface for agent execution.

Treat it seriously,
and you get more predictable runs,
cleaner handoffs,
and fewer expensive surprises disguised as intelligence limits.

If you want to continue this arc, read [AGENTS.md Patterns for Real Repositories](./27_agentsmd_patterns_and_antipatterns.md) for tactical patterns and anti-patterns.
