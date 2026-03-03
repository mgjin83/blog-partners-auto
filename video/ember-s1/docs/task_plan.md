# Task Plan: bible/series_bible.md 작성

> 작성일: 2026-03-01 | 전면 수정: 2026-03-02
> 근거: docs/findings.md
> 산출물: bible/series_bible.md + bible/characters.md (스켈레톤) + bible/timeline.md (스켈레톤)

---

## 포맷 확정

| 항목 | 스펙 |
|------|------|
| 에피소드 길이 | 40~50초 |
| 시즌1 편수 | 10편 |
| 캐릭터 | 고양이 얼굴 + 인간 몸 (의인화) |
| 장르 | 고정 아님. 10편이 하나의 시리즈로 연결 |

## 톤 원칙 (모든 에피소드에 적용)

1. 매 에피소드에 최소 1회, 시청자의 예상을 깨는 전환을 넣는다
2. 주인공은 자기 사람을 지키기 위해 손을 더럽히는 인간이다. 그 과정에서 도덕적 대가를 치른다
3. 주인공의 성장은 소중한 것을 포기하는 선택으로 보여준다
4. 세계관은 배경의 빛, 색감, 분위기로 느끼게 한다
5. 설정보다 중요한 건 관계를 통한 서사다. 캐릭터 간 관계가 변하는 순간이 에피소드의 중심이다
6. 매 에피소드 마지막 5초는 해결되지 않은 상황을 보여주며 끊는다

---

## 10개 섹션 구조

### Section 1: Document Header
**내용**: 교차 참조 테이블, 버전 이력

### Section 2: Series Overview
**내용**: 로그라인, 프레미스, 장르/톤, 포맷 스펙, 타깃 오디언스

### Section 3: World-Building
**내용**: 배경 설정
- 장소 카탈로그: 반복 등장 배경 (빛·색감·분위기 키워드 중심)
- 세계관은 텍스트 설명이 아닌 비주얼 무드로 정의

### Section 4: Tone Principles
**내용**: 6가지 톤 원칙 상세 + 에피소드별 검증 체크리스트
- 이 섹션이 시리즈의 핵심 규칙
- 편집자가 에피소드를 검증할 때 이 원칙을 기준으로 판단

### Section 5: Character Role Map
**내용**: 서사적 역할, 관계 변화 아크
- 소규모 캐스트 (3~5명)
- 모든 캐릭터 = 고양이 얼굴 + 인간 몸
- 관계 변화가 에피소드의 중심 → 관계 매트릭스 포함

### Section 6: 10-Episode Arc Structure
**내용**: 3-Act 에피소드 테이블
- 10편 테이블 (제목 / 시놉시스 / 중심 관계 / 전환 / 도덕적 대가 / 마지막 5초)
- 복선 심기/회수 매핑

### Section 7: Recurring Story Patterns
**내용**: 반복 패턴
- 에피소드 템플릿: 40~50초 구조 (Hook → Development → Unresolved End)
- 전환(subversion) 유형 분류
- 복선 뱅크

### Section 8: Viral Clip Guidelines
**내용**: 바이럴 최적화
- 에피소드 자체가 바이럴 단위
- 10~15초 티저 추출 기준
- VIRAL_CLIP 태그

### Section 9: Production Constraints
**내용**: AI 생성 특성 → 서사 규칙
- 40~50초 = 3~5샷 구성
- 분위기 연출 가이드 (빛·색감 = Kling 강점 활용)

### Section 10: Glossary & Naming Conventions
**내용**: 용어 통일, 파일 명명 규칙

---

## 편집자 검증 항목 ↔ 섹션 매핑

| # | 편집자 검증 항목 | 대응 섹션 |
|---|-----------------|-----------|
| 1 | 자극(위기/반전/갈등) 충분한가 | Section 4: 톤 원칙 1 (예상을 깨는 전환) |
| 2 | 클리프행어가 걸리는가 | Section 4: 톤 원칙 6 (마지막 5초) |
| 3 | 느슨한 구간 없는가 | Section 7: 에피소드 템플릿 (40~50초에 정체 구간 불가) |
| 4 | 캐릭터 성격 일치하는가 | Section 5 → characters.md |
| 5 | 톤 원칙이 지켜졌는가 | Section 4: 6가지 원칙 전체 |
| 6 | 복선 제대로 회수되는가 | Section 7: 복선 뱅크 + Section 6 매핑 |
| 7 | 타임라인과 모순 없는가 | Section 6 → timeline.md |
| 8 | 이전 에피소드와 연속성 유지 | Section 6: 에피소드 테이블 연속성 |

---

## 동시 생성물

### bible/characters.md (스켈레톤)
- Section 5 기반. 소규모 캐스트 상세 설정
- 모든 캐릭터 = 고양이 얼굴 + 인간 몸

### bible/timeline.md (스켈레톤)
- Section 6 기반. 10편 이벤트 타임라인

---
---

# Task Plan: bible/style_guide.md 작성

> 작성일: 2026-03-02
> 근거: docs/findings.md §6 (Kling 프롬프트 리서치)
> 의존: bible/series_bible.md Section 3 (World-Building) + Section 9 (Production Constraints)
> 소비자: 비주얼팀 (visual_guide.md → style_guide.md → character_sheets/ → scene_prompts/)
> 산출물: bible/style_guide.md

---

## 문서 목적

비주얼팀(캐릭터 디자이너 + 씬 디자이너)이 Kling 프롬프트를 작성할 때 참조하는 **비주얼 규칙서**.
series_bible.md가 "무엇을 이야기하는가"를 정의한다면, style_guide.md는 "어떻게 보여주는가"를 정의한다.

## 소비자 워크플로우에서의 위치

```
series_bible.md (원본 설정)
       ↓
style_guide.md (비주얼 규칙) ← 이 문서
       ↓
character_sheets/ (캐릭터별 프롬프트)
       ↓
scene_prompts/ (씬별 프롬프트)
       ↓
Kling API → 클립 생성
```

---

## 7개 섹션 구조

### Section 1: 프롬프트 마스터 포맷
**내용**: 모든 프롬프트가 따르는 표준 구조
- 프롬프트 공식: `[샷 타입] + [캐릭터] + [동작] + [환경] + [카메라] + [조명/무드] + [스타일]`
- 최적 길이: 30~60단어
- 강조 구문: `++핵심 요소++`
- 시간 순서 지시: `"initially... then... finally"`
- 고정 접미사 (Style Lock): 모든 프롬프트 끝에 동일하게 붙이는 스타일 어휘
- 표준 네거티브 프롬프트

**근거**: findings.md §6 프롬프트 구조

### Section 2: 색감·조명 팔레트
**내용**: series_bible.md Section 3의 장소 카탈로그를 Kling 프롬프트 키워드로 변환
- 장소별 색감 팔레트 (L1~L5)
- 분위기 규칙 4가지 → 프롬프트 키워드 매핑
- 분위기별 키워드 뱅크 (비, 네온, 따뜻한 조명, 안개, 그림자)
- 에피소드별 지배적 무드 매핑 (EP 01~10)

**근거**: series_bible.md Section 3 + findings.md §6 키워드 뱅크

### Section 3: 캐릭터 비주얼 규칙
**내용**: 고양이 얼굴 + 인간 몸 캐릭터의 프롬프트 규칙
- 공통 규칙: `"cat face, human body"` 기본 포함, 묘종별 특징 반복
- Character DNA 템플릿 (캐릭터 디자이너가 작성할 양식)
- Character Pack 구성 요건 (전신 4방향, 표정 6종, 액션 포즈 3+)
- 의복 규칙: 캐릭터별 기본 의상 + 상황별 변형
- DO NOT ALLOW 공통 목록

**근거**: findings.md §6 캐릭터 일관성 4단계 아키텍처

### Section 4: 샷 구성 가이드
**내용**: 에피소드 내 샷 시퀀스 설계 규칙
- 40~50초 에피소드 = 7~8개 세그먼트 (각 5~10초)
- 샷 타입별 용도·안정성·프롬프트 키워드
- 카메라 움직임 안전도 테이블
- 에피소드 표준 샷 시퀀스 (Hook → Development → Unresolved End의 비주얼 표현)
- 전환 샷 규칙: 캐릭터 간 세그먼트 이음새를 숨기는 방법

**근거**: findings.md §6 샷 타입·카메라 움직임 + series_bible.md Section 7 에피소드 템플릿

### Section 5: Image-to-Video 워크플로우
**내용**: Kling 생성 파이프라인 단계별 규칙
- 텍스트만으로 생성하지 않는다. Image-to-Video가 기본
- 4단계: Character DNA → Character Pack → Shot Keyframe → Animation
- 키프레임 생성 시 규칙
- 애니메이션 프롬프트 규칙 (동작과 카메라만 기술, 외형은 이미지가 결정)
- Elements 기능 활용법 (레퍼런스 1~4장, Omni 캐릭터 엘리먼트)
- 시드 값 재사용 규칙

**근거**: findings.md §6 Image-to-Video 필수 + Elements 기능

### Section 6: 금지 사항 → 대안 경로
**내용**: Kling 제한 사항을 서사/연출 규칙으로 변환
- 빠른 카메라 복합 움직임 → 단일 움직임으로 분리
- 상충 조명 → 샷당 조명 환경 1개
- 다수 캐릭터 동시 → 1~2명 중심 + 전환 샷
- 복잡한 물리 동작 → 표정과 조명으로 감정 전달
- 텍스트 렌더링 → 자막 레이어로 처리

**근거**: findings.md §6 제한 사항 + series_bible.md Section 9

### Section 7: QA 체크리스트
**내용**: 생성된 클립의 품질 검증
- 캐릭터 얼굴이 레퍼런스 팩과 일치하는가
- 조명 방향이 씬 내에서 일관적인가
- 모핑, 플리커, 여분 사지 아티팩트가 없는가
- 색감 팔레트가 에피소드 무드와 일치하는가
- 카메라 움직임이 부드럽고 동기 부여되었는가
- 전환 샷이 자연스러운가

**근거**: visual_guide.md 성공 기준 + video_guide.md 성공 기준

---

## 검증: 소비자 파일과의 정합성

| 소비자 | 소비자가 style_guide.md에 기대하는 것 | 대응 섹션 |
|--------|--------------------------------------|----------|
| visual_guide.md 캐릭터 디자이너 | "style_guide.md의 비주얼 규칙과 일치" | Section 3 |
| visual_guide.md 씬 디자이너 | "style_guide.md의 프롬프트 규칙과 일치" | Section 1, 2, 4 |
| video_guide.md 영상 생성 | "style_guide.md의 비주얼 톤과 일치" | Section 2, 7 |
| series_bible.md Section 3 | 장소별 비주얼 무드 | Section 2 |
| series_bible.md Section 9 | AI 제작 제약 → 서사 규칙 | Section 5, 6 |
