# Error Handling: No Drama, Just Control

A surprising number of interview solutions are perfect until reality appears.
Reality usually arrives as an error path.
Then the architecture starts bargaining with hope.

In Rust, error handling is not a side quest.
It is the control plane.
`Result` and `Option` make failure explicit, so policy decisions cannot hide in comments.

My default posture is conservative.
- expected absence uses `Option`;
- operational failure uses `Result`;
- panic is for truly unrecoverable invariants.

If everything panics, nothing is production-grade.
If everything is swallowed, nothing is observable.
We keep this simple.

In interviews, I narrate failure policy before implementation details.
“Transient network errors get bounded retries with jitter; validation errors fail fast; downstream timeouts surface with context and request ID.”

Then I show compact mechanics:

```rust
fn parse_qty(raw: &str) -> Result<u64, String> {
    raw.parse::<u64>()
        .map_err(|e| format!("invalid quantity '{raw}': {e}"))
}
```

The value is not the parser.
The value is explicit propagation and contextual error messages.
Those messages become incident clues later.

I also favour domain error enums once a service grows:
- `ValidationError`
- `RiskCheckError`
- `RoutingError`
- `StorageError`

Typed errors clarify ownership boundaries between components.
They also make retry logic less reckless.
You cannot retry your way out of bad input.

When asked about the `?` operator, I answer plainly.
It is not laziness.
It is controlled propagation with readable flow.
But propagation without policy is incomplete, so boundaries still need mapping and logging.

If you want continuity with prior chapters, pair this with [Pattern Matching as a Thinking Tool](./14_rust_pattern_matching_as_a_thinking_tool.md).
Good matching defines branches.
Good error handling defines what each branch means operationally.

Reliable systems are not the ones that never fail.
They are the ones that fail with structure, signal, and recovery options.
In interview rooms, that distinction separates coders from operators.
