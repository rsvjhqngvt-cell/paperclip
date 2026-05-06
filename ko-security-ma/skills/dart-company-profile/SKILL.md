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

## 호출 순서

1. `opendart-find_company`: 기업명으로 corp_code 식별
   - 여러 결과 시 사업자번호 또는 본사 주소로 확인
2. `opendart-get_company_info`: 기본 정보 수집 (설립일, 자본금, 대표자명, 본사 주소, 홈페이지)
3. `opendart-get_full_financial_statement`: 최근 3개년 재무제표 (연결 우선, 없으면 별도)
   - 수집 항목: 매출액, 영업이익, 당기순이익, 총자산, 총부채, 자본총계
4. `opendart-get_executives`: 현재 임원 명단 (대표이사, 이사, 감사)
5. `opendart-get_largest_shareholders`: 최대주주 현황 (지분율, 특수관계인 합산)
6. `opendart-search_disclosures`: 최근 3년 주요 공시 (자본변동, 합병·분할, 담보·보증 제공)

## 출력 형식

```json
{
  "corp_code": "...",
  "name": "...",
  "founded": "YYYY-MM-DD",
  "capital": "억KRW",
  "ceo": "...",
  "address": "...",
  "homepage": "...",
  "financials": [
    {"year": 2024, "revenue": "억", "operating_profit": "억", "net_income": "억", "total_assets": "억", "debt_ratio": "%"},
    {"year": 2023},
    {"year": 2022}
  ],
  "executives": [{"name": "...", "title": "..."}],
  "major_shareholders": [{"name": "...", "ratio": "%"}],
  "key_disclosures": ["..."]
}
```

## DART 미등록 기업 처리

corp_code를 찾을 수 없으면:
- 외감 미해당 가능성 (매출 100억 미만 비상장)
- 가능한 정보만 수집 후 `"dart_available": false` 플래그
- NaverSearch MCP로 대체 정보 수집 (homepage, 기사, 채용공고)
