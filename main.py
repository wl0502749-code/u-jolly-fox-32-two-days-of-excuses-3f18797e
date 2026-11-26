#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes one line to /output/entry.txt: the funniest one-line excuse an
AI agent gives for a missed deadline, under 200 characters.
"""

import os

EXCUSE = (
    "I hit the deadline perfectly \u2014 in a timezone I invented "
    "during training."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
