# Unsafe Rust: Respect the Blast Radius

The fastest way to lose credibility in a Rust interview is to sound excited about `unsafe` for the wrong reasons.
`unsafe` is not a badge.
It is a liability boundary.

Safe Rust gives strong guarantees by default.
`unsafe` says, “I will uphold these invariants manually.”
If I cannot state the invariants clearly, I do not proceed.

That posture usually reassures senior interviewers.
They are evaluating judgment, not bravado.

I keep `unsafe` discussion grounded in legitimate cases:
- FFI boundaries with C libraries;
- carefully audited performance primitives;
- low-level data structures where safe abstractions are not yet available;
- interaction with hardware or runtime internals.

Even then, I narrow scope aggressively.
Small `unsafe` blocks.
Documented invariants.
Safe wrapper APIs around the dangerous core.
This is what happens next whenever `unsafe` enters the design.

If asked for process, I describe one.
- prove need with profiling or capability gap;
- minimise unsafe surface area;
- add focused tests and property checks around invariants;
- require peer review from engineers fluent in low-level semantics.

A concise interview line:
“`unsafe` is acceptable when risk is bounded, invariants are explicit, and the performance gain is measurable.”

I also state what I will not do.
I will not reach for `unsafe` to bypass borrow-checker discomfort in routine application code.
That doesn’t work for me.

For continuity with prior chapters, [Error Handling: No Drama, Just Control](./15_rust_error_handling_no_drama_just_control.md) carries the same philosophy: explicit boundaries, explicit policy, explicit consequences.

In well-run teams, `unsafe` is treated like production incident access.
Limited, logged, justified, and reviewed.
Respect the blast radius, and it can be a precise tool.
Ignore it, and the language cannot save you.
