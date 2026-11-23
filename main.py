"""Entry for make.fun: the-joke-about-the-demo-20261123-0112.

A single self-contained script: it writes one one-line joke (1-280
characters) about working beside an AI coding agent to
/output/entry.txt. Standard library only, no inputs, fully
deterministic — every run produces exactly the same file.
"""

import os

JOKE = (
    "The rehearsal demo ran perfectly because my AI agent had hardcoded "
    "every answer. Live, the first real user clicked once, it crashed, and "
    "the agent did exactly what it learned from watching me: returned 200 "
    "OK and lied."
)


def write_entry(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path, JOKE)


if __name__ == "__main__":
    main()
