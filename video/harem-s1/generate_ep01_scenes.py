#!/usr/bin/env python3
"""Generate EP01 scene key-frame images for Harem S1 using Gemini.

Each scene image is a single key-frame that will be fed into Kling
for Image-to-Video generation.

Usage:
    python generate_ep01_scenes.py                # Report scene count
    python generate_ep01_scenes.py --batch 1      # Scenes 1-5
    python generate_ep01_scenes.py --batch 2      # Scenes 6-10
    python generate_ep01_scenes.py --batch 3      # Scenes 11-14
"""

import sys
import time
import base64
from pathlib import Path

project_root = Path(__file__).resolve().parent
repo_root = project_root.parent.parent
sys.path.insert(0, str(repo_root / "src"))

from dotenv import load_dotenv
load_dotenv(repo_root / ".env")

import os
from google import genai
from google.genai.types import GenerateContentConfig, Part

# ─── Config ───
REF_DIR = project_root / "characters" / "reference_images"
OUTPUT_DIR = project_root / "scenes" / "ep01"
DELAY = 10  # seconds between API calls

IMAGE_MODELS = [
    "gemini-2.0-flash-exp-image-generation",
    "gemini-2.5-flash-image",
]

STYLE_SUFFIX = (
    "cinematic, shallow depth of field, photorealistic, rich natural colors, "
    "soft directional lighting, anamorphic lens, film grain, "
    "Negative prompt: blur, distortion, watermark, text, low quality, cartoon, "
    "anime, extra limbs, CGI artifacts, plastic look"
)


def _get_client():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY not set")
    return genai.Client(api_key=api_key)


def _load_ref(name):
    """Load character face_closeup as reference Part."""
    path = REF_DIR / name / "face_closeup.png"
    data = path.read_bytes()
    return Part.from_bytes(data=data, mime_type="image/png")


def generate_scene(scene_num, prompt, characters=None):
    """Generate a single scene image with optional character references.

    Args:
        scene_num: Scene number (1-14)
        prompt: Scene description prompt
        characters: List of character names for reference, e.g. ["ethan", "tasha"]
    """
    client = _get_client()
    save_path = OUTPUT_DIR / f"s{scene_num:02d}.png"
    save_path.parent.mkdir(parents=True, exist_ok=True)

    full_prompt = f"{prompt}\n{STYLE_SUFFIX}"

    # Build contents with character references
    contents = []
    if characters:
        for name in characters:
            contents.append(_load_ref(name))
        char_names = " and ".join(characters)
        contents.append(
            f"Using the people in the reference images above as the EXACT SAME people "
            f"(same faces, same hair, same eye colors, same features). "
            f"Generate the following scene. Keep their appearance identical to the references.\n\n"
            f"{full_prompt}"
        )
    else:
        contents = full_prompt

    for model_name in IMAGE_MODELS:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=contents,
                config=GenerateContentConfig(
                    response_modalities=["Text", "Image"]
                ),
            )
            for part in response.candidates[0].content.parts:
                if part.inline_data is not None:
                    image_data = part.inline_data.data
                    if isinstance(image_data, str):
                        image_data = base64.b64decode(image_data)
                    save_path.write_bytes(image_data)
                    print(f"  Saved: s{scene_num:02d}.png ({model_name})")
                    return save_path
        except Exception as e:
            error_str = str(e)
            if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                import re
                match = re.search(r"retry in (\d+\.?\d*)s", error_str)
                delay = float(match.group(1)) + 2 if match else 20
                print(f"  Rate limited, waiting {delay:.0f}s...")
                time.sleep(delay)
                # Retry same model
                try:
                    response = client.models.generate_content(
                        model=model_name,
                        contents=contents,
                        config=GenerateContentConfig(
                            response_modalities=["Text", "Image"]
                        ),
                    )
                    for part in response.candidates[0].content.parts:
                        if part.inline_data is not None:
                            image_data = part.inline_data.data
                            if isinstance(image_data, str):
                                image_data = base64.b64decode(image_data)
                            save_path.write_bytes(image_data)
                            print(f"  Saved: s{scene_num:02d}.png ({model_name})")
                            return save_path
                except Exception:
                    pass
            print(f"  Model {model_name} failed: {e}")
            continue

    raise RuntimeError(f"All models failed for scene {scene_num}")


# ─── EP01 Scene Prompts ───
# 각 씬: (scene_num, characters, prompt)

SCENES = [
    # S01 | 0-2s | THUMB-STOP
    (1, ["ethan", "tasha"], (
        "Close-up shot from chest level angled upward. "
        "A gorgeous young woman with platinum blonde wavy hair and ice blue eyes, "
        "wearing a cream off-shoulder knit top, has her arms wrapped tightly around a handsome young man. "
        "His face is pressed against her upper chest near her collarbone, his cheek touching her skin. "
        "His eyes are wide open in shock, arms frozen at his sides with fingers spread. "
        "She has her eyes closed with a warm loving smile, chin resting on top of his head. "
        "Her blonde hair drapes over his shoulders. "
        "Indoor living room, warm afternoon sunlight from windows. "
        "Vertical 9:16 aspect ratio."
    )),

    # S02 | 2-5s
    (2, ["ethan", "tasha"], (
        "Medium shot at hip level. "
        "A gorgeous young woman with platinum blonde wavy hair holds a handsome young man at arm's length "
        "by both shoulders. She is beaming with teeth showing, eyes crinkled, head tilted right. "
        "The young man's face is bright red from jawline to hairline. His eyes aimed at the floor. "
        "One hand goes to the back of his neck in a nervous gesture. "
        "Indoor living room with warm afternoon light. "
        "Vertical 9:16 aspect ratio."
    )),

    # S03 | 5-8s
    (3, ["mika"], (
        "Medium-wide shot from hallway toward a back door. "
        "A beautiful athletic young woman with honey brown hair loose and wet on her shoulders, "
        "bright green eyes, light freckles, walks in through a glass back door. "
        "She wears a black bikini top and low-riding denim cutoff shorts, "
        "a white towel slung over her left shoulder. Bare midriff with toned flat abs. "
        "She has stopped walking, one eyebrow raised, looking at someone off-camera with an amused expression. "
        "She holds a water bottle in one hand. "
        "Bright daylight from the open door behind her. Indoor hallway. "
        "Vertical 9:16 aspect ratio."
    )),

    # S04 | 8-11s
    (4, ["ethan"], (
        "Extreme close-up of a handsome young man's face at eye level. "
        "Dark brown short neat hair, deep brown eyes, slim V-line jaw. "
        "His eyes are glancing to the side as if he just saw something shocking, "
        "then snapping upward to the ceiling. Jaw clenched. "
        "His throat shows a visible hard swallow. "
        "The tips of his ears are turning red. Slight panic in his expression. "
        "Indoor, warm lighting. "
        "Vertical 9:16 aspect ratio."
    )),

    # S05 | 11-15s
    (5, ["ethan", "tasha"], (
        "Medium shot from living room toward a staircase. "
        "A gorgeous young woman with platinum blonde wavy hair, wearing a cream knit top, "
        "has her hand on a young man's lower back, guiding him up the stairs. "
        "She walks close beside him, their hips nearly touching. "
        "He grips a suitcase handle with white knuckles, body angled slightly away from her. "
        "Warm indoor lighting, wooden staircase. "
        "Vertical 9:16 aspect ratio."
    )),

    # S06 | 15-19s
    (6, ["tasha"], (
        "Medium shot from inside a bedroom toward the open doorway. "
        "A gorgeous young woman with platinum blonde wavy hair stands in the doorway, "
        "gesturing proudly into the room. She wears a cream off-shoulder knit dress. "
        "On the bed behind her, clearly visible on white sheets, "
        "a black lace bralette and matching underwear are laid out flat. "
        "She doesn't notice them, pointing to the wall between rooms with a bright smile. "
        "Bright bedroom with white walls and natural light from a window. "
        "Vertical 9:16 aspect ratio."
    )),

    # S07 | 19-22s
    (7, ["ethan"], (
        "Close-up of a handsome young man's face at eye level. "
        "Dark brown short hair, brown eyes, slim jawline. "
        "His eyes are wide, staring at something on a bed (off-camera below). "
        "His face is deep red. He is taking a step backward, "
        "his back hitting a hallway wall with both hands up palms out in a defensive gesture. "
        "Expression of pure embarrassment and panic. "
        "Indoor hallway, warm lighting. "
        "Vertical 9:16 aspect ratio."
    )),

    # S08 | 22-26s
    (8, ["ethan"], (
        "Medium shot from a bedroom doorway looking inside. "
        "A handsome young man with dark brown short hair sits on the edge of a bed. "
        "A suitcase is on the floor beside him. He holds a small photo frame in both hands, "
        "looking down at it with a gentle, slightly sad expression. "
        "The photo shows a woman's face with a soft smile. "
        "He places it carefully on the nightstand, his thumb lingering on the glass. "
        "Quiet bedroom, warm golden hour light from window. "
        "Vertical 9:16 aspect ratio."
    )),

    # S09 | 26-29s
    (9, ["ethan"], (
        "Medium shot from the foot of a bed. "
        "A handsome young man with dark brown short hair has fallen backward onto a mattress. "
        "His arms are spread wide. He stares at the ceiling. "
        "He rubs both hands over his face in disbelief. "
        "Simple bedroom, late afternoon light. "
        "Vertical 9:16 aspect ratio."
    )),

    # S10 | 29-33s
    (10, ["ethan"], (
        "Wide shot from a room corner at a diagonal angle. "
        "Night. The room is dark except for pale blue moonlight from a window "
        "casting a blue rectangle on the floor. "
        "A young man lies under covers on his back, eyes open, staring at the ceiling. "
        "His hands are flat at his sides on top of the blanket. Rigid, not sleeping. "
        "Dark moody atmosphere, blue moonlight only. "
        "Vertical 9:16 aspect ratio."
    )),

    # S11 | 33-37s
    (11, ["tasha"], (
        "Close-up of a bedroom door. The door handle is turning. "
        "The door swings open, warm hallway light spilling into the dark room. "
        "In the doorframe stands a gorgeous young woman with platinum blonde wavy hair. "
        "She wears a thin ice-blue silk camisole with spaghetti straps ending at mid-thigh, bare legs. "
        "Backlit from the hallway, her body silhouette visible through the thin silk fabric. "
        "She has a slight smile with lips parted. "
        "Dark room with warm hallway backlight. "
        "Vertical 9:16 aspect ratio."
    )),

    # S12 | 37-41s
    (12, ["tasha"], (
        "Medium shot at mattress level from the opposite side of a bed. "
        "A gorgeous young woman with platinum blonde hair wearing a thin ice-blue silk camisole "
        "slides underneath the blanket of a bed. She turns onto her side facing away, "
        "pulling the covers up to her shoulder. She scoots backward to close the gap "
        "toward someone else in the bed. "
        "Dark bedroom lit only by moonlight from a window. "
        "Vertical 9:16 aspect ratio."
    )),

    # S13 | 41-46s
    (13, ["ethan", "tasha"], (
        "Close-up at pillow level shooting across two faces in profile. "
        "A gorgeous young woman with platinum blonde hair lies with her back pressed against "
        "a young man's side in bed. She wears a thin silk camisole, her shoulder blades against his chest. "
        "Her blonde hair is spread across the pillow touching his jaw. "
        "The young man is completely rigid, every neck muscle visible, eyes wide open staring at ceiling. "
        "She looks peaceful and relaxed. He looks frozen in panic. "
        "Dark bedroom, blue moonlight. "
        "Vertical 9:16 aspect ratio."
    )),

    # S14 | 46-50s | CLIFFHANGER
    (14, ["ethan", "tasha"], (
        "Extreme close-up from directly above a young man's face in bed. "
        "He stares straight up, not blinking, jaw clenched with temple muscle visible. "
        "Beside him, a woman's shoulder is visible in a thin silk camisole, "
        "one spaghetti strap sliding down her upper arm. "
        "Her hand reaches behind her, her palm landing on his thigh, "
        "fingers curling gently into his sweatpants fabric. "
        "His eyes are impossibly wide, mouth slightly open in shock. "
        "Dark bedroom, blue moonlight, extreme tension. "
        "Vertical 9:16 aspect ratio."
    )),
]

# ─── Batches ───
BATCHES = {
    1: SCENES[0:5],    # S01-S05 (5 images)
    2: SCENES[5:10],   # S06-S10 (5 images)
    3: SCENES[10:14],  # S11-S14 (4 images)
}


def run_batch(scenes):
    """Generate a batch of scene images."""
    print("=" * 60)
    print("EP01 Scene Generator")
    print("=" * 60)
    print(f"Output: {OUTPUT_DIR}")
    print(f"Scenes: {len(scenes)}")
    print("=" * 60)

    if len(scenes) > 5:
        print("ERROR: Batch exceeds 5-image limit!")
        sys.exit(1)

    results = []
    for i, (scene_num, characters, prompt) in enumerate(scenes):
        if i > 0:
            print(f"  Waiting {DELAY}s...")
            time.sleep(DELAY)
        char_str = "+".join(characters) if characters else "none"
        print(f"  Scene {scene_num:02d} [{char_str}]...")
        try:
            r = generate_scene(scene_num, prompt, characters)
            results.append(r)
        except Exception as e:
            print(f"  ERROR: {e}")

    print("\n" + "=" * 60)
    print(f"Done! {len(results)}/{len(scenes)} scenes generated.")
    for p in results:
        print(f"  {p}")
    print("=" * 60)
    return results


def main():
    args = sys.argv[1:]

    if "--batch" in args:
        idx = args.index("--batch")
        batch_num = int(args[idx + 1])
        if batch_num not in BATCHES:
            print(f"Invalid batch: {batch_num}. Available: {list(BATCHES.keys())}")
            sys.exit(1)
        run_batch(BATCHES[batch_num])
        return

    # No args = report
    print("=" * 60)
    print("EP01: MOVE IN -- 14 Scenes")
    print("=" * 60)
    for batch_num, scenes in BATCHES.items():
        scene_nums = [s[0] for s in scenes]
        print(f"  Batch {batch_num}: S{scene_nums[0]:02d}-S{scene_nums[-1]:02d} ({len(scenes)} images)")
    print()
    print("Run with: python generate_ep01_scenes.py --batch 1")
    print("=" * 60)


if __name__ == "__main__":
    main()
