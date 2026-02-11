# Skills as Reusable Capability Units

In agentic systems, prompts alone do not scale.
Reusable skills do.

A skill is a packaged workflow:
context, instructions, tools, and output contract.

## Why skills matter

Without skills, each task is partially reinvented.

Symptoms:

- variable quality,
- repeated prompt crafting,
- brittle handoffs,
- slow onboarding.

Skills turn best practice into reusable operations.

## Anatomy of a strong skill

A useful skill defines:

- problem scope,
- trigger conditions,
- required inputs,
- tool calls and sequence,
- output schema,
- fallback path,
- escalation boundary.

If one element is missing,
execution drift appears.

## Skill lifecycle

Treat skills as product assets:

1. identify repeatable pain,
2. extract winning workflow,
3. package into skill format,
4. validate on live tasks,
5. version and improve.

No lifecycle means no reliability.

## Design principle: narrow first

A broad “do anything” skill sounds powerful.
Under pressure, it fails.

Better pattern:

- one job,
- one clear entry point,
- one reliable output.

Specialisation increases trust.

## Contracts before cleverness

For each skill, define contracts explicitly:

- input contract,
- execution contract,
- output contract.

If contracts are vague,
review time explodes.

## Governance and discoverability

Skill libraries fail when people cannot find the right unit.

Maintain an index with:

- skill name,
- one-line use case,
- required permissions,
- example invocation,
- known limits,
- owner.

Discovery is part of system performance.

## Metrics for a skill library

Track:

- reuse frequency,
- success rate,
- average completion time,
- escalation rate,
- incidents per skill version.

If reuse is low,
fit or discoverability is broken.

## Anti-patterns

- skills requiring hidden tribal context,
- skills with no output contract,
- skills calling too many tools by default,
- skills never updated after failures.

That is not a library.
That is a museum.

## Practical adoption sequence

- Week 1: package top three repeated workflows.
- Week 2: add contracts and examples.
- Week 3: instrument metrics.
- Week 4: retire low-performing versions.

Small cadence.
Steady reliability gains.

## The core idea

Skills are the layer between raw model ability and dependable execution.

Build narrowly.
Version deliberately.
Measure honestly.
