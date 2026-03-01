# CLAUDE.md

## 이 문서의 역할
모든 에이전트가 지키는 최소한의 규칙. 팀별 상세 지침은 각 팀 guide에 있다.

## 언어 원칙
모든 문서(CLAUDE.md, 팀별 guide, bible/)는 아래 원칙으로 작성한다:
- 금지형("~하지 마라") 대신 지향형("~할 때는 이렇게 한다")으로 쓴다
- 제한이 필요하면 올바른 경로를 함께 제시한다
- 실패를 경고하는 대신 성공의 기준을 명시한다

## 워크플로우
모든 작업은 이 흐름을 따른다:
1. 리서치 → findings.md에 정리
2. 계획 → task_plan.md에 작성
3. 인간이 "implement" 또는 동의 표현을 하면 구현 시작
4. 구현 완료 → 산출물 파일 생성 + progress.md 업데이트

코드 작성은 task_plan.md 승인 후에 시작한다.

## 산출물 기준
작업 완료의 기준: 다음 단계 에이전트가 이 산출물로 바로 작업할 수 있는가?
모든 작업은 구체적 파일로 완료한다. 감상이나 요약은 산출물이 아니다.

## bible/ 운영
bible/은 전체 사업의 원본 설정이다.
수정이 필요하면 problems.md에 사유를 작성하고 관리자에게 보고한다.
관리자가 검토 후 인간에게 보고하고, 인간이 승인하면 반영한다.

## 컨텍스트 관리
컨텍스트 윈도우는 유한하다.
1. 작업 시작 시 자기 팀 guide + 관련 bible/ 파일을 읽는다
2. 핵심 정보를 docs/working_context.md에 압축 정리한다
3. 작업 중에는 working_context.md를 참조한다
4. 원본 확인이 필요하면 해당 파일을 다시 연다
5. 작업 완료 후 working_context.md를 삭제한다

## 세션 시작 루틴
1. progress.md 읽기
2. problems.md 확인
3. 자기 팀 guide 읽기

## 팀별 guide 위치
각 에이전트는 CLAUDE.md + 자기 팀 guide만 읽는다:
- 관리자: /docs/director_guide.md
- 스토리팀: /docs/story_guide.md
- 비주얼팀: /docs/visual_guide.md
- 영상팀: /docs/video_guide.md
- 블로그팀: /docs/blog_guide.md

다른 팀의 guide는 읽지 않는다. 팀 간 연계는 관리자가 담당한다.
