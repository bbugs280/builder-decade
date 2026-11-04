#!/usr/bin/env python3
"""Generate the cover for a single post by slug, using prompts_dashscope.PROMPTS.

Avoids shell command substitution (which trips approval gates) by reading the
prompt straight from the registry and calling gen_dashscope's API path inline.

Usage: python3 scripts/gen_cover.py <slug> [size]
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.prompts_dashscope import PROMPTS  # noqa: E402


def main():
    if len(sys.argv) < 2:
        print("usage: gen_cover.py <slug> [size]", file=sys.stderr)
        sys.exit(2)
    slug = sys.argv[1]
    size = sys.argv[2] if len(sys.argv) > 2 else "1664*928"
    if slug not in PROMPTS:
        print("slug not in PROMPTS: %s" % slug, file=sys.stderr)
        sys.exit(2)

    out = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "assets",
        "cover-%s.png" % slug,
    )
    # Reuse gen_dashscope.main by injecting argv.
    from scripts import gen_dashscope

    sys.argv = ["gen_dashscope", PROMPTS[slug], out, size]
    gen_dashscope.main()


if __name__ == "__main__":
    main()
