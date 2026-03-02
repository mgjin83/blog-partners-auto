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

```
cinematic, shallow depth of field, film noir aesthetic,
desaturated color palette, high contrast, low-key lighting,
anamorphic lens, professional color grading
```

이 어휘는 바꿔 쓰지 않는다. `"film noir aesthetic"`을 `"dark detective mood"`로 의역하면 일관성이 깨진다.

### 표준 네거티브 프롬프트 (모든 생성에 사용)

```
blur, distortion, watermark, text overlay, low quality, flickering,
morphing faces, extra limbs, bright colors, cartoon, anime, pixar,
smiling, oversaturated, plastic look, CGI artifacts, inconsistent lighting
```

네거티브 프롬프트에서는 원하지 않는 것을 직접 기술한다. `"no robots"` 가 아니라 `"robots"`.

### 프롬프트 예시

**EP 01 — 꽃집에 애쉬가 들어오는 장면:**
```
Medium shot of ++a calico cat-face figure in a florist apron++,
turning toward the door as a grey tabby figure stumbles in,
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

- **매력적 외형 원칙**: 모든 캐릭터는 시청자의 시선을 끄는 매력적인 외형으로 디자인한다. 주인공과 주요 조연은 미남/미녀 기반으로 설계하되, 캐릭터 성격에 맞는 개성을 부여한다. 고양이 얼굴이지만 조형미와 균형감을 갖춰야 하며, 눈·무늬·표정에서 오는 매력이 캐릭터 인지도와 팬덤 형성의 핵심이다.
- 모든 캐릭터 프롬프트에 `"cat face, human body"` 를 기본 포함한다
- 묘종별 특징(귀 형태, 무늬, 눈 색)을 매 프롬프트에 반복한다
- 의복은 현대 일상복. 캐릭터 성격을 반영한다
- 표정 연기가 핵심이므로 얼굴 클로즈업 비중을 높인다
- 한 프레임에 캐릭터 1~2명까지. 3명 이상 시 왜곡 위험

### 캐릭터별 매력 방향

| 캐릭터 | 매력 키워드 | 프롬프트 반영 |
|--------|-----------|-------------|
| LUNA | 날카로우면서 여린 아름다움 | `beautiful almond-shaped expressive eyes`, `delicate features`, `striking calico pattern` |
| ASH | 거칠지만 부드러운 인상 | `handsome rugged features`, `warm round eyes`, `strong gentle presence` |
| DUCHESS | 압도적 우아함과 위엄 | `stunningly beautiful`, `regal elegant features`, `commanding presence` |
| MILO | 따뜻하고 신뢰감 있는 외형 | `warm handsome features`, `kind honest eyes`, `trustworthy appearance` |

### 캐릭터별 프롬프트 핵심 (상세는 character_sheets/에서 관리)

| 캐릭터 | 묘종 키워드 | 눈 색 | 체형 | 기본 의상 |
|--------|-----------|-------|------|----------|
| LUNA | calico cat face, white base with orange and black patches | green eyes | average build | florist apron (꽃집) / dark coat (밤 외출) |
| ASH | grey tabby cat face, grey stripes | yellow eyes | larger build than Luna | casual clothes / torn clothes (EP 01) |
| DUCHESS | persian cat face, fluffy white fur, flat face | blue eyes | elegant build | luxurious dark clothing, jewelry |
| MILO | orange tabby cat face, orange stripes, warm features | amber eyes | average build | police uniform (근무) / casual (비번) |

### Character DNA 템플릿

캐릭터 디자이너는 각 캐릭터에 대해 아래 항목을 확정한다:

```
# [캐릭터명] — Character DNA

## 얼굴 앵커
- 묘종:
- 눈 색:
- 눈 형태:
- 귀 형태:
- 무늬 패턴:
- 수염:
- 구별 포인트 (흉터, 반점 등):

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

### 에피소드 = 7~8개 세그먼트

40~50초 에피소드를 5~10초 클립으로 조립한다:

| # | 세그먼트 | 길이 | 샷 타입 | 서사 기능 |
|---|---------|------|---------|----------|
| 1 | Hook | 5s | Wide 또는 Establishing | 장소·분위기. 첫 프레임이 스와이프를 막는다 |
| 2 | 캐릭터 진입 | 5s | Medium | 주인공 소개 또는 상황 제시 |
| 3 | 감정 비트 | 5s | Close-up | 표정, 반응, 디테일 |
| 4 | 상호작용 | 5s | Medium two-shot 또는 OTS | 대화, 대면, 긴장 |
| 5 | 상대 반응 | 5s | Close-up | 상대 캐릭터의 감정 |
| 6 | 핵심 순간 | 5~10s | Medium | 전환, 결정, 드라마틱 액션 |
| 7 | 마지막 5초 | 5s | 상황에 따라 | 해결되지 않은 긴장. 비주얼로 "끝나지 않았다"를 전달 |

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
고양이 얼굴 + 인간 몸은 스타일라이즈드 캐릭터이므로, 텍스트 프롬프트만으로는 에피소드 간 일관성이 유지되지 않는다.

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
- 스타일 락과 네거티브 프롬프트를 사용
- 배경은 단색(`plain grey background`)으로 캐릭터만 분리
- 4방향 전신 + 표정 6종 + 액션 포즈 3+ = 최소 13장

**3단계 (Shot Keyframe 생성):**
- Character Pack 이미지를 Elements로 업로드
- 환경 레퍼런스도 Elements로 함께 업로드 (최대 4장)
- 프롬프트는 구도와 배치만 기술. 캐릭터 외형은 Elements가 결정
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

### Elements 활용

- Kling Elements에 레퍼런스 이미지 1~4장 동시 업로드 → 시각적 정체성 추출·유지
- 캐릭터 + 환경 + 소품을 함께 업로드하면 조합 결과가 안정적
- v3.0 Omni: 3~8초 캐릭터 영상에서 외형+음성을 추출, 재사용 가능한 엘리먼트 생성
- 복수 엘리먼트 조합 시 각각의 특징이 교차 오염 없이 유지됨

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
| 애니메/카툰 스타일 불안정 | 리얼리스틱 느와르 베이스 유지. Image-to-Video로 스타일 고정 |
| 눈/손 플리커 | 표정 장면에서 생성 후 QA. 문제 프레임 발견 시 재생성 |
| 클립 최대 5~15초 | 에피소드 = 7~8개 세그먼트로 분할 조립. 전환 샷으로 이음새 자연스럽게 |

---

## Section 7: QA 체크리스트

### 클립 생성 후 (영상팀)

| # | 체크 항목 | 통과 기준 |
|---|----------|----------|
| 1 | 캐릭터 얼굴이 Character Pack과 일치하는가 | 묘종, 눈 색, 무늬가 레퍼런스와 동일 |
| 2 | 조명 방향이 씬 내에서 일관적인가 | 광원 위치가 세그먼트 간 모순 없음 |
| 3 | 모핑/플리커/여분 사지가 없는가 | 5~10초 클립 전체를 프레임 단위로 확인 |
| 4 | 색감이 에피소드 무드 테이블과 일치하는가 | Section 2의 에피소드별 지배적 색감 참조 |
| 5 | 카메라 움직임이 부드럽고 동기 부여되었는가 | 급격한 떨림, 비의도적 줌 없음 |
| 6 | 전환 샷이 이음새를 자연스럽게 숨기는가 | 캐릭터 전환 전후로 시각적 리셋 존재 |

### 에피소드 조립 후 (편집팀)

| # | 체크 항목 | 통과 기준 |
|---|----------|----------|
| 1 | 40~50초 러닝타임을 충족하는가 | 39초 이하, 51초 이상은 재편집 |
| 2 | Hook (첫 5초)이 시각적 자극을 주는가 | 3초 안에 시청자의 주의를 잡는 비주얼 |
| 3 | 마지막 5초가 해결되지 않은 긴장인가 | series_bible Section 4 원칙 6 참조 |
| 4 | 세그먼트 간 흐름이 자연스러운가 | 색감 점프, 조명 불일치 없음 |
| 5 | 자막 타이밍이 대사와 일치하는가 | 자막이 음성/입 움직임과 동기화 |
| 6 | 세로(9:16) 포맷인가 | 가로 여백 없음 |
