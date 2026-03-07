# Smart Pointers in the Real World

Smart pointers sound comforting until you choose the wrong one in production.
Then they become very educational.
Usually at inconvenient hours.

I treat each pointer type as a contract with cost.
No contract, no default.

`Box<T>` is straightforward ownership on the heap.
Useful for recursive types and controlled indirection.
Low drama.

`Rc<T>` enables shared ownership in single-threaded contexts.
`Arc<T>` does the same across threads with atomic reference counting overhead.
That overhead is often acceptable.
On very hot paths, it deserves measurement.

`RefCell<T>` gives interior mutability with runtime borrow checks.
Powerful, but it moves some guarantees from compile time to runtime.
I use it deliberately, not casually.

`Mutex<T>` coordinates mutable access across threads.
Correctness first, always.
But lock scope and contention policy matter if latency is a first-class requirement.

In interviews, I give a decision sequence:
- can plain ownership solve this?
- if sharing is needed, is it single-thread (`Rc`) or multi-thread (`Arc`)?
- if mutability is shared, what is lock scope and contention risk?

That sequence prevents “Arc<Mutex<...>> by reflex.”
I’m not convinced reflex architecture is senior behaviour.

Sometimes `Arc<Mutex<T>>` is exactly right.
The key is to articulate why, and where contention will be bounded.
If I can’t do that, I redesign.

A brief interview phrase I rely on:
“I’ll start with the simplest ownership model, then introduce shared-state primitives only where the data flow demands them.”

That sounds conservative because it is.
Conservative design is often faster to stabilise.

Smart pointers are excellent tools.
They are not personality traits.
Choose them like you choose risk limits: explicitly, with consequences in view.
