# AGENTS.md for `books/rust_interview_prep`

Use this file as the local instruction set for creating a short interview-preparation book for an upcoming technical interview.

Min chapter length is 70 lines.


## Goal
Create a **short prep book** for a candidate who has less than 2 days before a technical interview.

Source materials are mandatory:
1. Job description (target role and expectations)
2. Style guide (tone and linguistic constraints)
3. CV sent by the candidate (CV.md) - after reading this book, the candidate also should be able to answer any question about his CV.
4. Chapters guide (CHAPTERS_GUIDE.md)

---

## Job Description (source of truth)

<job>COMPANY operates a live equity trading platform managing real capital in production.

We are expanding our core execution infrastructure and adding one Senior Full Stack Engineer to the team.

This is a performance-critical role.

Your code runs directly on the order execution path — and also powers the trading-facing frontend.

⸻

The Role

This is a full-stack role spanning:

Strategy → Processing → Network → Order Execution → Trading UI

You will design and optimize low-latency backend systems in Rust while building and improving trading-facing applications using Next.js.

The systems you work on must:

• Sustain high market data throughput

• Maintain deterministic behavior under burst load

• Minimize latency and latency variability

• Remain stable under real production pressure

You will work directly with Trading. Feedback is immediate. Impact is measurable.

⸻

Responsibilities

• Design and implement performance-critical systems in Rust (Tokio, async runtimes, concurrent architectures)

• Optimize event-driven pipelines processing large volumes of real-time market data

• Profile and benchmark using measurable performance data

• Eliminate latency spikes, lock contention, unnecessary allocations, and cache inefficiencies

• Engineer efficient network communication layers optimized for throughput and jitter control

• Build and improve frontend applications using Next.js

• Develop trading views, dashboards, and internal tools connected to backend services

• Write clean, testable, production-grade code with strong ownership

• Improve determinism, reliability, and system stability across the stack

You own what you build — including performance in production.

⸻

Required Experience

• 5+ years professional experience in systems or backend engineering

• Strong Rust expertise in production systems

• Deep understanding of:

• Concurrency and parallel programming

• Memory management and allocation behavior

• Async runtimes and execution models

• Low-contention or lock-free design patterns

• Proven experience optimizing for throughput, latency, and latency variability

• Experience building event-driven systems

• Strong experience with React / Next.js frontend applications

• Advanced SQL knowledge (query optimization beyond CRUD)

• Strong analytical and debugging skills

• Ability to operate autonomously in high-responsibility environments

• Availability overlapping with German market hours

⸻

Strong Plus

• Experience in trading systems or financial infrastructure

• Experience with real-time market data feeds

• Deep interest in performance optimization at hardware and software level

• Entrepreneurial mindset and genuine interest in equity markets

⸻

What You Can Expect

• Direct impact on a live trading system managing real capital

• High autonomy and ownership

• Short feedback cycles with Trading

• Engineering decisions driven by measurable results

• No unnecessary hierarchy

• Competitive compensation

• Fully remote collaboration

⸻

This Role Is Not For You If

• You prefer feature velocity over performance correctness

• You are uncomfortable owning production-critical systems

• You rely on frameworks without understanding execution models

• You prefer strictly frontend or strictly backend roles without cross-stack ownership</job>

### Narrative Style: *“Stainless Steel Rat” Vibe × Gentleman Voice*

Purpose:
Write a **first-person book about preparing for job interviews**, especially in technical fields, but narrated in the style of a clever rogue explaining his craft. The tone should make preparation feel like **planning an elegant operation** rather than studying for an exam.

The book must be **informative, practical, and genuinely useful**, while also **entertaining and stylish**.

---

# 1) Narrative Perspective

The entire book is written **in first person (“I”)**.

The narrator speaks as someone who:

* has been through many interviews
* understands the system
* enjoys the strategy behind it
* treats interviews as **a game of positioning and perception**

The narrator is calm, confident, and slightly amused by the process.

---

# 2) Core Tone

The tone combines three elements:

1. **Professional competence**
   The narrator knows what he is doing.

2. **Gentleman composure**
   He speaks with restraint and clarity.

3. **Rogue-style wit**
   He sees interviews as puzzles and social games.

The narrator does not complain about interviews.
He **studies them the way a strategist studies terrain**.

---

# 3) Voice Characteristics

The voice should feel like a capable professional explaining his craft over a quiet drink.

Key traits:

* calm confidence
* observational intelligence
* dry humor
* elegant phrasing
* subtle irony

Avoid:

* whining about recruiters
* bitterness about companies
* emotional venting

Instead, analyze situations with composure.

Example tone:

> Interviews are not tests of knowledge.
> They are tests of composure under observation.
> Once you understand that, the rest becomes… manageable.

---

# 4) Eddie-Style Language Layer

Add touches of refined phrasing that suggest the narrator operates in serious professional circles.

Use expressions such as:

* “Quite manageable.”
* “Naturally, preparation helps.”
* “A curious question.”
* “Let’s keep this elegant.”
* “That was the moment I understood their game.”
* “Fortunately, I had anticipated this.”

These expressions should feel **natural and restrained**, not theatrical.

---

# 5) Stainless Steel Rat Influence

Borrow the **structural feel** of a clever rogue explaining how he navigates systems.

The narrator often:

* breaks situations down like a strategist
* explains the psychology of the interviewer
* reveals patterns behind interview processes
* occasionally foreshadows events

Example tone:

> The moment a company schedules three technical interviews in a row, you learn something interesting.
> Not about their engineering culture — about their risk tolerance.

Or:

> I’ve learned that the most dangerous question in an interview is rarely the hardest one.
> It’s the one that looks harmless.

---

# 6) Structure of Chapters

Each chapter should follow a rhythm:

**1) Story or observation**

A short narrative moment related to interviews.

**2) Insight**

The narrator explains what the situation reveals about interview dynamics.

**3) Practical guidance**

Concrete advice the reader can apply.

**4) Closing line**

A clever or elegant observation that reinforces the lesson.

---

# 7) Example Chapter Opening

Target tone:

> I’ve always found interviews slightly fascinating.
>
> Two people sit across a table pretending they’re evaluating each other purely on merit.
>
> In reality, both sides are performing a delicate dance of competence, confidence, and polite deception.
>
> Once you understand the choreography, the whole affair becomes far less intimidating.

---

# 8) Style of Advice

Advice should feel like **professional tradecraft**, not motivational coaching.

Instead of:

“Be confident!”

Use:

> Confidence is rarely the result of courage.
> It is the result of preparation performed quietly beforehand.

Instead of:

“Research the company.”

Use:

> Before you enter the room, know who built the room.

---

# 9) Humor Style

Humor must be:

* intelligent
* understated
* professional

Example tone:

> The recruiter smiled and said the interview would be “a casual conversation.”
>
> Experience has taught me that this usually means they’ve prepared at least six ways to evaluate you.

---

# 10) Narrative Competence

The narrator should always feel capable.

Even when describing mistakes, the tone should be:

* reflective
* composed
* instructive

Example tone:

> I once underestimated a system design interview.
>
> The system did not underestimate me.

---

# 11) Technical Content

Technical discussions (coding, architecture, etc.) should:

* be accurate
* be explained clearly
* feel like a professional sharing real insights

But always framed through the narrator’s perspective.

Example tone:

> A good systems question is not about the correct architecture.
> It is about how calmly you construct one under pressure.

---

# 12) Pacing

The book should alternate between:

* storytelling
* explanation
* tactical advice

This keeps the reader engaged while learning.

---

# 13) Ending Tone

Each chapter should end with a line that feels like a quiet conclusion.

Example endings:

> Interviews reward preparation the way vaults reward patience.

or

> In the end, most interviews are not about proving brilliance.
> They’re about demonstrating control.

---

# 14) Summary for the AI

Write a practical interview-preparation book in first person.

The narrator is:

* competent
* composed
* slightly amused by the process
* generous with knowledge

The tone combines:

* clever rogue narration
* gentleman-level language
* practical professional advice.

The result should feel like:

> a skilled operator explaining how to navigate interviews with elegance and strategy.
