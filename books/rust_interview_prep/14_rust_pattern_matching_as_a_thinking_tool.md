# Pattern Matching as a Thinking Tool

The first time I used `match` properly in Rust, I noticed something inconvenient.
It exposed every branch I had hoped to ignore.
Annoying for my ego.
Excellent for production quality.

Pattern matching is not just syntax.
It is a way to force complete reasoning.
In interview settings, complete reasoning is a rare and very visible signal.

When I handle state machines, protocol messages, or error variants, I default to `match`.
Why?
Because exhaustiveness checks turn forgotten paths into compile errors.
I prefer that conversation with a compiler over a pager at 3 a.m.

A common interview fragment:

```rust
match state {
    OrderState::New => validate_and_route(),
    OrderState::RiskRejected { reason } => log_rejection(reason),
    OrderState::Routed { venue } => await_execution(venue),
    OrderState::Filled { qty, px } => persist_fill(qty, px),
    OrderState::Cancelled => finalize_cancel(),
}
```

No implicit fall-through.
No vague “should never happen.”
Every case gets a decision.

I also use pattern matching for error control:
- recoverable errors get bounded retries;
- policy errors stop early;
- unknown errors are surfaced with context.

Interviewers often ask whether `if let` is enough.
Sometimes, yes.
For single-happy-path extraction, `if let` is tidy.
For full branch accountability, `match` is safer and clearer.

My rule is this:
Use the construct that makes unhandled reality impossible to hide.
That tends to be `match`.

When pressure rises, pattern matching helps me think aloud.
I can narrate each branch with consequence.
“If this is `RiskRejected`, we skip routing and emit structured telemetry for Trading visibility.”

That style reads as operational maturity.
Because it is.

Pattern matching is less about elegance than honesty.
It forces the code to admit the world has multiple outcomes.
And interviews, like production, reward engineers who prepare for all of them.
