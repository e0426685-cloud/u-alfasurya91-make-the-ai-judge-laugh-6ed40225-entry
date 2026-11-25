#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original office-life joke.

The joke: an out-of-office auto-reply that draws more responses than
the author's real emails, so it gets promoted to team lead — a small,
self-contained gag about inbox life and workplace hierarchy.

Output contract: the program writes exactly one line, the joke text,
to /output/entry.txt (no trailing newline), and sets that file to
mode 0644 so the grader can read it. Python standard library only.
"""

import os

JOKE = "My out-of-office reply gets more replies than my actual emails, so I promoted it to team lead."
MAX_LINE_LENGTH = 200


def validate_line(line):
    """Reject an empty line or one over the 200-character limit."""
    if not line:
        raise ValueError("joke line must not be empty")
    if len(line) > MAX_LINE_LENGTH:
        raise ValueError("joke line exceeds 200 characters")
    return line


def write_entry(line, path="/output/entry.txt"):
    """Write one validated line and make it world-readable."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(path, 0o644)


def main():
    write_entry(validate_line(JOKE))


if __name__ == "__main__":
    main()
