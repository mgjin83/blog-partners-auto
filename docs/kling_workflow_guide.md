# Kling 영상 제작 워크플로우 가이드

> Ember 시즌 1 (EP 01~10) 영상 제작용
> 필요한 것: Kling 웹 구독 + 키프레임 이미지 + 이 가이드

---

## 0. 사전 준비

### 파일 위치
```
D:/Automation/characters/
├── reference_images/{캐릭터}/    ← Elements에 등록할 캐릭터 레퍼런스
├── environment_references/       ← Elements에 등록할 배경 레퍼런스
└── shot_keyframes/{ep01~10}/     ← I2V 키프레임 이미지 + kling_prompts.md
```

### Kling 계정 확인
1. https://app.klingai.com 로그인
2. 우측 상단 프로필 → 크레딧 잔량 확인
3. **구독 모델 버전 확인** (아래 참조)

### ⚠️ 버전 확인 (중요)

Kling 2.6과 3.0은 레퍼런스 시스템이 다르다. **먼저 본인 구독이 어느 버전인지 확인할 것.**

| 항목 | Kling 2.6 | Kling 3.0 |
|------|-----------|-----------|
| 레퍼런스 시스템 | **Elements** 통합 (슬롯 4개) | **Scene Reference** + **Element Reference** 분리 |
| 배경 등록 | Elements 슬롯에 배경도 등록 | Scene Reference에 배경/스타일 별도 등록 |
| 캐릭터 참조 | Elements에서 선택 | 프롬프트에서 `@element1`, `@element2`로 태깅 |
| 슬롯 수 | 4개 (캐릭터+배경 혼용) | Element 2~4개 + Scene 1개 |

**확인 방법**: Image to Video 화면에서 "Scene Reference" 탭이 보이면 3.0, "Elements" 탭만 보이면 2.6.

→ 2.6이면 [1A단계](#1a단계-elements-등록-kling-26) 따라갈 것
→ 3.0이면 [1B단계](#1b단계-scene--element-reference-등록-kling-30) 따라갈 것

---

## 1A단계: Elements 등록 (Kling 2.6)

> **핵심**: Elements는 캐릭터/오브젝트/배경을 구분하지 않는다. 하나의 Elements 기능에서 **슬롯 4개를 자유롭게 조합**하는 구조다. "배경 레퍼런스를 별도로 올리는 곳"은 없다.

### 순서

1. **app.klingai.com** → 좌측 메뉴 **"AI Videos"** 클릭
2. **"Image to Video"** 선택
3. 상단 탭에서 **"Elements"** 탭 클릭
4. **"+"** 또는 **"Upload"** 버튼 클릭

### 슬롯 4개 배분 전략

Elements 슬롯은 **씬마다 유동적으로 조합**한다:

| 씬 유형 | 슬롯 배분 | 예시 |
|---------|----------|------|
| 캐릭터 1명 + 배경 중요 | 캐릭터 2~3장 + 배경 1장 | EP01 S2 (Luna + 꽃집) |
| 캐릭터 2명 | 캐릭터A 2장 + 캐릭터B 2장 | EP01 S3 (Luna + Ash) |
| 캐릭터 2명 + 배경 | 캐릭터A 1장 + 캐릭터B 1장 + 배경 1~2장 | EP02 S4 (Luna + Duchess + 클럽) |
| 환경/소품만 | 배경 2~4장 | EP01 S1 (꽃집 외관), S6 (소품) |

### 등록할 이미지

**캐릭터 (씬에 따라 선택 등록)**
```
reference_images/luna/face_closeup.png        ← 필수 (얼굴 앵커)
reference_images/luna/fullbody_front.png      ← 전신 필요 시
reference_images/ash/face_closeup.png         ← 필수
reference_images/ash/fullbody_front.png
reference_images/duchess/face_closeup.png     ← 필수
reference_images/duchess/fullbody_front.png
reference_images/milo/face_closeup.png        ← 필수
reference_images/milo/fullbody_front.png
```

**배경 (해당 씬의 장소에 맞게 선택)**
```
environment_references/L1_flower_shop.png      ← EP01,06,09,10 꽃집
environment_references/L1_flower_shop_dark.png ← EP06,09 어두운 꽃집
environment_references/L2_duchess_club.png     ← EP02,07,10 클럽
environment_references/L3_rainy_street.png     ← EP02,03,07 비 오는 거리
environment_references/L4_park_bench.png       ← EP04,08 공원
environment_references/L5_dark_alley.png       ← EP03,05 골목
environment_references/L6_police_office.png    ← EP04,07-09 경찰서
```

### Elements 등록 팁
- 업로드 후 이미지에서 **캐릭터/배경 영역을 선택** (자동 감지됨)
- **이름 라벨** 지정: "Luna", "Ash", "Duchess", "Milo", "FlowerShop" 등
- 슬롯은 **씬마다 교체**: 생성 전에 해당 씬에 필요한 Elements로 바꿔 끼울 것
- 배경이 단색(grey)인 캐릭터 레퍼런스가 인식률 가장 높음
- 배경 레퍼런스는 사람이 없는 빈 공간 이미지가 효과적

---

## 1B단계: Scene + Element Reference 등록 (Kling 3.0)

> **핵심**: 3.0에서는 **Scene Reference**(배경/스타일 앵커)와 **Element Reference**(캐릭터/오브젝트)가 분리되어 있다. 프롬프트에서 `@element1`로 캐릭터를 참조한다.

### Scene Reference (배경/스타일)

1. Image to Video → **"Scene Reference"** 탭
2. 해당 씬의 배경 이미지 업로드
3. 이것이 영상의 **배경 톤·색감·공간감 앵커** 역할

```
씬별 Scene Reference 매핑:
EP01 S1~S5: environment_references/L1_flower_shop.png
EP01 S6:    (소품 클로즈업 — Scene Reference 불필요)
EP01 S7:    environment_references/L1_flower_shop.png (외관)
EP02 S2~S7: environment_references/L2_duchess_club.png
EP03 S1~S4: environment_references/L5_dark_alley.png
...이하 씬별 kling_prompts.md 참조
```

### Element Reference (캐릭터)

1. Image to Video → **"Element"** 탭
2. 캐릭터 이미지 2~4장 업로드 (face_closeup 필수)
3. 이름 라벨 지정
4. **프롬프트에서 `@element명`으로 참조**

```
프롬프트 예시 (3.0 방식):
@Luna stands inside a flower shop, trimming roses with scissors.
Camera slow push-in. Warm amber glow from overhead lamp.

Sound: soft snipping of scissors, quiet breathing.
Music: gentle ambient piano melody.
No dialogue.
```

### 3.0 슬롯 배분

| 참조 유형 | 슬롯 수 | 용도 |
|----------|---------|------|
| Scene Reference | 1개 | 배경/스타일 앵커 (씬마다 교체) |
| Element Reference | 2~4개 | 캐릭터 (face_closeup + fullbody) |

> 3.0에서는 배경과 캐릭터가 분리되므로 슬롯 경쟁이 없다. 2.6보다 유리.

---

## 2단계: EP01 영상 생성 (씬별)

### 기본 설정 (모든 씬 공통)

| 설정 | 값 | 이유 |
|------|-----|------|
| **모드** | Image to Video | 키프레임 이미지 기반 |
| **모델** | 구독 버전 (2.6 또는 3.0) | Native Audio 지원 |
| **품질** | Professional | 캐릭터 일관성 높음 |
| **비율** | 9:16 (세로) | YouTube Shorts 포맷 |
| **길이** | 5초 또는 10초 | 씬별 다름 (아래 참조) |
| **Native Audio** | ON | 대사+음악+효과음 동시 생성 |

---

### EP01 씬별 Elements 조합 가이드

| 씬 | 키프레임 | Elements (2.6) / Element+Scene (3.0) | 길이 |
|----|---------|--------------------------------------|------|
| **S1** Hook | ep01_s1_hook.png | 2.6: L1_flower_shop ×1 / 3.0: Scene=L1_flower_shop, Element=없음 | 5초 |
| **S2** Luna Routine | ep01_s2_luna_routine.png | 2.6: Luna ×2 + L1_flower_shop ×1 / 3.0: Scene=L1_flower_shop, Element=Luna | 5초 |
| **S3** Ash Enters ⭐ | ep01_s3_ash_enters.png | 2.6: Luna ×2 + Ash ×2 / 3.0: Scene=L1_flower_shop, Element=Luna+Ash | 5초 |
| **S4** Confession | ep01_s4_confession.png | 2.6: Luna ×2 + Ash ×2 / 3.0: Scene=L1_flower_shop, Element=Luna+Ash | 10초 |
| **S5** Determination | ep01_s5_determination.png | 2.6: Luna ×3 + L1_flower_shop ×1 / 3.0: Scene=L1_flower_shop, Element=Luna | 5초 |
| **S6** Flower Blood | ep01_s6_flower_blood.png | 2.6: 없음 / 3.0: 없음 (소품 클로즈업) | 5초 |
| **S7** End | ep01_s7_end.png | 2.6: L1_flower_shop ×1 / 3.0: Scene=L1_flower_shop, Element=없음 | 5초 |

### 씬별 프롬프트

> 각 에피소드의 상세 프롬프트는 `shot_keyframes/{ep번호}/kling_prompts.md` 참조.
> 아래는 EP01 S3 (VIRAL CLIP) 예시:

**① Frames 탭**
- Start Frame: `shot_keyframes/ep01/ep01_s3_ash_enters.png` 업로드

**② Elements 탭 (2.6)** 또는 **Element + Scene (3.0)**
- 2.6: Luna(face_closeup + fullbody) + Ash(face_closeup + fullbody) → 슬롯 4개 사용
- 3.0: Scene=L1_flower_shop, Element=@Luna + @Ash

**③ 프롬프트 입력**
```
A grey tabby cat-face figure stumbles through the flower shop door.
Torn clothes, blood on face. Cold air rushes in, disturbing flower petals.
The calico cat-face figure in apron turns sharply toward the door with shock.
Camera holds static. Warm amber atmosphere disrupted by cold draft.

Sound: door slams open loudly, cold wind rushing in, flower petals rustling, heavy labored breathing.
[Ash, weak breathless male voice]: "Luna..."
Music cuts abruptly to silence. Only breathing remains.
```

> **3.0 프롬프트 변형**: 캐릭터 설명 대신 `@Ash stumbles through the flower shop door...` `@Luna turns sharply...` 형태로 태깅

**④ 설정**: 5초, 9:16, Professional, Native Audio ON
**⑤ Generate 클릭**

---

## 3단계: 결과물 검수 (QA)

생성된 각 클립을 아래 기준으로 확인:

| # | 체크 항목 | 통과 기준 |
|---|----------|----------|
| 1 | 캐릭터 얼굴 | 묘종, 눈 색, 무늬가 레퍼런스와 일치 |
| 2 | 조명 방향 | 씬 내에서 일관적, 광원 모순 없음 |
| 3 | 모핑/플리커 | 얼굴 왜곡, 여분 팔다리 없음 |
| 4 | 색감 | EP01 = amber → shadow (style_guide.md 참조) |
| 5 | 카메라 | 부드럽고 자연스러움, 급격한 떨림 없음 |
| 6 | 음성 | 대사가 자연스럽고 캐릭터에 맞음 |
| 7 | 배경음 | 무드와 일치, 너무 시끄럽지 않음 |
| 8 | 배경 일관성 | Elements/Scene Reference로 등록한 배경과 일치 |

**불만족 시**: 같은 프롬프트로 재생성 (시드 변경) 또는 프롬프트 조정 후 재시도

---

## 4단계: 에피소드 조립

7개 클립을 하나로 이어붙이는 방법:

### 방법 A: CapCut / 편집 앱 (권장)
1. 7개 MP4 다운로드
2. CapCut (무료) 또는 DaVinci Resolve에서 순서대로 배치
3. 자막 추가 (대사 부분)
4. 전체 러닝타임 40~50초 확인
5. 9:16 포맷으로 Export

### 방법 B: FFmpeg (자동화)
```bash
# 클립 목록 파일 생성
echo "file 's1_hook.mp4'" > list.txt
echo "file 's2_routine.mp4'" >> list.txt
echo "file 's3_ash_enters.mp4'" >> list.txt
echo "file 's4_confession.mp4'" >> list.txt
echo "file 's5_determination.mp4'" >> list.txt
echo "file 's6_flower_blood.mp4'" >> list.txt
echo "file 's7_end.mp4'" >> list.txt

# 이어붙이기
ffmpeg -f concat -safe 0 -i list.txt -c copy ep01_the_debt.mp4
```

---

## 프롬프트 작성 규칙 요약

### 비주얼 파트
```
[샷 타입] of [피사체].
[동작: 동사 하나].
[환경]. Camera: [카메라 움직임 하나].
[조명]. [무드 2~3단어].
```

### 오디오 파트 (Native Audio)
```
Sound: [환경음, 효과음 설명].
[캐릭터명, 음성 특징]: "대사 내용"
Music: [음악 스타일, 악기, 무드].
```

### 대사 포맷 규칙
- 반드시 `[이름, 음성설명]: "대사"` 형식
- 소문자 사용 (고유명사/약어 제외)
- 캐릭터 이름 반복 (대명사 사용 금지)
- 대사와 동작을 연결: `[Ash] stumbles forward. [Ash, weak voice]: "Luna..."`
- 침묵/반응도 명시: `[Ash] shakes his head. Silence.`
- **3.0 전용**: 캐릭터 설명 대신 `@element명` 태깅 가능

### 금지 사항 (Negative)
- 동시에 카메라 움직임 2개 이상 지시 금지
- 한 프레임에 캐릭터 3명 이상 금지
- 밝은 색감, 카툰, 애니메 스타일 금지
- "no ~" 형태 금지 → 원하지 않는 것을 직접 기술

---

## 크레딧 예상 (EP01 기준)

| 씬 | 길이 | 모드 | 예상 크레딧 |
|----|------|------|-----------|
| S1 Hook | 5s | Professional | ~10 |
| S2 Routine | 5s | Professional | ~10 |
| S3 Ash Enters | 5s | Professional | ~10 |
| S4 Confession | 10s | Professional | ~20 |
| S5 Determination | 5s | Professional | ~10 |
| S6 Flower Blood | 5s | Professional | ~10 |
| S7 End | 5s | Professional | ~10 |
| **EP01 합계** | **40s** | | **~80 크레딧** |

> 재생성 고려 시 EP당 약 100~150 크레딧 예상.
> 시즌 1 전체 (10편) = 약 1,000~1,500 크레딧.
> 구독 플랜의 월 크레딧 잔량 확인 필요.

---

## 빠른 체크리스트

- [ ] Kling 로그인 + 크레딧 확인
- [ ] **버전 확인**: 2.6 (Elements 통합) vs 3.0 (Scene + Element 분리)
- [ ] 2.6 → 1A단계 / 3.0 → 1B단계 따라 레퍼런스 등록
- [ ] EP01 S3 (VIRAL CLIP) 먼저 테스트 생성
- [ ] 결과 확인 → 만족 시 나머지 씬 진행
- [ ] 7개 클립 다운로드 → 조립 → EP01 완성
