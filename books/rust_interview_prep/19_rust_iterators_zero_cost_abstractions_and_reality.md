# Iterators, Zero-Cost Abstractions, and Reality

I like elegant iterator chains.
I also like predictable latency.
Fortunately, those preferences are not mutually exclusive.

Rust iterators are called zero-cost abstractions for a reason.
In many cases, the compiler inlines aggressively and emits code comparable to manual loops.
The phrase “in many cases” matters.

In interviews, I avoid ideology.
I explain intent and cost.
If an iterator pipeline is clear and measurable, I keep it.
If it obscures control flow in a critical section, I simplify.

A readable example:

```rust
let approved: Vec<&Order> = orders
    .iter()
    .filter(|o| o.is_valid())
    .take(limit)
    .collect();
```

This is compact and usually efficient.
But if the pipeline grows into a puzzle, I split stages.
Readability is a reliability tool.

Interviewers sometimes press with, “Wouldn’t a loop be faster?”
My answer: maybe, maybe not.
I benchmark before rewriting expressive code into imperative noise.
And I pay attention to allocation side effects around `collect()`.

I also mention short-circuiting methods (`any`, `find`, `position`) because they express intent and can reduce unnecessary work.
Clear intent makes optimisation and debugging easier later.

There is a practical bridge to [Memory and Allocation Behavior](./17_rust_memory_and_allocation_behavior.md):
iterator style is only half the story;
allocation patterns decide much of the latency reality.

My interview principle is stable.
Use abstractions that keep reasoning sharp.
Measure when performance claims appear.
Refactor only where evidence points.

Elegant code is welcome.
Unmeasured certainty is not.
