# The Questions I Ask Them

At some point they lean back and ask,
"Do you have any questions for us?"
That is not courtesy.
That is another round.

Weak candidates ask about perks too early.
Anxious candidates ask nothing.
I ask questions that reveal operating reality.
If I am going to own production-critical systems, I need facts, not slogans.

I group my questions into four packets.
Latency.
Reliability.
Decision process.
Ownership boundaries.
This keeps the conversation structured even when time is short.

Latency first, because this role lives there.
"Which service currently dominates end-to-end order-path latency at p99?"
"Where do you see the largest latency variance during market open?"
If they cannot answer, I learn something important.
If they can, I learn where I can contribute fastest.

Then reliability.
"What was your last serious trading incident, and what changed afterward?"
This is a curious question, and deliberately so.
Mature teams answer with specifics and corrective mechanisms.
Immature teams answer with reassurance.

I ask about observability with precision.
"Do engineers on this team have direct access to tracing, flamegraphs, and production dashboards?"
Ownership without visibility is theatre.
I do not sign up for theatre.

Next comes decision process.
"Who can stop a release if hot-path risk is unclear?"
"How are trade-offs documented when trading urgency conflicts with architecture hygiene?"
These questions reveal whether engineering judgment is respected when pressure rises.

For full-stack scope, I probe cross-team friction.
"How do backend and frontend agree on schema evolution and rollback policy?"
If they describe stable API contracts, excellent.
If they rely on heroic coordination, I mark risk.
The failure patterns from [API Contracts Between Rust and Frontend](./38_api_contracts_between_rust_and_frontend.md) tend to reappear quickly.

I also ask about onboarding with intent.
"What would success look like in my first 30 days on-call-adjacent work?"
Good answers are concrete.
Named services.
Named metrics.
Named mentors.

Compensation questions are valid, but timing matters.
I discuss them after technical alignment is clear.
Before that, I optimize for fit and mission clarity.
Money is important.
Mismatch is expensive.

There is one question I nearly always include.
"Why did the last strong engineer leave this area, if someone did?"
The pause before the answer is often more informative than the answer itself.

I avoid adversarial posture.
Calm, direct, polite.
I am not interrogating them.
I am reducing uncertainty.
Both sides deserve that.

When answers are vague, I follow up gently.
"Could you walk me through a specific recent example?"
Specifics are hard to fake and easy to trust.

I end with alignment.
"From what you’ve heard today, where do you see my strongest fit, and where would you want deeper proof?"
This invites honest signal exchange before final decisions calcify.

Candidates often forget this point.
The reverse interview is where seniority becomes visible.
Anyone can solve a puzzle on a whiteboard.
Not everyone can evaluate an operating environment with composure.

If I ask well, I either gain conviction or save myself a costly mistake.
Both outcomes are victories.
