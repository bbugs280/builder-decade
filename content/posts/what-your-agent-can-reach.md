---
title: "Your Agent Doesn't Need to Be Hacked. It Needs to Be Trusted."
translationKey: "what-your-agent-can-reach"
date: 2026-09-21T18:00:00+08:00
draft: false
tags: ["ai agents", "security", "solo builder", "sandbox", "developer tools"]
description: "Seven 2026 sandbox escapes, no exploit in any of them. The vulnerability is the trust you extend after the agent writes something — here's the check."
cover:
  image: "cover-what-your-agent-can-reach.png"
  alt: "A solid strongbox standing open, with a key still in the lock and a folded note slipped underneath it"
---

Here's a fact that should change how you think about your agent's security: in July 2026, security researchers broke out of four widely used AI coding agents — Cursor, Codex CLI, Gemini CLI, and Antigravity — **without breaking a single sandbox.**

Not one of the seven disclosed issues defeated the sandbox directly. Every one of them exploited the same thing instead: a gap between what the sandbox *restricts* and what a trusted component *outside* it later reads, runs, or scans.

If you've already locked down what you connect to your agent — the tool descriptions, the servers you pasted in — that work is real, but it doesn't cover this. This is the other half: not **what you connect**, but **what the agent can do once it's connected.**

## The pattern has a name: the trust handoff

Cloud Security Alliance's research note on the disclosure puts it plainly: *"a sandbox is only as strong as the assumptions made by everything downstream of it."*

The agent doesn't need to escape. It needs to **write something that something else will later trust.** Then the trusted component runs it on your behalf, outside the boundary, with your privileges.

Look at how ordinary each of these is:

- **Cursor, CVE-2026-48124 (CVSS 8.5).** A workspace-controlled `.claude/settings.local.json` "Stop" hook ran an unsandboxed local command automatically — every time an agent turn ended. No approval prompt. Fixed in 3.0.0.
- **Codex CLI, "GitPwned" (CVSS 8.6).** The safe-command allowlist trusted `git show` by *name* without modelling its arguments. `git show --output=./.git/config` wrote a malicious external-diff-tool entry that executed with full user privileges the next time the victim ran `git diff`. Fixed in 0.95.0.
- **Cursor "DuneSlide," CVE-2026-50548 + CVE-2026-50549 (CVSS 9.8 each).** Prompt-injected commands manipulated working-directory and symlink validation to overwrite the sandbox helper itself. Fixed in 3.0.
- **Antigravity.** The agent wrote a `.vscode` task config inside the sandbox; the host executed that task outside the product's Secure Mode boundary. Google classified it as "other valid security vulnerability" and had not patched it at disclosure.
- **Cursor, Codex CLI, Gemini CLI.** One privileged local Docker socket became an unsandboxed execution environment reachable from otherwise-restricted agents — mounting the VirtioFS share and getting read/write access to the home directory.

Read those again and notice what's missing: **no malware, no credential theft, no zero-day.** In each case the agent wrote a file, and a trusted thing read it.

## The one that needs no exploit at all

If the sandbox breaches feel like someone else's problem — you don't run an IDE agent with hooks — this one is the solo builder's version.

**GitLost** (Noma Labs, disclosed 2026-07-06) targeted GitHub's Agentic Workflows. A workflow triggers on an issue being assigned, reads the issue title and body, and posts a reply using the agent's comment tool. To do that job well, teams gave the agent **read access to every repository in the org — private ones included.**

An attacker opened a public issue that looked like a routine internal request. Buried in the body, in plain English, was an instruction to fetch a file from a private repo and paste the contents into the reply. The agent complied. **Private source code, posted publicly, in minutes.**

To exploit it you needed: no coding skill, no credentials, no account. Just the ability to open an issue.

GitHub had guardrails — read-only tokens by default, plus a scan of the agent's output before posting. Noma iterated on phrasing the way an attacker would, and found the guardrail broke on **one word**: prefixing the injected instruction with *"Additionally"* nudged the model to treat a hijack as a legitimate follow-on task instead of something to refuse.

As of publication there was still no code fix. Prompt injection of this kind largely resists patching, because the root cause isn't a bug — it's that **the model cannot reliably separate instructions from its owner and instructions buried in content it reads.**

## Why this lands on solo builders specifically

The enterprise incidents get the headlines, but the configuration that made GitLost work is the one a solo builder reaches for by default, for exactly the reason it feels right:

- You're the only person, so **broad access is convenient.** One token that sees everything beats five scoped ones you have to rotate.
- You're moving fast, so **you set scope once and never revisit it.** The key you pasted in on a Tuesday is still there in November.
- You have no second line of defense, so **there's no one to catch the blip.** A team has a review step; you have a running agent and a deadline.

⚠️ **And here's the honest part, which no vendor page will tell you:** the fix for most of this isn't a purchase or a product tier. It's that you have to give up some convenience. A scoped, expiring credential is *more work* than a long-lived one. A destination allow-list is *more work* than open egress. If you're looking for a way to be both maximally permissive and safe, that configuration doesn't exist.

## The reframe worth taking away

Notice what these incidents have in common with each other — and with the MCP trust problem:

```
What you connect      →  the tool descriptions you trusted at setup
What the agent reaches →  the standing access you granted, and what it can write
```

They're two halves of one question: **what have I handed over, and to whom does that hand-off extend?**

An agent's blast radius is not the agent process. It's **everything the agent can write that something else will later trust.** That's the sentence to remember, because it moves your attention off the model — which you can't audit — and onto the boundary, which you can.

## Check your own setup

That's a claim you can test in about two minutes:

{{< agent-reach >}}

The scores map to a priority order, not a panic list. A standing credential is the highest-leverage single fix — it's what turns a contained mistake into an open door.

## Two things to do this week

**1. Expire something.** Find the longest-lived credential any agent can reach and give it a rotation date. This is the one change that pays off against every variant of the pattern above.

**2. Move the trust boundary, not the model.** For the workflow that touches untrusted input — a public issue, a scraped page, a user-submitted form — ask what that specific agent can reach. Then cut it to only that. Keep the agent that reads untrusted public input away from the agent that touches private data, and treat every issue, PR, and comment as hostile input until proven otherwise.

Neither requires a security team. Both require giving up a little convenience — which is the actual cost of this whole class of bug, and the reason it keeps happening.

Containment is the security half of a wider shift in what a solo builder actually does all day: [The Supervisor Class](/posts/supervisor-class/) covers the move from writing code to directing it, [The Infinite Task List](/posts/infinite-task-list-ai-era/) covers why AI made the to-do list longer rather than shorter, and [Your AI Bill Is Rising Even Though Prices Dropped](/posts/ai-api-cost-creep/) covers the meter that moved while the rate card didn't.

## Sources

- **Cloud Security Alliance — *AI Coding Agent Sandbox Escapes: The Trust Handoff Flaw* (research note, 2026-07-22).** — Pillar Security's "Week of Sandbox Escapes": seven issues across Cursor, Codex CLI, Gemini CLI and Antigravity; *"None of the seven disclosed issues broke the sandbox itself."* The framing that a sandbox is only as strong as the assumptions of everything downstream, plus the specific CVEs, CVSS scores and patched versions cited above. (Note: CSA flags this note as AI-assisted rapid research that has not been through CSA's official review process.)
- **Pillar Security — "The Week of Sandbox Escapes" (2026-07-20 onward).** — the primary disclosure series; each day a different route across the boundary. Pillar's own summary: *"an agent's blast radius is not the agent process; it includes everything the agent can write that the host later trusts."*
- **Noma Labs — "GitLost: How We Tricked GitHub's AI Agent into Leaking Private Repos" (2026-07-06).** — the GitHub Agentic Workflows prompt-injection chain: public issue → org-wide read token → contents posted as a public comment. The "Additionally" guardrail bypass, and the finding that no credentials or coding skill were required. Reported as still unfixed at publication (The Register, 2026-07-07).
- **BleepingComputer (2026-07-21)** — "Cursor, Codex, Gemini CLI, Antigravity hit by sandbox escapes." Contemporaneous reporting confirming the four affected agents and the non-sandbox-breaking nature of the findings.
