# Networking on the Hot Path

Network code is wonderfully democratic.
It punishes everyone who assumes the wire is cheap.
I had learned that before my first trading interview, and it saved me several minutes of embarrassment.

On the hot path, networking choices are latency choices.
Protocol framing, buffering, batching, and parse strategy all leave fingerprints on p99.
I discuss them as operational trade-offs, not textbook trivia.

Interview baseline:
- choose transport according to delivery semantics, not habit;
- keep message framing explicit and parse-friendly;
- minimise copies across boundaries;
- define reconnect and retry policy before failure arrives.

TCP versus UDP questions appear regularly.
I answer with context.
TCP offers ordered reliable delivery with head-of-line consequences.
UDP offers lower overhead and fewer guarantees, so recovery logic moves up the stack.
Neither is universally superior.
The workload decides.

I also mention batching carefully.
Micro-batching can improve throughput and reduce syscall overhead.
Over-batching can increase queueing delay and harm tail latency.
The right batch size is measured, not guessed.

In Rust interview terms, I keep memory and parsing in view.
Avoid gratuitous allocations, prefer reusable buffers where safe, and treat parse errors as policy events, not surprises.
Bad frames should be observable and bounded.

For conceptual continuity, [Memory and Allocation Behavior](./17_rust_memory_and_allocation_behavior.md) remains relevant here; network throughput often fails first on allocation patterns rather than socket API choices.

A practical line I use when asked how to optimise network handling:
“I profile copy cost, parse cost, and queue delay separately before changing transport-level assumptions.”

Hot-path networking rewards engineers who respect constraints.
Elegant abstractions are welcome.
Unmeasured packet mythology is not.
