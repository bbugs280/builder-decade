---
title: "SEO for Indie Hackers: Rank for the Query That Pays, Skip the Rest"
translationKey: "seo-for-indie-hackers"
date: 2026-08-29T00:00:00+08:00
lastmod: 2026-09-02T08:00:00+08:00
draft: false
tags: ["solo builder", "seo", "organic traffic", "distribution", "long tail"]
description: "Most SEO advice is written for teams with a year to burn. The solo-builder version is narrower: win one high-intent query per product, ship the technical floor once, and let the page compound while you build. Here's the decision rule, not the 40-post content calendar."
cover:
  image: "cover-seo-for-indie-hackers.png"
  alt: "One query, one page, compounding traffic for the solo builder"
---

Most SEO advice is written for companies with a content team and a year to burn. The indie hacker has neither — you have a Stripe account, a weekend cadence, and a product that needs signups *now*. So here's the honest version: the SEO that matters to you is a **subset** of the SEO that matters to everyone else. You skip the parts that need scale, and you go hard on the parts that need *precision*.

The difference is a decision, not a tactic. A team buys a keyword tool and produces forty posts hoping one ranks. A solo builder can't afford that — so instead you pick **one query** and own it.

## The core idea: one query, one page, one decision

Forget blogging every week. Forget building topical authority across a whole category. As a solo builder, your goal is to rank for **one high-intent query per product** — the phrase someone types when they're sixty seconds from paying.

That query has a shape. It contains a **problem**, not a topic ("send cold email without landing in spam," not "email marketing"). It implies **purchase intent** — the person is solving, not browsing. And you can answer it **completely on one page**, better than whatever ranks third today. If you can't beat the top three results on a single page, it's the wrong query.

This is the opposite of the volume game. You don't need 10,000 searches a month; you need *your* one hundred searches a month where everyone who lands clicks "sign up." Low volume plus high intent beats high volume plus zero intent, every time — and it's winnable by a new domain with no authority.

## The compounding you can't buy

There's one number that explains why SEO beats every other channel for someone with no ad budget: **it compounds, and nothing else does.**

A paid ad stops the moment the money stops. A Product Hunt launch spikes and fades in 48 hours. But a page that ranks keeps pulling visitors in month three, month twelve, month twenty-four — while you sleep, while you code, while you work the day job. It's the only distribution channel that appreciates instead of decaying. Five pages, each quietly earning a hundred visitors a month, is a thousand visitors that cost you nothing after the writing.

That's why the timeline discipline matters. SEO is slow — three to six months before meaningful traffic, not three weeks. The trap is treating that as a reason to *defer* it. It's the opposite: the slowness is the reason to **start now**, before you need the traffic, and let the early pages mature in the background while you build the next thing.

## What to actually build

If you only write three kinds of pages for the rest of the year, write these:

**1. The comparison or "alternative" page.** "X vs. Y" and "best [tool] alternatives" capture the highest-converting searcher there is: someone who has already decided to buy *something* in your category, and is shopping. You're not convincing them of a need — you're winning an existing decision. This is where solo products win their first hundred users, because it's where intent is already resolved.

**2. The specific use-case page.** "How to [do one concrete task] with [your product]." These capture the mid-funnel searcher who already has the adjacent tool and needs the last piece. Lower volume, near-zero competition, and it converts because it names their exact problem.

**3. The long-tail question you already answered.** Every support ticket, every "how do I…" in your DMs, is a query nobody's ranking for yet. Turn the answered ones into pages. Low competition, and each one compounds.

Three pages done well outperform thirty done badly. The decision is narrow-and-rank, never wide-and-fade.

## Own the AI answer, not just the blue link

There's a second audience now, and it's the quiet one. When someone asks ChatGPT or Perplexity "what's the best tool for X," the model cites the pages it can *read cleanly*. A solo builder's single tight, factual page has an advantage here that big sites don't: LLMs favor dense, specific, self-contained content over vague marketing prose — and you can write that cheaply because you *know* the problem deeply.

Winning that citation is a backlink and a brand mention in one, for zero additional spend. It costs three cheap things: clean semantic HTML, `og:` tags with an image URL that actually resolves, and a `llms.txt` file describing your site. That last one is the single highest-leverage AI optimisation there is — one markdown file.

## The technical floor (do once, never again)

- **Search Console, day one.** Not a nice-to-have — it's the only data source that tells you which queries actually bring people to you. Without it, Google finds your new pages on its own slow schedule and you're flying blind. This step is manual; you have to verify the property yourself.
- **One clean H1, one target phrase.** Title tag ≈ H1 ≈ the searcher's phrase, phrased naturally. No stuffing.
- **Structured data.** `Article` or `Product` schema with a real author and a logo that resolves. Miss these and your rich results and AI citations silently fail.
- **Fast and mobile.** Page speed is a ranking signal and, more importantly, a *conversion* signal. If it's not instant, fix that before you write another word.

## What to skip

- **Keyword-volume chasing.** A 10,000-search keyword you'll never rank for drives zero traffic. Your fifty searches of people who click "sign up" are worth more.
- **The forty-post content calendar.** That's the team play. You're one person. One page per product, done completely.
- **Backlink campaigns.** One genuinely useful page, mentioned in the communities you're already in, beats six months of cold outreach.

## The one-line version

> Pick one query your customer types when they're about to buy. Own it with one page. Submit your sitemap. Then stop doing SEO and go ship the next thing.

*This is the quiet half of the distribution pair — where [getting your first users](/posts/how-to-get-first-users-solo/) is the social playbook that meets buyers where they already gather, this is the passive engine that captures them when they're *already searching*. Both run on the same principle: show, don't sell. For the build side of the triangle, see [why one person can now ship](/posts/one-person-team/).*

---

## Sources

- Carta — Solo Founders Report 2025: the solo-founded share of new US startups rose from 23.7% (2019) to 36.3% (H1 2025) — the structural shift that makes a "one page per product" SEO discipline realistic for a single person rather than a content team.
- Stripe Atlas — Startups in 2025 Year in Review: 20% of startups charged their first customer within 30 days (up from 8% in 2020) — the collapsed time-to-first-dollar that makes *capturing existing search intent* (comparison/use-case pages) more urgent than building fresh demand.
- The "organic search compounds while paid/social spikes decay" contrast and the "comparison pages convert highest" claim are drawn from the observable behavior of bootstrapped SaaS founders in public communities (Indie Hackers, X build-in-public) rather than a single citable study — treat them as observed pattern, not measured effect. Specific traffic figures are not cited because reliable primary numbers vary too widely by niche to state responsibly.
