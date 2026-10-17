# builderdecade cron failure — actual mechanism (2026-10-17)

## What I claimed, and why it was wrong

I told Vincent the cron "proposed a spent lever three weeks running" and that "its #1
candidate had already shipped as post #46." **The second half was wrong**, and I should
have checked before saying it.

## The real timeline

```
2026-10-16 08:02   cron runs, shortlists `first-hire-timing-numbers` as #1
2026-10-16 11:41   commit a8b6927 — "When to Hire Your First Employee" SHIPS
```

The commit came **3.5 hours AFTER** the cron run. The cron proposed a topic that did
not yet exist. Vincent approved it and it shipped the same day. **That is the pipeline
working exactly as designed.**

What actually happened is the reverse of my claim: the **queue** was one post behind
the **repo**, because the Oct-16 post shipped after discovery and nothing wrote back to
the queue. When a later session read the queue, `first-hire-timing-numbers` still sat
there as 🟡 pending while the repo already carried it. That is a **bookkeeping lag**,
not a bad recommendation.

## So what IS actually wrong

### F1. 🔴 The cron never re-reads the repo before shortlisting

The prompt tells the agent to derive candidates from GSC footholds. It does **not**
require listing `content/posts/`, `content-zh/posts/`, and `assets/cover-*.png` before
shortlisting. The queue header at line 24 asserts this rule in prose ("Every Stage-1
run must ls ... BEFORE shortlisting") but it lives in the *vault note*, not in the
*prompt* — and the agent reads the prompt, not last week's note.

Evidence this is the real gap: the Oct-14 run caught its own duplicate by reasoning
("its #1 `nanocorp-numbers` is a duplicate — `solo-founders-winning` already carries
the Carta 36% figure"), i.e. **dedupe happened by luck and recall**, not by a check.
Relying on the model to remember 47 slugs is not a gate.

### F2. 🟡 The shortlist has no required structure carrying the lever rating

The prompt says "state the ledger verdict inline" and "the shortlist must LEAD with the
live lever." Both runs still delivered a **numbered list of content posts** as the
head items. The lever table appeared *below* the shortlist as an "honest lever menu,"
which reads as an appendix rather than a veto. Vincent then reasonably picks from the
numbered list — which is why three content posts got picked in a row.

**The veto is prose, not structure.** A model generating prose will keep producing a
numbered content list, because that is the shape a "shortlist" has.

### F3. 🟡 No write-back to the queue after a post ships

Nothing records "this candidate shipped." The queue's own line 26 says
`first-hire-timing-numbers → ✅ SHIPPED` — but a human wrote that during a
daily-driver session on 2026-10-17, not the cron. So the next run reads a queue that is
still stale unless someone notices.

### F4. 🟢 `first-100-users-numbers` was proposed twice (Oct 12, Oct 14), never shipped

Not a defect, just worth noting: the queue held a live, never-executed candidate while
spent content posts kept being picked. The dedupe problem is downstream of Vincent
selecting from the numbered list.

## The fix

1. **Mandatory, mechanical repo reconciliation as Step 0** — list both content dirs and
   covers, build the shipped-slug set, and REJECT any candidate whose slug is in it.
   This must be a command to run, not a principle to remember.
2. **Restructure the shortlist so the lever rating is load-bearing** — every candidate
   must print its lever + ledger rating inline, and the shortlist must be ordered by
   lever liveness, with a spent-lever candidate printed under an explicit
   `OVERRIDING LEDGER` heading, never in the main list.
3. **Self-reconciling queue write-back** — the run must mark any candidate now present
   in the repo as SHIPPED before appending new candidates.
