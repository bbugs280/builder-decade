#!/usr/bin/env bash
#
# Regression test: EN and ZH home pages MUST NOT mix languages.
#
# Bug (2026-08-23): `layouts/list.html` used the GLOBAL `site.RegularPages`
# (all languages) instead of the per-language `.Site.RegularPages`. On the
# Linux CI build, Go's map iteration order let the ZH posts win pagination on
# the EN home page, so `/` served Chinese titles + `/zh/posts/...` links while
# still declaring `lang=en`. Local macOS builds happened to order EN first, so
# the bug was invisible locally — it only reproduced in CI.
#
# Fix: `where .Site.RegularPages "Type" "in" site.Params.mainSections`
# (current-language scope) instead of `where site.RegularPages ...` (global).
#
# This test rebuilds the site (mirroring CI exactly) and asserts:
#   - EN home (`/`)     → no CJK titles, no `/zh/` post links
#   - ZH home (`/zh/`)  → no English titles, all post links under `/zh/`
#   - per-language post count ≤ content count (no cross-language bleed-in)
#   - no EN slug leaks into ZH home and vice-versa (anchored)
#
# Portable: uses only POSIX tools (no GNU grep -P). CJK detection via a
# character-class grep through an explicit UTF-8 byte range.
#
# Usage:  bash tests/test_language_isolation.sh   (from repo root)
# Exit:   0 = pass, 1 = fail (prints the offending lines)

set -u

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

HUGO_BIN="${HUGO_BIN:-hugo}"
BASEURL="${BASEURL:-https://builderdecade.com/}"

FAIL=0
fail() { echo "FAIL: $1" >&2; FAIL=1; }
ok()   { echo "  ok: $1"; }

echo "== building (mirrors CI: --gc --minify --baseURL) =="
rm -f .hugo_build.lock
tmp_publish="$(mktemp -d)"
"$HUGO_BIN" --gc --minify --baseURL "$BASEURL" --destination "$tmp_publish" >/dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "FAIL: hugo build failed" >&2
  rm -rf "$tmp_publish"
  exit 1
fi
PUB="$tmp_publish"
echo "  build ok"

EN="$PUB/index.html"
ZH="$PUB/zh/index.html"
for f in "$EN" "$ZH"; do
  [ -f "$f" ] || { echo "FAIL: missing output $f" >&2; rm -rf "$tmp_publish"; exit 1; }
done

# Extract the array of "aria-label ... href=..." link tokens from a page.
# Output: one token per line like:  entry-link aria-label="<title>" href=<url>
extract_links() {
  # tr turns the '>' boundary into a newline; grep keeps only entry-link tokens
  tr '>' '\n' < "$1" | grep -oE 'entry-link aria-label="[^"]*" href=[^ ]*'
}

# CJK detection (portable): match any UTF-8 sequence for U+4E00–U+9FFF etc.
# Use LC_ALL=C grep over byte ranges E4 EA EB EF E8 E9 for common CJK blocks.
has_cjk() {
  # $1 = string to test
  printf '%s' "$1" | LC_ALL=C grep -qE $'\xE4[\xB8-\xBF]|\xE5[\x80-\xBF]|\xE6[\x80-\xBF]|\xE7[\x80-\xBF]|\xE8[\x80-\xBF]|\xE9[\x80-\xBF]'
}

EN_EXPECTED=$(find content/posts     -maxdepth 1 -name '*.md' ! -name '_index.md' | wc -l | tr -d ' ')
ZH_EXPECTED=$(find content-zh/posts  -maxdepth 1 -name '*.md' ! -name '_index.md' | wc -l | tr -d ' ')

echo "== EN home (/): no Chinese, no /zh/ links, no bleed-in =="

EN_LINKS=$(extract_links "$EN")

# 0. ORDER-INDEPENDENT bleed-in check: sum post links across ALL pages of each
#    language and compare to the per-language content count. When the global
#    `site.RegularPages` bug is present, EN home lists 24 posts (12 EN + 12 ZH)
#    and ZH also lists 24 — this fires deterministically even when map ordering
#    happens to put EN first locally.
en_total=0
for f in "$PUB/index.html" "$PUB"/page/*/index.html; do
  [ -f "$f" ] || continue
  n=$(extract_links "$f" | grep -c 'entry-link' || true)
  en_total=$((en_total + n))
done
zh_total=0
for f in "$PUB/zh/index.html" "$PUB"/zh/page/*/index.html; do
  [ -f "$f" ] || continue
  n=$(extract_links "$f" | grep -c 'entry-link' || true)
  zh_total=$((zh_total + n))
done
en_expected_pages="$EN_EXPECTED"
zh_expected_pages="$ZH_EXPECTED"
if [ "$en_total" -gt "$en_expected_pages" ]; then
  fail "ORDER-INDEPENDENT: EN lists $en_total posts total (expected $en_expected_pages) — cross-language bleed-in"
else
  ok "EN total posts across all pages == $en_total (≤ $en_expected_pages)"
fi
if [ "$zh_total" -gt "$zh_expected_pages" ]; then
  fail "ORDER-INDEPENDENT: ZH lists $zh_total posts total (expected $zh_expected_pages) — cross-language bleed-in"
else
  ok "ZH total posts across all pages == $zh_total (≤ $zh_expected_pages)"
fi

# 1. no CJK in any EN post link title
cjk_hits=0
while IFS= read -r line; do
  [ -z "$line" ] && continue
  if has_cjk "$line"; then
    fail "EN home has CJK post link: $line"
    cjk_hits=$((cjk_hits+1))
  fi
done <<< "$EN_LINKS"
[ "$cjk_hits" -eq 0 ] && ok "no CJK post titles on EN home"

# 2. no /zh/ post links on EN home
zh_hits=$(printf '%s\n' "$EN_LINKS" | grep -cE 'href=[^ ]*/zh/' || true)
if [ "$zh_hits" -ne 0 ]; then
  fail "EN home has /zh/ post links:"; printf '%s\n' "$EN_LINKS" | grep -E 'href=[^ ]*/zh/' >&2
else
  ok "no /zh/ post links on EN home"
fi

# 3. EN count ≤ expected (extra = bleed-in)
EN_COUNT=$(printf '%s\n' "$EN_LINKS" | grep -c 'entry-link' || true)
if [ "$EN_COUNT" -gt "$EN_EXPECTED" ]; then
  fail "EN home shows $EN_COUNT posts, expected ≤ $EN_EXPECTED (bleed-in)"
else
  ok "EN post count $EN_COUNT ≤ $EN_EXPECTED"
fi

echo "== ZH home (/zh/): no English titles, all /zh/ links, no bleed-in =="

ZH_LINKS=$(extract_links "$ZH")

# 4. no English titles on ZH home: a title is "English" iff it has NO CJK bytes
#    (a ZH title may legitimately embed Latin proper nouns like "AI" / "No-Code"
#     — those still carry CJK, so the zero-CJK test is the correct discriminator)
en_hits=0
while IFS= read -r line; do
  [ -z "$line" ] && continue
  # strip the aria-label wrapper, test the title body only
  title=$(printf '%s' "$line" | sed -E 's/^.*aria-label="post link to (.*)" href=.*/\1/')
  if ! has_cjk "$title"; then
    fail "ZH home has an English (no-CJK) post title: $line"
    en_hits=$((en_hits+1))
  fi
done <<< "$ZH_LINKS"
[ "$en_hits" -eq 0 ] && ok "no English (CJK-free) post titles on ZH home"

# 5. every ZH post link is under /zh/
non_zh=$(printf '%s\n' "$ZH_LINKS" | grep 'entry-link' | grep -vcE 'href=[^ ]*/zh/' || true)
if [ "$non_zh" -ne 0 ]; then
  fail "ZH home has non-/zh/ post links:"; printf '%s\n' "$ZH_LINKS" | grep 'entry-link' | grep -vE 'href=[^ ]*/zh/' >&2
else
  ok "all ZH post links under /zh/"
fi

# 6. ZH count ≤ expected
ZH_COUNT=$(printf '%s\n' "$ZH_LINKS" | grep -c 'entry-link' || true)
if [ "$ZH_COUNT" -gt "$ZH_EXPECTED" ]; then
  fail "ZH home shows $ZH_COUNT posts, expected ≤ $ZH_EXPECTED (bleed-in)"
else
  ok "ZH post count $ZH_COUNT ≤ $ZH_EXPECTED"
fi

echo "== cross-language slug check (anchored) =="
for slug in ship-one-tiny-thing what-agents-cant-do; do
  # EN home must not link to /zh/posts/<slug>
  if printf '%s\n' "$EN_LINKS" | grep -qE 'href=[^ ]*/zh/posts/'"$slug"; then
    fail "EN home links to ZH slug /zh/posts/$slug"
  else
    ok "EN home has no /zh/posts/$slug link"
  fi
  # ZH home must not link to a bare EN URL (/posts/<slug> immediately after the
  # domain — no /zh/ segment). Anchor on the domain so /zh/posts/<slug> (which
  # legitimately contains the substring "/posts/<slug>") does NOT false-match.
  if printf '%s\n' "$ZH_LINKS" | grep -E 'entry-link' | grep -qE 'href='"$BASEURL"'posts/'"$slug"; then
    fail "ZH home links to EN slug /posts/$slug"
  else
    ok "ZH home has no /posts/$slug link"
  fi
done

echo "== language switcher (lang-menu) targets the CURRENT page, not home =="
# Bug (2026-08-30): theme header.html used `site.Home.Translations`, so the
# header lang-toggle always linked to the home page's translation (/zh/ or /)
# instead of the CURRENT page's translation (/zh/posts/<slug>/ etc). Fix: the
# header override uses `.Translations` (the current page's).
# Assert: on a deep post page, the lang-menu href points at the SAME slug in the
# other language (contains /<lang>/posts/<slug>), NOT the bare home (/zh/ only).

# Extract the lang-menu link(s) from a page's header.
# The minifier strips attribute quotes, so match the bare `lang-menu` token and
# grab the first href that follows it (the lang switcher's only anchor).
lang_menu_hrefs() {
  # The header is one long minified line. Match the lang-menu anchor directly:
  # it is the ONLY anchor inside the <ul class=lang-menu> block and immediately
  # follows the literal token `lang-menu>`. Use sed to flexibly capture up to a
  # 200-char window (POSIX sed has no {0,300} grep cap) then pull href=.
  sed -n 's/.*lang-menu>\(.\{0,200\}\).*/\1/p' "$1" | grep -oE 'href=[A-Za-z0-9:./_-]*' | head -1
}

# A representative deep post (must exist in both languages).
DEEP_SLUG="infinite-task-list-ai-era"
EN_POST="$PUB/posts/$DEEP_SLUG/index.html"
ZH_POST="$PUB/zh/posts/$DEEP_SLUG/index.html"
[ -f "$EN_POST" ] || { echo "WARN: no EN post $DEEP_SLUG to test lang-menu (skipping)"; EN_POST=""; }
[ -f "$ZH_POST" ] || { echo "WARN: no ZH post $DEEP_SLUG (skipping)"; ZH_POST=""; }

if [ -n "$EN_POST" ]; then
  en_menu=$(lang_menu_hrefs "$EN_POST")
  if printf '%s\n' "$en_menu" | grep -qE 'href=[^ ]*/zh/posts/'"$DEEP_SLUG"; then
    ok "EN post lang-menu → /zh/posts/$DEEP_SLUG (same post, not home)"
  else
    fail "EN post lang-menu does NOT link to the ZH translation of the same post: $en_menu"
  fi
  # And it must NOT link to the bare home /zh/
  if printf '%s\n' "$en_menu" | grep -qE 'href=[^ ]*/zh/?([ ">]|$)'; then
    fail "EN post lang-menu links to bare /zh/ (home), not the translated post"
  fi
fi

if [ -n "$ZH_POST" ]; then
  zh_menu=$(lang_menu_hrefs "$ZH_POST")
  if printf '%s\n' "$zh_menu" | grep -qE 'href=[^ ]*/posts/'"$DEEP_SLUG"; then
    ok "ZH post lang-menu → /posts/$DEEP_SLUG (same post, not home)"
  else
    fail "ZH post lang-menu does NOT link to the EN original of the same post: $zh_menu"
  fi
fi

rm -rf "$tmp_publish"

echo ""
if [ "$FAIL" -ne 0 ]; then
  echo "RESULT: FAIL"
  exit 1
else
  echo "RESULT: PASS"
  exit 0
fi
