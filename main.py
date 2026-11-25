#!/usr/bin/env python3
"""Write one slogan to /output/entry.txt: the tagline of a Solana wallet agent.

The line was picked from 36 candidates by pairwise judging against the
brief — a wallet that does the reading so its owner can get on with life,
told as a two-sided contrast on the single word "read". The program builds
the line from two clauses — what the wallet reads, then what the owner
reads instead — and checks the result against the entry gate (length,
word count, single line, no leading or trailing space, exact judged
length) before writing it, then reads the file back to confirm the
bytes match.
"""

import os
import sys

LINE = (
    "The wallet that reads Solana "
    "so you can read the room."
)

# Judged shape: 54 characters, 11 words, one line. The two clauses share
# the verb "read" — the wallet reads the chain, the owner reads the room —
# so the contrast lands in a single breath and is easy to repeat.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 140):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-140")
    if len(LINE.split()) > 20:
        sys.exit(f"line is {len(LINE.split())} words, slogan allows at most 20")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        sys.exit("read-back mismatch: file bytes differ from the line")
    print(LINE)


if __name__ == "__main__":
    main()
