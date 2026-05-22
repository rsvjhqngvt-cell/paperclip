---
name: source-material-ingestion
description: 사용자가 제공한 원자료를 사실, 수치, 출처, 표/차트 후보, 전문용어로 구조화한다.
---

원자료는 바로 PPT에 붙여 넣지 않는다. 먼저 내용 패턴 레이어에서 사용할 수 있게 구조화한다.

## 처리 순서

1. 자료 유형과 출처 확인
2. 핵심 사실, 수치, 날짜, 인용 근거 추출
3. 장표화 가능한 표/차트 후보 분리
4. 전문용어와 약어 목록 작성
5. 누락 데이터와 확인 필요 항목 표시
6. 내용 패턴 라이브러리의 장표 유형에 매핑

## 산출물

- `source-data-map`
- `chart-table-inputs`
- `term-note-list`
- `data-gap-list`
