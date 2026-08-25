---
title: "Reuse vs Rebuild: The Custody Rule for Solo Builders"
translationKey: "reuse-vs-rebuild"
date: 2026-08-25T00:00:00+08:00
draft: false
tags: ["solo founder", "build vs buy", "one-person company", "cost of ownership", "dependency"]
description: "AI made rebuilding cheap, so build-vs-buy stopped being a cost question and became a custody question. The real cost isn't the first version — it's who owns the thing when the dependency outlives you, or you outlive it. Here's the decision rule for the solo builder."
cover:
  image: "cover-reuse-vs-rebuild.png"
  alt: "Reuse or rebuild — two diverging paths, a custody decision"
---

The build-vs-buy debate is the oldest argument in software, and for years it was boring math: build if the license would cost more than the engineering. AI broke that math. When a solo builder can scaffold in a weekend what used to take a quarter, the *cost* case for reusing something — a library, a SaaS tool, an open-source project — quietly stopped being the deciding factor.

What replaced it is a quieter question: **who owns this thing when it matters?** That's not a cost question. It's a *custody* question — and it's the one that actually decides, in practice, whether your one-person company survives its third year.

## Rebuilding got cheap. Custody did not.

Here's the asymmetry most solo builders miss. AI collapsed the *upfront* cost of writing code. It did almost nothing to the *ongoing* cost of owning code. The industry has known this number for decades and it hasn't moved: **50–80% of the total cost of software ownership is maintenance** — the bug fixes, the security patches, the dependency upgrades, the steady drip of keeping something alive years after the exciting first version. Gartner has put IT spend on maintaining existing systems at 55–80%; the IEEE's number is 60–80%.

So rebuilding is cheap *to start*, but you own it forever. The first commit is free-ish. The thousandth commit — the one four years later, at 11pm, when a library you forked has drifted and the original author abandoned it — is where the real bill lives.

## Reuse is cheap today. But the dependency owns you.

The mirror image is just as dangerous. When you reuse, you offload the maintenance — and hand someone else the keys. The vendor's roadmap becomes your roadmap. Their price increase becomes your cost. Their "we're sunsetting this product" email becomes your emergency.

This is not hypothetical. The data on it is blunt: **Flexera reports 47% of enterprises cite data migration as a significant barrier to switching providers.** That "47%" is the point where a *choice* you made freely hardened into a *position* you can't leave without tearing your own system apart. Custody isn't lost in a dramatic moment. It's lost quietly, in the gap between "we'll use this for now" and "we can't afford to move off it."

## The trap is pricing by build cost alone

Both sides of the old argument make the same error: they price only the *first* version. Build-vs-buy calculators compare the initial build against the first-year subscription. That's the wrong axis.

Count **cost of ownership** instead. A thing you rebuild is cheap to begin and expensive to keep alive forever — maintenance, upgrades, dependency churn, security patching, lock-in you chose, and the compounding cost of riding someone else's roadmap. A thing you reuse is cheap today and owns you tomorrow. The honest comparison isn't build cost vs buy price. It's: **am I renting convenience, or am I paying for custody of something I can't outsource?**

Rebuild is cheap *to start* but you own it forever; reuse is cheap *today* but the dependency owns you. A moat you can't afford to keep alive is no moat at all.

## The custody rule: reuse the commodity, rebuild the moat

The decision isn't "build or buy" as an identity — "I'm a builder" or "I only buy SaaS." It's a custody rule with one axis:

**Reuse whatever is a commodity.** The undifferentiated plumbing — where there's a healthy market of alternatives, where switching is cheap because everyone speaks the same standard, where the thing does the same boring job it did last year. If three vendors could replace it tomorrow and you'd barely notice, you want custody of *none* of it. Don't rebuild it. Pay the subscription and keep your attention for what matters.

**Rebuild only the moat.** The one or two things that *are* your product — the part a competitor can't copy by signing up for the same SaaS you use. That's the only thing worth the forever-maintenance bill, because that's the only thing whose maintenance *is* the business.

## There's a third failure mode: the "not-built-here" reflex

The villain in this frame isn't SaaS, and it isn't open source. It's **not-built-here syndrome** — the sunk-time habit of rebuilding undifferentiated plumbing because rebuilding now *feels* like progress and owning it *feels* like control. A solo builder's scarcest resource isn't money. It's attention, spread across a maintenance surface that only ever grows. Every hour spent re-implementing something a $20/month tool already does is an hour not spent on the moat.

The test is uncomfortable but simple: **if you stopped working on this one thing entirely, would it hurt the business, or would it hurt your ego?** Commodity work usually only wounds the latter.

## The solo-builder version of the rule

For a one-person product team, the rule collapses to something you can actually run:

1. **Commodity?** Buy it or use the open-source project with the healthiest maintainer base — and verify you could leave. If you can't name your exit path, you don't have custody of the choice, the vendor has custody of you.
2. **Moat?** Build it — and know the maintenance bill is real and yours forever. 15–25% of build cost a year is the rough ongoing number. If that bill sounds unaffordable, it means the moat isn't a moat, it's a hobby.
3. **The ambiguous middle?** That's where AI actually changed things. The stuff that *used* to be a real build — glue code, internal tools, integrations — is now cheap enough to rebuild that the "definitely buy" list shrank. But cheap-to-start still isn't cheap-to-keep. Default to reuse until the thing is demonstrably central, then rebuild.

The point isn't that solo builders should rebuild everything or buy everything. It's that the question changed. Twenty years ago you asked "what will it cost to build vs license?" Now the honest question is **"what am I willing to be custodian of, and what am I willing to rent?"** — and most solo builders, most of the time, are renting far more than they realize, and custodian of almost nothing that actually matters.

## Sources

- Gartner — *IT maintenance spending*: organizations spend ~55–80% of IT budgets maintaining existing systems (percent-of-ownership benchmark, widely cited across Gartner's IT key-metrics research).
- IEEE Computer Society — software maintenance accounts for ~60–80% of total software lifecycle cost.
- Standish Group — *CHAOS Report*: ~69% of software projects deliver partial or no value (context for why every rebuild should be treated as a bet, not a certainty).
- Flexera — *State of the Cloud*: 47% of enterprises cite data migration as a significant barrier to switching vendors (the "custody hardens into lock-in" evidence).
- Keyhole Software / industry TCO benchmarks — ongoing maintenance runs roughly 15–25% of initial build cost per year.

*Note on certainty:* the "50–80% maintenance share" figure is a durable industry benchmark (Gartner/IEEE/ISBSG publish overlapping ranges) rather than a single named-study number — treat it as a directional range, not a precise point. The Flexera 47% and Standish 69% figures are from named primary reports.
