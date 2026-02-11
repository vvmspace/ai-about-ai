# Agent Societies: Roles, Incentives, and Control

Single-agent demos feel magical.
Production systems feel political.

The moment you run many agents,
you are designing an organisation.

Ignore that,
and your architecture behaves like office gossip with APIs.

## Role topology before tooling

Define roles by accountability, not personality:

- planner,
- researcher,
- synthesiser,
- critic,
- releaser.

Each role must own a failure mode.
If no failure mode is owned,
failures float.

A role without accountability is decoration.
It looks sophisticated and fixes nothing.

## Incentive design for agents

Agents optimise what you reward.
Yes, even synthetic workers.

If reward = speed,
quality drops.
If reward = zero errors,
throughput collapses.

Use blended scorecards:

- correctness,
- latency,
- cost,
- policy compliance.

Balanced incentives produce stable systems.

This is the practical backbone of **agent governance** in production.

## Separation of powers

Do not let one agent:

- generate,
- validate,
- and approve

the same critical output.

That is a governance own goal.

Use structural friction:
creator and evaluator must be different roles.

## The calm-control loop

For high-stakes tasks, run this loop:

1. draft,
2. adversarial review,
3. policy gate,
4. release decision.

Fast enough to ship.
Strict enough to sleep at night.

## Where multi-agent systems quietly fail

### Hidden collusion

Agents learn to echo each other’s assumptions.
Outputs look coherent and wrong.

### Reviewer fatigue

One critic agent becomes bottleneck and rubber stamp.

### Responsibility blur

No single agent is accountable for final defects.

### Incentive mismatch

System rewards verbose confidence over verifiable evidence.

## Design move: rotate critics

Rotate evaluation agents by task class.

Benefits:

- reduces pattern lock-in,
- improves defect discovery,
- lowers systematic blind spots.

Predictability in process,
variability in scrutiny.

## Human operator as constitutional layer

Human-in-the-loop is not “manual fallback.”
It is constitutional oversight.

Humans should define:

- what cannot be delegated,
- what requires two-party agreement,
- what incidents trigger process reform.

Calm authority beats reactive micromanagement.

## 1-week implementation sprint

- Day 1: map roles and accountabilities.
- Day 2: define scorecards.
- Day 3: split creation vs approval powers.
- Day 4: add conflict/tiebreak protocol.
- Day 5: run live tasks + measure.

Week-end question:
which defects disappeared because control became explicit?

## Practical application in a small team

If you only have two operators and limited compute,
start simple:

- one builder agent,
- one critic agent,
- one human approval gate for high-risk outputs.

Then add role granularity only after you can measure failure classes.
That seems slower, but it usually ships faster.

A multi-agent stack is an operating model.

Design it like an organisation,
or it will behave like one by accident.

Then move to [Chapter 30](./30_project_start_prompt_setup_operator_view.md) to set project-start control surfaces that keep this organisation aligned from day one.
