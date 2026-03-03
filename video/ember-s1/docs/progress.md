# Progress

## 완료된 작업

### bible/series_bible.md 작성 (2026-03-02)
- **산출물**: bible/series_bible.md (10개 섹션, "Ember" 느와르 드라마)
- **포맷**: 40~50초 × 10편, 서양인 인간 캐릭터
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
  - EP 09 S3 눈 색 통일
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
- **SDK**: google-genai (Gemini 2.0 Flash Image Generation)
- **환경 설정**: .env (GOOGLE_API_KEY), pyproject.toml (google-genai 의존성 추가)
- **이미지 생성 모듈**: src/blog_partners_auto/tools/image_generator.py
  - Style Lock + Negative Prompt 자동 삽입
  - 모델 fallback (gemini-2.0-flash-exp-image-generation → gemini-2.5-flash-image → nano-banana-pro-preview)
  - Rate limit 자동 재시도
  - **reference_image 멀티모달 입력** 지원 (face_closeup을 레퍼런스로 사용)
- **캐릭터 시트 4개**: characters/character_sheets/{luna,ash,duchess,milo}.md
- **실행 스크립트**: scripts/generate_characters.py (CLI 인자로 캐릭터 선택 가능)

### 캐릭터 리디자인: 고양이 → 서양인 인간 (2026-03-03)
- **변경 사유**: 고양이 얼굴 캐릭터의 매력 부족 → 서양인 인간으로 전면 교체
- **영향 범위**: 프로젝트 전체 (설정 문서, 대본, 이미지, 프롬프트)
- **캐릭터 외형 변경**:

| 캐릭터 | 이전 (고양이) | 변경 (서양인 인간) |
|--------|-------------|------------------|
| LUNA | calico cat face, green eyes | auburn hair, green eyes, freckles, delicate features |
| ASH | grey tabby cat face, yellow eyes | dark brown messy hair, hazel eyes, stubble, strong jaw |
| DUCHESS | persian cat face, blue eyes | platinum blonde, ice blue eyes, sharp cheekbones, porcelain skin |
| MILO | orange tabby cat face, amber eyes | sandy blonde, warm brown eyes, clean-cut, athletic |

- **문서 수정 완료**:
  - bible/characters.md — 4캐릭터 외형 섹션 전면 재작성
  - bible/series_bible.md — 세계관, 캐릭터 목록, 프롬프트 규칙 등 수정
  - bible/style_guide.md — 캐릭터 비주얼 규칙, 매력 키워드, DNA 템플릿, QA 체크리스트 수정
  - docs/kling_workflow_guide.md — 프롬프트 예시, QA 기준 수정
  - characters/character_sheets/{luna,ash,duchess,milo}.md — 전면 재작성
  - scripts/season1/ep_01~10_script.md — 10편 전체 캐릭터 설명 교체
  - characters/shot_keyframes/ep01~10/kling_prompts.md — 10파일 전체 교체
  - scripts/regenerate_consistent.py — 캐릭터 정의 교체
  - scripts/generate_characters.py — 캐릭터 정의 교체
  - scripts/generate_keyframes_ep01.py — 프롬프트 교체
  - scripts/generate_keyframes_all.py — 프롬프트 교체
  - scripts/generate_preproduction.py — 캐릭터 정의 교체
  - scripts/generate_expressions.py — 캐릭터 정의 교체
  - src/blog_partners_auto/tools/image_generator.py — CHARACTER_BASE 및 레퍼런스 프롬프트 수정

### 캐릭터 레퍼런스 이미지 전체 재생성 (2026-03-03)
- **총 56장** (기존 고양이 이미지 백업 → 서양인 인간으로 교체)
- **방식**: face_closeup을 canonical reference로 사용하는 멀티모달 입력 방식

| 캐릭터 | 장수 | 외형 일관성 | 눈 색상 |
|--------|------|------------|---------|
| LUNA | 15장 | auburn hair, freckles 유지 | green eyes |
| ASH | 13장 | dark brown hair, stubble 유지 | hazel eyes |
| DUCHESS | 13장 | platinum blonde, sharp features 유지 | ice blue eyes |
| MILO | 15장 | sandy blonde, clean-cut 유지 | warm brown eyes |

- **Ash torn_clothes 의상 변형 2장**: content filter로 실패 (bloodstains 관련)

### Shot Keyframe 전체 재생성 (2026-03-03)
- **총 62장** 재생성 완료 (EP01 7장 + EP02-10 55장)
- EP01~EP10 전체 키프레임을 서양인 인간 캐릭터로 재생성
- 기존 고양이 키프레임 백업 완료 (shot_keyframes_cat_backup/)

### 시즌 1 전체 Kling 프롬프트 수정 (2026-03-03)
- **산출물**: 10개 kling_prompts.md 전체 수정
- **변경**: 모든 cat-face 캐릭터 설명 → 서양인 인간 설명
- **검증**: grep으로 cat/tabby/calico/persian/whiskers 참조 0건 확인

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
| **캐릭터 에셋** | characters/reference_images/ (4캐릭터) | 완료 (56장, 서양인 인간) |
| | characters/environment_references/ | 완료 (7장) |
| | characters/character_sheets/ | 완료 (4개, 인간 버전) |
| **Shot Keyframes** | characters/shot_keyframes/ep01~10/ | 완료 (62장, 인간 버전) |
| **Kling 프롬프트** | characters/shot_keyframes/ep01~10/kling_prompts.md | 완료 (인간 버전) |
| **생성 스크립트** | scripts/generate_characters.py | 완료 (인간 버전) |
| | scripts/generate_expressions.py | 완료 (인간 버전) |
| | scripts/generate_preproduction.py | 완료 (인간 버전) |
| | scripts/regenerate_consistent.py | 완료 (인간 버전) |
| | scripts/generate_keyframes_ep01.py | 완료 (인간 버전) |
| | scripts/generate_keyframes_all.py | 완료 (인간 버전) |
| **핵심 모듈** | src/blog_partners_auto/tools/image_generator.py | 완료 (인간 버전) |

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
    ├── reference_images/             # 캐릭터 레퍼런스 이미지 (56장, 서양인 인간)
    │   ├── luna/                     # 15장 (기본+표정+앵글+액션+의상)
    │   ├── ash/                      # 13장 (torn_clothes 2장 미생성)
    │   ├── duchess/                  # 13장
    │   └── milo/                     # 15장 (기본+표정+앵글+액션+의상)
    ├── environment_references/       # 환경 레퍼런스 (7장)
    ├── reference_images_cat_backup/  # 기존 고양이 이미지 백업
    ├── shot_keyframes_cat_backup/    # 기존 고양이 키프레임 백업
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
| 캐릭터 레퍼런스 이미지 | 56장 (서양인 인간) |
| 환경 레퍼런스 이미지 | 7장 |
| Shot Keyframes | 62장 (서양인 인간) |
| **이미지 총합** | **125장** |
| Kling 프롬프트 파일 | 10개 (63씬) |
| 에피소드 대본 | 10편 |

## 다음 단계 (영상 제작)

- **Step 1**: Kling 웹 로그인 → Element Reference에 캐릭터 4명 등록 + Scene Reference에 배경 등록
- **Step 2**: EP01 S3 (VIRAL CLIP) 먼저 테스트 생성 → 품질 확인
- **Step 3**: 만족 시 나머지 씬 순차 진행 (kling_prompts.md 참조)
- **Step 4**: 에피소드별 클립 다운로드 → 편집 조립 (CapCut/DaVinci/FFmpeg)
- **Step 5**: 자막 추가 → 최종 Export (9:16, 40~50초)
- 워크플로우 상세: `docs/kling_workflow_guide.md` 참조
