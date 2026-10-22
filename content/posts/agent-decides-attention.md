---
title: "Claude Duet Explained: What It Does, Who Can Use It, and What You Give Up"
translationKey: "agent-decides-attention"
date: 2026-10-22T10:00:00+08:00
lastmod: 2026-10-22T17:00:00+08:00
draft: false
tags: ["claude duet", "ai agent", "proactive agent", "solo builder", "delegation", "attention"]
keywords: ["claude duet", "what is claude duet", "claude duet explained", "claude duet review", "proactive agent", "anthropic duet"]
description: "Claude Duet is Anthropic's proactive agent: it scans your apps, writes a morning brief, and asks before acting. What it does, who gets in, what you give up."
cover:
  image: "cover-agent-decides-attention.png"
  alt: "A sorting tray of blank unlabelled cards, one card lifted out and set apart from the rest"
faq:
  - q: "What is Claude Duet?"
    a: "Claude Duet is a proactive AI agent from Anthropic, released 21 October 2026. Instead of waiting for you to ask a question, it checks the apps you connect to it every few hours, sends you a short morning brief of what it thinks matters, messages you during the day when something needs you, and carries out tasks in the background on its own cloud computer."
  - q: "Is Claude Duet available yet?"
    a: "It is a research preview on a waitlist, open to US subscribers on Claude Pro and Max plans. It runs as a standalone app on iOS, Android and claude.ai, and uses the same usage limits as the rest of Claude. At the time of writing it was not generally available, including outside the US."
  - q: "How is Claude Duet different from ChatGPT or a normal Claude chat?"
    a: "A chat tool only responds when you type. Claude Duet starts the conversation itself: it decides what to surface, and it keeps working while your laptop is closed. The genuinely new part is not task execution or approval prompts, which have existed for years, but the decision about which of your open items deserves your attention."
  - q: "Does Claude Duet act without asking?"
    a: "It reads and drafts freely, but Anthropic says it shows you exactly what it plans to do and waits for your approval before sending messages, making payments, signing documents or deleting anything. Some actions are blocked even with approval, such as trading securities or moving money between accounts."
  - q: "What is the main risk of using Claude Duet?"
    a: "The decision about what reaches you happens before you see anything, so there is no approval step at that layer. If the agent leaves something out, you never learn it existed, and the log of what it chose not to surface sits with Anthropic rather than with you."
---

Anthropic released something on 21 October that most people will skim past, because it looks like another assistant. It is worth ten minutes, because the thing it changes is not speed. It changes who decides what you spend your morning on.

It is called Claude Duet. Before arguing about it, here is what it actually is.

## What Claude Duet is, in one paragraph

Duet is a proactive agent. Instead of waiting for your question, it watches the apps you connect and comes to you: it scans your inbox, calendar, invoices and messages every few hours, writes a short morning brief of what it thinks matters, and messages you during the day when something needs doing. It also works while you are away — it runs on a computer of its own in the cloud, so it keeps drafting replies or chasing unpaid invoices after your laptop is shut. In Anthropic's own words, it is "designed for judgment — deciding what needs you, what can wait, and when to check first."

## Who can use it right now

Not many people, yet. It is a research preview on a waitlist, open to US subscribers on the paid Claude Pro and Max plans. It is a standalone app on iOS, Android and claude.ai, and it uses the same usage limits as the rest of Claude. If you are outside the US, or on the free plan, you cannot get in today.

That detail matters less than it sounds. The behaviour is what is worth understanding, and the same pattern will arrive in every assistant within a year.

## The three things it does

**It looks through your stuff and tells you what it found.** It scans your connected apps every few hours, then writes a morning brief of what it thinks matters. You can change what it reports on and how often.

**It does work while you are away.** It can draft a reply, chase an unpaid invoice, prepare payroll, or build a small dashboard, then tells you when it is finished.

**It asks before it does anything that counts.** It reads and drafts freely, but shows you what it plans to do and waits before sending a message, paying, signing a document or deleting anything. Some actions are blocked even if you approve them — moving money between accounts, for example.

## Only the first one is actually new

Sit with that, because the other two are old. Software has executed tasks for decades. Permission prompts have existed since the first delete button.

What is new is the **first** one: a machine deciding, on its own, which of your open items is worth putting in front of you — and which ones it will say nothing about at all.

That is a different job from answering. Answering is bounded: you ask, it responds, you judge the reply. Deciding what to tell you is unbounded, continuous, and happens before you are aware there was a decision to make.

## What this means if you already use agents

If you have used any agent — Claude Code, a coding assistant, a task bot — you know the loop: you give it a job, it works, you check the result. The loop starts with you.

Duet moves the starting point. Its output is not only work done, it is *a judgement about what deserves your attention*. So what you are assessing is no longer whether it completed a task correctly. It is whether it picked the right things to interrupt you about.

Three shifts follow.

**Your review effort moves from output to triage.** Checking a drafted email is easy — you read it. Checking whether a drafted email *should have been the one it chose* is much harder, because you would need to know what else it considered and silently discarded.

**Its failure mode is quiet.** A broken agent gives you an error. An assistant that leaves things out gives you a shorter brief, and a shorter brief looks like a good week. Nobody reports the alert that never arrived.

**The record of its decisions sits with the vendor.** You can test a model against ten known cases and see the diff. To test what got left out, you would need the log of what it chose not to surface — and that log is on their side of the fence, not yours.

## For everyone else, the change is slower and bigger

Most people will use this the way they use email — without thinking about the mechanism. That is fine, and it is how software usually arrives.

But the shape of the change is worth naming. When you read a morning brief, you are reading an edited version of your own life. Something chose the items. In a newspaper you at least know an editor chose, and roughly why. Here the editing is invisible and personalised, and it adapts to what you clicked on yesterday.

That is not a reason to refuse it. It is a reason to notice the first time your brief feels thin, and ask whether it is a quiet week or a filter that has quietly decided something is not for you.

## The part you can check

To be fair to it, the safety controls are written down and easy to follow. Actions go through an approval step, there is a separate filter guarding credit card numbers and identity documents, and it never sees your passwords directly.

The line between preparing work and finishing it is drawn in the right place, and it is worth saying plainly: an assistant that prepares and does not commit is better than one that commits and apologises afterwards. If you take one idea from this launch, take that one. You can copy it into your own setup today without renting anything.

But notice what that line does not cover. The approval step sits at the moment something is **done**. It does not sit at the moment something is **noticed**. Nobody reviews the decision to leave a message out of your morning brief, because by the time you read the brief, that decision has already been made.

## What to do about it, as one person

Three things, in the order they help most.

**Copy the prepare-then-commit split into your own setup.** If you have anything running on a schedule, the most useful change this week is not a better model. It is a hard line between what it puts together and what it is allowed to send. A draft you can throw away. A send you cannot.

**Write down what your assistant decided not to show you.** Almost nobody does this and almost everybody needs it. If anything is filtering, ranking or summarising for you, record what it dropped as well as what it kept. Otherwise you cannot tell a genuinely quiet week from a filter that quietly broke.

**Do not hand over the decision before you can check it.** Letting a tool judge what matters is not a mistake. Letting one judge it when you cannot check is. If you cannot answer "what did it decide to hide from me last month", you have not hired an assistant. You have bought a blind spot that also drafts your email.

## Where this leaves you

This site has argued that you should rent the model and build the wiring around it yourself, because the wiring is the part you keep. That argument still holds.

What changed is that a product like this arrives with the wiring already done — and then goes one step further, by taking over the decision about what reaches you. Not a faster assistant, but a decision you used to make yourself, handed over, at the moment when the only sign it went wrong is something that quietly never reached you.

Use it if you want. It will probably be good, and the way it separates preparing from committing shows care. Just be clear about what you are trading. Rent the model, rent the work, keep the judgement about what matters. The first two come back when you cancel. The third does not come back with an audit trail.

## Common questions about Claude Duet

**Is it free?** No. It requires a paid Claude Pro or Max plan, and background monitoring uses the same usage limits as the rest of Claude — Anthropic notes that checking more often burns through your allowance faster.

**Does it replace ChatGPT?** Not directly. A chat tool answers when asked. Duet starts the interaction and decides what you hear about. The overlap is the writing help; the difference is who initiates.

**Can I turn it off?** You can disconnect any app it has access to. The broader question — whether you can see what it decided to keep from you — is the one this post argues about, and it is not something a toggle solves.

*Claude Duet is a research preview from Anthropic, open by waitlist to US Pro and Max subscribers at the time of writing. What it does is described from Anthropic's own announcement; I could not test the product, and the argument about what it means is mine, not theirs.*
