#!/usr/bin/env bash
# 회계연도 1970 서한: 공식/무료 묶음본에 없어 archive.org의 1970 연차보고서
# (검색가능 스캔본)에서 받아 Chairman's Letter만 추출한다.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
UA="Mozilla/5.0"
BASE="https://archive.org/download/berkshirehathawayannualreports"
TMP="$(mktemp -d)"

# 원본: 전체 연차보고서 검색가능 PDF
curl -sL --compressed --retry 3 --max-time 180 -A "$UA" \
  "$BASE/berkshirehathaway1970_text.pdf" \
  -o "$ROOT/shareholder-letters/original/1970.pdf"

# 서한 추출용 OCR 텍스트
curl -sL --compressed --retry 3 --max-time 60 -A "$UA" \
  "$BASE/berkshirehathaway1970_djvu.txt" -o "$TMP/1970.txt"

python3 - "$TMP/1970.txt" "$ROOT/shareholder-letters/markdown/1970.md" <<'PY'
import re, sys
lines = open(sys.argv[1], encoding="utf-8").read().splitlines()
# "To the Stockholders of" ~ "Chairman of the Board" 사이가 서한 본문
start = next(i for i, l in enumerate(lines) if "To the Stockholders of" in l)
end = next(i for i, l in enumerate(lines) if "Chairman of the Board" in l)
text = "\n".join(lines[start:end + 1])
text = text.replace("¬ \n", "").replace("¬\n", "").replace("¬", "")
text = re.sub(r"\n\s*\d+\s*\n", "\n\n", text)      # 본문 중 페이지번호 줄
text = re.sub(r"[ \t]+", " ", text)
text = "\n".join(l.rstrip() for l in text.splitlines())
text = re.sub(r"\n{3,}", "\n\n", text)
open(sys.argv[2], "w", encoding="utf-8").write(text.strip() + "\n")
print("1970.md:", len(text.strip().splitlines()), "lines")
PY
rm -rf "$TMP"
