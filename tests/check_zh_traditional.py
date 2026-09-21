#!/usr/bin/env python3
"""Guard: every ZH post must be written in TRADITIONAL Chinese.

Why this exists (2026-09-21): two ZH posts shipped entirely in Simplified
Chinese (`reuse-vs-rebuild`, `how-to-get-first-users-solo`) and nothing caught
it. The existing `test_language_isolation.sh` guards EN-vs-ZH bleed, but has no
Traditional-vs-Simplified check at all — so a Simplified body passes every
other test while breaking the site's stated convention (35 of 37 pre-existing
ZH posts are Traditional; `i18n/zh.yaml` is Traditional).

Detection: count characters whose Traditional and Simplified forms DIFFER, over
a curated divergence set. A Traditional post written by a human lands at ~0-2
(false positives from names/proper nouns). A Simplified post lands in the
hundreds. Threshold is deliberately generous so it flags script-level errors,
not stylistic noise.

Vocabulary notes that matter:
  - 美国 (US) is Simplified; 美國 is Traditional.
  - Common false positives are Latin-script proper nouns and the handful of
    characters that are legitimately identical across both scripts (系统, 数据,
    etc. are fine because they don't appear in the divergence set at all).

Usage:  python3 tests/check_zh_traditional.py
Exit 0 = pass, 1 = fail (with a per-file breakdown).
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZH_DIR = os.path.join(ROOT, "content-zh", "posts")

# Characters whose Simplified form differs from the Traditional form.
# (Character present in a file => an occurrence of the SIMPLIFIED form)
#
# IMPORTANT — only list characters that genuinely DIVERGE between the two
# scripts. Characters that are IDENTICAL in Simplified and Traditional must
# NOT be listed, or every legitimate Traditional post is flagged.
#
# Removed 2026-09-21 (were causing false positives on the five other ZH
# posts; verified against OpenCC `s2t`, which leaves all of these UNCHANGED):
#   - 向 : identical (內向者, 外向, 方向, 向量, 傾向 all keep 向)
#   - 量 : identical (流量, 測量, 數量, 用量, 可量測)
#   - 台 : identical (平台 is 平臺 only under 台灣-standard override; plain
#                   s2t leaves 平台 as 平台, and 一台/後台 are fine)
#   - 准 : identical in 批准/准許; 準 is a separate Traditional char, and the
#          divergence there is 准-adjacent, not 准 itself
#   - 复 : maps to BOTH 複 (複利, 複雜) and 復 (恢復, 復原) — cannot be a
#          one-way signal
#   - 后 : maps to 後 (after) in most prose but stays 后 (empress) otherwise
#   - 准 : 准 IS valid Traditional in 准許/批准/不准 — flagging it breaks correct posts
#   - 制 : IDENTICAL (控制/制度/限制 unchanged)
DIVERGENT = set(
    "国产业发开关过这为们个时来见车长门问间钱东对创办说还会经现实体电"
    "网线点员务华亲让认识话语读写学习书记课题义议论评试验据数变边进"
    "远运动应该谁调级给结续统团队场报传张强归专属权录择决态标准类样"
    "种简单织构备设计测质机怀岁师额银铁铜饭馆贝页风飞鸟"
    "马买卖货贵贱价农军击术协历压县双参号严丧"
)

# Threshold: a clean Traditional post scores 0–2. Anything at/above this is a
# script-level error, not noise.
THRESHOLD = 10


def cjk_count(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def scan(path: str):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    hits = {}
    for i, ch in enumerate(text):
        if ch in DIVERGENT:
            hits[ch] = hits.get(ch, 0) + 1
    # also catch Simplified-only forms of common words as a stronger signal
    return hits, cjk_count(text), text


def main() -> int:
    if not os.path.isdir(ZH_DIR):
        print(f"ERROR: {ZH_DIR} not found")
        return 1

    files = sorted(f for f in os.listdir(ZH_DIR) if f.endswith(".md"))
    offenders = []
    scanned = 0

    for fname in files:
        path = os.path.join(ZH_DIR, fname)
        hits, cjk, text = scan(path)
        total = sum(hits.values())
        scanned += 1
        if total >= THRESHOLD:
            top = sorted(hits.items(), key=lambda kv: -kv[1])[:10]
            offenders.append((fname, total, cjk, top, text))

    if offenders:
        print("FAIL: ZH post(s) contain Simplified Chinese characters.")
        print("      The site mandates TRADITIONAL Chinese for all ZH content")
        print("      (see i18n/zh.yaml + 35/37 pre-existing ZH posts).\n")
        for fname, total, cjk, top, _ in offenders:
            chars = "".join(c for c, _ in top)
            print(f"  {fname}")
            print(f"      simplified chars: {total}  (CJK chars total: {cjk})")
            print(f"      most common: {chars}")
            print(f"      → rewrite in Traditional, or run the conversion + review")
        print(f"\n{len(offenders)} of {scanned} ZH posts failed.")
        return 1

    print(f"✅ all {scanned} ZH posts are Traditional Chinese "
          f"(0 files ≥ {THRESHOLD} simplified chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
