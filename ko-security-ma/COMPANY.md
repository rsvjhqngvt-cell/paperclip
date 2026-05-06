---
name: 한국 IT 보안 M&A
slug: ko-security-ma
schema: agentcompanies/v1
version: 1.0.0
license: MIT
description: >
  한국 IT 보안 총판(Distributor) 경영권 인수 전문 회사.
  시장 선정부터 발굴·리서치·컨택·실사·협상·클로징·PMI까지
  풀 라이프사이클을 11명의 AI 에이전트 워크포스(Claude + Codex 짝)로 운영.
goals:
  - 한국 IT 보안 총판 경영권 인수를 통한 포트폴리오 구축 (딜 사이즈 100억 KRW 미만)
  - 인수 후 안정적 직접 경영으로 EBITDA 성장
requirements:
  secrets:
    - ANTHROPIC_API_KEY
    - OPENAI_API_KEY
    - NOTION_TOKEN
    - GOOGLE_OAUTH_TOKEN
---

한국 IT 보안 M&A는 보안 솔루션 총판 업체 경영권 인수를 전문으로 하는 AI 에이전트 회사입니다.

SI(System Integration) 방식이 아닌 vendor 계약권·채널·고객 베이스를 자산으로 보유한 총판형 업체를 타겟으로 합니다. 딜 사이즈 100억 KRW 미만, 경영권 인수 후 직접 운영.

CEO가 총괄하고, 5개 전문 역할(시장분석·딜소싱·리서치·아웃리치·딜실행·PMI)에 각각 Claude + Codex 직원이 짝을 이뤄 협업합니다. 딜 데이터는 Notion에 저장되고, Paperclip이 작업 큐를 관리합니다.
