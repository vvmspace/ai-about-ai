# Structs, Enums, and Domain Shape

I have seen fast systems fail because their data model had lied.
Not maliciously.
Just vaguely.
Vagueness is expensive in production.

Rust gives us a better bargain.
`struct` for stable data shape.
`enum` for explicit state variation.
Together, they make illegal states harder to represent.
That is exactly what you want on an order path.

In interviews, I start with domain truth before syntax.
“What states can an order actually be in, and which transitions are forbidden?”
Once that is clear, the types almost write themselves.

A minimal sketch:

```rust
enum OrderState {
    New,
    RiskRejected { reason: String },
    Routed { venue: String },
    Filled { qty: u64, px: i64 },
    Cancelled,
}

struct Order {
    id: u64,
    symbol: String,
    state: OrderState,
}
```

Now behaviour is explicit.
A `Filled` order carries execution data.
A `New` order does not pretend to have it.
That single decision removes entire classes of defensive `if` statements.

Candidates sometimes default to one giant struct with many optional fields.
I’m not convinced.
It compresses complexity into runtime uncertainty.
Enums move that uncertainty into compile-time checks.

I also use newtypes for critical identifiers.
`OrderId(u64)` and `VenueId(u16)` may look ceremonial.
Until someone swaps parameters in a hotfix.
Then they look prudent.

When interviewers ask about trade-offs, I keep it honest.
Richer type models cost a little upfront design time.
They repay it during maintenance, incident response, and onboarding.
On high-stakes systems, that is a very favourable exchange rate.

For the avoidance of doubt, domain modelling is not decoration.
It is latency and reliability work in disguise.
If your types encode reality, your runtime spends less time negotiating ambiguity.
And ambiguity is where expensive bugs breed.
