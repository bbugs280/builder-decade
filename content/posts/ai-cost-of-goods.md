---
title: "The One-Person Company Spending $1M a Year on AI"
date: 2026-10-17T08:00:00+08:00
lastmod: 2026-10-17T08:00:00+08:00
draft: false
tags: ["ai cost", "solo founder", "cost of goods", "one-person company", "ai leverage", "unit economics"]
description: "A one-person company is spending over $1M a year on AI and making $3M. The ratio underneath is the part nobody quotes — and it is the number that decides whether AI leverage is real."
translationKey: "ai-cost-of-goods"
cover:
  image: "cover-ai-cost-of-goods.png"
  alt: "A single wooden chair dwarfed by a floor-to-ceiling wall of blank cardboard crates, one warm lamp — one person's scale beside a wall of cost"
---

Earlier this month, the CEO of Perplexity mentioned something in passing that deserves more attention than it got. Aravind Srinivas said there's **one solopreneur — literally a one-person company — spending upwards of a million dollars a year** on the product, and **making about $3 million a year** doing it.

The story got retold as an AI-leverage anecdote. One person! Seven figures of spend! Automate everything!

Which it is. But the retelling skips the only number that matters, because the two mentioned in the same sentence are not the story. The story is their **ratio**.

## The number nobody quotes

Divide the two figures and you get a business, not an anecdote.

```text
AI spend        $1,000,000   per year
Revenue         $3,000,000   per year
─────────────────────────────────────
Gross           $2,000,000   before any other cost
COGS ratio          ~33%     of revenue
Headcount              1
```

**Thirty-three percent cost of goods, on one pair of hands.** Not 3%. Not "negligible." A *third of every dollar* goes to the thing that does the work.

That is a perfectly respectable business — plenty of healthy software companies run 25–40% gross margins. But it is not the frictionless, near-free leverage the genre insists on. It's a real cost base with a real margin, and it behaves like manufacturing, not like software.

## Why the ratio is the useful number

Three reasons this framing beats the headline.

**It makes AI spend comparable to something.** "A million dollars" is a scary number that means nothing on its own. "A third of revenue" means you can hold it against payroll, against hosting, against customer acquisition. It becomes a line item instead of a shock.

**It scales inversely with efficiency, which is the actual skill.** The same $3M revenue at half the spend is a 17% COGS business — dramatically healthier. The interesting question isn't whether one person *can* spend a million. It's **whether the spend is buying revenue or just buying motion.** Those look identical on a dashboard and completely different on a P&L.

**It kills the "AI is basically free" assumption before it sets.** Every solo builder I know has, at some point, mentally rounded AI spend to zero because the subscription is $20 a month. The subscription is not the cost. The subscription is the *entry fee* to a metered system that bills you in proportion to how much work you ask it to do. At small scale the rounding is harmless. At scale it *is* the business model.

## The split that decides everything

A million dollars of AI spend can be one of two things.

**Cost of goods.** You buy inference, you sell an outcome, the margin between them is yours. Spend rises with revenue and the ratio stays roughly flat — or improves with better routing. This is a business.

**Cost of motion.** You buy inference, and it produces drafts, explorations, retries, and things that were nearly right. Revenue doesn't move. This is a very expensive hobby with a dashboard.

The distinction is not about *how much* you spend, and it is not about which model you use. It's whether you can trace spend to a unit of revenue. If you can't — and most solo builders can't, because nobody makes them — then the million dollars is a meter running next to a business that is, at best, adjacent to it.

> The one-person company spending $1M a year is not impressive because the number is large. It's impressive if the number is *earned back*. Otherwise it's just a bigger version of the same mistake a $50-a-month builder makes — spending on motion and calling it leverage.

## What this means if you're not spending a million

The useful part of this story is not aspirational. It's a prompt to compute a number you have probably never computed.

Most solo builders know their subscription costs and their hosting bill. Almost none know their **AI spend as a percentage of revenue**. It's the one line of the P&L that arrived recently, sits on a card with a variable amount on it, and gets a glance rather than a calculation.

Write the two numbers down — this month's AI spend, this month's revenue — and divide. Whatever the answer, you now have a baseline, and a baseline is the only thing that lets you tell the difference between leverage and motion.

The calculator below does the arithmetic, and it will also show you the ratio at the scale of the story above, so you can see where you sit against a business that is genuinely working at this size.

{{< solo-calc mode="cogs" >}}

## The uncomfortable version of the question

There's a version of this that's more useful than "can I spend a million dollars on AI," and it's harder to sit with.

**Of the money you spend on AI, how much of it produced something a customer paid for?**

Not "helped me work." Not "saved me time." Not "made the build faster." Those are all real, and none of them is revenue. The million-dollar solopreneur can answer that question, at least in aggregate — $1M in, $3M out, the ratio is the answer whether or not anyone likes it.

If you can't answer it, that's not a reason to stop using AI. It's a reason to start measuring, because the ratio you don't measure is the one that quietly decides your margin for you.

That measurement starts one level down from this post. The ratio here is the company-scale view; the discipline that produces a number worth dividing is built project by project, where a single build can quietly [creep past its own token budget](/posts/ai-api-cost-creep/) before anyone adds up the column. Set the number before the first line of code — [treat the build as running on a meter](/posts/metered-build/), not a flat monthly plan — and the ratio above stops being a surprise at the end of the quarter and becomes something you were steering all along.

## Sources

- **Perplexity CEO Aravind Srinivas**, interview clip published October 2026 — the one-person company spending "upwards of a million dollars a year" and making "$3 million a year by automating." Reported secondhand via social clip; the figures are his characterisation, not an audited filing. Treated here as a **stated order of magnitude**, which is all the ratio argument needs.
- **Perplexity business context** (valuation ~$20B, ~$750M annualised revenue as of August 2026, 5× YoY) — as reported in the same interview coverage. Included only to establish that the company quoting the number is a real, large business rather than a promotional claim.
- **Stripe Atlas / Carta data on solo founding** — 63% of new C corps formed through Stripe Atlas in Q2 2026 were solo-founded; solo founding up 53% since 2019. Context for why one-person companies at this scale are becoming a category rather than an outlier. Both datasets measure different lifecycle moments (incorporation vs. equity), which explains the spread between them.
- **Caveat carried deliberately:** the spend and revenue figures come from a platform CEO describing a customer, not from that customer's books. Nobody has audited them. This post uses them as a **round ratio** (~1:3), not as precise figures — and the argument holds at 1:2.5 or 1:3.5 equally well.
