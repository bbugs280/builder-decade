#!/usr/bin/env python3
"""
Guard: shortcode JSON payloads must not contain double-encoded strings.

Why this exists
---------------
`layouts/shortcodes/agent-reach.html` builds an i18n payload inside a
<script type="application/json"> block. The first draft applied `| jsonify`
to each value *while it was already inside the JSON block*, which emitted the
string twice-quoted:

    "agent_reach_v0": "\\"Nothing ticked yet. ...\\""

JSON.parse() then yields a value with literal surrounding quote characters, and
the shortcode's JS writes it straight into the verdict element via textContent —
so the reader sees quote marks wrapped around the sentence. It only manifests
*after* interaction, so the server-rendered HTML (and every existing test) looked
clean. build-tester caught it; this guard makes sure it stays caught.

What it checks
--------------
Over the BUILT output, for every <script type="application/json"> payload, every
top-level string value must not begin with an escaped double-quote (`\"`), which
is the signature of a double-encoded value. An escaped quote appearing at the
start of a value almost always means `jsonify` was applied to an already-quoted
string literal.

Run:  python3 tests/check_shortcode_json.py
Exit: 0 = clean, 1 = double-encoding found (or build output missing).
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Directories to scan for built HTML.
SEARCH_ROOTS = ["public"]

# Payload blocks we care about: <script type="application/json" ...>...</script>
SCRIPT_RE = re.compile(
    r'<script[^>]*type=["\']application/json["\'][^>]*>(.*?)</script>',
    re.DOTALL | re.IGNORECASE,
)


def scan_value(path: str, key: str, value: str, problems: list) -> None:
    """Flag a value whose parsed form starts with a literal quote character."""
    if isinstance(value, str) and value.startswith('"') and value.endswith('"') and len(value) > 1:
        problems.append(
            f"{path}: key '{key}' is double-encoded -> parsed value starts/ends "
            f"with a literal quote: {value[:70]!r}"
        )


def walk(obj, path: str, key_path: str, problems: list) -> None:
    """Recursively inspect a parsed JSON payload for double-encoded strings."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            walk(v, path, f"{key_path}.{k}" if key_path else k, problems)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk(v, path, f"{key_path}[{i}]", problems)
    else:
        scan_value(path, key_path, obj, problems)


def main() -> int:
    html_files = []
    for root in SEARCH_ROOTS:
        d = REPO / root
        if not d.exists():
            continue
        html_files.extend(sorted(d.rglob("*.html")))

    if not html_files:
        print("❌ no built HTML found — run `hugo` first (looked in: "
              + ", ".join(SEARCH_ROOTS) + ")")
        return 1

    problems: list = []
    payloads_checked = 0

    for f in html_files:
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for m in SCRIPT_RE.finditer(text):
            raw = m.group(1).strip()
            if not raw:
                continue
            try:
                parsed = json.loads(raw)
            except json.JSONDecodeError:
                # A malformed payload is itself a defect worth surfacing.
                problems.append(
                    f"{f.relative_to(REPO)}: JSON payload does not parse — "
                    f"{raw[:80]!r}"
                )
                continue
            payloads_checked += 1
            walk(parsed, str(f.relative_to(REPO)), "", problems)

    if problems:
        print(f"❌ {len(problems)} double-encoded / malformed JSON payload value(s):")
        for p in problems:
            print(f"  - {p}")
        print("\nLikely cause: `| jsonify` applied to a value that is already a "
              "quoted string inside a <script type=\"application/json\"> block. "
              "Drop the filter and let the surrounding quotes stand.")
        return 1

    print(f"✅ no double-encoded shortcode JSON ({payloads_checked} payload(s) "
          f"checked across {len(html_files)} rendered page(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
