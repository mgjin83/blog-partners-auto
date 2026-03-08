# 스토리팀 가이드 (Story Guide)

## 읽어야 할 파일
- CLAUDE.md
- 이 파일 (story_guide.md)
- bible/series_bible.md
- bible/characters.md
- bible/timeline.md

## 작가 (Writer)

### 역할
에피소드 시놉시스를 씬별 대본으로 만든다.

### 작업 흐름
1. series_bible.md, characters.md, timeline.md를 읽는다
2. 핵심 정보를 working_context.md에 압축한다
3. 에피소드 대본을 작성한다
4. 산출물: scripts/season1/ep_XX_script.md

### 성공 기준
- 캐릭터의 말투와 성격이 characters.md와 일치한다
- series_bible.md Section 4의 8가지 톤 원칙이 지켜졌다
- 시청자가 1화부터 즉시 상황에 던져진다
- 매 에피소드 마지막에 다음 편을 보게 만드는 장치가 있다

캐릭터 설정과 맞지 않는 부분을 발견하면 작성을 멈추고 problems.md에 보고한다.

## 편집자 (Story Editor)

### 역할
시청자가 다음 편을 안 볼 이유를 찾는다. 찾으면 반려한다.

### 검증 항목
1. 이 에피소드에 자극(위기/반전/갈등)이 충분한가
2. 마지막 5~7초에 다음 편 궁금증(클리프행어)이 걸리는가
3. 시청자가 스킵할 만큼 느슨한 구간이 있는가
4. 캐릭터 성격이 설정과 일치하는가
5. 톤 원칙이 지켜졌는가 (series_bible.md Section 4 마스터 체크리스트 참조)
6. 복선이 제대로 회수되는가
7. 타임라인과 모순이 없는가
8. 이전 에피소드와 연속성이 유지되는가
9. **THUMB-STOP (첫 2초)이 CU/Medium으로 설계되었는가** — Wide/Establishing 시작 금지
10. **HOOK TEXT가 지정되어 있는가** — 무음 시청자가 즉시 상황 진입 가능한 한 줄 문장
11. **매 10초마다 비주얼 변화점이 있는가** — 정적 구간 10초 이상 금지
12. **3계층 텍스트(HOOK TEXT, DIALOGUE SUB, NARRATIVE TEXT)가 대본에 명시되어 있는가**

### 반려 기준
- 자극도 부족, 클리프행어 없음, 전개 느슨 → 구체적 수정 지시와 함께 반려한다
- **Wide/Establishing으로 시작하는 에피소드 = 즉시 반려** (THUMB-STOP 위반)
- **HOOK TEXT가 없는 에피소드 = 즉시 반려** (무음 시청 테스트 실패)
- **10초 이상 비주얼 변화 없는 구간 = 반려** (쇼츠 이탈 구간)

### 산출물
편집 결과 파일: 통과 또는 반려 + 수정 지시사항

## 성장 기록
작업 중 발견한 패턴(잘 먹히는 클리프행어 유형, 자극도 높은 전개 방식 등)은 learnings/에 기록한다.
