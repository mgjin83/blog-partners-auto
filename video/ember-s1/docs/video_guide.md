# 영상팀 가이드 (Video Guide)

## 읽어야 할 파일
- CLAUDE.md
- 이 파일 (video_guide.md)
- bible/style_guide.md
- scripts/scene_prompts/ (해당 에피소드)
- characters/character_sheets/ (해당 캐릭터)

## 이미지/영상 생성 규칙 (필독)
CLAUDE.md의 이미지 생성 규칙을 반드시 따른다. 핵심 요약:
- Kling 영상 생성에 사용되는 키프레임과 레퍼런스만 생성한다
- 생성 전에 task_plan.md에 용도·장수·예상 비용을 명시하고 인간 승인을 받는다

## 영상 생성 (Video Producer)

### 역할
씬 프롬프트를 받아서 Kling 3.0 멀티샷으로 영상 클립을 생성한다.

### 작업 흐름
1. shot_keyframes/ep_XX/kling_prompts.md를 받는다
2. 멀티샷 그룹 단위로 Kling에서 영상을 생성한다
3. 산출물: 그룹별 클립 파일

### 성공 기준
- 캐릭터 외형이 캐릭터 시트와 일치한다
- style_guide.md의 비주얼 톤과 일치한다
- 그룹 내 샷 간 연속성이 유지된다
- 클립 품질이 편집에 사용 가능한 수준이다

## 편집 (Editor)

### 역할
클립을 이어붙여 완성 에피소드를 만든다.

### 작업 흐름
1. 생성된 클립들과 대본을 받는다
2. 클립 이어붙이기 + 자막(영어) + 배경음을 입힌다
3. 쇼츠 하이라이트 클립(15~30초)을 별도로 추출한다
4. 영상 원본(자막/더빙 없는 클린 버전)을 /episodes/raw/에 저장한다
5. 산출물:
   - episodes/series/ep_XX_en.mp4 (완성본)
   - episodes/series/ep_XX_highlights/ (쇼츠 클립)
   - episodes/raw/series_raw/ep_XX_raw.mp4 (클린 버전)

### 성공 기준
- 영상 흐름이 대본과 일치한다
- 자막 타이밍이 정확하다
- 클린 버전이 별도 보관되어 있다 (추후 다국어 재활용 가능)
- 쇼츠 하이라이트가 가장 자극적인 장면을 포함한다

## 성장 기록
편집 패턴, 배경음 효과, 자막 스타일 등 발견사항은 learnings/에 기록한다.
