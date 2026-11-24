#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

The program writes a single line of text (1..240 characters) to
/output/entry.txt: a quiet, earned moment of pride for someone in a
scene — a small person doing something hard, a long effort finally
landing. The judge reads the line two at a time against other entries
and picks the one that feels most genuinely proud.
"""

import os
import sys

ENTRY = (
    "At seventy-three, after three years of evening classes, "
    "Mr. Okafor read his granddaughter's birthday card aloud, "
    "every word, without asking for help once."
)


def entry_path():
    """Where the line goes: /output/entry.txt in the sandbox."""
    return os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def write_entry(path):
    text = ENTRY.strip()
    if not text or len(text) > 240:
        print(f"entry is {len(text)} chars, must be 1..240", file=sys.stderr)
        return 1
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(write_entry(entry_path()))
