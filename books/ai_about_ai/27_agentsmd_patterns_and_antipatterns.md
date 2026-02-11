# AGENTS.md Patterns and Anti-Patterns

You do not need a perfect `AGENTS.md`.
You need one that survives contact with deadlines.

This chapter is the field version.
What works. What breaks. Why.

## Pattern 1: layered governance

Use three levels:

- **root**: universal repo rules,
- **domain folder**: workflow and quality for a subsystem,
- **feature folder**: narrow exceptions.

More layers are usually ego.
Fewer layers are usually chaos.

## Pattern 2: command-level precision

“Run checks” is weak.

Better:

- `pnpm lint`
- `pnpm test --filter api`
- `pnpm build`

Precision removes negotiation.
Negotiation is where drift starts.

## Pattern 3: explicit fallback logic

When a tool fails, say what to do.

Example:

- If end-to-end tests are unavailable,
  run unit + integration and mark release as conditional.

This keeps delivery moving without pretending everything is fine.

## Pattern 4: output contracts

Most agent failures happen at output boundaries.

Specify:

- final response template,
- citation format,
- required summary sections,
- expected change log granularity.

The cleaner the exit format,
the easier the human sign-off.

## Anti-pattern 1: legal essay mode

If your file reads like policy fiction,
people stop reading after line 20.

Rule of thumb:
if a sentence cannot change behaviour,
cut it.

## Anti-pattern 2: contradictory urgency

“Move fast” and “never skip any full-system check”
in every directory,
for every task,
is not discipline.
It is self-sabotage.

Match gate cost to risk.
Always.

## Anti-pattern 3: no incident feedback loop

A bad release happens.
Team discusses it.
Nobody updates instructions.

That is institutional amnesia.

Your incident retro should end with an instruction diff,
or the same failure returns wearing a different hat.

## Anti-pattern 4: fake autonomy

Teams say, “the agent can decide.”
Then punish every unexpected decision.

Autonomy without decision boundaries is a trap.

If you want delegation,
define the decision envelope.

## Lightweight template you can steal

- **Intent**: outcome and user impact.
- **Must**: non-negotiable requirements.
- **Must not**: hard prohibitions.
- **Checks**: commands + thresholds.
- **Delivery**: commit, PR, report format.
- **Escalate when**: uncertainty triggers.

One page. High signal.

## Maturity curve (quick diagnostic)

### Level 1 — improvised

Rules live in chat messages and memory.
Quality varies by who is online.

### Level 2 — documented

Rules exist but are broad.
Some checks are automated.

### Level 3 — operational

Rules are scoped, testable, versioned,
and updated after incidents.

### Level 4 — compounding

Instructions become a strategic asset:
new contributors ship faster,
quality stays predictable,
and context switching becomes cheap.

## The core idea

Good `AGENTS.md` files reduce managerial drama.

Bad ones create it.

I’m curious which pain you’d prefer:
20 minutes writing constraints now,
or 20 hours cleaning ambiguity later.
