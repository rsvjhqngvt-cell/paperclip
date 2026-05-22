---
name: ko-security-market-research
description: 한국 IT 보안 시장 조사에 최적화된 Naver Search 쿼리 패턴 및 정보 소스
allowed-tools:
  - mcp__claude_ai_PlayMCP__NaverSearch-search_news
  - mcp__claude_ai_PlayMCP__NaverSearch-search_blog
  - mcp__claude_ai_PlayMCP__NaverSearch-search_webkr
  - mcp__claude_ai_PlayMCP__NaverSearch-search_academic
---

한국 IT 보안 시장 리서치를 위한 검색 전략과 정보 소스 가이드입니다.

초기 타깃 세그먼트와 세부 쿼리 팩은 `references/initial-target-segments.md`를 우선 참조하세요.

## 시장 규모/트렌드 검색

```
"한국 정보보안 시장" site:kisa.or.kr
"보안 산업 실태조사" {현재 연도}
"IT 보안 시장 규모" "억원" {현재 연도}
"사이버 보안 투자" "국내" {현재 연도}
```

## Segment별 총판 발굴 검색

```
"{vendor명} 한국 총판"
"{vendor명} 공식 파트너"
"{segment} 솔루션 유통사"
"{vendor명} 리셀러"
"{segment} 보안 솔루션 공급사"
```

예시:
- "CrowdStrike 한국 총판"
- "EDR 솔루션 유통"
- "ZTNA 공식 파트너"
- "Darktrace 파트너사"

## 우선순위 세그먼트별 쿼리 팩

### 1) ZTNA / SASE

```
"ZTNA 한국 총판"
"SASE 한국 총판"
"Zscaler 한국 파트너"
"Netskope 한국 파트너"
"Palo Alto Prisma Access 파트너"
"제로트러스트 구축 파트너" 보안
```

### 2) IAM / PAM

```
"PAM 한국 총판"
"IAM 한국 총판"
"CyberArk 한국 파트너"
"BeyondTrust 한국 파트너"
"Duo 파트너" 한국
"Okta 파트너" 한국 보안
```

### 3) 클라우드 보안 (CNAPP / CSPM / CWPP)

```
"클라우드 보안 한국 총판"
"CNAPP 한국 파트너"
"CSPM 한국 파트너"
"CWPP 한국 파트너"
"Wiz 한국 파트너"
"Prisma Cloud 한국 파트너"
"Lacework 한국 파트너"
```

### 4) AI Security / Agent Security / Guardrails

```
"AI 보안 스타트업" 한국
"LLM 보안" 한국 기업
"AI 레드팀" 한국
"AI 가드레일" 한국
"에이전트 보안" 한국
"prompt injection 방어" 한국 기업
"AI 보안 파트너" 한국
```

### Watchlist) OT / ICS 보안

```
"OT 보안 한국 총판"
"ICS 보안 한국 파트너"
"Claroty 한국 파트너"
"Nozomi 한국 파트너"
"Dragos 한국 파트너"
```

## 기업 평판/이슈 검색

```
"{기업명} 대표"
"{기업명} 수상"
"{기업명} 납품"
"{기업명}" 사고 OR 해킹 OR 소송 OR 개인정보
"{대표자명}" 업계 OR 협회 OR 인터뷰
```

## 업계 이벤트/네트워크 검색

```
"한국정보보호산업협회" KISIA
"보안엑스포" SECON
"ISC KOREA" {현재 연도}
"정보보안 컨퍼런스" {현재 연도}
```

## 입찰/공공사업 검색

```
"{기업명}" 나라장터 OR 입찰 OR 낙찰
"{솔루션명}" 공공 OR 정부 OR 지자체
```

## 주요 정보 소스

- **KISA 보안산업 실태조사**: 연간 시장 규모, 기업별 매출 (상위사)
- **IDC Korea 보안 시장 예측**: 유료 보고서 (요약은 뉴스에서 검색 가능)
- **보안뉴스 (boannews.com)**: 보안 전문 미디어, 기업 뉴스 풍부
- **데이터넷 (datanet.co.kr)**: 네트워크/보안 인프라 전문 미디어
- **CISO Summit / ISEC**: 업계 행사, 기업 참여 정보
