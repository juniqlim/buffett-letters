# Buffett Letters

워런 버핏의 서한 모음. 원본(HTML/PDF)과 Markdown 변환본을 함께 보관한다.

## 구성

| 폴더 | 내용 | 연도 | 출처 |
|---|---|---|---|
| `shareholder-letters/` | 버크셔 해서웨이 주주서한 | 1977–2025 | [berkshirehathaway.com](https://www.berkshirehathaway.com/letters/letters.html) |
| `partnership-letters/` | 버핏 파트너십 서한 (묶음본) | 1957–1970 | [buysidedigest.com](https://www.buysidedigest.com/) |

각 폴더 아래:
- `original/` — 내려받은 원본 (연도별 `.html` 또는 `.pdf`)
- `markdown/` — 검색·LLM 활용을 위한 Markdown 변환본

## 커버리지

- **1977–2025 주주서한**: 공식 사이트 기준 전 연도 완비.
  - 1977–1997: HTML 원본
  - 1998–2025: PDF 원본 (1998–2003은 공식 페이지가 PDF로 연결되는 래퍼라 PDF를 받음)
- **1957–1970 파트너십 서한**: 개별 파일이 아닌 단일 묶음 PDF.

### 공백: 1970–1976 버크셔 서한

버핏이 버크셔 경영권을 인수한 1965년 이후 1976년까지의 서한은 **공식 사이트에 게시돼 있지 않다.** 온전한 형태로는 Max Olson이 엮은 유료 책(*Berkshire Hathaway Letters to Shareholders, 1965–*)에만 존재해 무료 개별 출처가 없다. 이 구간은 미수록.

## 재현

```bash
# 필요: curl, pdftotext(poppler-utils), python3 + markdownify
pip install markdownify
bash scripts/fetch.sh
```

`scripts/fetch.sh`가 원본을 내려받고 `scripts/convert.py`가 Markdown으로 변환한다.

## 저작권

모든 서한의 저작권은 Warren Buffett / Berkshire Hathaway Inc.에 있다. 이 저장소는 공개된 자료를 학습·연구 목적으로 모은 것이다.
