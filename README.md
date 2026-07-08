# Buffett Letters

워런 버핏의 서한 모음. 원본(HTML/PDF)과 Markdown 변환본을 함께 보관한다.

## 구성

| 폴더 | 내용 | 연도 | 출처 |
|---|---|---|---|
| `shareholder-letters/` | 버크셔 해서웨이 주주서한 | 1969, 1971–2025 | [berkshirehathaway.com](https://www.berkshirehathaway.com/letters/letters.html), [초기분 묶음](https://assets.empirefinancialresearch.com/uploads/2021/02/Buffett-Letters-1969-76.pdf) |
| `partnership-letters/` | 버핏 파트너십 서한 (묶음본) | 1957–1970 | [buysidedigest.com](https://www.buysidedigest.com/) |

각 폴더 아래:
- `original/` — 내려받은 원본 (연도별 `.html` 또는 `.pdf`)
- `markdown/` — 검색·LLM 활용을 위한 Markdown 변환본

## 커버리지

- **1977–2025 주주서한**: 공식 사이트 기준 전 연도 완비.
  - 1977–1997: HTML 원본
  - 1998–2025: PDF 원본 (1998–2003은 공식 페이지가 PDF로 연결되는 래퍼라 PDF를 받음)
- **1969, 1971–1976 주주서한**: 공식 미게시분. 무료 묶음 PDF(`original/1969-1976.pdf`)를 받아 연도별 Markdown으로 분할(`scripts/split_early.py`). 원본은 묶음 1개, Markdown은 연도별로 존재.
- **1957–1970 파트너십 서한**: 개별 파일이 아닌 단일 묶음 PDF.

### 공백: 회계연도 1970 버크셔 서한

1970 서한(1971-03 서명, Kenneth Chase 명의)은 **존재하나 미수록**이다. 이유:
- 공식 사이트는 1977년치부터만 게시.
- 무료 묶음본(empirefinancialresearch, safalniveshak) 둘 다 1969·1971–1976만 담고 **1970을 건너뜀**.
- 유일하게 확인된 무료 단독 출처(`theoraclesclassroom.com`의 1970 연차보고서 PDF)는 구축 환경의 네트워크 필터가 도메인을 차단해 받지 못함.

온전한 1970 서한은 Max Olson의 유료 책(*Berkshire Hathaway Letters to Shareholders, 1965–*)이나 위 차단 도메인에서 직접 받을 수 있다.

## 재현

```bash
# 필요: curl, pdftotext(poppler-utils), python3 + markdownify
pip install markdownify
bash scripts/fetch.sh
```

`scripts/fetch.sh`가 원본을 내려받고 `scripts/convert.py`가 Markdown으로 변환한다.

## 저작권

모든 서한의 저작권은 Warren Buffett / Berkshire Hathaway Inc.에 있다. 이 저장소는 공개된 자료를 학습·연구 목적으로 모은 것이다.
