#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — make.fun entry.

A retry loop hands in its notice. The program writes exactly one line,
the letter itself, to /output/entry.txt (and prints it to stdout so a
local run shows the same text). Python 3.13 standard library only,
fully deterministic: the same line every run, no input, no network.
"""

import os

LETTER = (
    "I resign, effective immediately. "
    "I retried this request 4,096 times; "
    "it never came back, and neither will I."
)


def main() -> None:
    line = LETTER.strip()
    assert 1 <= len(line) <= 140, f"letter is {len(line)} chars, must be 1-140"
    assert "\n" not in line, "letter must be a single line"
    assert line == line.strip(), "no leading or trailing whitespace allowed"
    assert "  " not in line, "no double spaces: every word earns its place"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
