#!/usr/bin/env bash
# Buffett letters fetcher — downloads originals and converts to Markdown.
# Requires: curl, pdftotext (poppler-utils), python3 + markdownify.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
UA="Mozilla/5.0"
BASE="https://www.berkshirehathaway.com/letters"

get() { curl -sL --compressed --retry 3 --max-time 90 -A "$UA" "$1" -o "$2"; }

echo "== Shareholder letters 1977-1997 (HTML) =="
for y in $(seq 1977 1997); do
  get "$BASE/$y.html" "$ROOT/shareholder-letters/original/$y.html"
done

# 1998-2003: the per-year .html page is only a wrapper linking to the real PDF.
echo "== Shareholder letters 1998-2003 (PDF behind wrapper) =="
get "$BASE/1998pdf.pdf"      "$ROOT/shareholder-letters/original/1998.pdf"
get "$BASE/final1999pdf.pdf" "$ROOT/shareholder-letters/original/1999.pdf"
get "$BASE/2000pdf.pdf"      "$ROOT/shareholder-letters/original/2000.pdf"
get "$BASE/2001pdf.pdf"      "$ROOT/shareholder-letters/original/2001.pdf"
get "$BASE/2002pdf.pdf"      "$ROOT/shareholder-letters/original/2002.pdf"
get "$BASE/2003ltr.pdf"      "$ROOT/shareholder-letters/original/2003.pdf"

echo "== Shareholder letters 2004-2025 (PDF) =="
for y in $(seq 2004 2025); do
  get "$BASE/${y}ltr.pdf" "$ROOT/shareholder-letters/original/$y.pdf"
done

echo "== Partnership letters 1957-1970 (bundled PDF) =="
get "https://www.buysidedigest.com/wp-content/uploads/2024/08/Warren-Buffett-Partnership-letters-1957-1970r.pdf" \
    "$ROOT/partnership-letters/original/buffett-partnership-letters-1957-1970.pdf"

echo "== Convert to Markdown =="
python3 "$ROOT/scripts/convert.py"

echo "Done."
