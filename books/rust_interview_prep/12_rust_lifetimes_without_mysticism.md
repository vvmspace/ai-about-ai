# Lifetimes Without Mysticism

The word “lifetime” frightens otherwise sensible engineers.
I understand why.
It sounds like compiler theology.
In practice, it is bookkeeping.

A lifetime answers one practical question:
How long is this reference guaranteed to stay valid?
Nothing more exotic than that.

I treat lifetimes as contracts between caller and callee.
If I return a reference, I must prove the source outlives the return value.
If I cannot prove it clearly, I return owned data instead.

In interview rounds, this posture saves time.
I do not chase ornate annotations first.
I redesign APIs so ownership flow is obvious.
The compiler then needs fewer explanations.

A classic example:

```rust
fn pick<'a>(left: &'a str, right: &'a str, choose_left: bool) -> &'a str {
    if choose_left { left } else { right }
}
```

Here, one lifetime parameter says both inputs and output share the same validity horizon.
Readable, defensible, and boring in the best way.

Where candidates stumble is accidental coupling.
They tie unrelated references to one lifetime, then wonder why borrow scopes explode.
I keep relationships explicit and minimal.
Only values that must be coupled get coupled.

I also remember the interview objective.
They are not hiring me to write the most ornate lifetime signature in Europe.
They are hiring judgment under constraints.

So my sequence is:
- start with owned types for clarity;
- introduce references where allocation or copying matters;
- annotate lifetimes only when inference cannot carry intent.

If a question becomes annotation-heavy, I say so directly.
“I can express this with explicit lifetimes, but I’d prefer reshaping the function boundary to make ownership simpler.”

That usually lands well.
It demonstrates that I optimise for maintainability, not ritual.

If you want a practical bridge from ownership basics, revisit [Ownership: The Rule That Bites First](./10_rust_ownership_the_rule_that_bites_first.md).
Ownership explains *why* lifetimes exist.
Lifetimes explain *where* borrowed data remains safe.

The secret is disappointingly plain.
Lifetimes are not magic.
They are timestamps on references.
Read them that way, and most confusion evaporates.
