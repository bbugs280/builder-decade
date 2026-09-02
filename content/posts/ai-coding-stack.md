---
title: "The AI Coding Stack I Actually Use (and Why I Stopped Swapping Tools)"
translationKey: "ai-coding-stack"
date: 2026-08-23T00:00:00+08:00
lastmod: 2026-09-02T08:00:00+08:00
draft: false
tags: ["AI coding", "tools", "Claude Code", "Cursor", "solo builder", "productivity"]
description: "The tool question isn't the one that matters, but people ask it constantly. Here's the actual stack a solo builder uses day to day in 2026 — one coding agent, a model, a few supporting tools — and the honest reasoning behind each choice, including why the default instinct to keep swapping tools is the thing actually costing you progress."
cover:
  image: "cover-ai-coding-stack.png"
  alt: "A focused AI coding toolchain, not a drawer full of tools"
---

There's a question every solo builder gets asked constantly, and it's the wrong one: *"which AI coding tool do you use?"*

The question implies the tool is the bottleneck — that if you just found the *right* assistant, the work would get easier. It won't. The tools are roughly equal now, and the gap between them is smaller than the gap between *using one well* and *using ten badly*. This post is about the stack I actually settled on, and the part of the story that usually gets skipped: the biggest win wasn't the tool, it was *stopping* the search.

## The stack, honestly

One coding agent, one model underneath it, and a handful of supporting tools. That's it. No dashboard of twelve assistants, no "I use X for frontend and Y for backend" gymnastics.

- **The agent:** a terminal-first coding assistant that edits files directly in the repo. Claude Code is my default; Cursor is the same idea in an editor. The distinction that actually matters isn't which one — it's *terminal-native vs. editor-native*, and either is fine. Pick one that edits your actual files and run it every day.
- **The model:** the strongest reasoning model your budget allows, pointed at whichever agent you picked. The agent is the interface; the model is the brain. You don't need to shop models — you need one that's reliably good at reading your whole codebase and not just a snippet.
- **Version control:** non-negotiable, and it's where most agent workflows go wrong. The agent is your *fastest* teammate, which means it's also your fastest *wrong* teammate. Git is the only thing that lets you take big swings and still get home.
- **The human filter:** you, reading every diff with "mild suspicion." This isn't a tool. It's the whole discipline, and it's the part no tool replaces.

## Why I stopped swapping

Here's the honest part that no tool-comparison video will tell you: **I spent the first stretch tuning my setup instead of building, and it was the least productive I've ever been.**

Every week there's a new "Claude Code killer." Every month a new model claims to be smarter. The temptation to switch is constant, and it *feels* like progress because you're busy. But swapping tools is what you do *instead of* building, and the switching cost is invisible until you add it up.

Two things ended it for me:

1. **The tools converged.** In 2026 the honest difference between the top assistants is small — smaller than the variance from one prompt to the next. The "which is best" debate is now mostly content-farm noise.
2. **Familiarity compounds.** The assistant that's been reading my repo for weeks knows my conventions, my file layout, my blind spots. A brand-new "better" tool knows none of it and would spend a week relearning. That head start matters more than any benchmark.

The best tool is the one you already know. Spend the switching energy on shipping instead.

## The one decision that actually matters

If you take one thing from this post, take this: **the agent's output is only as good as what you ask it to read.**

The single highest-leverage behavior isn't prompt-engineering a perfect one-liner. It's giving the agent *context* — pointing it at the right files, telling it which code it's allowed to change and which is frozen, writing down the constraint that lives only in your head. An agent with the full picture writes boring, correct code. An agent with half the picture writes confident, plausible bugs.

That's the real skill, and it's why the beginner guide's loop — *describe, generate, judge, correct* — is the whole game. The tool does the mechanics. You own the "judge" step.

## What I'd tell a solo builder starting today

- **Pick one agent, commit for a month.** Don't evaluate a second one until you've built four things with the first. You can't judge a tool you haven't pushed on.
- **Point it at one real project, not toy prompts.** The tool only reveals itself when it has to navigate actual files, actual errors, actual context.
- **Git everything before you ask.** The habit of "commit, then agent, then read the diff" is what separates shipping solo from breaking solo.
- **Read every diff with mild suspicion.** The agent is superhuman at speed and untrustworthy at judgment. Your job is the judgment.

There is no hidden stack that makes it easy. There's one agent, a model, git, and you reading the diff. That's the whole toolchain — and the toolchain was never the hard part.

*This is the "how" behind [why one person can now ship what took a team](/posts/one-person-team/). Just starting? [Begin here, no CS degree required](/posts/ai-beginner-start/).*

---

## Sources

- Stack Overflow 2025 Developer Survey — 84% of developers use or plan to use AI tools; 51% use them daily; only 3.1% "highly trust" AI output, and 45.7% somewhat or highly distrust it.
- Pragmatic Engineer — AI Tooling 2026: 46% of developers rank Claude Code as their most-loved AI coding tool; solo/indie segments skew toward AI-first tooling.
