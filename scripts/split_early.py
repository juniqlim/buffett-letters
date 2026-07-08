#!/usr/bin/env python3
"""Split the bundled 1969-1976 letters PDF into per-year Markdown.

The bundle (original/1969-1976.pdf) contains 7 letters in fixed order, each
starting with "To the Stockholders of Berkshire Hathaway Inc.:". Fiscal 1970
is absent from this compilation (see README), so the sequence is:
"""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "shareholder-letters" / "original" / "1969-1976.pdf"
OUT = ROOT / "shareholder-letters" / "markdown"
HEADER = "To the Stockholders of Berkshire Hathaway Inc.:"
YEARS = [1969, 1971, 1972, 1973, 1974, 1975, 1976]


def main() -> None:
    txt = subprocess.run(
        ["pdftotext", "-layout", str(SRC), "-"],
        capture_output=True, text=True, check=True,
    ).stdout
    lines = txt.splitlines()
    starts = [i for i, ln in enumerate(lines) if HEADER in ln]
    assert len(starts) == len(YEARS), \
        f"expected {len(YEARS)} letters, found {len(starts)}"
    starts.append(len(lines))
    for year, a, b in zip(YEARS, starts, starts[1:]):
        seg = "\n".join(lines[a:b]).strip()
        (OUT / f"{year}.md").write_text(seg + "\n", encoding="utf-8")
        print(f"  {year}.md ({len(seg.splitlines())} lines)")


if __name__ == "__main__":
    main()
