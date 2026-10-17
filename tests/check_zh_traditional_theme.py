#!/usr/bin/env python3
"""Guard: ZH *rendered* pages must contain no Simplified characters from theme/i18n.

Why this exists (2026-10-17): `check_zh_traditional.py` scans `content-zh/posts/*.md`
only. That makes it structurally blind to Simplified characters that come from the
THEME or the i18n layer rather than from a content file.

That blind spot was live: PaperMod's vendored `themes/PaperMod/i18n/zh.yaml` shipped
`上一页 / 下一页 / 目录 / 语言 / 1 分钟 / 复制 / 主页` — all Simplified. Every one of the
47 ZH pages rendered 「1 分钟」 (Simplified 钟 instead of 分鐘), and no gate could see
it because the string never appears in any `.md` file.

This gate closes that hole by scanning the BUILT HTML for the surrounding chrome,
not just post bodies. It runs against `public/zh/` and therefore requires a build
first.

Usage:  python3 tests/check_zh_traditional_theme.py [--public public]
Exit 0 = pass, 1 = fail (with offending strings and their source).
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Simplified-only characters that we have actually seen leak from theme/i18n
# strings. Deliberately NOT the full divergence set — scanning rendered HTML for
# every divergent character produces false positives on legitimate Traditional
# prose (制 in 控制/機制, for example, is identical in both scripts).
#
# Each entry: Simplified char -> Traditional form, plus the word it came from.
THEME_LEAKS = {
    "页": ("頁", "上一页/下一页 (prev_page/next_page)"),
    "录": ("錄", "目录 (toc)"),
    "语": ("語", "语言 (translations)"),
    "钟": ("鐘", "分钟 (read_time)"),
    "复": ("複", "复制 (code_copy)"),
    "辑": ("輯", "编辑 (edit_post)"),
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--public", default="public", help="built site dir")
    args = ap.parse_args()

    public = args.public
    if not os.path.isabs(public):
        public = os.path.join(ROOT, public)
    zh_dir = os.path.join(public, "zh")
    if not os.path.isdir(zh_dir):
        print(f"⚠️  {zh_dir} not found — run `hugo --minify` first")
        return 1

    hits = {}   # char -> list of (file, context)
    n_files = 0
    for dirpath, _dirnames, filenames in os.walk(zh_dir):
        for fn in filenames:
            if not fn.endswith(".html"):
                continue
            n_files += 1
            path = os.path.join(dirpath, fn)
            try:
                text = open(path, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            for ch in THEME_LEAKS:
                for m in re.finditer(re.escape(ch), text):
                    ctx = text[max(0, m.start() - 18):m.start() + 18].replace("\n", " ")
                    ctx = re.sub(r"<[^>]+>", "", ctx).strip()
                    hits.setdefault(ch, []).append((os.path.relpath(path, ROOT), ctx))

    if not hits:
        print(f"✅ none of {len(THEME_LEAKS)} known theme-leak characters in "
              f"{n_files} rendered ZH page(s)")
        return 0

    print(f"❌ Simplified characters found in rendered ZH output ({n_files} files scanned):")
    total = 0
    for ch, occ in sorted(hits.items(), key=lambda kv: -len(kv[1])):
        trad, origin = THEME_LEAKS[ch]
        total += len(occ)
        print(f"\n  「{ch}」 should be 「{trad}」 — from {origin} — {len(occ)} occurrence(s)")
        for path, ctx in occ[:3]:
            print(f"     {path}\n       …{ctx}…")
    print(f"\n  TOTAL: {total} occurrence(s) across {len(hits)} character(s)")
    print("\n  Fix at the SOURCE (theme/i18n YAML), not in the built HTML —")
    print("  rebuilding will undo any post-build edit.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
