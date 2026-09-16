# 2026-09-16 — Remove all identity leaks from the anonymous blog (EN + ZH)

## Root Cause

builderdecade.com is spec'd **fully anonymous** (`builderdecade` skill: no Vincent, no
HSBC, no bank-architect angle, no employer reference). The site had **seven live
identity leaks across six files and two languages**, and the mandated pre-commit
leak scan could not see any of them.

**Why the scan never caught it — two stacked holes:**

1. **The scan only covered `content/`.** Four of the seven leaks lived in `layouts/`
   and `i18n/` — template and translation files, which the regex never touched. This
   was found by the build-tester gate, not by the scan.
2. **On this session's first pass, the scan was narrowed even further** — run against
   the 5 filenames being edited rather than the full content tree. That is why it
   reported "clean" while `content/posts/memory-is-the-product.md` shipped the string
   "HSBC" in its body.

**A previous session's note in the skill described the content-only regex as the
complete check.** It was not, and the gap was load-bearing.

## Changes

Seven leaks removed. Wording variants kept natural in each language — the ZH is a
genuine translation, not a literal back-translation of the EN.

| File | Leak | Fix |
|---|---|---|
| `layouts/partials/extend_post_content.html` | `"written by Vincent"` (template default) | removed the name |
| `i18n/en.yaml` | `author_bio: "written by Vincent"` | removed the name |
| `i18n/zh.yaml` | `author_bio: "由 Vincent 撰寫"` | removed the name |
| `content/about.md` | `written by **Vincent**` | "with AI agents as the team" |
| `content-zh/about.md` | `由 **Vincent** 撰寫` | "以 AI 代理作為團隊" |
| `content/posts/welcome.md` | `written by Vincent` | removed the name |
| `content-zh/posts/welcome.md` | `由 Vincent 撰寫` | removed the name |
| `content/posts/memory-is-the-product.md` | **`"HSBC cards stay title-only."`** in a live post body | → `"Client work stays out of the logs."` |

**⚠️ The `i18n` fix was the load-bearing one.** `extend_post_content.html` renders
`{{ i18n "author_bio" | default "..." }}` — so the `i18n/en.yaml` value **overrides**
the template default. Editing the template alone would have changed **nothing** on
the live site. Both had to change.

## Files Affected

- `layouts/partials/extend_post_content.html` — template default bio de-named
- `i18n/en.yaml` — `author_bio` translation de-named (this is what actually renders)
- `i18n/zh.yaml` — `author_bio` ZH translation de-named
- `content/about.md` — "Who writes this" paragraph, first-person → neutral
- `content-zh/about.md` — same, ZH
- `content/posts/welcome.md` — closing byline
- `content-zh/posts/welcome.md` — closing byline, ZH
- `content/posts/memory-is-the-product.md` — **employer name in a live post body** →
  generic equivalent rule example

## Verification

Definitive scan over **every published surface** (not just content):
```bash
cd ~/Projects/builder-decade && grep -rniE \
  "vincent|hsbc|gcb|gaincut|ideafactory|yeung|beets|wayne" \
  content/ content-zh/ layouts/ i18n/ hugo.yaml
→ ZERO matches
```

- **Hugo build:** `hugo --gc` clean — EN 270 / ZH 302, 0 errors
- **Binary false positives triaged:** `static/images/hero.png` + 18 `assets/cover-*.png`
  matched the regex on raw binary bytes. Verified with `strings | grep` → **no real
  string present**. Not leaks.
- **Non-published hits triaged and left alone:**
  - `scripts/prompts_dashscope.py` — "Vincent" in a dev-only prompt comment
  - `scripts/linkedin-api-vs-mcp-draft.md` — internal LinkedIn draft ("GCB4-safe")
  - `docs/changes/2026-09-16.md` — the leak-scan command itself
  These never reach a reader; correcting them adds churn without changing exposure.

## Impact

- The anonymity spec now holds across **all 74 pages** (37 EN + 37 ZH) including
  every post's author-bio block, the About page, and the Welcome post
- **No SEO cost.** The author *entity* is unaffected and remains correctly declared:
  `<meta name=author content="Builder Decade">` + JSON-LD
  `"author": {"@type":"Organization","name":"Builder Decade"}`. A bare first name in
  a bio paragraph carries no ranking signal Google can resolve to an entity; the
  schema does that work. Removing it costs nothing measurable.
- ZH and EN remain natural reading in their own languages (no translationese)

## Open

- **The skill's leak scan is now documented as two commands** (`content*/` **and**
  `layouts/ + i18n/ + hugo.yaml`), because one check could never have found the
  template/i18n class. Patched into `builderdecade` SKILL.md this session.
- **`content/posts/memory-is-the-product.md` needed a body edit, i.e. a content
  change, not just a bio change.** Worth a broader audit for the same class: any post
  that quotes real agent rules or real working examples risks carrying employer or
  product specifics. The regex catches the named cases; it will not catch a
  paraphrase that identifies by context.
- **Generalisation:** a passing scan is only evidence about what it *can* see. When
  a check reports clean, state what surface it covered.
