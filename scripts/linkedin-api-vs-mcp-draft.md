# LinkedIn draft — "API vs MCP" (decision view, GCB4-safe)

Everyone is writing about MCP. Here's the question I actually have to answer at work, not on a blog:

**When do I let an agent talk to a provider's API directly — and when do I put the protocol in front of it?**

It used to frustrate me that the answer seemed to be "it depends." So I stopped asking "API or MCP" and split the question into the two things that were actually being decided:

1. **Transport** — how the bytes get from the agent to the capability.
2. **Guardrails** — what the agent is allowed to do.

That split is the whole answer. MCP doesn't make an agent safer — the "stop it from deleting everything" property lives in the *scope you grant* and the *tool surface you expose*, not in the transport. What MCP actually buys is uniformity: every client talks to every tool the same way.

So the rule I use in architecture reviews is one question:

**Will a second consumer ever need this resource?**

- One agent, one consumer, a guardrail that's just a scoped token → call the API directly. Fewer layers, fewer things to break, one less dependency to migrate when the spec moves under you.
- Multiple agents or clients hitting the same resource, a provider you expect to swap, or a gnarly integration someone already solved → the protocol earns its keep.

The protocol won the standards war, and for the big platforms with thousands of agents it's clearly the right answer. But for the single-purpose integration, the default should be leaner than the hype suggests.

How do you decide — do you default to the API, or reach for the standard?
