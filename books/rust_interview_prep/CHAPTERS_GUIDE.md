# Rust Interview Prep — Chapters Guide (45 Chapters)

This guide defines a 45-chapter arc for a short, high-impact interview-prep book in English.
The reader is a capable engineer with limited Rust writing experience, preparing for a high-stakes role in trading infrastructure.

Story frame: each chapter feels like part of one elegant operation — from reconnaissance to final offer.
Narrative voice: first person, calm, tactical, slightly amused.

---

## Act I — Reconnaissance (1–9)

### 01. The Call Before Dawn
Focus: The opening moment when I receive the interview invitation and realize this is not a casual backend role. Set stakes (live capital, latency, ownership), emotional baseline, and mission framing.

### 02. Reading the Terrain, Not the Brochure
Focus: How to dissect a job description like an operator: separate marketing language from technical demands. Extract core capabilities: determinism, throughput, jitter control, production ownership.

### 03. Inventory of Weapons
Focus: Honest skills audit. I map what I know well (general backend, debugging, architecture) and what is weak (Rust fluency). Show how to convert weakness into a clear sprint plan.

### 04. The CV Is Already Testimony
Focus: Why every line in CV can become a question. Build a method to defend each bullet with one story, one metric, one technical decision, and one lesson.

### 05. Two-Day War Plan
Focus: A concrete preparation schedule for less than 48 hours. Time blocks for Rust fundamentals, async/concurrency, system design, SQL, frontend, and mock answers.

### 06. Interviews Are Observation Under Load
Focus: Psychological model of interviews. They are not just Q&A; they test reasoning under pressure. Explain composure routines and how to think aloud effectively.

### 07. Talking to Humans, Not Checklists
Focus: Recruiter and hiring-manager conversations. How to ask precise questions about team, latency budget, incident ownership, and success criteria.

### 08. Building My Prep Notebook
Focus: Create a compact notebook: key Rust rules, common pitfalls, benchmark phrases, STAR stories, CV defense snippets, and questions to ask interviewers.

### 09. What Success Looks Like
Focus: Define target performance for each round (not perfection). Build pass criteria: clarity, trade-off thinking, correctness-first mindset, production awareness.

---

## Act II — Rust Core Discipline (10–20)

### 10. Ownership: The Rule That Bites First
Focus: Explain ownership from first principles for someone who almost never wrote Rust. Include why it exists, how it improves reliability, and interview-style examples.

### 11. Borrowing Without Bleeding
Focus: Immutable and mutable borrowing, aliasing rules, and common borrow checker errors. Teach practical heuristics to fix code during interviews.

### 12. Lifetimes Without Mysticism
Focus: Intuition for lifetimes, when to annotate, when to redesign API instead. Focus on interview-relevant understanding, not academic depth.

### 13. Structs, Enums, and Domain Shape
Focus: Modeling data for trading/event systems. Why enums are powerful in Rust. Show expressive domain modeling and safer state representation.

### 14. Pattern Matching as a Thinking Tool
Focus: `match`, destructuring, exhaustiveness, and avoiding fragile branching logic. Include examples of robust error and state handling.

### 15. Error Handling: No Drama, Just Control
Focus: `Result`, `Option`, `?`, custom error types, and when to fail fast. Frame error handling as reliability engineering.

### 16. Traits: Interfaces With Teeth
Focus: Traits, trait bounds, generics, and practical polymorphism. Explain when to choose generics vs trait objects in interview answers.

### 17. Memory and Allocation Behavior
Focus: Stack vs heap, `Vec` growth, `String` costs, cloning pitfalls, and allocation minimization. Tie directly to latency variance in trading systems.

### 18. Smart Pointers in the Real World
Focus: `Box`, `Rc`, `Arc`, `RefCell`, `Mutex` — what they solve and what they cost. Include “what not to use by default” guidance.

### 19. Iterators, Zero-Cost Abstractions, and Reality
Focus: How iterator pipelines stay expressive yet performant. Discuss when explicit loops are clearer and how to justify either choice in interviews.

### 20. Unsafe Rust: Respect the Blast Radius
Focus: What `unsafe` means, invariants, common justified use-cases, and why interviewers care about judgment more than bravado.

---

## Act III — Concurrency, Async, and Performance (21–33)

### 21. Concurrency Mental Models
Focus: Threads, tasks, message passing, shared state. Build intuition for choosing architecture under load.

### 22. Tokio Execution Model, Plainly
Focus: How async runtime scheduling works, cooperative multitasking, and implications for latency-sensitive code.

### 23. Async Rust Without Hand-Waving
Focus: `async/.await`, futures, pinning intuition, cancellation, and common beginner mistakes that appear in interviews.

### 24. Channels and Backpressure
Focus: `mpsc`, bounded queues, producer-consumer patterns, and preventing silent overload in event pipelines.

### 25. Locking, Contention, and Throughput
Focus: Mutex/RwLock trade-offs, sharding state, reducing critical sections, and identifying contention hotspots.

### 26. Lock-Free and Low-Contention Patterns
Focus: Atomics basics, ring buffers, ownership transfer patterns, and where lock-free is useful vs reckless.

### 27. Determinism Under Burst Load
Focus: Designing systems that behave predictably under spikes: queue policy, load shedding, ordering guarantees, bounded work.

### 28. Networking on the Hot Path
Focus: TCP/UDP trade-offs, framing protocols, batching, and minimizing copy/parse overhead in market data paths.

### 29. Profiling Before Opinions
Focus: Practical workflow with flamegraphs/benchmarks. Teach how to answer “how would you optimize this?” with evidence, not folklore.

### 30. Benchmark Design That Interviewers Trust
Focus: Micro vs macro benchmarks, warmup, noise control, and interpreting percentile latency, not just average.

### 31. Cache Locality and Data-Oriented Thinking
Focus: CPU cache effects, layout choices, and why algorithmic complexity alone is not enough for low-latency systems.

### 32. Failure Modes in Real-Time Pipelines
Focus: Timeouts, retries, duplicates, out-of-order messages, poison queues, and graceful degradation.

### 33. Production Readiness Checklist
Focus: Logging, metrics, alerting, canarying, rollback plans, and ownership expectations in production-critical teams.

---

## Act IV — Full-Stack and System Design Rounds (34–40)

### 34. Architecture Interview: Drawing Under Pressure
Focus: A repeatable whiteboard method: requirements, bottlenecks, components, critical path, failure handling, observability.

### 35. Trading Pipeline End-to-End
Focus: Design a sample flow: strategy signal → risk checks → order routing → execution feedback → UI updates. Include latency budget reasoning.

### 36. SQL Beyond CRUD
Focus: Query plans, indexing strategy, hot/cold data, time-series patterns, and how to discuss optimization trade-offs clearly.

### 37. Next.js for Backend Engineers
Focus: Essential frontend concepts for this role: rendering modes, data fetching, state boundaries, and real-time dashboard concerns.

### 38. API Contracts Between Rust and Frontend
Focus: Stable schemas, versioning, error envelopes, pagination/streaming choices, and avoiding accidental coupling.

### 39. Testing Strategy Across the Stack
Focus: Unit, integration, load, and property tests. What to automate first when time is short.

### 40. Debugging Stories They Actually Remember
Focus: How to narrate difficult incidents with structure: symptom, hypothesis, instrumentation, fix, prevention.

---

## Act V — Interview Performance and Offer Decision (41–45)

### 41. Behavioral Questions as Signal Engineering
Focus: Convert “tell me about a time” into concise proof of ownership, judgment, and collaboration under stress.

### 42. The Rust Live-Coding Round
Focus: Tactics for coding with partial Rust fluency: narrate intent, keep scope small, compile mentally, and recover from borrow-checker blocks gracefully.

### 43. The Questions I Ask Them
Focus: High-quality reverse interview questions about latency targets, incident process, technical debt, and decision autonomy.

### 44. Negotiation With Composure
Focus: Offer discussion, compensation framing, scope clarity, and boundary-setting without drama.

### 45. After the Handshake
Focus: 30/60/90-day onboarding plan if hired; post-mortem plan if rejected. End with agency, craft, and long-game career positioning.

---

## Notes for Writing Each Full Chapter

- Keep first-person perspective throughout.
- Begin with a short scene or observation.
- Transition into one core insight.
- Provide concrete, reusable tactics.
- End with one crisp closing line.
- Keep technical examples realistic for trading/high-load systems.
- Ensure each chapter helps the reader both pass interviews and defend the CV.
