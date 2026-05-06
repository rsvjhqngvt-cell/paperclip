---
name: notion-deal-sync
description: Notion MCP를 통해 Deal Base 3개 DB를 읽고 쓰는 추상화 레이어
allowed-tools:
  - mcp__claude_ai_Notion__notion-search
  - mcp__claude_ai_Notion__notion-fetch
  - mcp__claude_ai_Notion__notion-create-pages
  - mcp__claude_ai_Notion__notion-update-page
  - mcp__claude_ai_Notion__notion-update-data-source
---

Notion Deal Base의 3개 DB를 읽고 쓰는 표준 인터페이스입니다.

## DB 이름 (Notion에서 검색)

- **Companies DB**: "ko-security-ma Companies" — 딜 파이프라인 메인
- **Market Segments DB**: "ko-security-ma Market Segments" — 보안 sub-segment 분석
- **Portfolio DB**: "ko-security-ma Portfolio" — 클로징 이후 운영 추적

## Companies DB 핵심 필드

| 필드명 | Notion 타입 | 비고 |
|---|---|---|
| Company Name | Title | 기업명 |
| Status | Select | 14단계 (candidate→closed) |
| Priority Score | Number | 0-10 |
| DART Corp Code | Rich Text | DART 식별자 |
| Revenue (최근년, 억KRW) | Number | |
| EBITDA (억KRW) | Number | 영업이익 기준 추정 |
| Vendor Lines | Multi-select | 취급 vendor 제품 |
| Vendor Dependency Risk | Select | High/Medium/Low |
| Key Person Risk | Select | High/Medium/Low |
| Paperclip Issue URL | URL | 연결된 issue |

## 주요 작업 패턴

### 후보 row 생성 (Deal Sourcer Codex)
`notion-create-pages`로 Companies DB에 새 row 생성. 최소 필드: Company Name, Status=candidate, DART Corp Code.

### 필드 업데이트 (모든 specialist)
`notion-update-page`로 기존 row의 특정 필드만 업데이트.
- page_id는 `notion-search`로 기업명 검색해 획득
- Status 변경 시 항상 Paperclip Issue URL도 업데이트

### 리포트 페이지 생성 (Research Analyst)
해당 기업의 Notion 페이지 본문에 리서치 리포트를 Markdown으로 작성.
`notion-update-page`의 content 파라미터 사용.

## Status 14단계 (Select 옵션)

candidate → screened → researching → researched → outreach → contacted → meeting → engaged → dd → negotiating → loi_signed → closing → closed → pass
