---
title: "Which Answer Are You Allowed to Act On? The Line Every Solo Builder Draws by Hand"
translationKey: "trust-scope-reversibility"
date: 2026-10-08T08:00:00+08:00
lastmod: 2026-10-08T08:00:00+08:00
draft: false
tags: ["ai agents", "solo builder", "automation", "delegation", "trust", "one person team", "reversibility"]
description: "The framework for what to hand an agent isn't about how smart the model is. It's reversibility × blast radius × stakes — and here's where the line sits for a one-person build."
cover:
  image: "cover-trust-scope-reversibility.png"
  alt: "A single control panel with one large switch, hand resting on it, about to commit"
---

There's a question every solo builder answers eventually, usually by getting it wrong once:

**Which answers am I allowed to act on without checking?**

Not "which tasks can AI do" — that's a capability question and the answers change every few months. This is a **sorting** question, and it doesn't change with the model. It changes with the *task*.

## The framework — and why it isn't the article

Let me be honest up front, because we do this on every post: **the grading framework itself is not new, and it is not ours.** Regulators, enterprise security teams, and academic groups have all published versions of it. Microsoft's agentic-risk guidance says *require approval for high-risk or irreversible actions*. A recent DeepMind paper on delegation names reversibility as the axis that decides how much authority you can hand over. Practitioners publish permission matrices grading actions by *blast radius × reversibility × stakes*. If you want the general framework, those sources will serve you better than a solo-builder blog, and I'll list them at the bottom so you can check them.

What none of them are written for is **you**: one person, one product, your own credentials, and no compliance department to catch the mistake. So that's the part worth writing. Here's the rule, applied to a one-person build.

## The sorting rule

Score the task on three axes. The **highest** axis sets the grade.

```
REVERSIBILITY   one-click undo  →  recoverable with hours of work  →  irreversible
BLAST RADIUS    only me, local  →  my own business or money        →  someone else
STAKES          trivial         →  money, deadline, trust          →  legal/safety/reputation
```

The result is a grade, and the grade decides the *control*, not the amount of trust:

| grade | what it means | the control |
|---|---|---|
| **G0** | read-only, local, trivial | hand it over — this is what the agent is for |
| **G1** | low blast radius, recoverable | let it run, keep the log |
| **G2** | anything high on one axis | gate it — agent proposes, you fire |
| **G3** | irreversible *and* (external *or* severe) | never unattended — prevent, don't review |

Grade by **real** reversibility, not by whether your editor has an undo button. A shell `rm` is G3 even when your IDE can rewind, because the rewind doesn't cover shell side-effects. This is the same discipline as our post on [why "done" is a claim, not a fact](/posts/done-is-a-claim/) — except that post is about *verifying an output*, and this one is one layer up: **deciding which outputs you were ever allowed to act on unattended in the first place.** A control that holds regardless of whether the agent is honest is not a verification ritual. It's a fence.

{{< solo-calc mode="scope" >}}

## The proof case: the agent that told me I was wrong

Here's the case that made me write this down. Anonymised, because that's how this site works.

I was tracking a cut phase. I believed I was losing weight — my own app showed a down day, then an up day, and I read the trend I wanted to read. I handed the agent **the entire dataset at once**, uncurated, and asked a plain question: am I actually losing, or maintaining?

It came back: *maintaining.* And it adjusted the plan accordingly.

It was right. What matters is **why** it was allowed to be right — and that's the whole point. That answer sat on the safe side of the line for one reason: **the cost of it being wrong was one more week of a plateau.** Cheap to be wrong. Fast to correct. The data was mine. So the agent could hold the pen.

Now imagine the identical model, same confidence, applied to a task on the other side of the line — moving money, sending the email to the client, publishing the page. Nothing about the *model* changed. Only the **reversibility** did. That's the entire argument.

## The part that actually buys you honesty

Here's the counterintuitive bit, and I think it's the real insight:

**The agent is only honest if it gets everything. A curated feed gets curated flattery.**

When I showed the agent my interpretation — the down day, the good news — I was inviting agreement. When I handed it the raw dataset, including the days that contradicted me, it had the material to disagree. **Honesty is a consequence of the exposure, not a property of the model.** You cannot prompt an agent into candour it was never given the data to reach.

Which inverts the usual instinct. The thing to fear isn't an agent with a wide view of your data. It's an agent with a **narrow** one that you've curated into agreement, and that you then act on because it agreed with you. Scope control exists to make *acting* safe — not to keep the agent ignorant.

## What this looks like on a one-person build

Three practical shapes, and none of them is a purchase:

**1. Fence by credential, not by prompt.** The instruction "don't touch production" is a suggestion. Removing the production credential is a fence. If an action is G3, the fix is not a better-worded system prompt — it's that the tool isn't in the box.

**2. Make the agent propose, and make the last step yours.** For G2, the agent can do all of the thinking and none of the committing. Let it assemble the action, tell you what will happen and how it got there, and leave the trigger to you. This is cheap, and it eliminates the whole category of "it acted beyond what I authorised."

**3. The prompt is not the safety net — the fence is.** This is the one that surprises people. A confirmation dialogue does **not** make you a good error-catcher; the research is blunt about it. Gates reduce bad actions, but they barely improve your ability to *catch* one. When the stakes are high enough that you couldn't realistically spot the error in the half-second the prompt is on screen, review is theatre. Prevention beats review every time.

## The reframe

Stop asking whether the agent is good enough to trust. That question has one answer and it goes stale in a quarter.

Ask instead: **if this were wrong, what would it cost me, and could I take it back?** That question has an answer for every task, and the answer doesn't care which model you're running.

The sorting rule quietly does something else, too: it tells you where to *stop supervising*. Everything at G0 and G1 should already be running without you — and every hour you spend watching work at those grades is an hour you didn't spend on the parts only you can do. The fence isn't there to make you slower. It's there so that the stuff above the line can move without you having to hover.

## Sources

- **Which actions are reversible, and what that implies for authority.** — *Intelligent AI Delegation* (Tomašev, Franklin & Osindero, Google DeepMind), which explicitly names **reversibility** as an axis governing how much authority can be delegated, and distinguishes irreversible real-world side effects (executing a trade, deleting a database, sending an external email) from reversible ones (drafting an email, flagging a record).
- **The practical grading method** (`blast radius × reversibility × stakes` → grade → control) is a widely published practitioner pattern; e.g. the LoopRails human-in-the-loop playbook, which also makes the point this post leans on hardest: **a confirmation prompt does not make a human a good error-catcher**, so prevention beats review where the error can't realistically be caught in time.
- **Enterprise agentic-risk guidance.** — Microsoft's *Reduce autonomous agentic AI risk* guidance: apply least privilege and least action, use deterministic controls to block prohibited actions regardless of model output, and **require approval for high-risk or irreversible actions**.
- **On prompt-based approval failing as a control.** — research on agentic delegation finds users calibrate trust **per task** rather than per agent, granting wide autonomy for advisory work while demanding confirmation for irreversible, externally visible actions; and names the failure *delegation regret* — regret not that the agent erred, but that it acted beyond what the user would have authorised.
- **On the verification layer this sits above.** — see this site's [***"Done" Is a Claim, Not a Fact***](/posts/done-is-a-claim/) for the output-verification ritual; this post is about the *scope* of authority, a separate control that holds whether or not the agent tells you the truth.
