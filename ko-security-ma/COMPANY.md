---
name: 한국 IT 보안 솔루션 · 총판 M&A
slug: ko-security-ma
schema: agentcompanies/v1
version: 1.0.0
license: MIT
description: >
  한국 IT 보안 솔루션 기업 및 총판/리셀러 경영권 인수 전문 회사.
  시장 선정부터 발굴·리서치·컨택·실사·협상·클로징·PMI까지
  풀 라이프사이클을 13명의 AI 에이전트 워크포스(Claude + Codex 짝)로 운영.
goals:
  - 한국 IT 보안 솔루션/총판 경영권 인수를 통한 포트폴리오 구축 (딜 사이즈 100억 KRW 미만)
  - 인수 후 직접 운영 및 bolt-on M&A로 반복 매출과 EBITDA 성장
requirements:
  secrets:
    - ANTHROPIC_API_KEY
    - OPENAI_API_KEY
    - NOTION_TOKEN
    - GOOGLE_OAUTH_TOKEN
---

한국 IT 보안 솔루션 · 총판 M&A는 보안 솔루션 기업, 총판, 리셀러, 채널 기반 운영형 보안회사, AI 보안 전문회사의 경영권 인수를 전문으로 하는 AI 에이전트 회사입니다.

SI(System Integration) 방식이 아닌 vendor 계약권·채널·고객 베이스·반복 매출을 자산으로 보유한 회사를 타겟으로 합니다. 총판형 업체뿐 아니라 유지보수·구독·운영 매출을 가진 솔루션 파트너도 포함합니다. 딜 사이즈 100억 KRW 미만, 경영권 인수 후 직접 운영.

CEO가 총괄하고, 6개 전문 역할(시장분석·딜소싱·리서치·아웃리치·딜실행·PMI·AI보안)에 각각 Claude + Codex 직원이 짝을 이뤄 협업합니다. 딜 데이터는 Notion에 저장되고, Paperclip이 작업 큐를 관리합니다.

투자 필터는 다음과 같습니다:
- vendor 파트너/총판 권한의 이전 가능성
- 라이선스/유지보수/구독/운영의 반복 매출 비중
- 고객·vendor 집중도와 핵심인력 의존도
- 오너 승계 가능성 및 인수 후 운영 인수인계 난이도
- 순수 SI/프로젝트 구축 매출 비중
- AI 에이전트/LLM 서비스의 입력·출력·툴콜·데이터 경계 통제 가능성
