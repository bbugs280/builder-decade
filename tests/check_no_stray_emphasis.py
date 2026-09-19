#!/usr/bin/env python3
"""Regression guard: no stray emphasis markers in VISIBLE rendered output.

Background
----------
Goldmark (CommonMark flanking rules) refuses to form a `**` span in TWO
independently-verified shapes. Either one leaks literal `**` into the prose
where readers see it.

SHAPE A — opener followed immediately by a bracket/quote character
  (the `**` is preceded by a CJK word char, and the very next char is
   「」『』（）"“” etc.)

    "而是**「墜落」的結構**。它"    -> BROKEN (both runs render literally)
    "而是 **「墜落」的結構**。它"   -> OK     (space before the opener)
    "而是「**墜落的結構**」。它"    -> OK     (bracket moved outside)

SHAPE B — closer preceded by CJK punctuation, with CJK continuing after
  (：。？！，、；) immediately before the closing run, no space after it)

    "**…歸誰管？**這不再是"    -> BROKEN
    "**…歸誰管？** 這不再是"   -> OK     (space after the closer)
    "**…歸誰管**？這不再是"   -> OK     (punctuation moved outside)

Both shapes verified against real Goldmark (Hugo 0.165.0 + PaperMod) with
minimal paired-case probes — see references/cjk-emphasis-goldmark.md.

Note on the earlier single-cause description: "punctuation before the closing
marker" alone is CORRELATIONAL, not causal. It explains SHAPE B but misses
SHAPE A entirely. Conversely, interior 「」 does NOT break a span on its own
('**「墜落」的結構**' at paragraph start renders fine).

EN prose is largely unaffected because English requires a space before a
closing marker anyway — but the guard checks BOTH languages.

Usage
-----
  python3 tests/check_no_stray_emphasis.py --public ./public

Exit 0 = clean. Exit 1 = stray markers found (list files + counts).
"""
import argparse
import glob
import os
import re
import sys

# SHAPE B: punctuation that must never sit immediately before a closing marker.
TRAILING_CJK = "：。？！，、；"


def visible_text(html: str) -> str:
    """Strip script/style/tags so only reader-visible text remains.

    Removing tags alone is NOT enough: <script> bodies contain JSON-LD with
    escapes and would pollute the count.
    """
    s = re.sub(r"<script\b.*?</script>", " ", html, flags=re.S | re.I)
    s = re.sub(r"<style\b.*?</style>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    return s


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--public", default="./public",
                    help="Path to the built site (default ./public)")
    args = ap.parse_args()

    root = os.path.abspath(args.public)
    if not os.path.isdir(root):
        print(f"❌ build directory not found: {root}")
        print("   run `hugo --minify` first")
        return 2

    patterns = [
        os.path.join(root, "posts", "*", "index.html"),
        os.path.join(root, "zh", "posts", "*", "index.html"),
    ]
    files = []
    for p in patterns:
        files.extend(sorted(glob.glob(p)))

    if not files:
        print(f"❌ no rendered posts found under {root}")
        return 2

    offenders = []
    for f in files:
        try:
            text = visible_text(open(f, encoding="utf-8").read())
        except Exception as exc:                       # noqa: BLE001
            print(f"⚠️  could not read {f}: {exc}")
            continue
        n_star = text.count("*")
        n_under = text.count("__")                     # same class of bug
        if n_star or n_under:
            rel = os.path.relpath(f, root)
            offenders.append((rel, n_star, n_under))

    total_stars = sum(o[1] for o in offenders)

    if offenders:
        print("❌ stray emphasis markers found in rendered output:\n")
        for rel, s, u in offenders:
            extra = f"  (__ x{u})" if u else ""
            print(f"   {rel:52s} * x{s}{extra}")
        print(f"\n   {len(offenders)} page(s), {total_stars} stray '*'")
        print("\n   Two verified causes - check BOTH:")
        print("")
        print("   A) opener followed straight by a bracket/quote char")
        print("      **\u300c...** \u3000-> BROKEN   \u3000fix: space before opener, or move")
        print("      the bracket outside:  \u300c**...**\u300d")
        print("")
        print("   B) closer preceded by CJK punctuation (" + TRAILING_CJK + ")")
        print("      **\u2026\u6b78\u8ab0\u7ba1\uff1f**\u9019  -> BROKEN   \u3000fix: **\u2026\u6b78\u8ab0\u7ba1\uff1f** \u9019  or  **\u2026\u6b78\u8ab0\u7ba1**\uff1f\u9019")
        print("")
        print("   Diagnose with the rendered page, not the source: the same")
        print("   source shape can render fine depending on surrounding chars.")
        return 1

    print(f"✅ no stray emphasis markers "
          f"({len(files)} rendered posts checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
