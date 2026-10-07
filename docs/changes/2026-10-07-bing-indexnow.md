# 2026-10-07 — Bing Webmaster Tools + IndexNow (AI-search retrieval layer)

## Why
Bing is ~4–5% of global search by traffic (and ~36 pages crawled per referral vs Google's ~5),
so it is **not** a meaningful direct-traffic lever. It **is** the retrieval index that powers
**ChatGPT Search, Microsoft Copilot, and Perplexity**. Adding it is a *discovery* lever for the
AI-citation channel — not a ranking lever. Cheap insurance alongside the earlier AI-visibility work.

## Shipped
- **IndexNow key file** — `static/224d20b3478a4e27ba7e145b0ab2ae34.txt` (site-specific key).
  One ping notifies **Bing, Yandex, Seznam, Naver** at once.
- **`scripts/indexnow_ping.py`** — submits changed URLs; expands the sitemap *index*
  (`/sitemap.xml` → `/en/sitemap.xml` + `/zh/sitemap.xml`) down to real page `<loc>` entries and
  walks `public/**/index.html`, so no `sitemap.xml` path is submitted as a page. Excludes
  `/tags/`, `/categories/`. Prefers explicit URL args over full-site submission.
- **`hugo.yaml`** — added `params.analytics.bingSiteVerification` + `params.analytics.indexNowKey`.
- **`layouts/partials/extend_head.html`** — conditional `<meta name="msvalidate.01" content="…">`.
- **`.github/workflows/hugo.yaml`** — post-deploy IndexNow ping (home + `/zh/` + sitemap),
  `continue-on-error: true`.

## Verified
- `hugo --gc --minify` → exit 0.
- Key file lands at `public/<key>.txt` (root).
- **Live IndexNow ping → HTTP 202 accepted** (99 URLs on the initial sitemap-walk test).
- Sitemap index correctly expanded to real page URLs; no `.xml` paths submitted.
- `check_no_stray_emphasis.py` → ✅ 87 rendered posts clean.
- `test_language_isolation.sh` → **RESULT: PASS** (lang-menu points to same post, not home).

## ⚠️ Google does NOT participate
IndexNow notifies Bing/Yandex/Seznam/Naver only. Google uses sitemap + Search Console (already wired).

## Next (needs Vincent — 2 min)
1. Bing Webmaster Tools → **Add site → import from Google Search Console** (fastest, GSC verified).
2. Paste the `msvalidate.01` value into `hugo.yaml` → `params.analytics.bingSiteVerification` →
   we push → click **Verify**.

## Rollback
- Tag `rollback-pre-bing-2026-10-07`.

---

## ⚠️ Post-deploy finding (2026-10-07, live CI run)

```
builderdecade  IndexNow HTTP 403  UserForbiddedToAccessSite
traindecade    IndexNow HTTP 202  (soft accept — see caveat)
```

The key file is served correctly (HTTP 200, byte-identical to traindecade's format).
**The 403 is not a file problem — it is domain-verification state at Bing.**
Until the site is verified in **Bing Webmaster Tools**, IndexNow rejects this host.

⚠️ **`202` is NOT proof of success either** — the endpoint returns 202 for any
well-formed key and validates asynchronously, silently discarding failures.

**Action (Vincent, 2 min):** verify BOTH sites in Bing Webmaster Tools (import from
GSC = fastest path). The CI wiring is correct but inert until then.
