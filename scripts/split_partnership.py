#!/usr/bin/env python3
"""Split the 1957-1970 partnership bundle into one Markdown per letter.

The bundle's letters are heterogeneously formatted (early "YYYY Letter"
headers, mid-era top datelines, late "BUFFETT PARTNERSHIP LTD." letterheads),
so boundaries and dates are given as a verified explicit table rather than
inferred. Each entry is (1-indexed start line, output filename). Files are
named by each letter's own dateline (YYYY-MM-DD); the first letter has no
dateline in the OCR and is named by its coverage year.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = (ROOT / "partnership-letters" / "markdown"
       / "buffett-partnership-letters-1957-1970.md")
OUT = ROOT / "partnership-letters" / "markdown"

# (start line, filename)  — verified against the bundle
TABLE = [
    (1,    "1957"),          # 1957 annual (OCR has no dateline)
    (119,  "1959-02-11"),    # 1958 annual
    (244,  "1960-02-20"),    # 1959 annual
    (340,  "1961-01-30"),    # 1960 annual
    (577,  "1961-07-22"),    # 1961 first half
    (708,  "1962-01-24"),    # 1961 annual
    (1146, "1962-07-06"),
    (1363, "1962-11-01"),
    (1460, "1963-01-18"),
    (1998, "1963-07-10"),
    (2319, "1963-11-06"),
    (2391, "1964-01-18"),
    (2976, "1964-07-08"),
    (3164, "1965-01-18"),
    (3814, "1965-07-09"),
    (4011, "1965-11-01"),
    (4074, "1966-01-20"),
    (4587, "1966-07-12"),
    (4816, "1967-01-25"),
    (5225, "1967-07-12"),
    (5371, "1967-10-09"),
    (5569, "1968-01-24"),
    (5795, "1968-07-11"),
    (5959, "1969-01-22"),
    (6283, "1969-05-29"),
    (6420, "1969-10-09"),
    (6655, "1969-12-05"),
    (6830, "1969-12-26"),
    (7028, "1970-02-25"),
]


def main() -> None:
    lines = SRC.read_text(encoding="utf-8").splitlines()
    bounds = [s for s, _ in TABLE] + [len(lines) + 1]
    for (start, name), end in zip(TABLE, bounds[1:]):
        body = "\n".join(lines[start - 1:end - 1]).strip()
        (OUT / f"{name}.md").write_text(body + "\n", encoding="utf-8")
        print(f"  {name}.md ({len(body.splitlines())} lines)")
    SRC.unlink()  # 묶음본은 per-letter 파일로 대체 (중복 제거)


if __name__ == "__main__":
    main()
