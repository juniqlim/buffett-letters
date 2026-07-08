#!/usr/bin/env python3
"""Convert downloaded originals (HTML/PDF) to Markdown."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def html_to_md(src: Path, dst: Path) -> None:
    from markdownify import markdownify
    html = src.read_text(encoding="utf-8", errors="replace")
    md = markdownify(html, heading_style="ATX")
    md = "\n".join(line.rstrip() for line in md.splitlines())
    while "\n\n\n" in md:
        md = md.replace("\n\n\n", "\n\n")
    dst.write_text(md.strip() + "\n", encoding="utf-8")


def pdf_to_md(src: Path, dst: Path) -> None:
    txt = subprocess.run(
        ["pdftotext", "-layout", str(src), "-"],
        capture_output=True, text=True, check=True,
    ).stdout
    dst.write_text(txt.strip() + "\n", encoding="utf-8")


def convert_dir(orig: Path, mdout: Path) -> None:
    mdout.mkdir(parents=True, exist_ok=True)
    for src in sorted(orig.iterdir()):
        if src.stem == "1969-1976":
            continue  # handled by split_early.py (per-year output)
        dst = mdout / (src.stem + ".md")
        if src.suffix == ".html":
            html_to_md(src, dst)
        elif src.suffix == ".pdf":
            pdf_to_md(src, dst)
        else:
            continue
        print(f"  {src.name} -> {dst.name}")


if __name__ == "__main__":
    convert_dir(ROOT / "shareholder-letters" / "original",
                ROOT / "shareholder-letters" / "markdown")
    convert_dir(ROOT / "partnership-letters" / "original",
                ROOT / "partnership-letters" / "markdown")
