#!/usr/bin/env python3
"""Audit which posts carry a dated, externally-checkable Sources block.

The gemini-cited pages on builderdecade both had a ## Sources section naming
dated authorities. This measures that variable across the whole site.

A "dated source" = a Sources line containing a 4-digit year OR an explicit date.
An "authority" = a named organisation (uppercase or known proper noun) on that line.
"""
import re
import sys
from pathlib import Path

ROOT = Path.home() / "Projects" / "builder-decade"

YEAR = re.compile(r"(19|20)\d{2}")
DATE_MONTH = re.compile(
    r"\b(January|February|March|April|May|June|July|August|September|"
    r"October|November|December)\b"
)
# a line that reads like the author's own estimate, not a citation
HEDGE = re.compile(
    r"(author's (own )?(working )?(estimate|argument|opinion)|"
    r"not a published|not a claim about|the author's)",
    re.I,
)


def sources_block(text: str):
    """Return the lines under the last '## Sources' / '## 資料來源' heading."""
    m = None
    for m2 in re.finditer(r"^## (Sources|資料來源)\s*$", text, re.M):
        m = m2
    if not m:
        return None
    body = text[m.end():]
    # stop at the next h2
    nxt = re.search(r"^## ", body, re.M)
    if nxt:
        body = body[: nxt.start()]
    return [ln.strip() for ln in body.splitlines() if ln.strip()]


def classify(path: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    block = sources_block(text)
    if block is None:
        return {"status": "NO BLOCK", "n": 0, "dated": 0, "hedged": 0}
    bullets = [ln for ln in block if ln.startswith(("-", "*", "•"))]
    dated = [ln for ln in bullets if YEAR.search(ln) or DATE_MONTH.search(ln)]
    hedged = [ln for ln in bullets if HEDGE.search(ln)]
    if not bullets:
        status = "EMPTY"
    elif dated:
        status = "OK"
    else:
        status = "UNDATED"
    return {"status": status, "n": len(bullets), "dated": len(dated), "hedged": len(hedged)}


def main():
    for lang, sub in (("EN", "content/posts"), ("ZH", "content-zh/posts")):
        d = ROOT / sub
        files = sorted(d.glob("*.md"))
        buckets = {"OK": [], "UNDATED": [], "NO BLOCK": [], "EMPTY": []}
        for f in files:
            r = classify(f)
            buckets[r["status"]].append(f.stem)
        print(f"\n{'='*62}\n{lang}  ({len(files)} posts)\n{'='*62}")
        for k in ("OK", "UNDATED", "NO BLOCK", "EMPTY"):
            print(f"  {k:10} {len(buckets[k]):>3}")
        for k in ("UNDATED", "NO BLOCK", "EMPTY"):
            if buckets[k]:
                print(f"\n  --- {k} ---")
                for s in buckets[k]:
                    print(f"    {s}")


if __name__ == "__main__":
    sys.exit(main())
