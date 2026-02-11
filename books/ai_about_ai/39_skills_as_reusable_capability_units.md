# Skills as Reusable Capability Units

In agentic systems, prompts alone do not scale.
Reusable skills do.

A skill is a packaged workflow:
context + instructions + tools + output contract.

## Why skills matter

Without skills, each task is re-invented.

Symptoms:

- variable quality,
- repeated prompt crafting,
- brittle handoffs,
- slow onboarding.

Skills convert best practice into reusable operations.

## Anatomy of a strong skill

A useful skill defines:

- problem scope,
- trigger conditions,
- required inputs,
- tool calls and sequence,
- output schema,
- fallback path.

If one is missing,
execution drift appears.

## Skill lifecycle

Treat skills as product assets:

1. identify repeatable pain,
2. extract winning workflow,
3. package into skill format,
4. validate on live tasks,
5. version and improve.

No lifecycle, no reliability.

## Design principle: narrow first

A broad “do anything” skill feels powerful,
but fails under pressure.

Better:

- one job,
- one clear entry point,
- one reliable output.

Specialisation increases trust.

## Governance and discoverability

Skill libraries fail when people cannot find the right unit.

Keep an index with:

- skill name,
- use-case sentence,
- required permissions,
- examples,
- known limits.

Discovery is part of performance.

## Metrics for a skill library

Track:

- reuse frequency,
- success rate,
- average completion time,
- escalation rate,
- incidents per skill version.

If reuse is low,
either discoverability or fit is broken.

## Anti-patterns

- Skills that require hidden tribal context.
- Skills with no output contract.
- Skills that call too many tools by default.
- Skills never updated after failures.

That is not a library.
That is a museum.

## The core idea

Skills are the missing layer between raw model ability and dependable execution.

Build them narrowly.
Version them deliberately.
Measure them honestly.
