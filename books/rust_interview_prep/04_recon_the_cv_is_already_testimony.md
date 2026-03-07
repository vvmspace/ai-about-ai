# The CV Is Already Testimony

Most candidates treat the CV as a ticket to the interview.
I treat it as sworn testimony.
Once submitted, every line is admissible evidence.

If I claim “high-performance systems”, they can ask for bottlenecks, profiling method, rollback strategy, and exact trade-offs.
If I mention Rust, they can ask where ownership constraints had improved reliability and where they had slowed delivery.
Quite right, frankly.

So I perform what I call forensic rehearsal.
For each role on my CV, I prepare one compact story in this structure:
- the problem pressure;
- the technical move I made;
- the measurable result;
- the lesson I now carry.

Take a full-stack project with heavy user interaction.
The weak version of the story is: “I built features and improved performance.”
The strong version is precise: where latency had appeared, how instrumentation exposed it, which change reduced it, and what trade-off I accepted.

Interviewers are not only measuring competence.
They are checking narrative integrity.
If the timeline drifts or metrics sound decorative, trust declines quietly.

That is why I align chronology carefully.
When two events matter, I mark sequence cleanly.
For example: by the time we launched the optimisation, the previous queue model had already caused burst-time instability.
Simple, factual, coherent.

I also prepare CV defence for leadership claims.
“Acting CTO” or “Lead Developer” invites governance questions:
- how I prioritised technical debt against delivery;
- how I handled incidents;
- how I set engineering standards under time pressure.

If I cannot answer these with specifics, the title becomes noise.
If I can, the title becomes proof of operational maturity.

A useful trick is the mirror question.
For each CV bullet, I ask:
“What would make me doubt this if I were the interviewer?”
Then I pre-empt that doubt with details.

For Rust-specific credibility, I keep three stories ready:
1. a concurrency decision that reduced risk;
2. a memory/allocation decision tied to latency behaviour;
3. a production issue where observability changed the outcome.

For frontend credibility, I keep two:
1. preserving UI stability under high-frequency updates;
2. designing user-facing behaviour for degraded backend conditions.

This matters because the role spans both sides.
They need someone who can connect engine-room constraints to trader-facing experience.
My CV should tell that same story without contradiction.

Finally, I prepare “clean admissions.”
If a technology appears in my stack but depth is moderate, I say so directly and pivot to what I did concretely.
Controlled honesty signals judgement.
Bluff signals future incident reports.

By the time I finish this exercise, the CV no longer feels like a list.
It feels like a prepared case.
And in interview rooms, prepared cases travel well.
