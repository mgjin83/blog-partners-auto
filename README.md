# Automation -- 콘텐츠 자동화 파이프라인

유튜브 쇼츠 + 블로그 파트너스 수익화를 위한 멀티채널 콘텐츠 생산 시스템.

## 사업 구조

| 채널 | 형태 | 언어 | 수익 모델 |
|------|------|------|-----------|
| 하렘 로맨스 코미디 (Harem S1) | 쇼츠 50초 x 10편 | 영어 | 유튜브 광고 |
| 네이버 블로그 | 리뷰/정보성 글 | 한국어 | 쿠팡 파트너스 |
| 워드프레스 블로그 | 리뷰/정보성 글 | 영어 | 아마존 어소시에이트 |

## 기술 스택

| 용도 | 도구 |
|------|------|
| 이미지 생성 | google-genai (Gemini 2.0 Flash) |
| 영상 생성 | Kling 3.0 웹 UI (Image to Video) |
| 작업 관리 | Claude Code + CLAUDE.md |

## 프로젝트 구조

```
D:\Automation\
├── CLAUDE.md                              # 에이전트 공통 규칙
├── README.md
│
├── video/                                 # 영상 프로젝트
│   ├── story_principles.md                #   공통 스토리 원칙 (전 시리즈)
│   ├── story_guide.md                     #   공통 스토리 가이드 (전 시리즈)
│   ├── harem-s1/                          #   [진행중] 하렘 로맨스 코미디 S1
│   │   ├── bible/
│   │   │   ├── characters.md              #     캐릭터 설정 (6인)
│   │   │   ├── series_bible.md            #     시리즈 바이블 (10편 아크)
│   │   │   └── timeline.md               #     타임라인 + 떡밥 맵
│   │   ├── scripts/season1/
│   │   │   └── ep_01~10_script.md         #     에피소드 대본 (씬별 CAM 지시)
│   │   └── docs/
│   │       └── progress.md               #     진행 기록
│   ├── ember-s1/                          #   [폐기] 느와르 드라마 S1
│   └── shorts/                            #   [예정] 독립형 쇼츠
│
├── blog/                                  # 블로그 프로젝트
│   ├── blog_guide.md                      #   블로그 작성 가이드
│   ├── naver/                             #   네이버 블로그 콘텐츠
│   ├── wordpress/                         #   워드프레스 콘텐츠
│   └── output/                            #   생성된 글
│       ├── ko/  (blog/, shorts/)
│       ├── en/  (blog/, shorts/)
│       └── es/  (blog/, shorts/)
│
├── docs/                                  # 운영 문서
│   ├── channel_ideas.md                   #   채널 아이디어
│   └── tech_radar.md                      #   도구/플러그인 리서치
│
├── logs/                                  # 작업 로그
│   ├── active.md                          #   활성 프로젝트 목록
│   ├── harem-s1.md                        #   하렘 S1 작업 로그
│   └── ember-s1.md                        #   Ember S1 로그 (폐기)
│
├── src/                                   # (레거시) 자동화 코드
└── tests/                                 # (레거시) 테스트
```

## 작업 규칙

- 새 대화 시작 → `logs/active.md` 먼저 읽기
- 이미지 생성 → 한 번에 최대 5장, 생성 전 유저 승인 필수
- 작업 완료 → 해당 프로젝트 로그에 기록
