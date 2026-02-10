# Tools, Permissions, and Safe Autonomy

The moment an agent can do something in the world,
it stops being a chat interface and becomes an operational actor.

## Safe autonomy begins with threat modelling

Before giving any agent a tool, ask four questions:

## Principle of least privilege, applied properly

“Least privilege” is often repeated and rarely implemented well.

- default read-only,
- narrowly scoped writes,

## Separate planning from execution

A robust architecture separates:

- **planner component** (decides what to do),
- **policy layer** (checks if it is allowed),

## Logging that actually helps after incidents

Every tool call should log:

- actor identity,
- timestamp,

---

Continue in depth: [Tools, Permissions, Safety](../ai_about_ai/13_agents_tools_permissions_safety.md).
