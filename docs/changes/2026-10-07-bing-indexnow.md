# 2026-10-07 — Bing Webmaster Tools + IndexNow (AI-search retrieval layer)

## Why
Bing is ~4–5% of global search by traffic (and ~36 pages crawled per referral vs Google's ~5),
so it is **not** a meaningful direct-traffic lever. It **is** the retrieval index that powers
**ChatGPT Search, Microsoft Copilot, and Perplexity**. Adding it is a *discovery* lever for the
AI-citation channel — not a ranking lever. Cheap insurance alongside the earlier AI-visibility work.

## Shipped
- **IndexNow key file** — `static/7544e52888da4e97b8e7921a794bd6d4.txt`
  (**Bing-issued** key — see "Resolution" below; the initial self-minted key was replaced).
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

## ✅ RESOLUTION (2026-10-07) — builderdecade IndexNow now HTTP 200

The 403 is **fixed**. Both decade sites ping clean:

```
traindecade.com    IndexNow 200 ✅
builderdecade.com  IndexNow 200 ✅
```

### Root cause — Bing's own docs, not inference

`bing.com/indexnow/getstarted` lists integration **Step 1 = "Generate API Key"**, and its
response-code table states:

```
403 Forbidden → "Key not valid (e.g. key not found, or file found but key not in file)"
```

Builderdecade's Bing IndexNow page was still the **onboarding hero** ("Take control of your SEO
game" + *Get Started* button) — no key, no status section. **Bing had never issued a key for the
domain.** The UUID we minted ourselves was invisible to Bing until a key was generated in Bing's
own UI. **The repo, key file, and deploy were all correct.**

### ⚠️ CORRECTION to the post-deploy finding below

The earlier note concluded *"the 403 is not a file problem — it is domain-verification state at
Bing."* **That was WRONG.** The BWT dashboard loaded fully (Home/Sitemaps/IndexNow/Backlinks),
proving the domain **was** verified. The real cause was the **un-generated IndexNow key** — a
second, independent Bing-side gate. Two false leads were burned before this landed:

- ❌ *"domain not verified → go verify"* — the dashboard loaded, so it was already verified.
- ❌ *"our key file is wrong / Bing cached a rejection"* — file served 200, byte-identical to the
  twin's. The problem was that Bing had never *issued* a key.

**⇒ Diagnose by PAGE STATE, not by error code.** `UserForbiddedToAccessSite` is identical whether
the domain is unverified OR the key is simply unregistered, so it cannot distinguish the two.

### Fix shipped (commit `b1fbab6`)

```
hugo.yaml                  indexNowKey → 7544e52888da4e97b8e7921a794bd6d4  (Bing-issued)
static/7544e5…d6d4.txt     new key file added
static/224d20…2ae34.txt    old key file DELETED (a leftover key file is a second wrong answer
                           at a guessable public URL — never leave one behind)
scripts/indexnow_ping.py   KEY constant updated
```

Swap must be **atomic across all three files** — a key file that doesn't match the YAML/script
constant, or a stale key file left served, re-breaks the handshake.

### Verified end-to-end

| Check | Result |
|---|---|
| New key file live | HTTP 200, content correct ✅ |
| Old key file | HTTP 404 ✅ |
| Re-ping (118 URLs) | HTTP 200 ✅ |
| Raw `api.indexnow.org` curl | HTTP 200 ✅ |

Two independent probes — the script's own report *and* a raw curl — so a 200 is not a
script-level false positive.

### Rollback
- Tag `rollback-pre-bing-key-swap-2026-10-07`.

### Scope — unchanged
This is the **AI-discovery layer** (Bing's index feeds **ChatGPT Search, Copilot, Perplexity**).
It does **not** address the pos-55–76 authority problem — that is still backlinks (0 referral
sessions measured). Plumbing is now green; the bottleneck is unchanged.

---

## ⚠️ Original post-deploy finding (2026-10-07, live CI run) — SUPERSEDED, see RESOLUTION above

```
builderdecade  IndexNow HTTP 403  UserForbiddedToAccessSite
traindecade    IndexNow HTTP 202  (soft accept — see caveat)
```

The key file is served correctly (HTTP 200, byte-identical to traindecade's format).

⚠️ **`202` is NOT proof of success either** — the endpoint returns 202 for any
well-formed key and validates asynchronously, silently discarding failures.

⚠️ **The "domain-verification state" diagnosis below was WRONG** — kept only as a record of the
false lead. The domain was verified; the missing piece was the un-generated IndexNow key.
