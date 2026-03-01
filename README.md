# Blog Partners Auto — 콘텐츠 자동화 파이프라인

유튜브 쇼츠 + 블로그 파트너스 수익화를 위한 멀티채널 콘텐츠 자동 생산 시스템.

## 사업 구조

| 채널 | 형태 | 언어 | 수익 모델 |
|------|------|------|-----------|
| 시리즈물 드라마 (회귀물) | 롱폼 3~5분 + 쇼츠 하이라이트 | 영어 우선 | 유튜브 광고 + PPL |
| 리트리버 일상 코미디 | 독립형 쇼츠 | 영어 우선 | 유튜브 광고 + PPL |
| 네이버 블로그 | 리뷰/정보성 글 | 한국어 | 쿠팡 파트너스 |
| 워드프레스 블로그 | 리뷰/정보성 글 | 영어 | 아마존 어소시에이트 |

## 팀 구성

| 팀 | 역할 | 가이드 |
|----|------|--------|
| 관리자 | 파이프라인 조율, 팀 간 중재 | `docs/director_guide.md` |
| 스토리팀 | 대본, 시나리오 작성 | `docs/story_guide.md` |
| 비주얼팀 | 캐릭터 디자인, 이미지 생성 | `docs/visual_guide.md` |
| 영상팀 | 영상 편집, 음악/효과음 | `docs/video_guide.md` |
| 블로그팀 | SEO 글 작성, 파트너스 링크 | `docs/blog_guide.md` |

## 워크플로우

```
리서치 → findings.md → 계획 → task_plan.md → 승인 → 구현 → progress.md 업데이트
```

## 프로젝트 구조

```
D:\Automation\
├── CLAUDE.md                          # 에이전트 공통 규칙
├── README.md
│
├── docs/                              # 운영 문서
│   ├── director_guide.md              #   관리자 가이드
│   ├── story_guide.md                 #   스토리팀 가이드
│   ├── visual_guide.md                #   비주얼팀 가이드
│   ├── video_guide.md                 #   영상팀 가이드
│   ├── blog_guide.md                  #   블로그팀 가이드
│   ├── task_plan.md                   #   현재 작업 계획
│   ├── findings.md                    #   리서치 결과
│   ├── progress.md                    #   진행 상황
│   ├── problems.md                    #   이슈/문제 기록
│   ├── changelog.md                   #   변경 이력
│   ├── channel_ideas.md               #   채널 아이디어 보관
│   └── tech_radar.md                  #   도구/플러그인 리서치
│
├── bible/                             # 사업 원본 설정 (수정 시 관리자 승인 필요)
│   ├── series_bible.md                #   시리즈 세계관
│   ├── characters.md                  #   캐릭터 설정
│   ├── timeline.md                    #   타임라인
│   ├── style_guide.md                 #   비주얼 스타일 가이드
│   ├── blog_voice.md                  #   블로그 톤앤매너
│   └── ppl_catalog.md                 #   PPL 상품 카탈로그
│
├── scripts/                           # 대본
│   ├── season1/                       #   시즌1 에피소드 대본
│   └── scene_prompts/                 #   장면별 이미지/영상 프롬프트
│
├── characters/                        # 캐릭터 에셋
│   ├── character_sheets/              #   캐릭터 시트
│   └── reference_images/              #   레퍼런스 이미지
│
├── episodes/                          # 완성 에피소드
│   ├── series/                        #   시리즈물 드라마
│   ├── retriever/                     #   리트리버 코미디
│   └── raw/                           #   클린 버전 (다국어 재활용용)
│
├── blog/                              # 블로그 콘텐츠
│   ├── naver/                         #   네이버 블로그 (쿠팡 파트너스)
│   └── wordpress/                     #   워드프레스 (아마존 어소시에이트)
│
├── learnings/                         # 복리 성장 데이터
│   ├── what_worked.md                 #   성공 사례
│   ├── what_failed.md                 #   실패 사례
│   └── style_discoveries.md           #   스타일 발견
│
├── src/                               # (레거시) 자동화 코드
├── tests/                             # (레거시) 테스트
└── output/                            # (레거시) 생성 콘텐츠 출력
```

## 스케일링 조건

- 쇼츠 채널: 구독자 1만 달성 시 새 채널 추가
- 네이버 블로그: 일일 방문자 1,000명 달성 시 새 블로그 추가
- 워드프레스: 월간 유니크 방문자 10,000명 달성 시 새 블로그 추가
