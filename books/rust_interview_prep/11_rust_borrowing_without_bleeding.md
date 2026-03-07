# Borrowing Without Bleeding

I once watched a candidate solve an elegant problem, then lose ten minutes in a duel with the borrow checker.
The code was clever.
The ownership story was not.

Borrowing is where Rust stops being theoretical and starts charging rent.
You can either learn the rules early, or pay in interview time later.
I prefer the first option.

The core constraint is blunt.
At any point, you may have:
- many immutable borrows, or
- one mutable borrow,
- but not both at once.

That is not cruelty.
It is how Rust prevents data races and invisible aliasing.
In trading systems, invisible aliasing is just delayed failure with better branding.

In interviews, I narrate this upfront.
“I’ll keep mutation scoped and short, then return to immutable reads for the rest of the flow.”

That sentence does two useful things.
It shows I know the rule.
It shows I design around it.

A common trap appears in loops:

```rust
for order in orders.iter_mut() {
    // mutate order
    // then attempt to also read orders elsewhere in same scope
}
```

If I need broader reads, I split phases.
Phase one mutates what is necessary.
Phase two reads from an immutable view.
No heroic tricks, just clean borrowing boundaries.

Another trap is returning references to temporary values.
If a function builds data locally and returns a reference, Rust objects politely.
Quite right too.
I either return owned data or pass in a buffer the caller owns.

My interview heuristic is simple:
- borrow for observation;
- own for transfer;
- mutate in narrow corridors.

When code fights these rules, I pause and reframe the data flow.
Trying to outsmart the borrow checker during a live round is usually theatrical self-harm.
Redesign is faster.

If pressure rises, I use this recovery line:
“Let me reduce lifetime overlap and shrink mutable scope; the logic is fine, the ownership boundaries need tidying.”

Interviewers hear judgment in that sentence.
And judgment is the scarce resource.

Borrowing feels strict until you notice what it buys: predictable reasoning under load.
Once that clicks, the rules stop feeling punitive.
They start feeling professional.
