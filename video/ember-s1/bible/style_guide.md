# Style Guide — Ember

> 참조: bible/series_bible.md Section 3 (World-Building) + Section 9 (Production Constraints)
> 소비자: 비주얼팀 (캐릭터 디자이너, 씬 디자이너) + 영상팀 (영상 생성, 편집)
> 이 문서는 "어떻게 보여주는가"의 원본이다. 모든 Kling 프롬프트는 이 문서의 규칙을 따른다.

---

## Section 1: 프롬프트 마스터 포맷

### 표준 구조

모든 프롬프트는 이 순서를 따른다:

```
[샷 타입] of [캐릭터/피사체], [동작: 동사 하나],
[환경: 장소 + 시간 + 날씨], camera: [카메라 움직임 하나],
[조명: 광원 + 방향 + 질감], [무드: 2~3 단어],
[Style Lock]
```

### 규칙

- **30~60단어.** 이 범위를 지킨다. 짧고 구조적인 프롬프트가 길고 모호한 프롬프트를 이긴다
- **`++핵심 요소++`** 구문으로 가장 중요한 피사체를 강조한다
- 클립 내 시간 진행이 필요하면 `"initially... then... finally"` 로 지시한다
- `"focus on"` 또는 `"centered on"` 으로 시선을 유도한다
- 전경/중경/배경을 분리 기술하면 깊이감이 살아난다

### Style Lock (모든 프롬프트 끝에 고정)

**이미지 생성용** (Gemini — 캐릭터 레퍼런스, 키프레임):
```
cinematic, shallow depth of field, natural rich colors,
soft directional lighting, anamorphic lens, photorealistic
```
> 이미지는 컬러풀하게 생성한다. 느와르 명암/컬러 보정은 영상 편집 단계에서 적용.

**영상 프롬프트용** (Kling I2V):
```
cinematic, shallow depth of field, film noir aesthetic,
high contrast, dramatic lighting, anamorphic lens,
professional color grading
```

이 어휘는 바꿔 쓰지 않는다. `"film noir aesthetic"`을 `"dark detective mood"`로 의역하면 일관성이 깨진다.

### 표준 네거티브 프롬프트 (모든 생성에 사용)

```
blur, distortion, watermark, text overlay, low quality, flickering,
morphing faces, extra limbs, cartoon, anime, pixar,
smiling, plastic look, CGI artifacts, inconsistent lighting
```

네거티브 프롬프트에서는 원하지 않는 것을 직접 기술한다. `"no robots"` 가 아니라 `"robots"`.

### 컬러 파이프라인

```
[이미지 생성] 컬러풀하게 생성 → [영상 편집] 느와르 명암·컬러 보정 적용
```
- 이미지 생성 단계에서는 desaturate/low-key 금지. 자연스러운 컬러 유지
- 느와르 톤은 CapCut/DaVinci 등 편집 단계에서 LUT·컬러 그레이딩으로 적용

### 프롬프트 예시

**EP 01 — 꽃집에 애쉬가 들어오는 장면:**
```
Medium shot of ++a young woman with auburn hair in a florist apron++,
turning toward the door as a tall man with dark brown hair stumbles in,
small flower shop interior at night, warm amber lighting from
overhead lamp, camera holds static, shock and fear on face,
cinematic, shallow depth of field, film noir aesthetic,
desaturated color palette, high contrast, low-key lighting,
anamorphic lens, professional color grading
```

---

## Section 2: 색감·조명 팔레트

### 장소별 프롬프트 키워드

| 장소 | 색감 팔레트 | 조명 키워드 | 분위기 키워드 |
|------|-----------|-----------|-------------|
| L1: 루나의 꽃집 | amber, green, warm tones | warm practical lamp light, amber glow, tungsten warmth | intimate, safe, melancholic when dark |
| L2: 더체스의 클럽 | blue, purple, cold neon | neon signs casting blue reflections, cold backlight | dangerous, elegant, predatory |
| L3: 비 오는 거리 | orange sodium, grey | rain-soaked, wet pavement reflections, single streetlight | lonely, transitional, tense |
| L4: 공원 벤치 | faded green, warm daylight | soft natural light, dappled shadows through leaves | peaceful (낮), hollow (밤) |
| L5: 어두운 골목 | darkness, distant neon glow | minimal light, distant neon reflections on wet brick | claustrophobic, secretive |

### 분위기 규칙 → 프롬프트 적용

| 서사 규칙 (series_bible Section 3) | 프롬프트 적용 |
|---|---|
| 꽃집이 밝을 때 = 루나가 자기 자신에 가깝다 | `warm amber lighting, flowers in full bloom, soft focus` |
| 꽃집이 어두울 때 = 루나가 자신을 잃어가고 있다 | `dim lighting, shadows across flowers, cold undertones creeping in` |
| 비 = 전환의 신호 | `rain falling heavily, rain streaks visible against backlight, wet surfaces` |
| 네온 = 더체스의 세계 | `neon signs casting [blue/purple] reflections, cold artificial light` |
| 자연광 = 과거/순수 | `soft natural daylight, warm golden tones, lens flare` |

### 에피소드별 지배적 무드

| EP | 지배적 장소 | 지배적 색감 | 감정 온도 |
|----|-----------|-----------|----------|
| 01 | 꽃집 (밝음→어두움) | amber → shadow | 따뜻함이 깨지는 순간 |
| 02 | 비 오는 거리 → 클럽 | grey → cold blue | 차가운 세계로 진입 |
| 03 | 골목 → 가로등 아래 | darkness → lonely orange | 고독한 공범 |
| 04 | 거리 (낮, 흐림) → 사무실 | overcast grey | 균열 |
| 05 | 실내 (어둡고 좁음) → 골목 | darkness, distant neon | 가해자의 탄생 |
| 06 | 꽃집 (밤, 조명 없음) | near-black, moonlight only | 진실의 무게 |
| 07 | 클럽 → 비 오는 거리 | cold blue → grey rain | 탈출 불가 |
| 08 | 공원 (오후) | warm daylight + shade | 빛과 그늘의 이별 |
| 09 | 꽃집 (낮, 블라인드 닫힘) | slivers of light | 갇힌 대면 |
| 10 | 클럽 → 꽃집 (따뜻하지만 텅 빔) | cold blue → empty amber | 자유의 고독 |

### 분위기 키워드 뱅크

**비:**
`rain-soaked`, `rain streaks visible against backlight`, `wet pavement reflections`, `rain pattering against fogged window`, `splashes of water`, `rain-slicked streets`

**네온:**
`neon signs casting [색상] reflections`, `neon bokeh`, `neon reflections in puddles`, `backlit by neon`, `flickering neon`, `neon light pulsing [색상]`

**따뜻한 조명:**
`warm practical lamp light`, `amber glow`, `warm golden tones`, `tungsten warmth`, `candlelight flicker`, `warm side lighting from [방향]`

**안개/연기:**
`light fog at ground level`, `smoke wisps curling`, `volumetric fog`, `haze diffusing light`, `atmospheric mist`

**그림자:**
`deep shadows`, `chiaroscuro lighting`, `venetian blind shadows`, `face partially in shadow`, `silhouette against [광원]`, `high contrast shadow play`

---

## Section 3: 캐릭터 비주얼 규칙

### 공통 규칙

- **매력적 외형 원칙**: 모든 캐릭터는 시청자의 시선을 끄는 매력적인 외형으로 디자인한다. 주인공과 주요 조연은 미남/미녀 기반으로 설계하되, 캐릭터 성격에 맞는 개성을 부여한다. 실사 기반의 조형미와 균형감을 갖춰야 하며, 눈빛·표정·조명에서 오는 매력이 캐릭터 인지도와 팬덤 형성의 핵심이다.
- 모든 캐릭터는 서양인 인간. 외형 핵심 특징(머리색, 눈 색, 얼굴 특징)을 매 프롬프트에 반복한다
- 의복은 현대 일상복. 캐릭터 성격을 반영한다
- 표정 연기가 핵심이므로 얼굴 클로즈업 비중을 높인다
- 한 프레임에 캐릭터 1~2명까지. 3명 이상 시 왜곡 위험

### 캐릭터별 매력 방향

| 캐릭터 | 매력 키워드 | 프롬프트 반영 |
|--------|-----------|-------------|
| LUNA | 날카로우면서 여린 아름다움 | `beautiful young woman`, `auburn hair`, `green eyes`, `delicate features with freckles` |
| ASH | 거칠지만 부드러운 인상 | `handsome rugged man`, `dark brown messy hair`, `hazel eyes`, `stubble`, `strong gentle presence` |
| DUCHESS | 압도적 우아함과 위엄 | `stunningly beautiful woman`, `platinum blonde hair`, `ice blue eyes`, `sharp cheekbones`, `commanding presence` |
| MILO | 따뜻하고 신뢰감 있는 외형 | `warm handsome man`, `sandy blonde hair`, `brown eyes`, `clean-cut`, `trustworthy appearance` |

### 캐릭터별 프롬프트 핵심 (상세는 character_sheets/에서 관리)

| 캐릭터 | 외형 키워드 | 눈 색 | 체형 | 기본 의상 |
|--------|-----------|-------|------|----------|
| LUNA | young woman, auburn hair, light freckles, delicate features | green eyes | slender build | florist apron (꽃집) / dark coat (밤 외출) |
| ASH | young man, dark brown messy hair, stubble, strong jaw | hazel eyes | tall broad-shouldered build | casual clothes / torn clothes (EP 01) |
| DUCHESS | woman in her 40s, platinum blonde sleek hair, sharp cheekbones, porcelain skin | ice blue eyes | tall elegant build | luxurious dark clothing, jewelry |
| MILO | young man, sandy blonde short hair, clean-shaven, warm features | warm brown eyes | athletic build | police uniform (근무) / casual (비번) |

### Character DNA 템플릿

캐릭터 디자이너는 각 캐릭터에 대해 아래 항목을 확정한다:

```
# [캐릭터명] — Character DNA

## 얼굴 앵커
- 머리색/스타일:
- 눈 색:
- 눈 형태:
- 피부:
- 얼굴 특징:
- 구별 포인트 (흉터, 주근깨 등):

## 체형·실루엣
- 체형:
- 키 (상대적):
- 자세/걸음걸이 특징:

## 시그니처 소품
- (예: 루나의 앞치마, 더체스의 보석)

## 기본 의상
- 상황 1:
- 상황 2:
- (의상 변경 시 별도 팩 필요)

## 스타일 락
- 기본: film noir realistic with subtle stylization
- 절대 아님: anime, cartoon, pixar, bright/cheerful

## DO NOT ALLOW
- (예: 웃는 표정 — 더체스 한정, 밝은 색 의상 — 루나 한정)
```

### Character Pack 구성 요건

캐릭터 디자이너가 생성·관리하는 레퍼런스 이미지 세트:

| 항목 | 수량 | 용도 |
|------|------|------|
| 전신 (정면, 3/4, 측면, 후면) | 4장 | 체형·실루엣·의상 기준 |
| 얼굴 클로즈업 (무표정) | 1장 | 얼굴 기준 |
| 표정 시트 | 6종 | 결심, 공포, 분노, 슬픔, 체념, 냉정 |
| 액션 포즈 | 3장+ | 걷기, 돌아보기, 기대기 등 |
| 의상별 추가 | 의상당 4장 | 의상 변경 시 별도 앵커 |

---

## Section 4: 샷 구성 가이드

### 에피소드 = 4개 구간 + 7~8개 클립

40~50초 에피소드를 4개 구간으로 나누고, 5~10초 클립으로 조립한다:

| 구간 | 시간 | 샷 타입 | 서사 기능 | 텍스트 |
|------|------|---------|----------|--------|
| **THUMB-STOP** | 0:00~0:02 | **CU 또는 Medium 전용** (Wide/Establishing 금지) | 엄지 멈춤. 감정이 강한 표정/충격적 상황/긴장된 신체 언어 | HOOK TEXT 필수 |
| **CONTEXT** | 0:02~0:08 | Medium / CU | 상황 파악. "무슨 일이 벌어지고 있는가" | NARRATIVE TEXT 가능 |
| **ESCALATION** | 0:08~0:38 | Mixed (매 10초 비주얼 변화 필수) | 관계 변화 + 전환 1회 | DIALOGUE SUB |
| **UNRESOLVED END** | 마지막 5~7초 | 상황에 따라 | 해결되지 않은 긴장. "끝나지 않았다" | 다음 화 유도 가능 |

**세그먼트 기본형 (ESCALATION 구간 내):**

| # | 세그먼트 | 길이 | 샷 타입 | 서사 기능 |
|---|---------|------|---------|----------|
| 1 | 감정 비트 | 5s | Close-up | 표정, 반응, 디테일 |
| 2 | 상호작용 | 5s | Medium two-shot 또는 OTS | 대화, 대면, 긴장 |
| 3 | 상대 반응 | 5s | Close-up | 상대 캐릭터의 감정 |
| 4 | 핵심 순간 | 5~10s | Medium | 전환, 결정, 드라마틱 액션 |

이 구조는 기본형이다. 에피소드 서사에 따라 세그먼트 수와 순서를 조정한다.

### 샷 타입별 용도

| 샷 타입 | 프롬프트 키워드 | 용도 | Kling 안정성 |
|---------|---------------|------|-------------|
| Wide/Establishing | `wide shot`, `establishing shot` | 장소·분위기 설정 | 높음 |
| Medium | `medium shot`, `waist-up` | 캐릭터+맥락, 대화 | 높음 (1명 기준) |
| Close-up | `close-up`, `tight shot` | 감정, 반응 | 보통 (얼굴 아티팩트 주의) |
| Extreme Close-up | `extreme close-up`, `macro` | 소품, 극적 강조 (손, 편지, 꽃잎) | 높음 |
| Over-the-shoulder | `over-the-shoulder shot` | 대화 시점, 전환 샷 | 보통 |

### 카메라 움직임

| 움직임 | 프롬프트 키워드 | 안전도 | 용도 |
|--------|---------------|--------|------|
| 정지 | `camera holds static` | 가장 안전 | 대화, 긴장, 강조. 기본값 |
| 느린 전진 | `slow push-in`, `slow dolly forward` | 안전 | 감정 드러남, 친밀감 |
| 느린 후퇴 | `camera slowly pulls back` | 안전 | 리빌, 고립감, 엔딩 |
| 트래킹 | `camera tracks alongside` | 보통 | 피사체 이동 따라감 |
| 팬 | `slow pan from left to right` | 보통 | 환경 훑기 |
| 로우앵글 | `low-angle shot` | 안전 | 위압감, 권력 (더체스 장면) |
| 하이앵글 | `high-angle shot` | 안전 | 취약함, 감시 (루나 장면) |

**핵심 규칙: 샷당 카메라 움직임은 1개.** 줌 + 팬 + 트래킹을 동시에 지시하면 아티팩트가 발생한다.

### 전환 샷 (이음새 숨기기)

캐릭터가 바뀌는 세그먼트 사이에 전환 샷을 넣으면 생성 이음새가 자연스럽다:
- 소품 클로즈업 (꽃, 봉투, 전화기, 빗방울)
- 실루엣 (얼굴 없이 몸의 윤곽만)
- 환경 디테일 (가로등, 네온 반사, 젖은 바닥)
- 오버숄더 (뒷모습에서 상대 얼굴로)

이 샷들은 시청자의 시각적 "리셋"을 제공한다. 캐릭터 렌더링 불일치가 눈에 덜 띈다.

---

## Section 5: Image-to-Video 워크플로우

### 기본 원칙

텍스트만으로 생성하지 않는다. **Image-to-Video가 기본 파이프라인이다.**
실사 기반 캐릭터이므로, 텍스트 프롬프트만으로는 에피소드 간 일관성이 유지되지 않는다.

### 4단계 파이프라인

```
[1단계] Character DNA (문서)
    ↓ 캐릭터 디자이너가 작성
[2단계] Character Pack (레퍼런스 이미지 세트)
    ↓ 캐릭터 디자이너가 생성
[3단계] Shot Keyframe (정지 이미지)
    ↓ 씬 디자이너가 레퍼런스 + 환경을 조합하여 생성
[4단계] Animation (Image-to-Video)
    ↓ 영상팀이 키프레임에 동작을 부여
```

### 단계별 규칙

**2단계 (Character Pack 생성):**
- Character DNA의 모든 앵커를 프롬프트에 포함
- 이미지 생성용 스타일 락과 네거티브 프롬프트를 사용
- 배경은 단색(`plain grey background`)으로 캐릭터만 분리
- Kling Element 등록에 필요한 최소 이미지만 생성: face_closeup (필수 1장) + fullbody_front (선택 1장) = 캐릭터당 1~2장
- 표정 시트, 앵글 시트, 액션 포즈 등 추가 에셋은 영상 제작 중 필요해진 시점에만 생성

**3단계 (Shot Keyframe 생성):**
- Character Pack 이미지를 Element Reference로 업로드
- 환경 레퍼런스는 Scene Reference로 별도 업로드
- 프롬프트에서 `@캐릭터명`으로 참조. 캐릭터 외형은 Element가 결정
- 결과물이 만족스러우면 이 이미지가 4단계의 입력이 된다

**4단계 (Animation):**
- 키프레임 이미지를 입력으로 사용
- 프롬프트는 **동작과 카메라만** 기술한다:
  ```
  Subtle motion. [동사 하나: turns head / reaches for envelope / stands up].
  Camera: [카메라 움직임 하나]. Style: maintain visual style, no flicker.
  ```
- 캐릭터 외형을 텍스트로 다시 묘사하지 않는다. 이미지가 결정한다
- 클립 길이: 5~10초

### Reference 활용 (Kling 3.0)

- **Scene Reference**: 배경/스타일 앵커 이미지 1장 → 씬의 톤·색감·공간감 고정
- **Element Reference**: 캐릭터 레퍼런스 2~4장 업로드 → 시각적 정체성 추출·유지
- 프롬프트에서 `@캐릭터명`으로 호출하면 Element가 자동 적용
- 복수 Element 조합 시 각각의 특징이 교차 오염 없이 유지됨

### 시드 값

동일 캐릭터의 연속 생성 시, 이전 생성의 시드 값을 재사용하면 정체성 일관성이 강화된다.

---

## Section 6: 제한 사항 → 대안 경로

| 제한 사항 | 대안 경로 |
|-----------|----------|
| 빠른 카메라 복합 움직임 시 아티팩트 | 샷당 카메라 움직임 1개. 복합 움직임은 2개 샷으로 분리 |
| 상충 조명 (실외 자연광 + 실내 스튜디오) 혼란 | 샷당 조명 환경 1개로 통일 |
| 3명 이상 캐릭터 동시 렌더 왜곡 | 1~2명 중심 촬영. 3번째 인물은 다음 샷 또는 음성으로 존재감 부여 |
| 복잡한 물리 동작 (달리기, 격투) 왜곡 | 감정은 표정 클로즈업으로. 물리 동작은 실루엣/미디엄 샷으로 디테일 회피 |
| 텍스트 렌더링 불안정 | 영상 내 텍스트는 후반 자막 레이어로 처리 |
| 애니메/카툰 스타일 불안정 | 실사 느와르 베이스 유지. Image-to-Video로 스타일 고정 |
| 눈/손 플리커 | 표정 장면에서 생성 후 QA. 문제 프레임 발견 시 재생성 |
| 클립 최대 5~15초 | 에피소드 = 7~8개 세그먼트로 분할 조립. 전환 샷으로 이음새 자연스럽게 |

---

## Section 7: QA 체크리스트

### 클립 생성 후 (영상팀)

| # | 체크 항목 | 통과 기준 |
|---|----------|----------|
| 1 | 캐릭터 얼굴이 Character Pack과 일치하는가 | 머리색, 눈 색, 얼굴 특징이 레퍼런스와 동일 |
| 2 | 조명 방향이 씬 내에서 일관적인가 | 광원 위치가 세그먼트 간 모순 없음 |
| 3 | 모핑/플리커/여분 사지가 없는가 | 5~10초 클립 전체를 프레임 단위로 확인 |
| 4 | 색감이 에피소드 무드 테이블과 일치하는가 | Section 2의 에피소드별 지배적 색감 참조 |
| 5 | 카메라 움직임이 부드럽고 동기 부여되었는가 | 급격한 떨림, 비의도적 줌 없음 |
| 6 | 전환 샷이 이음새를 자연스럽게 숨기는가 | 캐릭터 전환 전후로 시각적 리셋 존재 |

### 에피소드 조립 후 (편집팀)

| # | 체크 항목 | 통과 기준 |
|---|----------|----------|
| 1 | 40~50초 러닝타임을 충족하는가 | 39초 이하, 51초 이상은 재편집 |
| 2 | **THUMB-STOP (첫 2초)이 CU/Medium인가** | Wide/Establishing이면 반려. 감정 표정/충격 상황/긴장 신체 언어 중 하나 |
| 3 | **HOOK TEXT가 첫 프레임에 있는가** | 상단 Bold 자막. 무음 시청자가 즉시 상황 진입 가능 |
| 4 | 마지막 5~7초가 해결되지 않은 긴장인가 | series_bible Section 4 원칙 6 참조 |
| 5 | 세그먼트 간 흐름이 자연스러운가 | 색감 점프, 조명 불일치 없음 |
| 6 | 자막 타이밍이 대사와 일치하는가 | 자막이 음성/입 움직임과 동기화 |
| 7 | 세로(9:16) 포맷인가 | 가로 여백 없음 |
| 8 | **NARRATIVE TEXT가 에피소드당 3회 이하인가** | 초과 시 텍스트 의존도가 높아짐. 비주얼 우선 원칙 위반 |
| 9 | **매 10초마다 비주얼 변화가 있는가** | 정적 구간 10초 이상이면 반려 |
| 10 | **무음 시청 테스트: 음소거로 시청 시 서사 파악 가능한가** | HOOK TEXT + DIALOGUE SUB + NARRATIVE TEXT로 서사 전달 확인 |

---

## Section 8: 텍스트 오버레이 규칙

> 3계층 텍스트 시스템 상세. 영상 편집 단계에서 적용한다.
> Kling/이미지 생성 단계에서 텍스트를 넣지 않는다.

### 3계층 텍스트 시스템

| 계층 | 명칭 | 목적 | 타이밍 |
|------|------|------|--------|
| 1 | **HOOK TEXT** | 무음 시청자의 즉시 진입 | 0:00 첫 프레임부터 ~2초 |
| 2 | **DIALOGUE SUB** | 대사 전달 | 대사 구간 |
| 3 | **NARRATIVE TEXT** | 서사 보조 (시간/장소/관계) | 필요 시점, 에피소드당 최대 3회 |

### HOOK TEXT 규칙

- **위치**: 화면 상단 1/3 (세로 9:16 기준 상단 Safe Area)
- **스타일**: Bold, 큰 글씨 (최소 48pt 상당), 백색, 드롭 셰도우 또는 아웃라인
- **길이**: 한 줄, 최대 15자 (한국어) / 8단어 (영어)
- **내용**: 충격/궁금증 유발 문장. 상황을 즉시 전달
- **금지**: 질문형 금지 ("무슨 일이?"), 추상적 표현 금지 ("운명의 밤")
- **좋은 예**: "오빠가 피투성이로 들어왔다", "She made a deal with the devil"
- **나쁜 예**: "그날 밤...", "Everything changed"

### DIALOGUE SUB 규칙

- **위치**: 화면 하단 1/4
- **스타일**: 일반 자막, 백색 + 반투명 블랙 배경 바
- **타이밍**: 음성 시작 0.1초 전 ~ 음성 종료 0.3초 후
- **한 줄 최대**: 2줄. 3줄 이상 시 분할

### NARRATIVE TEXT 규칙

- **위치**: 화면 중앙 또는 하단 (DIALOGUE SUB과 겹치지 않게)
- **스타일**: Italic, 작은 글씨 (36pt 상당), 페이드 인 0.3초 / 페이드 아웃 0.3초
- **용도**: 시간 경과 ("2년 전"), 장소 전환 ("더체스의 클럽"), 관계 정보 ("소꿉친구이자 경찰")
- **빈도 제한**: 에피소드당 최대 3회. 초과 시 비주얼 의존도 저하
- **금지**: 감정 해설 ("루나는 슬펐다"), 스토리 요약 ("지금까지의 이야기")

### 텍스트 레이어 간 충돌 방지

- HOOK TEXT와 DIALOGUE SUB는 동시 표시하지 않는다 (HOOK TEXT가 끝난 뒤 DIALOGUE SUB 시작)
- NARRATIVE TEXT와 DIALOGUE SUB가 겹칠 경우, NARRATIVE TEXT를 상단으로 이동
- 화면에 동시 표시되는 텍스트 레이어는 최대 1개
