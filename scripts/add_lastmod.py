#!/usr/bin/env python3
"""Add a `lastmod` field to every builder-decade post that has `date:` but no `lastmod:`.

Freshness signal for Google's quality reviewers. Idempotent.
"""
import glob
import re

LASTMOD = "2026-09-02T08:00:00+08:00"
files = sorted(glob.glob("content/posts/*.md") + glob.glob("content-zh/posts/*.md"))

updated = []
skipped = []
for f in files:
    s = open(f).read()
    if "date:" not in s:
        skipped.append((f, "no date field"))
        continue
    if "lastmod:" in s:
        skipped.append((f, "has lastmod already"))
        continue
    s2 = re.sub(
        r"(^date:.*$)",
        r"\1\nlastmod: " + LASTMOD,
        s,
        count=1,
        flags=re.M,
    )
    if s2 != s:
        open(f, "w").write(s2)
        updated.append(f)
    else:
        skipped.append((f, "no change"))

print(f"updated {len(updated)} files")
for f in updated:
    print(f"  + {f}")
print(f"skipped {len(skipped)} files")
