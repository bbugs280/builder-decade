---
title: "The Day Your AI Vendor Shuts Down: Exit Cost for Solo Builders"
translationKey: "ai-vendor-exit-cost"
date: 2026-10-19T09:00:00+08:00
lastmod: 2026-10-19T09:00:00+08:00
draft: false
tags: ["ai api", "vendor lock-in", "deprecation", "solo builder", "technical debt", "model retirement"]
description: "One retired model endpoint can break a shipped app overnight. Here's how to price the exit before you rent the brain."
cover:
  image: "cover-ai-vendor-exit-cost.png"
  alt: "A workshop shelf of blank unlabelled crates, one slot empty where a component used to sit"
---

An app can ship, work perfectly, and pass every test — and then stop working because somebody else changed a string.

Not your code. Not your deploy. A model name in an API call. The endpoint stayed up; the model behind it was retired, and the API politely returned a 404 in a JSON envelope, as though your request had always been malformed.

This is not a rare edge case. It is the normal operating rhythm of a market where models are released, superseded and withdrawn on a schedule you do not control. And it lands differently on a solo builder than on a company: a team gets a vendor email that routes to a platform group and a migration ticket. One person gets a user message saying the feature "doesn't work anymore."

## You can vendor a library. You cannot vendor a model

The instinct, when you have been burned by a dependency before, is to reach for the standard playbook: pin the version, or maintain a fork.

Both work on open source, and neither works here.

```
LIBRARY                           MODEL ENDPOINT
publish the source       yes      no
run it yourself          yes      no
patch it yourself        yes      no
fork it and move on      yes      no
version stay available   yes      no — the version is a served endpoint
```

You are not depending on a package. You are depending on **a service that someone else operates, prices, and may withdraw** — and whose version numbers are not yours to hold still. `pin` gives you reproducibility of your request, not availability of their response.

That distinction is the whole post. The harness you build is genuinely yours. The brain inside it is rented, and the rental can end.

## The exit cost nobody budgets

Every AI build has two bills. The one you track is the running bill — tokens, requests, the monthly line item. The one that hurts is the exit bill, and it only ever appears once, at the worst possible moment.

Exit cost is everything you must do, on the day a model or vendor goes away, to keep the product alive:

```
DETECT      know it broke, before a user tells you
LOCATE      find every call site — not just the obvious one
REWRITE     re-fit prompts, params, output shapes to a new model
RE-EVAL     prove the new model is not worse on YOUR cases
SHIP        deploy, then handle the quality drift you did not predict
```

That is not a bill that scales with how much AI you use. It scales with **how many places you used it and how much you never wrote down.** A hobby script with one call has a five-minute exit. A shipped app with six call sites, bespoke prompts per site, and no evaluation set has a multi-day exit — and it arrives unannounced.

The trap is that exit cost is **invisible until it is due**. Nothing in normal operation tells you what it will be. It is the technical-debt shape, one layer down: you cannot measure it by reading the code, only by trying to leave.

## What actually makes an exit cheap

Five things, in the order they save the most time. All of them are cheap to do now and expensive to do later.

**1. One call site, not six.** Route every model interaction through a single internal function — your own thin wrapper. Then "the model changed" is one edit, not a search. This is the single highest-leverage item on the list, and it is the one most solo builds skip because a second, slightly different call is easier in the moment.

**2. Name the model, don't hardcode the string.** A model identifier scattered across files is a deployment hazard: you cannot change what you cannot find. One config value, read once.

**3. Keep an evaluation set of ten real cases.** Not a benchmark — ten inputs from your actual users, with the outputs you accepted. This is what turns "did the new model get worse?" from a feeling into a diff. Without it, every migration is a leap of faith, and the fear of that leap is what keeps people pinned to a dead endpoint.

**4. Treat the prompt as product code.** Version it, review it, keep it in the repo next to the call it belongs to. A prompt that exists only in a vendor dashboard is not yours and cannot be migrated.

**5. Watch for withdrawal, don't assume permanence.** A model-list endpoint or a changelog page you check monthly is a thirty-minute-a-year insurance premium. The failure mode is not "the vendor disappeared" — it is "the vendor deprecated one model and you found out from a user."

## The uncomfortable conclusion

None of this is a reason not to build on an API. The alternative — train and serve your own model — is not available to one person for most tasks, and pretending otherwise is its own kind of bluff.

The point is narrower and more useful: **the model being a commodity does not make your dependency on it cheap.** Commodity pricing and exit cost are independent variables. A vendor can cut prices by 90% and still retire the exact endpoint your product runs on. The bill you optimise and the bill that ends your product are different bills.

So price the exit at build time, while it costs an afternoon. It is the one piece of this stack you can actually de-risk, because the failure is not exotic — it is scheduled, and it will arrive whether or not you planned for it.
