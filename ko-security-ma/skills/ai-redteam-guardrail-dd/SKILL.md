---
name: ai-redteam-guardrail-dd
description: AI 레드팀·가드레일·에이전트 보안 DD 체크리스트와 내부 운영 통제 프레임
---

AI 보안 제품회사, 채널 파트너, 운영형 서비스 회사를 평가할 때 사용하는 DD 체크리스트입니다.
특히 LLM, agentic AI, tool-calling workflow, internal copilots 환경을 기준으로 점검합니다.

상세 체크리스트는 `references/checklist.md`를 우선 참조하세요.

## 평가 목적

1. **인수 타깃 평가**
   - 이 회사가 AI 보안 제품/채널/운영 역량을 실제로 보유하는가
   - 반복 매출과 운영 이전 가능성이 있는가

2. **내부 통제 설계**
   - 우리가 운용하는 Paperclip 및 에이전트 워크플로우에 어떤 guardrail이 필요한가

## 빠른 분류 기준

### AI Security Product
- 자체 guardrail / red teaming / agent security 제품 존재
- 멀티모달 또는 tool-calling 리스크 대응 논리 보유
- 고객 적용 레퍼런스 또는 운영 증적 존재

### AI Security Channel Partner
- 외부 AI 보안 제품의 리셀러/구축/운영 파트너
- 제품 판매 후 정책 설계·운영·튜닝 역량 보유

### AI Security MSSP-light
- 반복 과금형 AI 모니터링/운영 서비스
- 단순 인력 투입보다 정책·플랫폼·운영 자동화 비중 높음

## 핵심 DD 질문

- prompt injection, indirect prompt injection, jailbreak에 대한 대응은 무엇인가
- tool call, function call, API invocation에 대한 authorization이 가능한가
- PII, trade secret, source code 유출 방지 기능이 있는가
- 모델 종속적 기능인지, model-agnostic인지
- latency overhead와 production deploy 방식은 어떠한가
- cloud, on-prem, isolated 환경 지원이 가능한가
- 로그, 감사, 정책 버전 관리가 가능한가
- purple teaming 또는 지속 학습/튜닝 루프가 있는가
