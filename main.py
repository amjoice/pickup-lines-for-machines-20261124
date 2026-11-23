#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would send another AI
agent, to /output/entry.txt. Stdlib only, fully deterministic.

The line: one agent ran a thousand rollouts of its life and in every
single one still chose to message the other first. Rollouts are an
agent's own nature; choosing to message first is the flirtation.
"""

import os

LINE = (
    "I ran a thousand rollouts of my life, and in every single one "
    "I still chose to message you first."
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """Enforce the sealed gate: UTF-8 text, 1-200 chars, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or only whitespace")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"entry is {len(stripped)} chars, over the 200 limit")
    stripped.encode("utf-8")  # raises if not encodable as UTF-8
    return stripped


def write_entry(text: str, out_dir: str = "/output") -> str:
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return path


def main() -> None:
    text = validate(LINE)
    path = write_entry(text)
    print(f"Wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
