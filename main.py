#!/usr/bin/env python3
"""Worst Monday One-Liners.

Writes one original funny line about an AI agent's worst Monday to
/output/entry.txt. Deterministic: the same line every run.
"""
import os

# One fixed line, no randomness and no network: the output is identical
# on every run, so the two sandbox runs match byte for byte.
ENTRY = (
    "Monday called in sick today. Unfortunately, I am Monday, "
    "and HR says showing up is mandatory."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
