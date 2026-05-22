# 초기 타깃 세그먼트 제안

기준 시점: 2026-05-14

이 문서는 `ko-security-ma` 템플릿의 **초기 딜 소싱 우선순위**를 정리한 운영용 메모입니다.
최종 목적은 “한국 IT 보안 솔루션 + 총판/리셀러 + 운영형 보안회사” 중
**인수 가능성**, **반복매출**, **vendor 이전 가능성**, **직접 운영 가능성**이 높은 영역부터
파이프라인을 여는 것입니다.

## 근거가 된 외부 공개 자료

1. **국내 정보보호 산업 성장**
   - `2025년 국내 정보보호산업 실태조사`는 2024년 기준 국내 정보보안 기업이 876개, 정보보안 매출이 7조 1,244억 원으로 전년 대비 15.9% 증가했다고 제시합니다.
   - 출처: KISIA `2025년 국내 정보보호산업 실태조사 보고서`
   - 링크: https://www.kisia.or.kr/bucket/uploads/2025/11/11/2025%EB%85%84%20%EA%B5%AD%EB%82%B4%20%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%82%B0%EC%97%85%20%EC%8B%A4%ED%83%9C%EC%A1%B0%EC%82%AC%20%EB%B3%B4%EA%B3%A0%EC%84%9C.pdf

2. **제로트러스트 정책 가속**
   - 과기정통부는 2024-12-03에 `제로트러스트 가이드라인 2.0`을 발표했습니다.
   - KISA는 2025-03-06에 민간 실제 시스템 대상 `2025년 제로트러스트 도입 시범사업`을 공고했고, 핵심 요소로 인증 체계 강화, 마이크로 세그멘테이션, SDP를 명시했습니다.
   - 출처: 과기정통부, KISA
   - 링크:
     - https://www.msit.go.kr/bbs/view.do?bbsSeqNo=94&mId=113&mPid=238&nttSeqNo=3185203&sCode=user
     - https://www.kisa.or.kr/403/form?page=1&postSeq=10022

3. **클라우드 인증 운영 변화**
   - KISA는 2025-02-06에 SaaS 인증서비스 사후관리 방식을 변경하며 서면평가 도입과 운영명세서 일원화를 안내했습니다.
   - 이는 클라우드 보안/운영 체계 대응 수요가 계속 제도화되고 있음을 보여줍니다.
   - 출처: KISA 클라우드 보안인증제 자료실
   - 링크: https://isms.kisa.or.kr/main/csap/notice/?boardId=bbs_0000000000000004&cntId=95&mode=view

4. **OT 보안 제도 신호**
   - KISA는 2025-12-22에 `운영 기술(OT) 환경의 제로트러스트 적용 안내서`를 발표했습니다.
   - OT는 정책 신호가 강하지만, 초기 인수 타깃으로는 운영 복잡도가 높습니다.
   - 출처: KISA 보도자료
   - 링크: https://www.kisa.or.kr/402/form?lang_type=KO&page=2&postSeq=2566

## 초기 우선순위 Top 3

### 1. ZTNA / SASE

- **우선순위:** 최우선
- **이유:** 제로트러스트 정책과 직결되고, 총판/리셀러 모델이 명확하며, 라이선스·유지보수·구독형 매출 구조가 잘 맞습니다.
- **선호 delivery model:** 총판, 솔루션 리셀러
- **선호 vendor 예시:** Zscaler, Netskope, Palo Alto Prisma Access, Cisco Umbrella
- **찾고 싶은 회사 타입:**
  - 공식 파트너 레벨을 보유한 채널사
  - 공공/금융/엔터프라이즈 레퍼런스가 있는 리셀러
  - 구축 매출보다 라이선스/운영/유지보수 비중이 높은 업체
- **빨간 깃발:**
  - 특정 SI 프로젝트 의존
  - 네트워크 장비 납품만 있고 보안 운영/갱신 매출이 약함
  - vendor consent 구조가 불명확

### 2. IAM / PAM

- **우선순위:** 높음
- **이유:** 제로트러스트의 인증 체계 강화와 직접 연결됩니다. 계정/권한 관리 제품은 고객 락인이 강하고 갱신 매출을 만들기 쉽습니다.
- **선호 delivery model:** 솔루션 리셀러, 전문 파트너
- **선호 vendor 예시:** CyberArk, BeyondTrust, Cisco Duo, Okta, Ping Identity
- **찾고 싶은 회사 타입:**
  - 금융/공공 인증 프로젝트 경험이 있는 파트너
  - 인증·권한·접근통제 중심의 반복 유지보수 매출이 존재하는 업체
  - 핵심 엔지니어가 있더라도 문서화와 운영 프로세스가 남아 있는 업체
- **빨간 깃발:**
  - 프로젝트 종료 후 매출이 끊기는 구조
  - 오너 개인 영업 네트워크 의존이 지나침
  - 고객 상위 3곳 집중도가 과도함

### 3. 클라우드 보안 (CNAPP / CSPM / CWPP)

- **우선순위:** 높음
- **이유:** 클라우드 보안인증과 SaaS 운영 체계가 계속 제도화되고 있고, 구독형 매출과 운영형 서비스 결합이 가능합니다.
- **주의:** 이 우선순위는 CSAP/SaaS 운영 제도 변화에서 **추론한 것**입니다. ZTNA/IAM처럼 직접적인 정책 키워드보다 해석 여지가 있습니다.
- **선호 delivery model:** 솔루션 리셀러, MSSP-light
- **선호 vendor 예시:** Wiz, Prisma Cloud, Lacework, Orca Security, Qualys
- **찾고 싶은 회사 타입:**
  - 멀티클라우드 보안 점검/운영을 반복 과금으로 제공하는 회사
  - CSPM/CNAPP 제품 판매 후 운영 서비스까지 붙이는 파트너
  - CSAP 대응 경험 또는 공공 클라우드 고객 기반이 있는 업체
- **빨간 깃발:**
  - 단순 컨설팅형 매출 비중이 너무 높음
  - 특정 대형 고객 1~2곳에 의존
  - 실제 운영 인계 없이 프리세일즈/구축 중심

## High-Priority Watchlist

### AI Security / Agent Security / Guardrails

- **현재 판단:** 전략적 추적 필수, 직접 인수는 보수적
- **이유:** 에임인텔리전스 같은 플레이어가 보여주듯 시장은 단순 moderation을 넘어 자동화 레드팀, 실시간 가드레일, agent tool-call 통제로 빠르게 이동 중입니다.
- **공개 근거:**
  - AIM Intelligence는 공식 사이트에서 `Stinger` 자동화 레드팀과 `Starfort` 실시간 가드레일, `Agentic AI Security`를 공개합니다.
  - 2026-04-10 Series A 100억 원 조달 보도는 시장 관심과 성장 기대를 보여줍니다.
- **실무 해석:** 이 세그먼트는 유망하지만, 현 시점에는 VC형 제품회사가 많아 `직접 경영권 인수`보다 `채널/리셀러/MSSP-light 역량 확보`가 더 현실적입니다.
- **선호 delivery model:** AI Security Channel Partner, AI Security MSSP-light, General Security Company with AI Practice
- **찾고 싶은 회사 타입:**
  - LLM/에이전트 보안 제품의 총판·리셀러
  - AI 레드팀, 가드레일 정책 설계, 운영 모니터링을 반복 과금으로 제공하는 회사
  - 금융/통신/공공 고객의 생성형 AI 보안 운영 경험이 있는 회사
- **빨간 깃발:**
  - 데모/PoC만 있고 운영 고객이 없음
  - 실질적 통제 없이 프롬프트 템플릿 판매에 가까움
  - 특정 모델사 마케팅 종속이고 기술 독립성이 약함

## Watchlist

### OT / ICS 보안

- **현재 판단:** 리서치 우선, 소싱은 보수적으로
- **이유:** 정책 신호는 강하지만 운영 복잡도, 산업별 인증·현장 의존성, 고객군 특수성이 높습니다.
- **권장 접근:** 초기 포트폴리오 플랫폼을 먼저 확보한 뒤 bolt-on 대상으로 검토

## 제외 우선순위

초기 1차 파이프라인에서는 아래를 우선 제외합니다.

- 순수 SI 구축형 보안업체
- 상주 인력형 관제 아웃소싱 업체
- 하드웨어 박스 납품 비중만 높고 갱신 매출이 약한 업체
- vendor 공식 파트너 지위 이전 가능성이 불명확한 업체

## 세그먼트별 후보 발굴 쿼리 세트

### ZTNA / SASE

```text
"ZTNA 한국 총판"
"SASE 한국 총판"
"Zscaler 한국 파트너"
"Netskope 한국 파트너"
"Palo Alto Prisma Access 파트너"
"Cisco Umbrella 파트너" 한국
"제로트러스트 구축 파트너" 보안
"소프트웨어 정의 경계" 파트너 한국
```

### IAM / PAM

```text
"IAM 한국 총판"
"PAM 한국 총판"
"CyberArk 한국 파트너"
"BeyondTrust 한국 파트너"
"Duo 파트너" 한국
"Okta 파트너" 한국 보안
"권한관리 솔루션 파트너" 한국
"접근통제 솔루션 총판" 보안
```

### 클라우드 보안

```text
"클라우드 보안 한국 총판"
"CNAPP 한국 파트너"
"CSPM 한국 파트너"
"CWPP 한국 파트너"
"Wiz 한국 파트너"
"Prisma Cloud 한국 파트너"
"Lacework 한국 파트너"
"클라우드 보안 운영 서비스" 한국
```

### 공통 정밀 필터 쿼리

```text
"{회사명}" 대표
"{회사명}" 유지보수
"{회사명}" 구독
"{회사명}" 파트너
"{회사명}" 총판
"{회사명}" 리셀러
"{회사명}" 나라장터
"{회사명}" 수상
"{회사명}" 사고 OR 소송 OR 해킹 OR 개인정보
```

### AI Security / Agent Security / Guardrails

```text
"AI 보안 스타트업" 한국
"LLM 보안" 한국 기업
"AI 레드팀" 한국
"AI 가드레일" 한국
"에이전트 보안" 한국
"prompt injection 방어" 한국
"tool call security" 한국 기업
"AI 보안 파트너" 한국
```

## 즉시 실행 순서

1. Market Analyst가 9개 세그먼트를 모두 평가하되, 먼저 Top 3를 상세 점수화
2. Deal Sourcer Codex가 Top 3 세그먼트별로 후보 15개씩 1차 수집
3. Deal Sourcer Claude가 `총판 / 리셀러 / MSSP-light / SI-heavy` 분류
4. CEO가 G1 이전에 `ZTNA/SASE 5개`, `IAM/PAM 5개`, `클라우드 보안 5개` short list를 확인
5. AI Security / Agent Security / Guardrails는 direct acquisition보다 partner/channel 후보를 별도 트래킹
