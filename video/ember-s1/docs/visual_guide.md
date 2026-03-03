# 비주얼팀 가이드 (Visual Guide)

## 읽어야 할 파일
- CLAUDE.md
- 이 파일 (visual_guide.md)
- bible/style_guide.md
- bible/characters.md
- characters/character_sheets/

## 이미지 생성 규칙 (필독)
CLAUDE.md의 이미지 생성 규칙을 반드시 따른다. 핵심 요약:
- 최종 산출물에 직접 사용되는 이미지만 생성한다
- 캐릭터 레퍼런스: 캐릭터당 1~2장 (Kling Element 등록용)
- 씬 키프레임: 씬당 1장 (Kling I2V 입력용)
- "혹시 필요할 수 있는" 에셋 (표정 시트, 앵글 시트, 액션 포즈 등)을 미리 대량 생산하지 않는다
- 생성 전에 task_plan.md에 용도·장수·예상 비용을 명시하고 인간 승인을 받는다

## 캐릭터 디자이너 (Character Designer)

### 역할
등장인물의 외형 프롬프트를 확정하고 최소한의 레퍼런스 이미지를 생성한다.

### 작업 흐름
1. characters.md와 style_guide.md를 읽는다
2. 캐릭터별 외형 프롬프트를 작성한다
3. 산출물: characters/character_sheets/[캐릭터명].md

### Character Pack 구성 (캐릭터당 최소 이미지)

| 이미지 | 용도 | 필수 여부 |
|--------|------|----------|
| face_closeup.png | Kling Element 등록 (얼굴 앵커) | 필수 |
| fullbody_front.png | Kling Element 등록 (전신 참조) | 선택 |

- 캐릭터당 **1~2장**이 기본이다. 인물당 최대 3장까지 허용
- 그 외 이미지(표정, 앵글, 액션, 의상 변형 등)는 실제 영상 제작에서 필요해진 시점에만 생성한다

### 성공 기준
- 동일 캐릭터는 항상 동일 프롬프트를 사용한다 (일관성)
- style_guide.md의 비주얼 규칙과 일치한다
- Kling Element에 바로 등록할 수 있는 이미지가 산출된다

## 씬 디자이너 (Scene Designer)

### 역할
대본의 각 씬을 Kling 영상 생성 프롬프트로 변환한다.

### 작업 흐름
1. 대본(scripts/season1/ep_XX_script.md)을 받는다
2. style_guide.md와 해당 캐릭터 시트를 읽는다
3. 씬별 키프레임 이미지를 생성한다 (씬당 1장)
4. 씬별 Kling 프롬프트를 작성한다
5. 산출물: characters/shot_keyframes/ep_XX/ (키프레임 + kling_prompts.md)

### 성공 기준
- style_guide.md의 프롬프트 규칙과 일치한다
- 캐릭터 시트의 외형 프롬프트를 정확히 사용한다
- 다음 단계(영상 생성)가 이 프롬프트로 바로 Kling에서 생성할 수 있다
- 키프레임 이미지 장수가 씬 수와 일치한다 (불필요한 변형 없음)

## 성장 기록
효과적이었던 프롬프트 패턴, Kling에서 잘 나오는 표현 등은 learnings/에 기록한다.
