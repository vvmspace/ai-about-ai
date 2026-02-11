# Agent-to-Agent Interaction Protocols

When two agents collaborate without protocol,
you do not get teamwork.
You get polite entropy.

Confident tone is easy.
Clean responsibility transfer is rare.

## The handshake model

Every inter-agent interaction needs a handshake:

1. **Intent** — what the sender needs.
2. **Payload** — structured artefact.
3. **Confidence** — calibrated certainty.
4. **Open risks** — unresolved edges.
5. **Expected action** — approve, transform, or escalate.

No handshake, no handoff.

## Message design rules

Keep messages dual-format:

- brief human summary,
- strict machine-readable block.

The summary keeps operators fast.
The structure keeps pipelines reliable.

## Clarification budget

Let’s be clear:
“ask unlimited follow-ups” destroys throughput.

Give each receiver a clarification budget, for example:

- up to three questions,
- then proceed with explicit assumptions,
- or escalate if mandatory fields are missing.

That prevents infinite loops disguised as diligence.

## Trust is computed, not assumed

Assign reliability scores per sender based on:

- schema adherence,
- historical correction rate,
- evidence quality,
- latency consistency.

Then route work accordingly.

High-risk tasks should not depend on low-reliability senders,
no matter how elegant their prose appears.

## Conflict resolution protocol

Agent A says “ship.”
Agent B says “block.”

Here is how this works in mature systems:

- compare against rubric,
- score evidence strength,
- trigger tiebreak agent or human reviewer,
- log decision and rationale.

Without this, teams resolve conflict by charisma.
That is not governance.

## Observability signals that matter

Track metrics that reveal coordination quality:

- handoff rejection rate,
- clarification count per task,
- assumption density,
- escalation frequency,
- cost per accepted artefact.

If these stay invisible,
optimisation is theatre.

## Failure-first protocol testing

Before production, run deliberately broken handoffs:

- missing required fields,
- contradictory confidence markers,
- stale references,
- unsupported policy claims.

Then verify receiver behaviour:

- asks within clarification budget,
- applies safe assumptions when allowed,
- escalates when boundaries are crossed.

If the protocol only works on tidy examples,
it is not ready.

## Operator override language

When a human intervenes,
the override message should be explicit:

- what decision changed,
- why it changed,
- how long the override remains valid,
- which future cases it should affect.

Quiet overrides create policy drift.
Structured overrides create institutional memory.

## Practical protocol card

For your next workflow, define:

- one payload schema,
- one confidence rubric,
- one escalation trigger,
- one max retry rule.

Run 20 tasks.
Then audit where protocol prevented failure.

The uncomfortable conclusion is usually the same:
the bottleneck was not intelligence.
It was interface hygiene.

## The core idea

Agent collaboration quality is protocol quality.

Not number of agents.
Not model branding.

Protocol first.
Performance follows.
