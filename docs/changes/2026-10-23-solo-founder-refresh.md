# 2026-10-23 — builderdecade: `solo-founder-vs-cofounder` refreshed with the 2026 data

**Type:** evidence refresh on an existing page. No new post. Both languages.

## Why this page, and not a new one

`zh/posts/solo-founder-vs-cofounder/` became the **site impression leader** in the 2026-10-23
discovery run — 23 impressions at pos 13.6, up from 7 impressions two days earlier. First time a
ZH page has led builderdecade.

The topic is also live right now ("1 in 3 companies are now solo-founded — the co-founder era is
ending" circulating across X, Substack and newsletters), so a page already ranking has fresh
evidence to receive.

**Four trend sources were checked first and all four were dead ends:**

```
Google Trends Trending Now  HK        zero on-niche (celebrities, 西藏地震, iphone duo 回收價)
Google Trends Trending Now  US / UK   zero on-niche (NFL, NBA, celebrities, politics)
Exploding Topics  fitness             all high-volume items already shipped by traindecade
Exploding Topics  AI                  Higgsfield / fraud detection / digital transformation
```

And the Exploding Topics AI candidates failed **Google Trends interest-over-time** verification:

```
higgsfield            US 90d   peak 100 (26 Sep) → 76 (23 Oct)   declining, no query surface
fraud detection       US 12m   peak 32  (Sep 26) → 6              collapsed
digital transformation US 12m  peak 100 (Jun 26) → 11              collapsed 89%
```

⚠️ **Method finding:** Exploding Topics ranks by **two-year cumulative growth**, never current
momentum. Every "+8,400%"-style figure can be describing a trend that already peaked. Always
cross-check with Google Trends interest-over-time before proposing.

## What was already on the page — do not re-add

The page already carried Carta's numbers, so most of the "fresh" evidence was not fresh:

```
ALREADY PRESENT   Carta 23.7% (2019) → 36.3% (H1 2025)
                  Carta 75% more ownership at exit
                  14.7% of priced-equity dollars (2024 vs 30% of startups)
                  Stack Overflow 84% AI-tool usage
GENUINELY NEW     Stripe Q2 2026 — 63% of Stripe Atlas C corps solo-founded
                  Stripe — 53% more revenue by month 24 (multi-founder)  ← the counterweight
                  Stripe — Series A medians $54.9M vs $53.6M
                  Solo Founders Annual Report 2026 — +53% since 2019
```

## What changed — one new section, both languages

`## The 2026 update: the gap is now measurable in both directions` / `## 2026 年的更新`

The section does three things:

1. **Reconciles the apparent contradiction** — Stripe sees incorporation (63%), Carta sees a later
   equity stage (~1/3). The same page states plainly that the two figures are **not directly
   comparable**, rather than presenting agreement.
2. **Carries the counter-argument in full** — the 53%-more-revenue-by-month-24 figure is stated as
   a blockquote and named as "the strongest argument against everything above". Not buried.
3. **Resolves it on the reader's own measure** — comparable rounds, and ownership at exit. If
   winning is month-24 revenue, teams win; if it is what you walk away with, solo is the better
   trade.

## ⚠️ Three defects the build-tester gate caught — all fixed before push

```
W-1  75% ownership figure WAS restated in the new section, ~600 words after the
     myth section already stated it. My first commit message claimed it had not
     been re-added — that claim was false. The new section now REFERENCES the
     earlier comparison instead of repeating the number.

W-2  ZH Sources section was never updated. The ZH page cited Stripe's 63% and
     the $54.9M/$53.6M round medians while its certainty note still read
     "以上數字皆出自 Carta 的一手報告". A page citing sources it does not list.
     Both ZH bullets added; certainty note reworded to match EN.

W-3  "C  corp" — a double space in the ZH body, surviving into the minified HTML.
```

**Why W-2 matters more than its size suggests:** the EN and ZH twins had diverged in *evidence*,
not just wording. An EN-only source list on a bilingual page means the ZH reader is asked to trust
a number that the page's own footer disclaims. When one language cites something, the other must
list it.

## Gate

```
hugo --minify                    exit 0, no new warnings
parity                           49 EN / 49 ZH
test_language_isolation.sh       PASS
check_zh_traditional.py          ✅ 49 ZH posts Traditional, 0 ≥10 simplified
check_no_stray_emphasis.py       ✅ 98 rendered posts clean
built-HTML verification          new section + both figures render in EN and ZH
lastmod                          bumped 2026-09-12 → 2026-10-23 (both languages)
```

## ⚠️ Lever ledger — stated honestly

This is the **evidence-refresh** move, which is closest to `metadata / tune` — rated **SPENT** in
`traffic-constraint-finding.md`. It is executed here under Vincent's 2026-10-22 standing override
(*"keep posting to find or discover new trends"*). The distinction that matters: this adds **new
primary-source numbers to a page Google is already showing**, which is not the same as rewriting
title/meta on a page with no momentum. Recorded, not re-argued.

REFERRAL remains the constraint and is still unexecuted.
