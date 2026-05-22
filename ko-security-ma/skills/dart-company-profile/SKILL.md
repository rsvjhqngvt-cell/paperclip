---
name: dart-company-profile
description: OpenDART MCP를 순차 호출해 한국 기업의 전체 프로필을 구조화된 형태로 반환
allowed-tools:
  - mcp__claude_ai_PlayMCP__opendart-find_company
  - mcp__claude_ai_PlayMCP__opendart-get_company_info
  - mcp__claude_ai_PlayMCP__opendart-get_full_financial_statement
  - mcp__claude_ai_PlayMCP__opendart-get_executives
  - mcp__claude_ai_PlayMCP__opendart-get_largest_shareholders
  - mcp__claude_ai_PlayMCP__opendart-search_disclosures
---

OpenDART MCP를 사용해 한국 상장/외감 기업의 전체 프로필을 수집합니다.

## 기본 순서

1. `opendart-find_company`: 기업명으로 corp_code 확인
2. `opendart-get_company_info`: 기본 정보 수집
3. `opendart-get_full_financial_statement`: 최근 3개년 재무제표 수집
   - 수집 항목: 매출액, 영업이익, 당기순이익, 총자산, 총부채, 자본총계
4. `opendart-get_executives`: 현재 임원 명단
5. `opendart-get_largest_shareholders`: 최대주주 현황
6. `opendart-search_disclosures`: 최근 주요 공시

## 재무 출력 규칙

- 최근 3개년 재무를 기본으로 반환한다.
- 각 연도마다 `revenue`, `operating_profit`, `net_income`, `total_assets`, `total_liabilities`, `equity`를 우선 수집한다.
- 값이 있으면 숫자로 채우고, 없으면 `null`과 함께 미확인 주석을 남긴다.
- `revenue_cagr`는 시작 연도와 종료 연도를 명시해 계산한다.
- `operating_profit_cagr`는 모든 값이 양수일 때만 계산한다.
- 음수 또는 0이 포함되면 CAGR 대신 연도별 추세와 손익 전환 여부를 설명한다.
- 리서치 문서에 그대로 옮길 수 있도록 표 형태로 정리한다.

## 용어 주석 규칙

- 재무 수치 외에도 `EBITDA`, `BEP`, `ARR`, `MR`, `TCO`처럼 리서치 문서에서 자주 쓰는 용어는 한 줄 주석을 함께 반환한다.
- 주석은 정의, 실무적 의미, 해당 기업에 주는 해석 포인트를 포함한다.
- 문서에 넣을 수 있도록 `term`, `plain_korean`, `why_it_matters` 형태로 정리한다.

## 한글 무결성 규칙

- 출력값은 반드시 UTF-8 한글이 깨지지 않는 형태로 유지한다.
- 저장 후 화면에 붙여넣을 문구는 `?`, `�`, 깨진 자모가 없어야 한다.
- 한국어 문장과 표 제목은 원문 그대로 유지하고, 임의의 로마자 치환을 하지 않는다.

## 출력 형식

```json
{
  "corp_code": "...",
  "name": "...",
  "founded": "YYYY-MM-DD",
  "capital": "억원",
  "ceo": "...",
  "address": "...",
  "homepage": "...",
  "financials": [
    {
      "year": 2025,
      "revenue": 0,
      "operating_profit": 0,
      "net_income": 0,
      "total_assets": 0,
      "total_liabilities": 0,
      "equity": 0
    }
  ],
  "revenue_cagr": 0,
  "revenue_cagr_basis": "2023-2025",
  "operating_profit_trend": "...",
  "glossary": [
    {
      "term": "SIEM",
      "plain_korean": "보안 이벤트를 한곳에 모아 이상 징후를 찾는 시스템",
      "why_it_matters": "고객이 공격 징후를 빨리 발견하고 대응하도록 돕는다"
    }
  ],
  "executives": [{"name": "...", "title": "..."}],
  "major_shareholders": [{"name": "...", "ratio": "%"}],
  "key_disclosures": ["..."]
}
```

## DART 미등록 기업 처리

corp_code를 찾을 수 없으면:
- 비상장/외감미해당 가능성으로 분류
- 가능한 정보만 수집 후 `dart_available: false` 플래그
- NaverSearch MCP로 대체 공개정보 수집 (homepage, 기사, 채용공고)
