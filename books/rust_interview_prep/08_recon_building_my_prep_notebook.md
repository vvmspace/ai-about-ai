# Building My Prep Notebook

When preparation time is short, memory becomes a liability.
Under pressure, even obvious facts go missing.
So I build one compact notebook and treat it as mission control.

Not a beautiful notebook.
A useful one.
Portable, brutal, and specific.

I keep six pages.
No more.
Constraint improves quality.

Page one: **Rust core rules**.
Ownership, borrowing limits, mutation boundaries, `Result` discipline, and three examples of borrow-checker fixes.
If I cannot explain a rule in two sentences, I rewrite it.

Page two: async and concurrency map.
I summarise Tokio scheduling assumptions, channel choices, cancellation behaviour, and lock scope warnings.
I include one line in bold: **"Bound queues, or be prepared for delayed failure."**

Page three: performance language.
Throughput, p50/p95/p99, jitter, contention, allocation pressure, cache locality.
No essays.
Only definitions and one practical example each.

Page four: CV defence snippets.
For each major bullet, I store this structure:
- context;
- hard metric;
- technical decision;
- trade-off;
- lesson.

Page five: interview questions for them.
Latency budget, production incident ownership, rollout policy, API contract governance, and success criteria for this role.
A good reverse question is often better than a good closing statement.

Page six: recovery scripts.
Three phrases for uncertainty, two phrases for correction, and one phrase to slow the room without sounding defensive.
My favourite: “Let me restate constraints to avoid solving the wrong problem.”

I review the notebook in short passes.
Morning, late afternoon, final evening.
Ten minutes each.
No marathon rereads.

The notebook is not there to teach me new ideas.
It is there to stabilise recall and language.
In interviews, that distinction matters.

I also annotate links to nearby chapters when helpful, mostly for sequence review.
If I need pressure routines, I jump back to [Interviews Are Observation Under Load](./06_recon_interviews_are_observation_under_load.md).
If I need tight recruiter questions, I revisit [Talking to Humans, Not Checklists](./07_recon_talking_to_humans_not_checklists.md).

By the final night, the notebook becomes psychological leverage.
I do not carry all knowledge in my head.
I carry an organised system that can reload it quickly.

Preparation feels lighter when the brain stops pretending it is perfect storage.
The notebook handles memory.
I handle judgment.
A very fair division of labour.
