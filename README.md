# Buffett Letters

워런 버핏의 서한 모음. 원본(HTML/PDF)과 Markdown 변환본을 함께 보관한다.

## 구성

| 폴더 | 내용 | 연도 | 출처 |
|---|---|---|---|
| `shareholder-letters/` | 버크셔 해서웨이 주주서한 | 1969–2025 | [berkshirehathaway.com](https://www.berkshirehathaway.com/letters/letters.html), [초기분 묶음](https://assets.empirefinancialresearch.com/uploads/2021/02/Buffett-Letters-1969-76.pdf), [1970](https://archive.org/details/berkshirehathawayannualreports) |
| `partnership-letters/` | 버핏 파트너십 서한 (묶음본) | 1957–1970 | [buysidedigest.com](https://www.buysidedigest.com/) |

각 폴더 아래:
- `original/` — 내려받은 원본 (연도별 `.html` 또는 `.pdf`)
- `markdown/` — 검색·LLM 활용을 위한 Markdown 변환본

## 커버리지

- **1977–2025 주주서한**: 공식 사이트 기준 전 연도 완비.
  - 1977–1997: HTML 원본
  - 1998–2025: PDF 원본 (1998–2003은 공식 페이지가 PDF로 연결되는 래퍼라 PDF를 받음)
- **1969, 1971–1976 주주서한**: 공식 미게시분. 무료 묶음 PDF(`original/1969-1976.pdf`)를 받아 연도별 Markdown으로 분할(`scripts/split_early.py`). 원본은 묶음 1개, Markdown은 연도별로 존재.
- **1970 주주서한**: 무료 묶음본 2종(empire·safalniveshak)이 모두 건너뛴 유일 공백이었다. [archive.org의 1970 연차보고서](https://archive.org/details/berkshirehathawayannualreports)(검색가능 스캔본)에서 받아 Chairman's Letter만 추출(`scripts/fetch_1970.sh`). `original/1970.pdf`는 서한이 아니라 **연차보고서 전체**(재무제표 포함)이고, `markdown/1970.md`는 서한 부분만 담는다. OCR 기반이라 극소수 표기 흔적이 있을 수 있다.
- **1957–1970 파트너십 서한**: 원본은 단일 묶음 PDF, Markdown은 **서한별 29개 파일**로 분할(`scripts/split_partnership.py`). 연차·반기·특별 서한이 모두 포함된다.
  - 파일명은 각 서한의 **dateline(작성일) `YYYY-MM-DD`**. 연차 서한은 이듬해 1~2월에 쓰였으므로 파일명 연도가 대상 연도보다 1 크다(예: `1959-02-11.md` = 1958년 실적 연차 서한). `1957.md`만 OCR에 dateline이 없어 대상 연도로 명명.

이로써 주주서한은 **1969–2025 전 연도 완비**(공백 없음).

## 재현

```bash
# 필요: curl, pdftotext(poppler-utils), python3 + markdownify
pip install markdownify
bash scripts/fetch.sh
```

`scripts/fetch.sh`가 원본을 내려받고 `scripts/convert.py`가 Markdown으로 변환한다.

## 저작권

모든 서한의 저작권은 Warren Buffett / Berkshire Hathaway Inc.에 있다. 이 저장소는 공개된 자료를 학습·연구 목적으로 모은 것이다.
