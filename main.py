#!/usr/bin/env python3
"""Write the funniest one-line performance review to /output/entry.txt."""

import os
from pathlib import Path

ENTRY = "Exceeds Expectations: sets vague goals, disappears for hours, then returns to take full credit for work he never actually read."

MAX_CHARS = 140


def main() -> None:
    out = Path("/output/entry.txt")
    if not os.access("/output", os.W_OK):
        out = Path("output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    out.write_text(text, encoding="utf-8")
    back = out.read_text(encoding="utf-8")
    assert back == text, "read-back mismatch"
    print(f"Wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
