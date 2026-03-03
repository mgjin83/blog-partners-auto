# Kling 3.0 영상 제작 워크플로우

> Ember 시즌 1 (EP 01~10) 영상 제작 가이드
> Kling 3.0 멀티샷 + Native Audio 기준

---

## 1. 사전 준비

### 필요한 파일

```
D:/Automation/characters/
├── reference_images/{캐릭터}/    ← Element에 등록할 캐릭터 이미지
├── environment_references/       ← Scene Reference로 사용할 배경 이미지
└── shot_keyframes/{ep01~10}/     ← 멀티샷 키프레임 이미지 + kling_prompts.md
```

### Kling 접속

1. https://app.klingai.com 로그인
2. 우측 상단 프로필 → 크레딧 잔량 확인
3. 좌측 메뉴 **AI Videos** → **Image to Video** → **Multi-Shot** 선택

---

## 2. 레퍼런스 등록

Kling 3.0은 **Scene Reference**와 **Element Reference** 두 가지로 나뉜다.

### Scene Reference = 배경

씬의 배경·톤·색감을 잡아주는 앵커 이미지. **그룹마다 1장** 등록한다.

**등록 방법**: Multi-Shot 화면 → **Scene Reference** 탭 → 이미지 업로드

**배경 이미지 목록**:

| 파일명 | 장소 | 사용 에피소드 |
|--------|------|-------------|
| `L1_flower_shop.png` | 꽃집 (밝은 버전) | EP01, 03, 10 |
| `L1_flower_shop_dark.png` | 꽃집 (어두운 버전) | EP06, 09 |
| `L2_duchess_club.png` | Duchess 클럽 | EP02, 07, 10 |
| `L3_rainy_street.png` | 비 오는 거리 | EP02, 03, 07 |
| `L4_park_bench.png` | 공원 벤치 | EP04, 08 |
| `L5_dark_alley.png` | 어두운 골목 | EP03, 05 |
| `L6_police_office.png` | 경찰서 | EP04, 07~09 |

### Element Reference = 캐릭터

캐릭터 얼굴·체형을 고정하는 레퍼런스. 프롬프트에서 **`@이름`으로 호출**한다.

**등록 방법**: Multi-Shot 화면 → **Element** 탭 → 이미지 업로드 → 이름 지정

**캐릭터별 등록할 이미지** (인물당 필수 1장, 최대 3장):

| 캐릭터 | 필수 (얼굴 앵커) | 선택 |
|--------|-----------------|------|
| Luna | `reference_images/luna/face_closeup.png` | `fullbody_front.png`, `angle_three_quarter.png` |
| Ash | `reference_images/ash/face_closeup.png` | `fullbody_front.png`, `angle_three_quarter.png` |
| Duchess | `reference_images/duchess/face_closeup.png` | `fullbody_front.png`, `angle_three_quarter.png` |
| Milo | `reference_images/milo/face_closeup.png` | `fullbody_front.png`, `angle_three_quarter.png` |

**등록 팁**:
- `face_closeup.png` 1장은 반드시 등록 (얼굴 일관성의 핵심)
- 필요 시 전신/앵글 추가 (최대 3장까지)
- 배경이 단색(grey)인 이미지가 인식률 가장 높음
- 이름 라벨은 영어로 정확히: "Luna", "Ash", "Duchess", "Milo"

---

## 3. 멀티샷 영상 생성

### 멀티샷이란?

여러 샷(씬)을 하나의 그룹으로 묶어 **연속된 영상**으로 생성하는 기능.
- 그룹 내 샷들은 동일한 Scene/Element 레퍼런스를 공유
- 캐릭터 외형, 조명, 분위기가 샷 간에 자연스럽게 이어짐
- **각 샷**: 3~15초 / **그룹 합계**: 최대 15초

### 공통 설정

| 설정 | 값 |
|------|-----|
| 모드 | Image to Video → **Multi-Shot** |
| 품질 | Professional |
| 비율 | 9:16 (세로) |
| Native Audio | **ON** |

### 커스텀 멀티샷 생성 순서

```
① Image to Video → Multi-Shot 모드 선택
② Scene Reference 설정         (그룹 전체에 적용될 배경)
③ Element 설정                 (그룹 전체에 적용될 캐릭터)
④ 키프레임 이미지 업로드        (그룹의 시작 프레임)
⑤ 프롬프트 입력                (그룹 전체를 하나의 연속 프롬프트로)
⑥ 하단 총 길이 설정             (그룹 합계와 정확히 일치시킨다)
⑦ Generate 클릭
```

**주의**: 하단 설정의 총 길이를 그룹 합계와 반드시 일치시켜야 한다. 불일치 시 생성 실패하거나 잘림.

### EP01 멀티샷 구성

에피소드 1편 = **3개 그룹** (10초 + 15초 + 15초 = 40초)

| 그룹 | 씬 구성 | Scene | Element | 총 길이 |
|------|---------|-------|---------|--------|
| **그룹 1** 평화로운 일상 | S1 Hook (5초) + S2 Routine (5초) | L1_flower_shop | Luna | 10초 |
| **그룹 2** 침입과 고백 ⭐ | S3 Ash Enters (5초) + S4 Confession (10초) | L1_flower_shop | Luna + Ash | 15초 |
| **그룹 3** 결심과 여운 | S5 Determination (5초) + S6 Flower (5초) + S7 End (5초) | L1_flower_shop | Luna | 15초 |

> 그룹별 상세 프롬프트: `shot_keyframes/ep01/kling_prompts.md` 참조

### 그룹 묶기 기준

- **같은 장소 + 같은 캐릭터 조합**이면 하나의 그룹으로 묶는다
- 캐릭터가 바뀌면 그룹을 나눈다 (Element가 달라지므로)
- 그룹 합계 15초를 초과하면 나눈다

---

## 4. 결과물 검수 (QA)

생성된 클립을 아래 항목으로 확인:

| # | 체크 항목 | 통과 기준 |
|---|----------|----------|
| 1 | 캐릭터 얼굴 | 머리색, 눈 색, 얼굴 특징이 레퍼런스와 일치 |
| 2 | 샷 간 연속성 | 그룹 내 샷 전환이 자연스러움 |
| 3 | 모핑/플리커 | 얼굴 왜곡, 여분 팔다리 없음 |
| 4 | 색감 | EP별 무드와 일치 |
| 5 | 카메라 | 부드럽고 자연스러움 |
| 6 | 음성 | 대사가 자연스럽고 캐릭터에 맞음 |
| 7 | 효과음 | SFX가 장면과 일치 |
| 8 | 배경 | Scene Reference와 일치 |

**불만족 시**: 해당 그룹만 재생성 (다른 그룹에 영향 없음).

---

## 5. 에피소드 조립

멀티샷 그룹 클립들을 이어붙여 최종 에피소드를 완성한다.

### 편집 작업

1. 그룹 클립 3개 다운로드 (MP4)
2. CapCut 또는 DaVinci Resolve에서 순서대로 배치
3. **BGM 추가**: 에피소드 전체에 걸치는 배경음악 1트랙 (Suno/Udio 등으로 생성)
4. **자막 추가** (대사 부분)
5. **컬러 그레이딩**: 느와르 톤 적용 (LUT 또는 수동 보정)
6. 전체 길이 40~50초 확인
7. 9:16 세로 포맷으로 Export

### FFmpeg (간단 이어붙이기)

```bash
cat > list.txt <<EOF
file 'ep01_group1.mp4'
file 'ep01_group2.mp4'
file 'ep01_group3.mp4'
EOF

ffmpeg -f concat -safe 0 -i list.txt -c copy ep01_raw.mp4
```

> 이어붙이기 후 편집 앱에서 BGM + 자막 + 컬러 그레이딩 작업.

---

## 프롬프트 작성 규칙

### 프롬프트 구조 (이 순서대로 작성)

```
1. 샷 타입 + 카메라 위치       "Medium shot, camera at left wall, shooting right."
2. 캐릭터 위치 (프레임 내)      "@Luna stands right side of frame."
3. 신체 방향                   "body facing right, head tilted down."
4. 구체적 동작 (동사+방향+대상)  "@Luna holds scissors in right hand, cuts stem."
5. 시선 방향                   "@Luna looks down at rose in left hand."
6. 카메라 동작                  "Camera: slow dolly forward over 10 seconds."
7. 조명 방향                   "Lighting: warm amber overhead lamp. Cold blue from open door."
8. 사운드 + 대사 (별도 블록)
```

### 오디오

```
Sound: [구체적 물리 소리: scissors cutting, door slam, knees hitting floor].
[캐릭터명, 음성 특징, 신체 상태]: "대사"
```

> **Music 프롬프트는 넣지 않는다.** BGM은 편집 단계에서 별도 적용.

### 핵심 규칙
- 캐릭터는 `@이름`으로 호출 (Element에 등록한 이름과 일치)
- 대사 포맷: `[이름, 음성설명]: "대사"` (영어)
- 대명사(he, she) 금지 → 항상 `@이름` 사용
- 한 프레임에 캐릭터 **최대 2명**
- 시간이 긴 클립은 **초 단위 구간**으로 나눠서 지시 (0-3초, 3-8초, 8-15초)

### 필수 명시 항목
- **표정**: 모든 캐릭터에 얼굴 근육 상태를 명시. 감정 단어 대신 물리 묘사 사용
  - 고통: "eyes squinted, mouth open gasping, face grimacing"
  - 충격: "eyes wide open, eyebrows raised high, mouth drops open"
  - 걱정: "brow furrowed tight, lips pressed together, eyes scanning rapidly"
  - 탈진: "eyes half-closed, brow wrinkled, chin trembling"
  - 수치: "eyes squeezed shut, brow creased, mouth pulled down"
  - 분노: "nostrils flare, eyebrows pinched, jaw thrust forward"
  - 결심: "eyes narrow, jaw clenches, lips press into thin hard line"
  - 평온: "lips closed with slight smile, eyes soft and half-lidded"
- **시선**: 모든 캐릭터에 "looks at [구체적 대상]" 명시. 카메라 응시 금지
- **신체 방향**: "body facing left", "back toward camera", "kneels on floor"
- **손 동작**: "grabs shoulders with both hands", "holds phone in right hand"
- **프레임 내 위치**: "left side of frame", "center frame", "background right"

### 금지 표현 → 대체

| 쓰지 않는다 | 대신 쓴다 |
|------------|----------|
| peaceful atmosphere | (삭제. 조명과 동작으로 표현) |
| expression shifts to determination | eyebrows lower, jaw clenches |
| shadow falls across her eyes | lighting: warm amber from left side only |
| cold draft disrupts atmosphere | wind gust from open door, petals scatter on floor |
| intimate close-up | faces 30cm apart, camera at side angle |
| haunting, fragile, ominous | (삭제. 분위기 형용사 사용 금지) |

---

## 크레딧 예상

| 그룹 길이 | Professional 모드 |
|----------|-----------------|
| 10초 | ~20 크레딧 |
| 15초 | ~30 크레딧 |

- EP01 (3그룹, 40초) ≈ **80 크레딧** (1회 생성 기준)
- 재생성 포함 시 EP당 약 100~150 크레딧
- **시즌 1 전체** (10편) ≈ 1,000~1,500 크레딧

---

## 체크리스트

- [ ] Kling 로그인 + 크레딧 확인
- [ ] Scene Reference에 배경 이미지 등록
- [ ] Element에 캐릭터 등록 (face_closeup 필수, 인물당 최대 3장)
- [ ] EP01 그룹 2 (VIRAL CLIP) 먼저 테스트 생성
- [ ] QA 통과 확인 → 그룹 1, 3 진행
- [ ] 3개 그룹 다운로드 → 편집 (이어붙이기 + BGM + 자막 + 컬러 그레이딩)
- [ ] EP01 완성 → EP02~10 반복

---

## 진행 순서 요약

```
1. Element에 캐릭터 등록
2. EP01 그룹 2 테스트 → QA
3. 만족하면 그룹 1, 3 생성
4. 3개 그룹 편집: 이어붙이기 + BGM + 자막 + 컬러 그레이딩
5. EP01 완성
6. EP02~10 반복
```
