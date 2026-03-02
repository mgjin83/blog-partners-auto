#!/usr/bin/env python3
"""Generate EP01 shot keyframes using consistent character references.

Each scene keyframe is generated with the relevant character's face_closeup
as multimodal reference input to ensure face consistency across keyframes.

Usage:
    python scripts/generate_keyframes_ep01.py          # All scenes
    python scripts/generate_keyframes_ep01.py s1 s3     # Specific scenes
"""

import sys
import time
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root / "src"))

from dotenv import load_dotenv
load_dotenv(project_root / ".env")

import importlib.util
_spec = importlib.util.spec_from_file_location(
    "image_generator",
    project_root / "src" / "blog_partners_auto" / "tools" / "image_generator.py",
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
generate_character_image = _mod.generate_character_image

REF_DIR = project_root / "characters" / "reference_images"
OUT_DIR = project_root / "characters" / "shot_keyframes" / "ep01"
DELAY = 5


# ============================================================
# EP01 SCENE KEYFRAMES
# ============================================================
# ref_chars: list of character names whose face_closeup to include as reference
# For scenes with no characters (props/environment only), ref_chars is empty.

SCENES = {
    "s1": {
        "filename": "ep01_s1_hook.png",
        "ref_chars": [],  # establishing shot, no character close-up
        "prompt": (
            "Establishing shot of a small flower shop at night, exterior view, "
            "warm amber light glowing softly through glass windows, "
            "a figure's silhouette visible inside arranging flowers, "
            "dark quiet street outside, wet pavement reflecting warm light, "
            "single streetlight casting orange glow, "
            "9:16 vertical composition, peaceful yet fragile atmosphere"
        ),
    },
    "s2": {
        "filename": "ep01_s2_luna_routine.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot inside a flower shop, "
            "this exact character wearing a florist apron over simple dark clothes, "
            "calico cat face with green eyes, "
            "gently trimming roses with small scissors, "
            "warm amber glow from overhead lamp, flowers everywhere, "
            "careful delicate movements, peaceful mood, "
            "9:16 vertical composition"
        ),
    },
    "s3": {
        "filename": "ep01_s3_ash_enters.png",
        "ref_chars": ["luna", "ash"],
        "prompt": (
            "Inside a flower shop, two characters visible, "
            "a grey tabby cat-face figure with yellow eyes stumbling through the front door, "
            "torn dirty clothes with bloodstains, injured, cold air rushing in, "
            "a calico cat-face figure with green eyes in florist apron turning sharply toward the door with shock, "
            "warm amber atmosphere disrupted by cold draft, flower petals disturbed, "
            "dramatic moment, 9:16 vertical composition"
        ),
    },
    "s4": {
        "filename": "ep01_s4_confession.png",
        "ref_chars": ["luna", "ash"],
        "prompt": (
            "Close-up shot inside flower shop, "
            "a calico cat-face figure with green eyes holding a wounded grey tabby cat-face figure with yellow eyes, "
            "the calico figure's green eyes wide with worry, "
            "the grey tabby looking up with fear in his yellow eyes, "
            "warm lamp light casting sharp shadows on both faces, "
            "intimate and tense atmosphere, "
            "9:16 vertical composition, focus on faces"
        ),
    },
    "s5": {
        "filename": "ep01_s5_determination.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Close-up portrait of a calico cat-face figure with green eyes, "
            "this exact character embracing someone, "
            "her green eyes looking past toward a dark doorway, "
            "expression shifting from fear to cold determination, "
            "the flower shop interior darkening, shadow falling across her eyes, "
            "dramatic lighting with half face in shadow, "
            "9:16 vertical composition, focus on her determined expression"
        ),
    },
    "s6": {
        "filename": "ep01_s6_flower_blood.png",
        "ref_chars": [],  # prop close-up, no character
        "prompt": (
            "Extreme close-up of a white rose lying on a wooden floor, "
            "next to fallen scissors, "
            "drops of blood slowly spreading across the white petals, "
            "warm amber lighting from above, "
            "the blood expands across the pure white surface, "
            "symbolic and haunting, shallow depth of field, "
            "9:16 vertical composition"
        ),
    },
    "s7": {
        "filename": "ep01_s7_end.png",
        "ref_chars": [],  # silhouettes only
        "prompt": (
            "Wide shot of a flower shop exterior at night, "
            "two silhouettes embracing visible through the warm lit window, "
            "a dark figure standing across the street watching, "
            "a phone screen illuminating the dark figure's hand, "
            "cigarette ember glowing orange, "
            "single orange streetlight reflecting on wet pavement, "
            "surveillance atmosphere, ominous, "
            "9:16 vertical composition"
        ),
    },
}


def generate_keyframe(scene_key: str, scene_cfg: dict):
    """Generate a single scene keyframe."""
    filename = scene_cfg["filename"]
    ref_chars = scene_cfg["ref_chars"]
    prompt = scene_cfg["prompt"]
    save_path = OUT_DIR / filename

    # Use character references if available
    # For multi-character scenes, use the first character as primary reference
    # and mention both in the prompt
    ref_image = None
    if ref_chars:
        primary = ref_chars[0]
        ref_path = REF_DIR / primary / "face_closeup.png"
        if ref_path.exists():
            ref_image = ref_path

    print(f"  {scene_key.upper()}: {filename}")
    if ref_image:
        print(f"    Reference: {ref_image.name} ({ref_chars[0]})")
    else:
        print(f"    Reference: none (environment/prop shot)")

    try:
        result = generate_character_image(
            prompt, save_path, reference_image=ref_image
        )
        print(f"    Saved: {result}")
        return result
    except Exception as e:
        print(f"    ERROR: {e}")
        return None


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    requested = [a.lower() for a in sys.argv[1:]] if len(sys.argv) > 1 else list(SCENES.keys())
    targets = {k: v for k, v in SCENES.items() if k in requested}

    if not targets:
        print(f"Unknown scene(s): {requested}")
        print(f"Available: {list(SCENES.keys())}")
        sys.exit(1)

    print("=" * 60)
    print("Ember EP01 - Shot Keyframe Generator")
    print(f"  Scenes: {', '.join(targets.keys())}")
    print("=" * 60)

    results = []
    for i, (key, cfg) in enumerate(targets.items()):
        if i > 0:
            time.sleep(DELAY)
        r = generate_keyframe(key, cfg)
        if r:
            results.append(r)

    print(f"\n{'='*60}")
    print(f"DONE! Generated {len(results)}/{len(targets)} keyframes.")
    print("=" * 60)


if __name__ == "__main__":
    main()
