#!/usr/bin/env python3
"""Add a `lastmod` field to every Hugo post (EN + ZH) missing one.

Freshness signal for Google's AdSense quality reviewers — emits `dateModified`
in JSON-LD. Idempotent: skips files that already carry a `lastmod:` line.

Usage:
    python3 scripts/add_lastmod.py [timestamp]
    # timestamp defaults to now (HKT +08:00)

Run from the Hugo repo root; globs `content/posts/*.md` + `content-zh/posts/*.md`.
If the ZH content dir differs (e.g. `content/zh/`), edit the globs.
"""
import glob
import re
import sys
from datetime import datetime, timedelta, timezone

HKT = timezone(timedelta(hours=8))
LASTMOD = (
    sys.argv[1]
    if len(sys.argv) > 1
    else datetime.now(HKT).strftime("%Y-%m-%dT%H:%M:%S+08:00")
)

files = sorted(glob.glob("content/posts/*.md") + glob.glob("content-zh/posts/*.md"))
if not files:
    print("no posts found (run from repo root; expected content/posts/*.md + content-zh/posts/*.md)")
    sys.exit(1)

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
    s2 = re.sub(r"(^date:.*$)", r"\1\nlastmod: " + LASTMOD, s, count=1, flags=re.M)
    if s2 != s:
        open(f, "w").write(s2)
        updated.append(f)
    else:
        skipped.append((f, "no change"))

print(f"updated {len(updated)} files")
for f in updated:
    print(f"  + {f}")
print(f"skipped {len(skipped)} files")
