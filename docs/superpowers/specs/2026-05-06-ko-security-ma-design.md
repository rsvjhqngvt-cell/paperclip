# 한국 IT 보안 M&A 회사 (ko-security-ma) — 설계 문서

**작성일**: 2026-05-06  
**상태**: 승인 대기  
**패키지 슬러그**: `ko-security-ma`

---

## 1. 개요

### 비즈니스 정체성

한국 IT 보안 총판 경영권 인수 전문 회사. Search fund / 마이크로 PE 모델.

- **타겟**: 한국 IT 보안 솔루션 **총판(Distributor)** 업체 (SI 제외)
- **딜 사이즈**: 100억 KRW 미만 경영권 인수
- **운영 방식**: 인수 후 직접 경영 (Principal investing)
- **부수 활동**: Buy-side advisory (매수 의향 고객 대상)

총판형 업체를 타겟으로 하는 이유: 자산이 사람(인력)이 아닌 **vendor 계약권 + 채널 + 고객 베이스**에 있어 인수 후 안정적 운영이 가능.

### 산업 테제

**IT 보안 총판 (SI 제외)** — 외산 보안 솔루션 1-3개 라인 보유한 마스터/서브 디스트리뷰터 또는 국산 보안 SW 총판. 매출 규모 30~200억 수준.

주요 타겟 segment (단계 1 분석에서 우선순위 결정):
- EDR / XDR / MDR
- NDR / NTA
- ZTNA / SASE
- IAM / PAM
- DLP / CASB
- OT / ICS 보안
- 클라우드 보안 (CWPP / CSPM)
- WAF / WAAP

---

## 2. 시스템 아키텍처

### 3-tier 구조

```
┌─────────────────────────────────────────────────────────────┐
│  Tier 1: BOARD (사용자)                                      │
│  - 5개 승인 게이트                                           │
│  - CEO와 전략 인터페이스                                     │
└──────────────────┬──────────────────────────────────────────┘
                   │ 승인 / 지시
┌──────────────────▼──────────────────────────────────────────┐
│  Tier 2: PAPERCLIP (Control Plane)                          │
│  - 11개 에이전트 (CEO + 10 specialists, Claude/Codex 짝)     │
│  - Issue 워크플로 (단계별 배정 + 핸드오프)                   │
│  - 활동 로그 · 예산 · 하트비트 · board approval             │
└──────────────────┬──────────────────────────────────────────┘
                   │ MCP / Skills
┌──────────────────▼──────────────────────────────────────────┐
│  Tier 3: 외부 시스템 (Data Plane)                           │
│                                                              │
│  Notion (Deal Base Master)                                  │
│    Companies DB · Market Segments DB                        │
│    Vendor Reference DB · Portfolio DB                       │
│                                                              │
│  데이터 소스 MCP                                            │
│    OpenDART · Naver Search · Gmail · Calendar · Drive       │
└─────────────────────────────────────────────────────────────┘
```

### 설계 원칙

1. **Paperclip = workflow engine, Notion = data store** — Issue 본문에는 Notion 페이지 링크만, 데이터 중복 없음
2. **Codex 협업은 adapter 차원** — 동일 직책에 Claude 1명 + Codex 1명, 협업 패턴은 AGENTS.md instructions에 인코딩
3. **외부 skill은 referenced, 한국/도메인 특화 skill은 vendored** — 마켓플레이스 skill은 `usage: referenced`, 내부 custom skill은 패키지에 포함

---

## 3. 조직도 및 에이전트 라인업

### 조직도

```
                       BOARD (사용자)
                            │
                            ▼
                   ┌────────────────┐
                   │  CEO (Claude)  │
                   └────────┬───────┘
                            │
       ┌───────────┬────────┼──────────────┬──────────────────┐
       ▼           ▼        ▼              ▼                  ▼
   Market     Deal       Research      Outreach          Deal Execution
   Analyst    Sourcer    Analyst       Manager           & PMI Lead
   ┌─┴─┐      ┌─┴─┐      ┌─┴─┐         ┌─┴─┐             ┌─┴─┐
 Claude Codex Claude Codex Claude Codex Claude Codex   Claude Codex
 [A: Peer]   [C: Split]   [A: Peer]    [B: Para+Synth]  [A: Peer]
```

총 11명. CEO 단독(Claude), 5 역할 각각 Claude + Codex 짝.

### 역할 정의

#### CEO (`ceo`, claude_local, claude-opus-4-7)
- **역할**: 전략 수립, 파이프라인 우선순위, board(사용자)와 인터페이스, 승인 게이트 관리
- **입력**: 사용자 지시·승인 결과, specialist 보고
- **출력**: 다음 단계 이슈 발급, 사용자 승인 요청, 일/주/월 다이제스트
- **트리거**: 일일 스케줄 / 사용자 지시 / approval resolution / specialist 보고 코멘트

#### Market Analyst pair (Peer Review — Pattern A)
- **역할**: 보안 sub-segment 매력도 분석, 산업 보고서 정리, vendor landscape mapping
- **단계**: 1 (Market Selection)
- **협업**: Claude 초안 작성 → Codex 리뷰·검토 → 합의 → CEO 보고
- **Skills**: `security-vendor-db`, `ko-security-market-research`, `notion-deal-sync`, `market-segment-analysis`, `competitive-intelligence`
- **MCP**: Naver Search, Drive, Notion

#### Deal Sourcer pair (Specialized Split — Pattern C)
- **역할**: 후보 발굴, 1차 스크리닝, Notion Companies DB 구축
- **단계**: 2~3
- **협업**: Codex — DART/Naver bulk fetching + Notion 입력 / Claude — 정성 스코어링 + 우선순위 (blockedBy Codex issue)
- **Skills**: `dart-company-profile`, `notion-deal-sync`, `security-vendor-db`
- **MCP**: OpenDART, Naver Search, Notion

#### Research Analyst pair (Peer Review — Pattern A)
- **역할**: 심층 리서치 (vendor 계약 안정성, 재무 다년치, 채널 mix, 핵심인력, 고객 집중도)
- **단계**: 4
- **협업**: Claude 초안 → Codex 리뷰 → 합의 → CEO 보고
- **Skills**: `dart-company-profile`, `ko-security-market-research`, `notion-deal-sync`, `competitive-intelligence`
- **MCP**: OpenDART, Naver Search, Notion, Drive

#### Outreach Manager pair (Parallel + Synthesis — Pattern B)
- **역할**: 컨택 전략, 메시지 초안, 미팅 자료 준비, 컨택 이력 관리
- **단계**: 5
- **협업**: Claude · Codex 각각 독립적으로 메시지·앵글 옵션 작성 → Claude(또는 CEO)가 합성·선택 → 사용자 검토
- **Skills**: `outreach-ko-owner`, `notion-deal-sync`, `cold-outreach`
- **MCP**: Gmail, Calendar, Naver Search, Notion

#### Deal Execution & PMI Lead pair (Peer Review — Pattern A)
- **역할**: DD 외부 위탁 코디네이션, 밸류에이션·협상 자료, 클로징 절차, PMI 통합 운영
- **단계**: 6~9
- **협업**: Claude 초안 → Codex 리뷰 → 합의 → CEO 보고
- **Skills**: `valuation-sme-ko`, `pmi-playbook-security-distributor`, `notion-deal-sync`, `valuation-fundamentals`, `dd-coordination`
- **MCP**: Gmail, Calendar, Drive, Notion

### Paperclip Collaboration 인코딩

| Pattern | Paperclip 구현 |
|---|---|
| A (Peer Review) | Issue assignee=Claude, 완료 시 `in_review` 전환 + Codex @멘션. Codex 리뷰 후 `done`. |
| B (Parallel+Synth) | 동일 후보에 Issue 2개 (각각 assignee). 완료 후 CEO synthesis Issue 생성. |
| C (Split) | Issue A: assignee=Codex (데이터 수집). Issue B: assignee=Claude (스코어링), `addBlockedBy: [A]`. |

---

## 4. 워크플로 (9단계 파이프라인)

### 전체 흐름

```
[1] Market Selection       Market Analyst pair (A)
         │ sub-segment 3-5개 선정 → Notion Market Segments DB
         ▼
[2] Sourcing               Deal Sourcer pair (C)
         │ segment별 후보 리스트업 → Notion Companies DB (candidate)
         ▼
[3] Pre-screening          Deal Sourcer pair (C 계속)
         │ 1차 필터 → status: screened
         ▼ ─── [GATE 1: 심층 리서치 진입 후보 선정]
[4] Deep Research          Research Analyst pair (A)
         │ 재무·vendor·채널·핵심인력 → status: researched
         ▼ ─── [GATE 2: 컨택 후보 선정]
[5] Outreach               Outreach Manager pair (B)
         │ 컨택·미팅 → status: contacted → meeting → engaged
         ▼ ─── [GATE 3: DD 발주 결정 (외부 비용)]
[6] Due Diligence          Deal Execution pair (A) — 외부 회계·법무 코디
         │ DD 보고서 수령·정리 → status: dd_complete
         ▼ ─── [GATE 4: 오퍼 제출 결정]
[7] Valuation/Negotiation  Deal Execution pair (A 계속)
         │ 밸류에이션·LOI → status: negotiating → loi_signed
         ▼ ─── [GATE 5: 클로징 최종 승인]
[8] Closing                Deal Execution pair (A 계속)
         │ SPA·자금·인수 → status: closed → Portfolio DB 이관
         ▼
[9] PMI                    Deal Execution pair (A 계속, recurring monthly)
           KPI 트래킹·운영 통합 → Portfolio DB
```

### CEO 일상 루틴

| 루틴 | 주기 | 내용 |
|---|---|---|
| Daily Digest | 평일 09:00 KST | 파이프라인 현황, 어제 진행, 오늘 우선순위 |
| Weekly Gate Review | 월요일 08:00 KST | 승인 게이트 대기 항목 일괄 처리 |
| Monthly PMI Report | 매월 1일 09:00 KST | 포트폴리오 KPI·운영 현황 |

### 자동 Pass 조건 (CEO 자율, 사용자 승인 불필요)

- Priority Score < 4 (1차 스크리닝)
- DD에서 딜 브레이커 발견 (vendor 계약 비이전, 부외부채 중대 건)
- 단, 자동 Pass 시 CEO가 이유 코멘트 기록 + 사용자 보고

---

## 5. 승인 게이트 (5개)

Paperclip board approval 기능으로 구현. CEO가 approval issue 생성 → 사용자 Paperclip UI에서 승인/거부 → 승인 시 CEO가 다음 단계 issue 자동 발급.

| Gate | 발동 조건 | 사용자 결정 사항 | 승인 후 액션 |
|---|---|---|---|
| **G1** | 후보 N개 screened | 심층 리서치 진입할 M개 선정 | Research Analyst에게 M개 issue 발급 |
| **G2** | M개 리서치 완료 | 컨택할 X개 / 보류 Y개 / Pass Z개 | Outreach Manager에게 X개 issue 발급 |
| **G3** | 미팅 완료, 매각 의향 긍정 | DD 발주 yes/no (외부 비용 수반) | DD 발주 issue 발급 + 외부 업체 컨택 |
| **G4** | DD 보고서 수령·요약 완료 | 오퍼 제출 yes/no + 가격 range 승인 | 밸류에이션·LOI issue 발급 |
| **G5** | SPA 초안 검토 완료 | 클로징 최종 승인 | 클로징 issue 발급, 완료 시 Portfolio DB 이관 |

---

## 6. Skills 인벤토리

### Custom Skills (vendored, 패키지 내부)

| Shortname | 용도 | 주요 사용 에이전트 |
|---|---|---|
| `dart-company-profile` | OpenDART 5개 API 순차 호출 → 구조화 프로필 | Deal Sourcer Codex, Research Analyst |
| `notion-deal-sync` | Notion MCP 추상화 — 3개 DB CRUD | 모든 specialist |
| `security-vendor-db` | 한국 IT 보안 vendor 참조 데이터 (외산·국산·segment) | Market Analyst, Deal Sourcer Claude |
| `ko-security-market-research` | Naver Search 보안 시장 특화 쿼리 패턴 + KISA/IDC 자료 | Market Analyst, Research Analyst |
| `outreach-ko-owner` | 한국 SMB 오너 cold outreach 문화·메시지 프레임 + 템플릿 | Outreach Manager |
| `valuation-sme-ko` | 한국 IT 보안 총판 SMB 밸류에이션 (EBITDA multiple, 리스크 조정) | Deal Execution |
| `pmi-playbook-security-distributor` | IT 보안 총판 인수 후 100일 플랜 + KPI 체크리스트 | Deal Execution |

### Referenced Skills (마켓플레이스)

`usage: referenced`, commit SHA는 import 시 `git ls-remote`로 확정.

| Shortname | 용도 |
|---|---|
| `paperclip` | Paperclip 에이전트 heartbeat 프로토콜 기본 동작 |
| `market-segment-analysis` | 산업 sub-segment 매력도 분석 프레임워크 |
| `competitive-intelligence` | 경쟁사·시장 플레이어 정보 수집·정리 |
| `cold-outreach` | 비즈니스 cold contact 메시지 작성·전략 |
| `valuation-fundamentals` | DCF·multiples·comparable 기업 밸류에이션 기초 |
| `dd-coordination` | 외부 DD 업체 발주·관리·결과 정리 |

### MCP 사용 권한

| MCP | 사용 에이전트 |
|---|---|
| OpenDART | Deal Sourcer Codex, Research Analyst |
| Naver Search | Market Analyst, Research Analyst, Outreach Manager |
| Notion | 모든 specialist (notion-deal-sync 통해) |
| Gmail | Outreach Manager, Deal Execution, CEO |
| Google Calendar | Outreach Manager, Deal Execution, CEO |
| Google Drive | Research Analyst, Deal Execution |

---

## 7. Notion Deal Base 스키마

### Companies DB (메인 파이프라인)

**Status 14단계**: `candidate → screened → researching → researched → outreach → contacted → meeting → engaged → dd → negotiating → loi_signed → closing → closed → [pass / dead]`

**주요 필드 그룹**:

| 그룹 | 주요 필드 |
|---|---|
| 기본 | Company Name, Status, Segment (→Market Segments), Priority Score (0-10), DART Corp Code |
| 재무 (DART) | Revenue, EBITDA, EBITDA Margin %, Revenue YoY Growth %, Net Debt (단위: 억KRW) |
| 사업 특성 | Vendor Lines (multi-select), Vendor Count, Vendor Dependency Risk, Key Person Risk, Customer Concentration, Contract Type |
| 컨택·딜 | Owner Name, Last Contact Date, Outreach Channel, DD Provider, DD Period, Valuation Low/High, LOI Date, Acquisition Price, Closing Date |
| 메타 | Paperclip Issue URL, Research Page (relation), Stage Entered Date, Pass Reason |

### Market Segments DB

Segment Name, Attractiveness Score, KR Market Size, Key Foreign Vendors, Estimated 총판 Count, Revenue Growth YoY %, Regulatory Tailwind, Priority, Analysis Date

### Vendor Reference DB (static)

Vendor Name, Category (Foreign/Domestic), Product Lines, Partner Tier System, 한국 총판 자격 조건, 주요 경쟁 vendor

### Portfolio DB (PMI 이후)

Company Name, Acquisition Date/Price, Monthly Revenue, EBITDA %, Vendor Lines, Integration Status, 100-Day Plan Status, Key Risks, Monthly Report Link, KPI Last Updated

---

## 8. 패키지 파일 레이아웃

```
ko-security-ma/
│
├── COMPANY.md
├── README.md
├── LICENSE                              (MIT)
├── .paperclip.yaml
│
├── agents/
│   ├── ceo/AGENTS.md
│   ├── market-analyst-claude/AGENTS.md
│   ├── market-analyst-codex/AGENTS.md
│   ├── deal-sourcer-claude/AGENTS.md
│   ├── deal-sourcer-codex/AGENTS.md
│   ├── research-analyst-claude/AGENTS.md
│   ├── research-analyst-codex/AGENTS.md
│   ├── outreach-manager-claude/AGENTS.md
│   ├── outreach-manager-codex/AGENTS.md
│   ├── deal-execution-claude/AGENTS.md
│   └── deal-execution-codex/AGENTS.md
│
├── teams/
│   ├── market-intelligence/TEAM.md
│   ├── deal-sourcing/TEAM.md
│   ├── research/TEAM.md
│   ├── outreach/TEAM.md
│   └── deal-execution/TEAM.md
│
├── projects/
│   ├── deal-pipeline/
│   │   ├── PROJECT.md
│   │   └── tasks/
│   │       ├── ceo-daily-digest/TASK.md         (recurring, 평일 09:00 KST)
│   │       ├── ceo-weekly-gate-review/TASK.md   (recurring, 월요일 08:00 KST)
│   │       └── ceo-monthly-pmi-report/TASK.md   (recurring, 매월 1일 09:00 KST)
│   └── market-research-kickoff/
│       ├── PROJECT.md
│       └── tasks/
│           └── initial-segment-analysis/TASK.md
│
└── skills/
    ├── dart-company-profile/SKILL.md
    ├── notion-deal-sync/SKILL.md
    ├── security-vendor-db/
    │   ├── SKILL.md
    │   └── references/vendor-list.md
    ├── ko-security-market-research/SKILL.md
    ├── outreach-ko-owner/
    │   ├── SKILL.md
    │   └── references/templates.md
    ├── valuation-sme-ko/SKILL.md
    ├── pmi-playbook-security-distributor/
    │   ├── SKILL.md
    │   └── references/checklist.md
    ├── paperclip/SKILL.md              (referenced)
    ├── market-segment-analysis/SKILL.md (referenced)
    ├── competitive-intelligence/SKILL.md (referenced)
    ├── cold-outreach/SKILL.md           (referenced)
    ├── valuation-fundamentals/SKILL.md  (referenced)
    └── dd-coordination/SKILL.md         (referenced)
```

### .paperclip.yaml 핵심 구조

```yaml
schema: paperclip/v1
agents:
  ceo:
    adapter: { type: claude_local, config: { model: claude-opus-4-7 } }
    inputs:
      env:
        ANTHROPIC_API_KEY: { kind: secret, requirement: required }

  market-analyst-claude:
    adapter: { type: claude_local, config: { model: claude-sonnet-4-6 } }
    inputs:
      env:
        ANTHROPIC_API_KEY: { kind: secret, requirement: required }

  market-analyst-codex:
    adapter: { type: codex_local }
    inputs:
      env:
        OPENAI_API_KEY: { kind: secret, requirement: required }

  # deal-sourcer, research-analyst, outreach-manager, deal-execution:
  # 동일 패턴 (claude_local / codex_local)

routines:
  ceo-daily-digest:
    triggers:
      - kind: schedule
        cronExpression: "0 9 * * 1-5"
        timezone: Asia/Seoul
  ceo-weekly-gate-review:
    triggers:
      - kind: schedule
        cronExpression: "0 8 * * 1"
        timezone: Asia/Seoul
  ceo-monthly-pmi-report:
    triggers:
      - kind: schedule
        cronExpression: "0 9 1 * *"
        timezone: Asia/Seoul
```

---

## 9. Codex 협업 분담 (구현 단계)

설계 문서 및 핵심 아키텍처: **Claude** 담당  
병렬 실행 가능한 파일 드래프팅: **Codex** 담당

| 작업 | 담당 |
|---|---|
| COMPANY.md, README.md, LICENSE | Claude |
| .paperclip.yaml 전체 | Claude |
| CEO AGENTS.md | Claude |
| 5개 Claude specialist AGENTS.md | Claude |
| 5개 Codex specialist AGENTS.md | **Codex** (병렬) |
| 5개 TEAM.md | **Codex** (병렬) |
| 7개 Custom SKILL.md | **Codex** (병렬, Claude 리뷰) |
| 6개 Referenced SKILL.md (shell 파일) | **Codex** (병렬) |
| PROJECT.md × 2, TASK.md × 4 | **Codex** (병렬) |
| 구현 계획 (writing-plans) | Claude |

---

## 10. 미결 사항 (구현 전 확정 필요)

1. **Referenced skill 마켓플레이스 SHA 확정** — agentcompanies.io / skills.sh에서 `market-segment-analysis`, `competitive-intelligence`, `cold-outreach`, `valuation-fundamentals`, `dd-coordination` 실제 repo + commit SHA 검색 필요. 없으면 custom으로 전환.
2. **Notion Workspace ID / DB ID** — `notion-deal-sync` skill 구현 시 필요. 사용자가 Notion에서 직접 확인 후 env var로 제공.
3. **Google OAuth scope** — Gmail·Calendar·Drive MCP 사용 시 필요. 사용자 인증 필요.
4. **예산 한도** — `.paperclip.yaml` 에이전트별 월 토큰 예산 (cents). 사용자 결정.
5. **1차 실행 segment** — `market-research-kickoff` 프로젝트의 초기 분석 대상 segment 우선순위 (사용자 지정 또는 CEO 자율).
