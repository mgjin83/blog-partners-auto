# Progress

## 완료된 작업

### bible/series_bible.md 작성 (2026-03-02)
- **산출물**: bible/series_bible.md (10개 섹션, "Ember" 느와르 드라마)
- **포맷**: 40~50초 × 10편, 고양이 얼굴 + 인간 몸
- **근거**: docs/findings.md (리서치), docs/task_plan.md (계획)
- **동시 생성물**: bible/characters.md (4인 캐스트 상세), bible/timeline.md (에피소드별 타임라인)

### bible/style_guide.md 작성 (2026-03-02)
- **산출물**: bible/style_guide.md (7개 섹션)
- **근거**: docs/findings.md §6 (Kling 프롬프트 리서치)

### 정합성 수정 5건 (2026-03-02)
- series_bible.md: 톤 원칙 6→8 (원칙 7 전술 관계, 원칙 8 결핍→방향→약속)
- series_bible.md: 편집자 체크리스트 6→8항 (전술 관계, 찐주 구조 추가)
- series_bible.md: Section 5에 찐주/짭주 구조 명시 (루나=찐주, 마일로=짭주)
- story_guide.md: 회귀 시스템 참조 삭제 → 톤 원칙 8가지 참조로 교체

### scripts/season1/ 에피소드 대본 10편 작성 (2026-03-02)
- **산출물**: ep_01_script.md ~ ep_10_script.md (10편 전체)
- **참조**: series_bible.md Section 6, style_guide.md 프롬프트 마스터 포맷, story_principles.md 원칙 7가지
- **구조**: 에피소드당 5~7씬, 씬별 연출/대사(영어)/Kling 프롬프트 포함
- **검증**: 8가지 톤 원칙 + 편집자 체크리스트 8항 전부 충족 확인
- **복선**: F01~F07 심기/회수 매핑 완료
- **삼자 교차점**: #1 (EP 06), #2 (EP 10) 배치 완료

### 시리즈 전체 정합성 검증 + 수정 8건 (2026-03-02)
- **검증 범위**: 10편 대본 × 4개 참조 문서 (series_bible, characters, timeline, story_principles)
- **Critical 수정 2건**:
  - 애쉬 나이/관계 통일: "남동생" → "오빠" (characters.md, series_bible.md)
  - EP 09 S3 눈 색: "amber-green" → "yellow" (characters.md 기준)
- **Moderate 수정 4건**:
  - EP 08 S5: "ASH — 7 missed calls" 추가 (EP 09 인지 경로 복선)
  - EP 07 S4: 루나 폰 촬영 디테일 추가 (EP 10 증거 수집 복선)
  - EP 10 S4: CCTV 캡처 증거 추가 (F05 회수 강화) + 몽타주 프롬프트 4분할
  - EP 06 메타: 삼자 교차점 #1 범위 명시 (EP 06~07 걸쳐 완성)
- **Minor 수정 2건**:
  - EP 10 S5: 프롬프트 2분할 (미디엄→클로즈업)
  - EP 10 S4: 제작 노트 추가

### story_principles.md 원칙 #8 추가 반영 (2026-03-02)
- **추가된 원칙**: #8 빈칸의 설계 (갈등 양쪽 납득 + 열린 질문)
- **series_bible.md**: 원칙 9 추가, 체크리스트 9항으로 확장 (8→9), "8가지"→"9가지"
- **story_guide.md**: "8가지"→"9가지" (2곳)
- **ep_01~10_script.md**: 편집자 체크리스트에 9번 항목 추가 (에피소드별 구체적 근거 기술)

### 캐릭터 레퍼런스 이미지 파이프라인 구축 (2026-03-02)
- **SDK**: google-genai (Gemini 2.0 Flash / 2.5 Flash Image)
- **환경 설정**: .env (GOOGLE_API_KEY), pyproject.toml (google-genai 의존성 추가)
- **이미지 생성 모듈**: src/blog_partners_auto/tools/image_generator.py
  - Style Lock + Negative Prompt 자동 삽입
  - 모델 fallback (gemini-2.0-flash-exp-image-generation → gemini-2.5-flash-image → nano-banana-pro-preview)
  - Rate limit 자동 재시도
  - **reference_image 멀티모달 입력** 지원 (face_closeup을 레퍼런스로 사용)
- **캐릭터 시트 4개**: characters/character_sheets/{luna,ash,duchess,milo}.md
- **실행 스크립트**: scripts/generate_characters.py (CLI 인자로 캐릭터 선택 가능)

### Pre-Production 에셋 전량 생성 (2026-03-02)
- **총 69장 생성** (Gemini 2.0 Flash Image Generation)
- **스크립트 3개**: generate_characters.py, generate_expressions.py, generate_preproduction.py

### 캐릭터 얼굴 일관성 재생성 (2026-03-03)
- **문제**: face_closeup과 다른 샷 간 얼굴이 일관되지 않음
- **해결**: face_closeup을 canonical reference로 사용하는 멀티모달 입력 방식 도입
- **스크립트**: scripts/regenerate_consistent.py
- **결과**: 4캐릭터 전체 58장 재생성 (face_closeup 원본 유지 + 나머지 전부 교체)

| 캐릭터 | 장수 | 얼굴 일관성 | 눈 색상 |
|--------|------|------------|---------|
| LUNA | 15장 | calico 패턴 유지 | green eyes |
| ASH | 15장 | grey tabby 줄무늬 유지 | yellow eyes |
| DUCHESS | 13장 | persian white fur + flat face 유지 | blue eyes |
| MILO | 15장 | orange tabby 줄무늬 유지 | amber eyes |

#### 캐릭터별 Character Pack (58장, 일관성 보장)

| 캐릭터 | 기본 (2) | 표정 (6) | 앵글 (3) | 액션 (3) | 의상 변형 | 소계 |
|--------|---------|---------|---------|---------|----------|------|
| LUNA | fullbody_front, face_closeup | determination, fear, anger, sadness, resignation, cold_composure | 3/4, side, back | walking, looking_back, leaning | dark_coat (2장) | 16 |
| ASH | fullbody_front, face_closeup | determination, fear, anger, sadness, resignation, cold_composure | 3/4, side, back | walking, looking_back, leaning | torn_clothes_ep01 (2장) | 16 |
| DUCHESS | fullbody_front, face_closeup | cold_composure, predatory_smile, displeasure, contempt, controlled_anger, possessive_satisfaction | 3/4, side, back | walking, looking_back, leaning | — | 14 |
| MILO | fullbody_front, face_closeup | concern, suspicion, quiet_disappointment, determination, warmth, cold_silence | 3/4, side, back | walking, looking_back, leaning | casual (2장) | 16 |

#### 환경 레퍼런스 (7장)

| 코드 | 장소 | 색감 | 사용 에피소드 |
|------|------|------|-------------|
| L1_flower_shop | 꽃집 (밝음) | amber, warm | EP 01, 06, 09, 10 |
| L1_flower_shop_dark | 꽃집 (어두움) | shadow, cold | EP 06, 09 |
| L2_duchess_club | 더체스의 클럽 | blue, purple neon | EP 02, 07, 10 |
| L3_rainy_street | 비 오는 거리 | orange sodium, grey | EP 02, 03, 07 |
| L4_park_bench | 공원 벤치 | warm daylight, green | EP 04, 08 |
| L5_dark_alley | 어두운 골목 | darkness, distant neon | EP 03, 05 |
| L6_police_office | 경찰 사무실 | fluorescent, institutional | EP 04, 07-09 |

### 시즌 1 전체 Shot Keyframe 생성 (2026-03-03)
- **총 62장** (Gemini 2.0 Flash Image Generation, 캐릭터 레퍼런스 기반)
- **스크립트**: scripts/generate_keyframes_ep01.py (EP01), scripts/generate_keyframes_all.py (EP02~10)
- **방식**: 캐릭터 등장 씬은 face_closeup을 멀티모달 레퍼런스로 사용하여 얼굴 일관성 유지

| EP | 제목 | 키프레임 수 |
|---|---|---|
| EP01 | The Debt | 7장 |
| EP02 | The Deal | 7장 |
| EP03 | Delivery | 7장 |
| EP04 | The Crack | 6장 |
| EP05 | Hands Dirty | 6장 |
| EP06 | Roots | 5장 |
| EP07 | The File | 5장 |
| EP08 | Ash and Bone | 5장 |
| EP09 | The Cost | 5장 |
| EP10 | Ember | 9장 |

### 시즌 1 전체 Kling 프롬프트 작성 (2026-03-03)
- **산출물**: 10개 kling_prompts.md (EP01~EP10, 총 63개 씬)
- **위치**: characters/shot_keyframes/{ep01~ep10}/kling_prompts.md
- **포맷**: Kling 2.6 Native Audio 프롬프트
  - 씬별 키프레임 파일명 매핑
  - Elements 지정 (캐릭터 활성화)
  - Sound / Music / 대사 (`[캐릭터명, 음성설명]: "대사"` 포맷)
  - 제작 노트 (VIRAL CLIP, 복선, 크레딧 예상)

## 현재 상태

| 카테고리 | 파일 | 상태 |
|---------|------|------|
| **기획** | docs/findings.md | 완료 |
| | docs/task_plan.md | 완료 |
| | docs/story_guide.md | 완료 |
| | docs/kling_workflow_guide.md | 완료 |
| **바이블** | bible/series_bible.md | 완료 |
| | bible/characters.md | 완료 |
| | bible/timeline.md | 완료 |
| | bible/style_guide.md | 완료 |
| | bible/story_principles.md | 완료 |
| **대본** | scripts/season1/ep_01~10_script.md | 완료 (10편) |
| **캐릭터 에셋** | characters/reference_images/ (4캐릭터) | 완료 (58장, 일관성 보장) |
| | characters/environment_references/ | 완료 (7장) |
| | characters/character_sheets/ | 완료 (4개) |
| **Shot Keyframes** | characters/shot_keyframes/ep01~10/ | 완료 (62장) |
| **Kling 프롬프트** | characters/shot_keyframes/ep01~10/kling_prompts.md | 완료 (10파일, 63씬) |
| **생성 스크립트** | scripts/generate_characters.py | 완료 |
| | scripts/generate_expressions.py | 완료 |
| | scripts/generate_preproduction.py | 완료 |
| | scripts/regenerate_consistent.py | 완료 |
| | scripts/generate_keyframes_ep01.py | 완료 |
| | scripts/generate_keyframes_all.py | 완료 |
| **핵심 모듈** | src/blog_partners_auto/tools/image_generator.py | 완료 |

## 파일 구조

```
D:/Automation/
├── .env                              # GOOGLE_API_KEY
├── pyproject.toml                    # google-genai 의존성
├── docs/
│   ├── findings.md                   # 리서치
│   ├── task_plan.md                  # 계획
│   ├── story_guide.md                # 스토리 가이드
│   ├── progress.md                   # (이 파일)
│   └── kling_workflow_guide.md       # Kling 웹 UI 워크플로우 가이드
├── bible/
│   ├── series_bible.md               # 시리즈 바이블
│   ├── characters.md                 # 캐릭터 상세
│   ├── timeline.md                   # 타임라인
│   ├── style_guide.md                # 스타일 가이드
│   └── story_principles.md           # 스토리 원칙
├── scripts/
│   ├── season1/
│   │   └── ep_01~10_script.md        # 에피소드 대본 10편
│   ├── generate_characters.py        # 캐릭터 초기 생성
│   ├── generate_expressions.py       # 표정 시트 생성
│   ├── generate_preproduction.py     # 앵글/액션/의상/환경 생성
│   ├── regenerate_consistent.py      # 일관성 재생성 (face_closeup 레퍼런스)
│   ├── generate_keyframes_ep01.py    # EP01 키프레임 생성
│   └── generate_keyframes_all.py     # EP02~10 키프레임 생성
├── src/blog_partners_auto/tools/
│   └── image_generator.py            # 이미지 생성 모듈 (Gemini API)
└── characters/
    ├── character_sheets/             # 캐릭터 DNA 시트 (4개)
    ├── reference_images/             # 캐릭터 레퍼런스 이미지 (58장)
    │   ├── luna/                     # 16장 (기본+표정+앵글+액션+의상)
    │   ├── ash/                      # 16장
    │   ├── duchess/                  # 14장
    │   └── milo/                     # 16장 (기본+표정+앵글+액션+의상)
    ├── environment_references/       # 환경 레퍼런스 (7장)
    └── shot_keyframes/               # 씬별 키프레임 + Kling 프롬프트
        ├── ep01/  (7 keyframes + kling_prompts.md)
        ├── ep02/  (7 keyframes + kling_prompts.md)
        ├── ep03/  (7 keyframes + kling_prompts.md)
        ├── ep04/  (6 keyframes + kling_prompts.md)
        ├── ep05/  (6 keyframes + kling_prompts.md)
        ├── ep06/  (5 keyframes + kling_prompts.md)
        ├── ep07/  (5 keyframes + kling_prompts.md)
        ├── ep08/  (5 keyframes + kling_prompts.md)
        ├── ep09/  (5 keyframes + kling_prompts.md)
        └── ep10/  (9 keyframes + kling_prompts.md)
```

## 총 에셋 수량

| 카테고리 | 수량 |
|---------|------|
| 캐릭터 레퍼런스 이미지 | 58장 |
| 환경 레퍼런스 이미지 | 7장 |
| Shot Keyframes | 62장 |
| **이미지 총합** | **127장** |
| Kling 프롬프트 파일 | 10개 (63씬) |
| 에피소드 대본 | 10편 |

## 다음 단계 (영상 제작)

- **Step 1**: Kling 웹 로그인 → Elements에 캐릭터 4명 등록 (reference_images 사용)
- **Step 2**: EP01 S3 (VIRAL CLIP) 먼저 테스트 생성 → 품질 확인
- **Step 3**: 만족 시 나머지 씬 순차 진행 (kling_prompts.md 참조)
- **Step 4**: 에피소드별 클립 다운로드 → 편집 조립 (CapCut/DaVinci/FFmpeg)
- **Step 5**: 자막 추가 → 최종 Export (9:16, 40~50초)
- 워크플로우 상세: `docs/kling_workflow_guide.md` 참조
