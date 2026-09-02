---
title: "When to Trust an Open Source Library: A Solo Builder's Due-Diligence Rule"
date: 2026-09-02T09:00:00+08:00
draft: false
tags: ["open source", "dependencies", "supply chain", "solo builder", "npm", "security"]
description: "\"It's free and it's popular\" is how a solo builder inherits someone else's abandoned project — or a credential-stealing worm. Here's the 5-point checklist to run before you npm install, in 30 minutes."
cover:
  image: "cover-open-source-dependency.png"
  alt: "Judging an open source dependency — a decision rule for solo builders"
translationKey: "open-source-dependency"
---

There's a moment every solo builder has had: you find a library that does *exactly* the thing you need, it's free, it has thousands of stars, and `npm install` is one keystroke away. It feels like the fastest possible decision you'll make all week.

That moment is the most expensive place to be fast.

A dependency isn't a purchase — it's a *relationship*. You don't pay for it up front; you inherit it. You inherit its bugs, its security posture, its maintenance schedule, and — the part nobody thinks about until it's too late — its *custody problem*. When the single maintainer who wrote it walks away, or gets their GitHub account taken over, it doesn't stop being your code. It becomes your code that you can no longer maintain.

Here's the rule a solo builder can actually run: **five checks, thirty minutes, before you trust a library with your product.**

## The cost is never the license fee. It's the casualty you inherit.

Open source feels free because there's no invoice. But the real cost shows up in three ways, and only one of them is money:

**Abandonment.** A library goes quiet — no commits for eighteen months, open issues piling up — and you're now maintaining a codebase you didn't write, in a language you may not know deeply, with no tests you can lean on. Nobody "chargebacks" an abandoned dependency; you just eat the hours.

**Protest and sabotage.** Sometimes the maintainer doesn't leave — they *burn it down*. In January 2022, the developer of `faker.js` and `colors.js` — two libraries thousands of projects depended on — deliberately broke them in protest over companies profiting off his unpaid work. Overnight, a library that "just worked" returned corrupted output, and builds failed across the internet. A solo builder with no fallback watched their product break because one person, who they'd never met, woke up angry.

**Compromise.** This is the one that keeps getting bigger. In March 2024, the XZ Utils backdoor nearly shipped a supply-chain attack into half the Linux servers on the planet — a years-long, patient infiltration of a maintainer relationship. And on August 4, 2026, an attacker compromised the maintainer account behind `keyv` and its `cacheable` family of packages — some with hundreds of millions of weekly downloads — and used it to push a credential-stealing worm across 444 packages in a matter of hours. A single compromised account, and "popular" became "poisoned."

None of these are arguments against open source. They're arguments against *blind* open source. The library isn't the risk. The *relationship* is.

## The five checks (thirty minutes, before you install)

You don't need an enterprise security team. You need to answer five questions, and you can do it in half an hour with a browser and a terminal.

**1. Bus factor — how many people actually maintain this?**
Look at the commit history. Is there *one* name, or a distributed group? A library with a single maintainer has a bus factor of one — that person gets hit by a bus, burns out, or gets compromised, and the library is done. This is the single highest-signal check. One active name = treat with extra caution; a rotating set of contributors over years = healthy.

**2. Last-commit cadence — is this alive, zombie, or dead?**
A living library commits regularly enough that security patches land. A *zombie* library is the worst kind: it still downloads millions of times a week, but nobody's actually maintaining it. This is disturbingly common — the OSSRA report has pegged the share of codebases containing *unmaintained* (zombie) components as high as 90%+ in recent years. Check the last commit date. Eighteen months of silence with open security issues is your answer, regardless of star count.

**3. Maintainer identity — is this a person I can verify, or a handle?**
Healthy projects have an identifiable human (or organization) behind them, ideally with two-factor authentication enabled — because MFA is the single biggest thing standing between that maintainer and the kind of account takeover that happened to `keyv`. A project whose maintainer is an anonymous handle with no history, no blog, no employer, is a red flag. Not always malicious — but always unauditable.

**4. Dependency-tree size — how much am I actually inheriting?**
That "small" library ships with its own dependencies, and those have dependencies. Run `npm ls` and look at the tree. A "one-tiny-utility" package that pulls in 400 transitive dependencies means you're inheriting 400 relationships you didn't research — any one of which carries the same abandonment or compromise risk. The smaller the tree, the fewer things can burn down your product overnight.

**5. License fit — can I actually use this the way I want to?**
Not every "open source" license is permissive. Copyleft licenses (like GPL) can impose obligations on *your* code if you distribute it. A common solo-builder mistake is assuming "open source = I can do whatever I want." Read the license — this one takes two minutes and prevents a legal headache you can't un-ship.

## What to do with the answer

The checklist isn't a pass/fail gate — it's a *grading rubric* that tells you how to treat each dependency:

- **Passes all five** (distributed maintainers, active commits, verifiable + MFA'd identity, small tree, permissive license) → use it freely. This is a genuine commodity; outsource it.
- **Fails on maintenance or bus-factor but is mission-critical** → this is your [reuse-vs-rebuild custody tension](/posts/reuse-vs-rebuild/). If it's central to your product and you can't risk it, you either fork it or rebuild it — because *owning* the weak dependency means owning its downtime.
- **Fails on identity or license** → walk away. There is no feature worth inheriting an unauditable relationship or a legal obligation over.

The point isn't paranoia. It's that the decision to add a dependency is a *custody* decision, not a cost decision — and a solo builder has nobody to delegate that custody to. You are the CISO, the maintainer of last resort, and the person who gets paged at 3am. Thirty minutes of due diligence is what turns "I hope this keeps working" into "I know exactly what I own."

## The reframe worth keeping

"Free and popular" is a marketing line, not a risk assessment. The library that feels like the fastest decision of your week is the one that quietly becomes the slowest liability of your year.

Run the five checks. Then install the thing — or don't — with the only thing that actually protects a solo builder: *knowing what you own.*

## Sources

- SafeDep. "npm Worm Poisons keyv, cacheable and 400+ Other Packages Across Twelve Organisations." Aug 4, 2026. — 2,234 poisoned versions across 444 package names, originating from one compromised maintainer GitHub account.
- Socket Research. "Popular npm Packages in the keyv and Cacheable Namespaces Compromised in Active Supply Chain Attack." Aug 4, 2026. — Maintainer account takeover; `preinstall` scripts that run credential-stealing code before a project's own code.
- Aikido Security. "Keyv and friends compromised in npm supply chain attack." Aug 4, 2026. — 444 packages / 1,381 versions, >2 billion monthly installs; `cacheable` family (flat-cache ~565M/mo, file-entry-cache ~557M/mo) all swept in.
- The Hacker News. "Keyv-Linked npm Worm Poisons Hundreds of Packages." Aug 4, 2026. — SafeDep later count: 1,684 poisoned versions / 420 names / nine organizations; cross-org propagation every 2–7 minutes.
- Synopsys Open Source Security & Risk Analysis (OSSRA). — ~90%+ of audited codebases contain unmaintained ("zombie") open-source components; cited for the zombie-dependency prevalence, downshifted as a directional range rather than an exact figure.
- XZ Utils backdoor (CVE-2024-3094), Mar 2024. — A multi-year infiltration of a maintainer relationship that nearly shipped a supply-chain backdoor into Linux distributions.
- `faker.js` / `colors.js` maintainer sabotage (Marak Squires), Jan 2022. — Maintainer deliberately broke both libraries in protest; thousands of dependent builds failed.
