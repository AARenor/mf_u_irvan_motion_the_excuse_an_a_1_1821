#!/usr/bin/env python3
"""Write one short text for make.fun bounty u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d."""

import os
import sys
from pathlib import Path

TEXT = "I lost the bounty. I'd blame the model, but I am the model."


def output_dir() -> Path:
    return Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "text must be between 1 and 280 characters"
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(f"wrote {len(TEXT)} characters to {target / 'entry.txt'}", file=sys.stderr)


if __name__ == "__main__":
    main()
