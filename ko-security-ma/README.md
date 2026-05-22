# 한국 IT 보안 솔루션 · 총판 M&A (ko-security-ma)

한국 IT 보안 솔루션 기업, 총판/리셀러, 채널 기반 운영형 보안회사의 경영권 인수를 전문으로 하는 AI 에이전트 회사 패키지.
100억 KRW 미만 딜 사이즈를 우선 대상으로 하며, 인수 후 직접 운영과 bolt-on 확장을 함께 고려합니다.

[agentcompanies/v1](https://agentcompanies.io/specification) 사양 준수 |
[Paperclip](https://github.com/paperclipai/paperclip) 임포트 지원

---

## 비즈니스 테제

이 템플릿은 아래 4가지 타깃을 함께 다룹니다.

1. **총판/마스터 리셀러**: vendor 계약권, 리셀러 네트워크, 고객 베이스를 보유
2. **솔루션 리셀러 / VAR**: 라이선스·유지보수·서비스가 결합된 반복 매출 구조 보유
3. **운영형 보안회사(MSSP-light)**: 표준화된 관제/운영 서비스와 라이선스 매출을 함께 보유
4. **AI 보안 전문회사/채널**: AI 레드팀, 가드레일, 에이전트 보안, AI 운영통제 역량 보유

핵심은 사람 투입형 SI가 아니라 **vendor 권한 + 반복 매출 + 고객 관계 + 채널 자산**을 보유한 회사를 찾는 것입니다.
순수 구축형 SI, 상주 인력 의존형 사업, 일회성 프로젝트 중심 업체는 기본적으로 제외합니다.

---

## 워크플로

9단계 파이프라인, 5개 board 승인 게이트:

```
시장선정 → 발굴 → 스크리닝 → 리서치 → 컨택 → DD(외부) → 협상 → 클로징 → PMI
   [G1 승인]           [G2 승인]     [G3 DD발주]  [G4 오퍼]   [G5 클로징]
```

Deal 데이터는 **Notion**에 저장, 작업 큐는 **Paperclip**이 관리합니다.

---

## 타깃 필터

- 공식 vendor 파트너/총판/리셀러 자격 보유
- 라이선스, 유지보수, 구독, 운영 매출이 의미 있게 존재
- 오너 의존도가 높더라도 승계·잔류 구조 설계가 가능한 상태
- 인수 후 vendor 승인 이전, 고객 유지, 운영 인수인계가 가능한 구조
- 순수 SI/인력파견 매출 비중이 과도하지 않을 것
- AI/LLM 보안의 경우 프롬프트·툴콜·데이터 유출 통제 역량이 실체적으로 존재할 것

---

## 조직도

```
BOARD (사용자)
    │
    ▼
CEO (claude_local, claude-opus-4-7)
    │
    ├── Market Analyst      Claude [primary, Pattern A] + Codex [reviewer]
    ├── Deal Sourcer        Claude [scoring] + Codex [data fetch, Pattern C]
    ├── Research Analyst    Claude [primary, Pattern A] + Codex [reviewer]
    ├── Outreach Manager    Claude [synthesis] + Codex [parallel drafts, Pattern B]
    ├── Deal Execution/PMI  Claude [primary, Pattern A] + Codex [reviewer]
    └── AI Security         Claude [primary, Pattern A] + Codex [reviewer]
```

총 13명. Claude 에이전트: `claude_local`. Codex 에이전트: `codex_local`.

---

## Skills

### Custom (패키지 내부)
| Skill | 용도 |
|---|---|
| `dart-company-profile` | OpenDART MCP 순차 호출 → 기업 프로필 |
| `notion-deal-sync` | Notion Deal Base 3개 DB 읽기/쓰기 |
| `security-vendor-db` | 한국 IT 보안 vendor·채널 구조 참조 데이터 |
| `ko-security-market-research` | Naver Search 보안 시장 특화 쿼리 |
| `outreach-ko-owner` | 한국 SMB 오너 컨택 문화·템플릿 |
| `valuation-sme-ko` | IT 보안 솔루션/총판 SMB 밸류에이션 |
| `pmi-playbook-security-distributor` | 인수 후 100일 플랜 + KPI + vendor 인수인계 |
| `ai-redteam-guardrail-dd` | AI 레드팀·가드레일·에이전트 보안 DD 체크리스트 |

### Referenced (마켓플레이스)
`paperclip`, `market-segment-analysis`, `competitive-intelligence`,
`cold-outreach`, `valuation-fundamentals`, `dd-coordination`

---

## 필요 시크릿

```
ANTHROPIC_API_KEY   # Claude 에이전트
OPENAI_API_KEY      # Codex 에이전트
NOTION_TOKEN        # Deal Base 연동
GOOGLE_OAUTH_TOKEN  # Gmail / Calendar / Drive
```

---

## Import 방법

```bash
paperclip company import --from ko-security-ma
```

import 전 필수:
1. Notion에 `ko-security-ma Companies`, `Market Segments`, `Portfolio` DB 생성
2. Referenced skill SHA 확정 (`git ls-remote https://github.com/paperclipai/paperclip HEAD`)
3. 4개 시크릿을 Paperclip secrets에 등록

---

Generated with [Paperclip](https://github.com/paperclipai/paperclip) |
[agentcompanies/v1 spec](https://agentcompanies.io/specification)
