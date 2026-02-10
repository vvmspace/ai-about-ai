# Instruction Stacks That Don’t Collapse

Most prompts fail because instruction hierarchy is unclear, not because prompts are short.

When hard rules, style preferences, and output requirements are mixed together, models produce unstable results.

## Build prompts as ordered stacks

A reliable stack has five layers:

1. **Role and objective**
2. **Hard constraints** (legal/compliance/technical)
3. **Process requirements**
4. **Output contract** (explicit schema)
5. **Style guidance**

If style appears above constraints, risk increases immediately.

## System vs user responsibilities

- **System level**: stable policies and non-negotiable rules.
- **User level**: case-specific inputs and changing details.

This separation prevents accidental policy overwrite.

## The conflict line you should always include

Add explicit behaviour for uncertainty:

> If constraints conflict or required data is missing, explain the conflict and request clarification.

Without this, models often invent confident answers.

## Common anti-patterns

- “Instruction soup” in one paragraph
- Critical rules hidden in narrative text
- “Try to” used where “must” is required
- No explicit output format

## Fast review checklist

Before shipping, confirm:

- Constraints are explicit and prioritised
- Output schema is unambiguous
- Conflict handling is defined
- Pass/fail can be evaluated objectively

The key idea:

**A prompt without hierarchy is a policy without governance.**

---

Continue in depth: [Instruction Stacks](../ai_about_ai/03_prompt_engineering_instruction_stacks.md).
