# Traits: Interfaces With Teeth

A polite trap appears in many Rust interviews.
They ask about abstractions.
Candidates answer with slogans about “clean architecture.”
Then someone asks what dispatch model they just chose.
Silence follows.

Traits are Rust’s interface mechanism, yes.
But they are also performance and API-shape decisions.
If I forget that, I design elegance first and pay latency later.

I frame traits in three layers.

Layer one: capability contracts.
A trait declares what behaviour a type must provide.
Useful, but ordinary.

Layer two: composition.
Trait bounds let me assemble behaviour without inheritance gymnastics.
`T: RiskCheck + RouteOrder` says more than three paragraphs of architecture prose.

Layer three: dispatch cost model.
This is where interviews get interesting.
Generics usually mean static dispatch and monomorphisation.
Trait objects (`dyn Trait`) mean dynamic dispatch and one extra indirection.
Neither is “always correct.”
Both are tools.

A compact example:

```rust
trait RiskCheck {
    fn approve(&self, order: &Order) -> bool;
}

fn process<C: RiskCheck>(checker: &C, order: &Order) -> bool {
    checker.approve(order)
}
```

In hot paths, I default to generics first.
Static dispatch gives predictable optimisation opportunities.
At plugin boundaries, I may accept `dyn Trait` for flexibility.
I say this explicitly in interviews.
Judgment beats dogma.

I also avoid over-abstracting too early.
Three traits and five blanket impls for one service is not sophistication.
It is future archaeology.

If the room asks, “When would you choose trait objects?” I answer plainly:
- runtime-selected strategies;
- heterogeneous collections of behaviour;
- boundaries where binary size from monomorphisation is becoming costly.

Then I add the boundary.
For the avoidance of doubt, I do not put dynamic dispatch on the most latency-sensitive inner loop without measurements.

Traits are called interfaces, but they are really leverage.
Used well, they make systems clearer and safer.
Used carelessly, they hide cost behind elegant signatures.
In this business, hidden cost is still cost.
