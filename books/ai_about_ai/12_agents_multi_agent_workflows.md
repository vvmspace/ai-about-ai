# Designing Multi-Agent Workflows

Most multi-agent projects fail in the same way:
not because models are weak,
but because handoffs are vague.

Agents are arranged like characters in a story,
not operators in a production line.

The result is activity without accountability.

## Orchestration is workflow engineering

A multi-agent system is not “many chats.”
It is a pipeline of commitments.

For each stage you must define:

- expected artefact,
- acceptance criteria,
- owner of validation,
- failure path.

Without these, errors cascade silently through polite language.

## Start from deliverables, not roles

Teams often begin with role names: researcher, writer, reviewer.
Better start point:

What concrete output must exist at each step?

Example:

1. Clarified brief (scope + constraints + open questions)
2. Evidence set (sources + confidence + gaps)
3. Draft output (schema-compliant)
4. Quality assessment (rubric scores + risk notes)
5. Final package (approved or escalated)

Role assignment comes after output design.

## Handoff contracts: the missing layer

Each inter-agent handoff should include a structured contract:

- payload schema,
- confidence score,
- unresolved questions,
- source references,
- explicit assumptions.

If assumptions are not declared, they become hidden failure points.

## Communication format matters

Free-form text is human-friendly but machine-ambiguous.
For repeated workflows, prefer mixed format:

- human-readable summary,
- machine-readable JSON block.

This supports both review and automation.

## Quality gates and circuit breakers

Never let an agent chain run indefinitely without checkpoints.

Add gates:

- Gate 1: scope validation,
- Gate 2: evidence sufficiency,
- Gate 3: policy compliance,
- Gate 4: release approval.

Add circuit breakers:

- low confidence,
- conflicting evidence,
- missing mandatory fields,
- policy uncertainty.

On trigger: pause and escalate.

## Field example: procurement assistant

A company built a multi-agent procurement flow:
intake -> vendor research -> proposal summary -> recommendation.

Initial version used loose text handoffs.
Result: recommendations lacked comparable criteria and occasionally ignored mandatory procurement rules.

After introducing handoff contracts + gate checks:

- comparison quality improved,
- policy misses dropped,
- human review became faster because outputs were consistent.

The models remained identical.
The workflow contract changed the outcome.

## Anti-patterns

### 1) Over-agenting
Creating too many specialist agents before validating basic chain reliability.

### 2) Hidden retries
Agent quietly re-runs itself until output “looks good,” masking instability.

### 3) No ownership of failures
When a result is wrong, nobody knows which stage violated criteria.

### 4) Missing cost observability
Token/tool costs per stage not tracked, making optimisation impossible.

## Practical drill: redesign one chain

For one existing multi-agent workflow:

1. Map current stages and outputs.
2. Define formal handoff schema at each stage.
3. Add one quality gate and one circuit breaker.
4. Run 15 real cases.
5. Measure: error rate, human review time, total cost per run.

Keep what improves all three dimensions, not just one.

## Governance is part of design

As workflows grow, orchestration decisions become governance decisions:

- who can approve exceptions,
- who changes rubric,
- who owns source quality,
- who audits incidents.

If governance is not explicit, orchestration drifts into tribal knowledge.

## The core idea

Multi-agent performance is not a function of agent count.
It is a function of handoff quality.

Get handoffs right and average models look excellent.
Get handoffs wrong and excellent models look broken.

Keep this line in your playbook:

**In agent systems, the interface is the architecture.**
