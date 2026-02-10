# Memory, State, and Long Tasks

Most agent systems do not fail long-running tasks because models are “not smart enough.”
They fail because **memory** is treated like a bucket.

## Memory is infrastructure

If an agent handles work across hours, days, or weeks,
state management becomes core architecture.

- what is stored,
- where it is stored,

## Three-tier memory model

A practical structure:

## State schemas beat free-form notes

For repeated workflows, represent state in structured fields:

- objective,
- current stage,

## Checkpointing for long tasks

Define checkpoints at fixed intervals or stage transitions.

- summarise progress,
- archive low-value detail,

---

Continue in depth: [Full chapter 14](../ai_about_ai/14_agents_memory_and_state.md).
