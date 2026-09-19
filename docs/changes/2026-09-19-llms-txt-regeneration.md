# 2026-09-19 — llms.txt regenerated from content (2 → 74 entries)

## Defect

`static/llms.txt` was hand-maintained and had drifted to **2 of 74 posts**,
while the site carries 37 EN + 37 ZH.

## Fix

Added `scripts/gen_llms_txt.py`, which generates the file from the content
directory so it cannot drift again. Header and About section adapted to
builderdecade's positioning (not copied from the traindecade twin).

```
before    2 entries
after    74 entries (37 EN + 37 ZH)
```

Also strips backslash-escaped quotes (`\"`) that Hugo frontmatter carries
through — these appeared literally in the first generated pass.

## ⚠️ Honest framing — llms.txt is not a traffic lever

Research (2026-09-19) contradicts the older "single highest-leverage AI
optimisation" framing:

- Google does not support llms.txt (Gary Illyes, Search Central Live 2025);
  Mueller likens it to the keywords meta tag
- 515M LLM-bot events → **408** requests to `/llms.txt`
- Ahrefs: **97%** of llms.txt files got zero requests in a month
- SE Ranking (300K domains): no correlation with citation frequency

Real use = **inference-time context loading** for agents already on the site.
Cheap insurance, not a discovery lever. Regenerated because it costs minutes
and the file was materially wrong — **not** because it will move traffic.

## Verification

```
llms.txt          74 entries, 0 cross-site leakage
language isolation PASS
stray-emphasis guard PASS (74 rendered posts)
hugo exit 0
```

## Follow-up

Older SEO guidance calling llms.txt "the single highest-leverage AI
optimisation" overstates it. Skills updated to reflect the measured evidence.
