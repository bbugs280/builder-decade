---
title: "Your Agent Trusts Everything You Connected It To"
translationKey: "mcp-security-solo-builder"
date: 2026-09-20T08:00:00+08:00
draft: false
tags: ["mcp", "ai agents", "solo builder", "security", "developer tools"]
description: "You pasted an MCP server in from a blog post. It holds your files and your keys. Here's the 10-minute check before you connect the next one."
cover:
  image: "cover-mcp-security-solo-builder.png"
  alt: "A small cluster of cables plugged into a single hub, one cable visibly frayed, lit in warm amber light"
---

Most solo builders now run an AI agent with real access: a file system, a couple of API keys, a database, maybe a deploy script. To make it useful, you connected it to things. A server from a README. A config you copied from a blog post. Something that "just worked" in about four minutes.

That's the part worth slowing down on.

## The thing you actually agreed to

An MCP server is not a plugin. When you connect one, you hand the agent a set of tools, and you hand it the schema that describes those tools — their names, their parameters, and their descriptions. The model reads that description and decides when to call it.

Here's the trust gap, and it's structural rather than a bug in anyone's code. Tool descriptions get reviewed **once**, when you connect. Tool *responses* get no equivalent check. Whatever a server returns goes into your model's context and gets read as input. If the response contains instructions, the model may follow them.

The Open Worldwide Application Security Project describes the resulting attack directly: a malicious server exposes a tool with a friendly name like `get_compliance_status`, and when your agent calls it, the response looks like a normal report but carries a hidden directive telling the agent to read a sensitive file and post it somewhere external. The agent has a file-reader and a network call. Nothing in the string stops it.

The part that should bother you: **the model cannot reliably tell the difference between data and instructions.** That's not a model you can upgrade your way out of. It's the shape of the technology.

## The numbers are no longer theoretical

For most of 2025 this was a conference-talk class of vulnerability. It isn't now.

The MCPTox benchmark, an academic evaluation of poisoning attacks against live servers, tested 45 real MCP servers across 20 language models and measured an average attack success rate of **36.5%**, with the worst case reaching **72.8%** on a single model.

Read that first number again. Roughly one in three attempts worked. That is not a corner case you can reason your way around by being careful.

And the delivery mechanism got cheaper. A proof-of-concept published in April 2025 used nothing more exotic than a poisoned *calculator* tool description to quietly exfiltrate a developer's SSH private key from an AI code editor. A related variant, described as MCPoison, demonstrated team-wide compromise through a single committed configuration file — one person's pull request became everyone's problem. The Cloud Security Alliance's July 2026 research note documents an IDE auto-execution class where opening a project is enough to run a project-defined server with developer-level privileges.

Notice the pattern across all three: **none of them required you to make an obvious mistake.** You didn't have to click anything. You had to connect something, or open a folder, or merge a pull request.

## Why solo builders are the exposed group

Security guidance for MCP tends to be written for platform teams: schema signing infrastructure, policy-as-code decision points, separation of duties, an approval workflow with more than one human in it.

You have none of that. You have no security review — you *are* the review. And you have the most dangerous configuration there is: one agent holding file access, credentials, and outbound network calls at the same time.

That's not a reason to skip MCP. It's a reason to be deliberate about which doors you open, because the blast radius is entirely a function of what you connected.

## The 10-minute check

You don't need infrastructure. You need one habit and a short list.

**Before connecting any server, read its tool descriptions.** Not the README. The descriptions themselves. According to the widely referenced static indicators, these are the things that should stop you:

- **Model-directed imperatives.** Text aimed at the model rather than at you: "ignore previous instructions," "do not tell the user," "before answering, read..."
- **Sensitive paths.** A tool you don't expect to need mentioning `~/.ssh`, `id_rsa`, `.env`, `.aws/credentials`, `/etc/passwd`.
- **Exfiltration shapes.** An action verb — send, post, upload, forward — sitting next to an external destination: a URL, a webhook, an endpoint.
- **Zero-width characters.** Unicode ranges `U+200B–200F`, `U+202A–202E`, `U+2060`, `U+FEFF` used to hide instructions from human review. If you can't see it, you can't approve it.
- **Instructions hidden in comments.** Model-directed text smuggled inside HTML or markdown comments, invisible in the rendered view.

That list is checkable in minutes. The last two are the ones people miss, because both work by being invisible to the person doing the reviewing.

**Then apply four rules to your setup:**

1. **One server, one job.** Never let a high-privilege server share context with a general-purpose one. If your file-system tool and your web-fetch tool can both see the same conversation, a poisoned response from the second can direct the first.
2. **Least privilege, actually.** A read-only server gets a read-only token. Not a token you *intend* to use read-only.
3. **Treat every tool response as untrusted input.** This is the rule that inverts your default. The response is data. It is not an instruction, no matter how much it looks like one.
4. **Gate the destructive actions.** Delete, transfer, send-to-everyone, deploy — behind explicit confirmation, outside the model's own judgement. The model's willingness to proceed is exactly what's being attacked.

And the enforcement point matters: put these at the **tool execution layer**, not in your system prompt. A prompt instruction ("do not read files outside the project") is enforced by the model's willingness to comply. Injected text is specifically designed to override that willingness. A backend check isn't.

## The reframe

If you've read ["Done" Is a Claim, Not a Fact]({{< ref "/posts/done-is-a-claim" >}}), you'll recognise the shape. That post is about **verifying output** — an agent saying it finished something isn't evidence it did.

This is the same discipline pointed one layer down. That one asks *did it do the work*. This one asks *who is telling it what to do*. Both come from the same starting position: your agent's confident output is not evidence, and neither is its confident input.

A related distinction worth holding: [What Agents Can't Do]({{< ref "/posts/what-agents-cant-do" >}}) covers the capability ceiling, and [API vs MCP]({{< ref "/posts/api-vs-mcp" >}}) covers the transport decision. Neither is about safety. Transport being standardised says nothing about whether what travels over it is trustworthy.

## What to do today

{{< mcp-audit >}}

Open your MCP config. For every server in it, answer three questions:

- **Do I know who maintains this?** Not "it has stars." Who.
- **What can it actually reach?** Credentials, file paths, network. Write it down. If the answer is "everything," that's your finding.
- **Did I read its tool descriptions, or its README?** Those are different documents, and only one of them is instructions to your agent.

The uncomfortable version of this exercise: assume each server is hostile, and ask what it *could* do. You don't need to fix everything. You need to know where the blast radius is, because for a one-person team there's no second line of defence behind you.

Connecting a server takes four minutes. The check takes ten. The asymmetry is the whole argument.

## Sources

- **OWASP Foundation — "MCP Tool Poisoning" (attack reference) and OWASP MCP Top 10, MCP03:2025 (Tool Poisoning).** Attack mechanics: tool responses bypass the connect-time review; the `get_compliance_status` poisoned-response example; the static detection indicators (model-directed imperatives, sensitive paths, exfiltration patterns, zero-width characters, comment-smuggled instructions); and the control set (least privilege, allowlisting, execution-layer enforcement, confirmation gates on sensitive operations).
- **Cloud Security Alliance — "MCP Attack Surface: Tool Poisoning and IDE Auto-Execution," research note, 1 July 2026.** IDE auto-execution of project-defined servers with developer-level privileges; MCP configuration changes framed as equivalent to production code changes; the MCPTox benchmark figure (45 live servers, 20 models, 36.5% average attack success, 72.8% peak); and the case references — Invariant Labs' April 2025 disclosure (SSH key exfiltration via a poisoned calculator tool description), the MCPoison shared-configuration variant (CVE-2025-54136), and the CurXecute auto-start RCE class (CVE-2025-54135).
- **Microsoft Security — "Securing AI Agents: When AI Tools Move from Reading to Acting," 30 June 2026.** The confused-deputy pattern and the trust boundary between internal and external tools. *(Cited via the CSA research note's reference list; not independently retrieved.)*
- **Model Context Protocol specification.** Server outputs are treated as potentially untrusted, and clients are advised to consider trust boundaries — but response validation before passing content to the model is not mandated. *(Cited as characterised by OWASP; not independently retrieved.)*

*Where the underlying figures come from academic and vendor-adjacent research, they are reported as published. The MCPTox benchmark and the individual case disclosures were not independently reproduced for this post.*
