# AI Red Team / Guardrail DD Checklist

기준 시점: 2026-05-14

이 체크리스트는 AI 보안 관련 타깃 회사를 평가하거나, 내부 에이전트 운영 통제를 설계할 때 사용합니다.

## 공개 참고 자료

- AIM Intelligence 공식 소개: https://www.aim-intelligence.com/about
- AIM Intelligence 공식 플랫폼: https://www.aim-intelligence.com/
- AIM Intelligence 공식 Agentic AI Security: https://www.aim-intelligence.com/agentic
- AIM Intelligence 공식 Press: https://www.aim-intelligence.com/press
- AIM Intelligence Series A 보도(2026-04-10): https://www.datanet.co.kr/news/articleViewAmp.html?idxno=210849

위 자료를 기준으로, 현재 시장에서 의미 있는 AI 보안 역량은 단순 텍스트 moderation이 아니라 아래로 확장되고 있다고 본다:
- 자동화 레드팀
- 실시간 guardrails
- agent tool-call 통제
- 멀티모달 입력/출력 통제
- on-prem / enterprise governance

## 1. 제품/기술 DD

### A. Red Teaming
- 자동화 공격 시나리오 생성이 가능한가
- prompt-level만이 아니라 end-to-end workflow를 점검하는가
- agentic workflow, tool-calling, API chaining을 다루는가
- 텍스트 외 이미지/오디오/파일 입력을 다루는가
- 결과 리포트가 재현 가능하고 고객이 remediation에 사용할 수 있는가

### B. Guardrails
- 실시간 입력/출력 차단이 가능한가
- 민감정보 masking / redaction이 가능한가
- 정책 기반 제어(policy-aware)가 가능한가
- 고객사별 custom policy 구성이 가능한가
- latency overhead가 운영 가능한 수준인가

### C. Agent Security
- tool call interception이 가능한가
- function argument, API parameter validation이 가능한가
- privilege escalation, goal hijacking, indirect prompt injection 방어 논리가 있는가
- coding agent, browser agent, DB agent, MCP-style toolchain을 지원하는가

## 2. 배포/운영 DD

- cloud SaaS만 가능한가, on-prem도 가능한가
- regulated environment(금융, 공공, 제조)에 배포 가능한가
- 운영 로그, 탐지 이력, 정책 변경 이력, 승인 이력이 남는가
- 고객이 false positive / false negative를 튜닝할 수 있는가
- purple teaming 또는 지속 개선 루프가 존재하는가

## 3. 상업 DD

- 제품회사인지, 구축회사인지, 운영회사인지 명확한가
- ARR / subscription / managed service 매출이 존재하는가
- 컨설팅 일회성 매출 비중이 과도하지 않은가
- 특정 모델사/클라우드사 의존도가 과도하지 않은가
- 고객군이 금융/공공/엔터프라이즈로 확장 가능한가

## 4. 인수 적합성 판단

### 직접 인수 적합
- 채널/운영 인수인계가 가능
- 핵심기술이 오너 개인 의존만으로 굴러가지 않음
- 반복 매출과 고객 운영 체계가 존재

### 파트너십 적합
- 기술력은 강하나 고성장 VC형 제품회사
- 경영권 인수보다 총판/리셀러/공동제안 구조가 유리

## 5. 내부 Paperclip 운영 통제 체크

- 외부 이메일 발송은 board approval 또는 role-based approval 필요
- 코드 실행과 브라우징, DB 접근을 role 별로 분리
- 툴 호출 전 parameter inspection 필요
- 민감정보가 prompt/context에 들어갈 때 redaction 필요
- agent action은 immutable log로 남겨야 함
- 고위험 action은 auto-pass 금지, human gate 필수
