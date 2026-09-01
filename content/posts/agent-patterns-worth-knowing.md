---
title: "3 Agent Patterns Worth Knowing (Before You Blame the Model)"
translationKey: "agent-patterns-worth-knowing"
date: 2026-09-01T07:30:00+08:00
draft: false
tags: ["ai agents", "agentic patterns", "tool use", "routing", "reflection", "solo builder"]
description: "When your agent misbehaves, the instinct is to swap the model or 'prompt harder.' Usually the real problem is the pattern you gave it. Routing, tool use, and reflection each solve a specific failure mode — here's when each one actually earns its cost."
cover:
  image: "cover-agent-patterns-worth-knowing.png"
  alt: "A branching decision between three pathways, not one straight line"
---

# 3 Agent Patterns Worth Knowing (Before You Blame the Model)

The first time an agent blows it, the instinct is to reach for a bigger model. The second time, to "prompt harder." Both miss the point.

An agent that goes wrong is usually not a dumb model. It's a model you handed the wrong *shape* to work in. The patterns you choose — how the model routes, what tools it can touch, whether it checks its own work — are what separate an agent that seems smart from one that keeps failing in the same predictable way.

There are three patterns worth knowing by name, not because they're trendy, but because each one exists to solve a **specific failure mode**. Learn which failure you're fighting, and the pattern picks itself.

## Pattern 1: Routing — for when inputs stop looking alike

The problem: one prompt is a refund request, the next is a billing bug report, the next is "what's your refund policy?" A single agent fielding all three will confidently barrel through them with the same generic treatment, because it has no reason to treat them differently.

**Routing** fixes this by introducing a decision before the action: classify the input, send it to the right specialist. That specialist can be a different prompt, a different model, or a different code path — the point is the *separation*, not the mechanism.

The failure mode routing solves is **heterogeneity**. One agent handling many kinds of inputs drifts toward the average. Routing says: the average answer is wrong for each specific case, so stop averaging.

The tell that you need it is simple — when you catch yourself writing "if the user is asking about X, then…" inside a single prompt, you're hand-coding a router in prose. Pull it out and make it a real decision.

## Pattern 2: Tool use — for when the model keeps making things up

Ask a model "what's your current balance" and it will answer confidently with a number it invented. This isn't laziness; a model only knows what it was trained on, and your balance isn't in there.

**Tool use** is the pattern that turns an agent from a *knowledge* system into an *action* system. Give it a function — `get_balance()`, `search_docs()`, `run_query()` — and it stops hallucinating the answer and starts *retrieving* it.

The failure mode tool use solves is **confabulation on missing data**. When the agent doesn't know and doesn't have a way to find out, it fills the gap with confident fiction. A tool is the escape hatch from fiction back to fact.

The subtle trap is the reverse problem: **tool explosion.** Add too many tools and every decision gets harder, not easier — the model now has to pick correctly from thirty options before it can act. For a solo builder, the discipline is to keep the tool surface small and sharply named. Three well-described tools beat thirty vaguely-worded ones every time.

## Pattern 3: Reflection — for when the work is subtle and wrong-ness is cheap

Some outputs are obviously right or wrong. Most interesting work isn't. A generated function passes the linter and is still subtly incorrect. A draft reads fine but says nothing.

**Reflection** adds a second pass: generate, then *critique against a criterion*, then revise. The agent checks its own work before you see it.

The failure mode reflection solves is **silent wrongness** — errors that don't error. It's the only one of the three that adds real **cost and latency** (a second model call, sometimes a loop of them), so it's the one you gate hardest. Reflection earns its cost only when:

- Correctness actually matters (a wrong answer is expensive — money, data, trust).
- You can name the criterion clearly ("does this compile and handle the empty case").
- You'd rather burn tokens than your own review time.

For a quick factual lookup or a speculative brainstorm, reflection is pure waste. For the code path that touches a user's data, it's the cheapest insurance you'll buy.

## The real skill is diagnosing the failure, not the pattern

Here's the reframe that matters for a solo builder, because *you* are the only one who'll debug this when it breaks:

**Don't reach for a pattern. Reach for the failure.**

- Agent gives generic, mushy answers to varied questions → **routing.**
- Agent invents facts or numbers → **tool use.**
- Agent's answers look right but don't hold up → **reflection.**

Every pattern you add buys a capability and *costs you a new way to fail* — more latency, more tokens, one more moving part to own. The solo-builder discipline isn't to stack all three. It's to add the *smallest* pattern that kills the failure you're actually seeing, and leave the rest out.

A bigger model won't fix a routing problem. A better prompt won't fix a missing tool. The pattern is the medicine, not the model — and knowing which of the three you need is the difference between "why does it keep doing this" and "there, fixed."

*This is the pattern-level companion to two earlier posts: [API vs MCP](/posts/api-vs-mcp/) (which *transport* your tools talk over) and [what AI agents still can't do](/posts/what-agents-cant-do/) (the ceiling no pattern reaches). This one is about the patterns themselves — what each is for, and when it's worth it.*

## Sources

- **Zheng et al., *Where LLM Agents Fail and How They Can Learn From Failures* (arXiv:2509.25370, 2025).** — AgentErrorTaxonomy: agent failures modularly span memory, reflection, planning, action, and system-level operations; a single root-cause error cascades through subsequent decisions. Grounds "diagnose the failure, not the pattern."
- **Ng, *Agentic Design Patterns* (DeepLearning.AI, 2025).** — reflection is the right pattern when output quality matters more than speed and when correctness criteria are clear enough to evaluate; it adds cost and latency not worth paying for simple queries.
- **OpenAI, *Agent Design Patterns* guide (2025).** — canonical framing of routing, tool use, and reflection; routing as a decision before action, tool use as action-enabling, reflection as self-critique.
- **LangChain / RAGyfied, *Agentic Design Patterns* (2025).** — the "tool explosion" problem: as you add tools, the agent's decisions get harder; group tools, use hierarchical selection, and impose call budgets.
