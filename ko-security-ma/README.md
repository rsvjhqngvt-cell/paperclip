# 한국 IT 보안 M&A (ko-security-ma)

한국 IT 보안 총판(Distributor) 경영권 인수를 전문으로 하는 AI 에이전트 회사 패키지.
100억 KRW 미만 딜 사이즈, 인수 후 직접 운영.

[agentcompanies/v1](https://agentcompanies.io/specification) 사양 준수 |
[Paperclip](https://github.com/paperclipai/paperclip) 임포트 지원

---

## 비즈니스 테제

IT 보안 솔루션 **총판형** 업체는 사람(인력)이 아닌 **vendor 계약권 + 채널 + 고객 베이스**를 자산으로 보유합니다.
SI(System Integration) 방식과 달리 인수 후 안정적 운영이 가능하며, 100억 미만 한국 중소 총판 시장은 경쟁이 낮습니다.

---

## 워크플로

9단계 파이프라인, 5개 board 승인 게이트:

```
시장선정 → 발굴 → 스크리닝 → 리서치 → 컨택 → DD(외부) → 협상 → 클로징 → PMI
   [G1 승인]           [G2 승인]     [G3 DD발주]  [G4 오퍼]   [G5 클로징]
```

Deal 데이터는 **Notion**에 저장, 작업 큐는 **Paperclip**이 관리합니다.

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
    └── Deal Execution/PMI  Claude [primary, Pattern A] + Codex [reviewer]
```

총 11명. Claude 에이전트: `claude_local`. Codex 에이전트: `codex_local`.

---

## Skills

### Custom (패키지 내부)
| Skill | 용도 |
|---|---|
| `dart-company-profile` | OpenDART MCP 순차 호출 → 기업 프로필 |
| `notion-deal-sync` | Notion Deal Base 3개 DB 읽기/쓰기 |
| `security-vendor-db` | 한국 IT 보안 vendor 참조 데이터 |
| `ko-security-market-research` | Naver Search 보안 시장 특화 쿼리 |
| `outreach-ko-owner` | 한국 SMB 오너 컨택 문화·템플릿 |
| `valuation-sme-ko` | IT 보안 총판 SMB 밸류에이션 |
| `pmi-playbook-security-distributor` | 인수 후 100일 플랜 + KPI |

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
