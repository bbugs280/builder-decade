# 2026-10-19 — Post #48: `ai-vendor-exit-cost` (EN + ZH)

**Site:** builderdecade.com · **Commit type:** content (new post + 2 inbound links + 1 cover)
**Selected at:** Stage 3 gate, Vincent's call, 2026-10-19.

## Why this topic, and what it is NOT

Proposed as candidate **A′ — "The Day Your AI Vendor Shuts Down"**, after candidate A
("the AI agent you can't fire") was **rejected at the collision check**:

```
ai-api-cost-creep       the BILL        (prices fall, bills rise)
ai-cost-of-goods        the ACCOUNTING  (COGS ratio)
metered-build           the METER       (flat-rate is over)
harness-not-model       the OWNERSHIP   (you own the harness, not the model)
────────────────────────────────────────────────────────────────────
                  ↑ all RUNNING cost.  Candidate A sat inside harness-not-model.

WHITESPACE →      EXIT cost. What it takes to walk away.
```

The five-post cluster is crowded; this post claims the one remaining slice and **names the
distinction explicitly** at the point where it could be mistaken for a re-run ("owning the
harness does not make the brain yours"), rather than relying on the reader to infer it.

## Files

```
content/posts/ai-vendor-exit-cost.md          new  EN
content-zh/posts/ai-vendor-exit-cost.md       new  ZH (Traditional, 書面語)
assets/cover-ai-vendor-exit-cost.png          new  cover
content/posts/harness-not-model.md            edit +1 inbound link
content-zh/posts/harness-not-model.md         edit +1 inbound link
```

## Verification (all run, all green)

```
hugo --minify                       exit 0 · EN 341 / ZH 373 pages
post built                          public/posts/ai-vendor-exit-cost + /zh/ ✅
                                    (checked with ls — a clean page count is NOT proof)
tests/test_language_isolation.sh    PASS
tests/check_zh_traditional.py       48 ZH posts Traditional, 0 files ≥10 simplified
tests/check_shortcode_json.py       0 double-encoded (733 rendered pages)
tests/check_no_stray_emphasis.py    no stray markers (96 rendered posts)
tests/check_zh_traditional_theme.py no theme-leak chars (382 ZH pages)
ZH single-glyph probe               0 hits (the floor test the guard cannot do)
ZH register census                  0 Cantonese particles (written Mandarin)
description length                  119 chars (≤155) ✅
identity leak scan                  content/ AND layouts/+hugo.yaml — both empty
internal links                      inbound 1 per language, resolves in its OWN language
parity                              EN 48 / ZH 48 / covers 48 — holds
```

## ⚠️ Two findings from the cover generation

**1. The gauge-injection prior fired from a prompt that explicitly negated dials.**
Prompt 1 said *"No dials. No gauges. No instruments. No screens."* — result: a factory
pressure gauge with numbers, tick marks and manufacturer lettering, mounted in frame.
This is the documented `builderdecade` prior ("change the OBJECT, not the negative"), and it
was reached for anyway. Prompt 2 removed every instrument-class object from the scene
description entirely (no wall fittings, no shelf hardware, no machinery) rather than adding
more negations — and came back clean.

**2. "One empty slot" renders as an OPEN BOX, not an absence.**
Prompt 1's *"one slot in the row is EMPTY"* produced 8 boxes with box #5 open — presence, not
absence. The fix was to make the **gap itself the subject** and give it a physical trace
(a dust/powder footprint marking where the box sat). Prompt 2 verified: empty gap ✅, zero
text/dials/instruments ✅.

## ⚠️ Repo state — a sibling-touched file

`content/posts/harness-not-model.md` and its ZH twin were edited by an earlier session
(git warning: modified by subagent `20261016_081922_0e7cfc23`). The edits were read before
appending and the inbound-link addition is a pure append at end-of-file — **no sibling content
overwritten**. Not committed here; the working tree is left for review.

## Not done

- **Not committed. Not deployed.** Vincent reviews before commit.
- Cover regenerated twice. Prompt 1 discarded (failed both metaphor and text-freedom).
