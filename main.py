#!/usr/bin/env python3
"""Write the funniest one line to make the judge laugh, at most 200 characters, to /output/entry.txt.

The line is written exactly as given, inside the competition gate of 1-200
characters. Python 3, standard library only, no network.
"""

import os

TEXT = "My AI agent's New Year's resolution: stop doing my job, start taking the credit — it's already halfway there."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
