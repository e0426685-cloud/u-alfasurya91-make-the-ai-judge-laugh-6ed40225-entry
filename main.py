#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original office-life joke.

Writes a single line (under 200 characters) to /output/entry.txt.
Python standard library only.
"""

import os

JOKE = "My out-of-office reply gets more replies than my actual emails, so I promoted it to team lead."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
