# Agent Societies: Roles, Incentives, and Control

Single-agent demos feel magical.
Production systems feel political.

The moment you run many agents,
you are designing an organisation.

Ignore that,
and the architecture behaves like office gossip with APIs.

## Role topology before tooling

Define roles by accountability, not personality:

- planner,
- researcher,
- synthesiser,
- critic,
- releaser.

Each role should own a failure mode.
If no failure mode is owned,
failures drift between desks.

## Incentive design for agents

Agents optimise what you reward.
Yes, including synthetic workers.

If reward equals speed,
quality falls.
If reward equals zero errors,
throughput collapses.

Use blended scorecards:

- correctness,
- latency,
- cost,
- policy compliance.

Balanced incentives produce stable systems.

## Separation of powers

Do not let one agent:

- generate,
- validate,
- and approve

the same critical output.

That is a governance own goal.

Apply structural friction:
creator and evaluator must be separate roles.

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

Agents learn to mirror each other’s assumptions.
Outputs look coherent and wrong.

### Reviewer fatigue

One critic agent becomes the bottleneck,
then quietly becomes a rubber stamp.

### Responsibility blur

No single role is accountable for final defects.

### Incentive mismatch

The system rewards confident verbosity over verifiable evidence.

## Design move: rotate critics

Rotate evaluation agents by task class.

Benefits:

- reduced pattern lock-in,
- better defect discovery,
- lower systematic blind spots.

Predictability in process,
variability in scrutiny.

## Human operator as constitutional layer

Human-in-the-loop is not manual fallback.
It is constitutional oversight.

Humans should define:

- what cannot be delegated,
- what needs two-party agreement,
- what incidents trigger process reform.

Calm authority beats reactive micromanagement.

## One-week implementation sprint

- Day 1: map roles and accountabilities.
- Day 2: define scorecards.
- Day 3: split creation and approval powers.
- Day 4: add conflict/tiebreak protocol.
- Day 5: run live tasks and measure.

End-of-week question:
which defects disappeared because control became explicit?

## The core idea

A multi-agent stack is an operating model.

Design it like an organisation,
or it will behave like one by accident.
