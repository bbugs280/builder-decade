# 2026-09-19 — Stray emphasis markers in ZH posts (44 → 0) + CI guard

## Problem

Readers saw literal `**` in the prose of two Simplified-Chinese posts:

```
zh/posts/reuse-vs-rebuild/index.html        * x40
zh/posts/solo-founder-burnout/index.html    * x4
= 44 stray markers on 2 pages
```

Invisible in source review — the Markdown looks correct; Goldmark drops the
span at render time.

## Root cause — TWO independent shapes (not one)

The previously documented cause ("Goldmark won't close a `**` run when the
closing marker follows CJK punctuation") is **correlational and incomplete.**
Six rounds of minimal paired-case probes against real Goldmark (Hugo 0.165.0 +
PaperMod) isolated two distinct triggers:

**Shape A — opener followed immediately by a bracket/quote character.**
The `**` is preceded by a CJK word char and the very next char is
`「」『』（）"“”`. Goldmark's left-flanking test rejects the opener, so *both*
runs render literally.

```
BROKEN   而是**「墜落」的結構**。它
OK       而是 **「墜落」的結構**。它      (space before the opener)
OK       而是「**墜落的結構**」。它       (bracket moved outside)
```

**Shape B — closer preceded by CJK punctuation, CJK continuing after.**

```
BROKEN   **…歸誰管？**這不再是
OK       **…歸誰管？** 這不再是           (space after the closer)
OK       **…歸誰管**？這不再是           (punctuation moved outside)
```

**Disproved along the way:**
- interior `「」` alone does NOT break a span — `**「墜落」的結構**` at
  paragraph start renders fine
- a space *before* `**` is enough to rescue Shape A
- the same source shape can render fine or broken depending on the adjacent
  characters, so **source review cannot decide this** — only the built page can

## Fix

Shape A: insert one space before the offending opener.
Shape B: insert one space after the offending closer.

11 insertions / 11 deletions across 2 files. No prose reworded.

## Verification

```
guard (rendered output)   44 -> 0 strays, 74 posts checked, exit 0
language isolation suite  RESULT: PASS
prose integrity           reuse-vs-rebuild 2788 chars = 2788  PASS
                          solo-founder-burnout 2691 chars = 2691  PASS

before (10 edits)  reuse 40 -> 32,  solo 4 -> 0
after  ( 2 edits)  reuse 32 -> 0
```

Prose integrity was proven by stripping **all** whitespace and `*` from the
old and new revisions and comparing byte-for-byte. Identical character counts
mean no word was lost, reordered, or invented — only spaces and marker
positions moved.

## Guard

`tests/check_no_stray_emphasis.py` runs on the **built** output (not source),
so it catches both shapes regardless of which one caused the defect. Wired
into `.github/workflows/hugo.yaml` after the language-isolation test.

The guard's own failure message was also corrected — it previously named only
the (incomplete) punctuation cause, which sends the next reader hunting the
wrong root cause. It now documents both shapes and says explicitly to
diagnose from the rendered page.

## Lesson

**The rendered page is the only trustworthy oracle for this class of bug.**
Every hand-derived predicate failed:

```
source regex                 77 hits vs guard's 44   -> over-reach
span regex                   45 hits in 27 files     -> matched spans, not defects
punctuation-adjacent fixer   broke solo 4 -> 8       -> couldn't tell opener from closer
fixer on render-fine files   would touch 3 of 4      -> dry-run caught it
bracket rule only            40 -> 32, 8 left        -> Shape B also real
```

The shipped fixer rebuilds and requires the rendered stray count to **strictly
drop** after every edit, reverting otherwise. No predicate was trusted.

## Follow-ups

- builderdecade ZH content is **Simplified Chinese**, unlike traindecade's
  Traditional — a separate script-consistency pass is warranted
- `Projects/BuilderDecade.md` does not yet exist in the vault
