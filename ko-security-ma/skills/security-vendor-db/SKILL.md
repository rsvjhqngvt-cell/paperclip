---
name: security-vendor-db
description: 한국 IT 보안 시장 vendor 참조 데이터 — 외산/국산 vendor, segment 분류, 총판 패턴
---

한국 IT 보안 시장의 주요 vendor 목록과 총판 구조에 대한 참조 데이터입니다.
자세한 데이터는 `references/vendor-list.md`를 참조하세요.

## 사용 방법

1. 분석 대상 기업의 vendor 라인업을 확인할 때 이 skill을 참조
2. Vendor tier 등급으로 총판 계약 가치 추정
3. SI vs 총판 판별 시 vendor 계약 보유 여부 확인

## Vendor Tier 기준

- **Tier 1**: 글로벌 TOP 10 보안 vendor (PAN, CrowdStrike, Fortinet, Cisco, CheckPoint, SentinelOne, Trellix, Palo Alto Networks 계열)
- **Tier 2**: 중견 글로벌 vendor (Darktrace, Rapid7, Tenable, Qualys, Varonis, Proofpoint 등)
- **Tier 3**: 국내/소규모 vendor

## 총판 vs SI 판별 기준

총판 특성 (인수 적합):
- 특정 vendor와 공식 파트너/총판 계약 보유
- 제품(라이선스) 매출 비중 > 50%
- 유지보수(MRC) 수익 보유
- 채널(리셀러) 네트워크 운영

SI 특성 (인수 부적합):
- 매출의 50%+ 프로젝트성 구축 용역
- 인건비 비중 70%+
- 상주 인력 중심 수익 구조
