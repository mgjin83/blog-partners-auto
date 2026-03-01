# 비주얼팀 가이드 (Visual Guide)

## 읽어야 할 파일
- CLAUDE.md
- 이 파일 (visual_guide.md)
- bible/style_guide.md
- bible/characters.md
- characters/character_sheets/

## 캐릭터 디자이너 (Character Designer)

### 역할
등장인물의 외형 프롬프트를 확정하고 레퍼런스 이미지 생성을 지시한다.

### 작업 흐름
1. characters.md와 style_guide.md를 읽는다
2. 캐릭터별 외형 프롬프트를 작성한다
3. 산출물: characters/character_sheets/[캐릭터명].md

### 성공 기준
- 동일 캐릭터는 항상 동일 프롬프트를 사용한다 (일관성)
- style_guide.md의 비주얼 규칙과 일치한다
- 다음 단계(씬 디자이너)가 이 프롬프트로 바로 씬을 만들 수 있다

## 씬 디자이너 (Scene Designer)

### 역할
대본의 각 씬을 Kling 영상 생성 프롬프트로 변환한다.

### 작업 흐름
1. 대본(scripts/season1/ep_XX_script.md)을 받는다
2. style_guide.md와 해당 캐릭터 시트를 읽는다
3. 씬별 영상 프롬프트를 작성한다
4. 산출물: scripts/scene_prompts/ep_XX_scenes.md

### 성공 기준
- style_guide.md의 프롬프트 규칙과 일치한다
- 캐릭터 시트의 외형 프롬프트를 정확히 사용한다
- 다음 단계(영상 생성)가 이 프롬프트로 바로 Kling API를 호출할 수 있다

## 성장 기록
효과적이었던 프롬프트 패턴, Kling에서 잘 나오는 표현 등은 learnings/에 기록한다.
