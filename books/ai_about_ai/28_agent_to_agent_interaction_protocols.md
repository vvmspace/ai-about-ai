# Agent-to-Agent Interaction Protocols

When two agents collaborate without protocol,
you do not get teamwork.
You get polite entropy.

Agents sounding confident is easy.
Agents transferring responsibility cleanly is rare.

## The handshake model

Every inter-agent interaction needs a handshake:

1. **Intent** — what the sender needs.
2. **Payload** — structured artefact.
3. **Confidence** — calibrated certainty.
4. **Open risks** — unresolved edges.
5. **Expected action** — approve, transform, or escalate.

No handshake, no handoff.

In practical terms, this is where *multi-agent systems* either scale or quietly fail.

## Message design rules

Keep messages dual-format:

- brief human summary,
- strict machine block.

The summary keeps operators fast.
The structured block keeps pipelines reliable.

If you only write for humans, automation breaks.
If you only write for machines, oversight slows to a crawl.

## Clarification budget

Let’s be clear:
“ask unlimited follow-ups” kills throughput.

Give each receiver a clarification budget, for example:

- up to 3 questions,
- then proceed with explicit assumptions,
- or escalate if mandatory fields are missing.

This avoids infinite loops disguised as diligence.

## Trust is computed, not assumed

Assign reliability scores per sender based on:

- schema adherence,
- historical correction rate,
- evidence quality,
- latency consistency.

Then route work accordingly.

High-risk tasks should not depend on low-reliability agents,
no matter how elegant their prose looks.

## Conflict resolution protocol

Agent A says “ship.”
Agent B says “block.”

Here’s what’s going to happen in mature systems:

- compare against rubric,
- score evidence strength,
- trigger tiebreak agent or human reviewer,
- log the decision and rationale.

Without this, teams resolve conflicts by charisma.
That is not governance.

## Observability signals that matter

Track these metrics:

- handoff rejection rate,
- clarification count per task,
- assumption density,
- escalation frequency,
- cost per accepted artefact.

If those are invisible,
optimisation is theatre.

This metric stack also improves operating decisions,
because teams can tune protocols with evidence rather than opinion.

## Practical protocol card

For your next workflow, define:

- one payload schema,
- one confidence rubric,
- one escalation trigger,
- one max retry rule.

Run 20 tasks.
Then audit where protocol prevented failure.

You will usually discover this uncomfortable truth:
the bottleneck was never “intelligence.”
It was interface hygiene.

## Operator checklist (fast version)

Before enabling autonomous loops, verify:

- schema fields are mandatory where needed,
- confidence labels map to explicit thresholds,
- escalation owners are named,
- retries have a hard cap,
- logs preserve decision traces.

If one item is missing,
be prepared for ambiguous failures.

Agent collaboration quality is protocol quality.

Not number of agents.
Not model branding.

Protocol first.
Performance follows.

For organisational design on top of these protocols, continue to [Agent Societies: Roles, Incentives, and Control](./29_agent_societies_roles_incentives_and_control.md).
