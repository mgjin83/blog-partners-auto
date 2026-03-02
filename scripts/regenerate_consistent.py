#!/usr/bin/env python3
"""Regenerate all character images using face_closeup as canonical reference.

Each character's face_closeup.png is the "ground truth" face.
All other images (fullbody, angles, actions, expressions, outfits) are
regenerated with that face as multimodal input to ensure consistency.

Usage:
    python scripts/regenerate_consistent.py              # All characters
    python scripts/regenerate_consistent.py luna          # One character
    python scripts/regenerate_consistent.py luna ash      # Specific characters
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
DELAY = 5

# ============================================================
# CHARACTER DEFINITIONS
# ============================================================
CHARACTERS = {
    "luna": {
        "base": (
            "calico cat face, cat face, human body, "
            "white base with orange and black patches, green eyes, "
            "average build, almond-shaped expressive eyes, thin white whiskers"
        ),
        "eyes": "green eyes",
        "default_outfit": "florist apron over simple dark clothes",
        "shots": {
            # --- fullbody ---
            "fullbody_front": (
                "Full body front view of this exact character, "
                "{outfit}, standing in a neutral pose facing the camera, "
                "plain grey background, full body visible head to toe"
            ),
            # --- angles ---
            "angles/three_quarter": (
                "Three-quarter view of this exact character, "
                "{outfit}, standing relaxed angled slightly to camera, "
                "plain grey background, full body visible head to toe"
            ),
            "angles/side_profile": (
                "Side profile view of this exact character, "
                "{outfit}, standing upright facing left, "
                "plain grey background, full body visible, side silhouette"
            ),
            "angles/back_view": (
                "Back view of this exact character, "
                "{outfit}, standing facing away from camera, "
                "plain grey background, full body visible head to toe"
            ),
            # --- actions ---
            "actions/walking": (
                "Medium shot of this exact character, "
                "{outfit}, walking forward with natural stride, "
                "plain grey background, dynamic pose"
            ),
            "actions/looking_back": (
                "Medium shot of this exact character, "
                "{outfit}, turning head to look over shoulder, body angled away, "
                "plain grey background, dramatic pose"
            ),
            "actions/leaning": (
                "Medium shot of this exact character, "
                "{outfit}, leaning against a wall with arms crossed, "
                "plain grey background, relaxed guarded pose"
            ),
            # --- expressions ---
            "expressions/determination": (
                "Close-up portrait of this exact character, {eyes}, "
                "determined expression, jaw set, eyes focused forward, "
                "plain grey background, focus on face"
            ),
            "expressions/fear": (
                "Close-up portrait of this exact character, {eyes}, "
                "fearful expression, wide eyes, ears slightly back, "
                "plain grey background, focus on face"
            ),
            "expressions/anger": (
                "Close-up portrait of this exact character, {eyes}, "
                "angry expression, narrowed eyes, tense face, "
                "plain grey background, focus on face"
            ),
            "expressions/sadness": (
                "Close-up portrait of this exact character, {eyes}, "
                "sad expression, downcast eyes, subtle grief, "
                "plain grey background, focus on face"
            ),
            "expressions/resignation": (
                "Close-up portrait of this exact character, {eyes}, "
                "resigned expression, weary eyes, hollow gaze, "
                "plain grey background, focus on face"
            ),
            "expressions/cold_composure": (
                "Close-up portrait of this exact character, {eyes}, "
                "cold composed expression, emotionless face, guarded eyes, "
                "plain grey background, focus on face"
            ),
        },
        "outfit_variants": {
            "outfit_dark_coat": {
                "outfit": "dark long coat over dark pants",
                "shots": ["fullbody_front", "face_closeup"],
            },
        },
    },
    "ash": {
        "base": (
            "grey tabby cat face, cat face, human body, "
            "grey stripes, yellow eyes, "
            "larger build, round warm-looking eyes, grey whiskers"
        ),
        "eyes": "yellow eyes",
        "default_outfit": "casual clothes with hoodie",
        "shots": {
            "fullbody_front": (
                "Full body front view of this exact character, "
                "{outfit}, standing in a neutral pose facing the camera, "
                "plain grey background, full body visible head to toe"
            ),
            "angles/three_quarter": (
                "Three-quarter view of this exact character, "
                "{outfit}, standing relaxed angled slightly to camera, "
                "plain grey background, full body visible head to toe"
            ),
            "angles/side_profile": (
                "Side profile view of this exact character, "
                "{outfit}, standing upright facing left, "
                "plain grey background, full body visible, side silhouette"
            ),
            "angles/back_view": (
                "Back view of this exact character, "
                "{outfit}, standing facing away from camera, "
                "plain grey background, full body visible head to toe"
            ),
            "actions/walking": (
                "Medium shot of this exact character, "
                "{outfit}, walking forward with natural stride, "
                "plain grey background, dynamic pose"
            ),
            "actions/looking_back": (
                "Medium shot of this exact character, "
                "{outfit}, turning head to look over shoulder, body angled away, "
                "plain grey background, dramatic pose"
            ),
            "actions/leaning": (
                "Medium shot of this exact character, "
                "{outfit}, leaning against a wall with arms crossed, "
                "plain grey background, relaxed guarded pose"
            ),
            "expressions/determination": (
                "Close-up portrait of this exact character, {eyes}, "
                "determined expression, jaw set, eyes focused forward, "
                "plain grey background, focus on face"
            ),
            "expressions/fear": (
                "Close-up portrait of this exact character, {eyes}, "
                "fearful expression, wide eyes, ears slightly back, "
                "plain grey background, focus on face"
            ),
            "expressions/anger": (
                "Close-up portrait of this exact character, {eyes}, "
                "angry expression, narrowed eyes, bared teeth slightly, "
                "plain grey background, focus on face"
            ),
            "expressions/sadness": (
                "Close-up portrait of this exact character, {eyes}, "
                "sad expression, downcast eyes, heavy grief, "
                "plain grey background, focus on face"
            ),
            "expressions/resignation": (
                "Close-up portrait of this exact character, {eyes}, "
                "resigned expression, weary eyes, slumped, "
                "plain grey background, focus on face"
            ),
            "expressions/cold_composure": (
                "Close-up portrait of this exact character, {eyes}, "
                "cold composed expression, emotionless stare, "
                "plain grey background, focus on face"
            ),
        },
        "outfit_variants": {
            "outfit_torn_clothes_ep01": {
                "outfit": "torn dirty clothes with bloodstains, injured appearance",
                "shots": ["fullbody_front", "face_closeup"],
            },
        },
    },
    "duchess": {
        "base": (
            "persian cat face, cat face, human body, "
            "fluffy white fur, flat face, blue eyes, "
            "elegant build, large piercing slightly narrowed eyes, white delicate whiskers"
        ),
        "eyes": "blue eyes",
        "default_outfit": "luxurious dark clothing, jewelry",
        "shots": {
            "fullbody_front": (
                "Full body front view of this exact character, "
                "{outfit}, standing in a poised elegant pose facing the camera, "
                "plain grey background, full body visible head to toe"
            ),
            "angles/three_quarter": (
                "Three-quarter view of this exact character, "
                "{outfit}, standing with elegant poise angled to camera, "
                "plain grey background, full body visible head to toe"
            ),
            "angles/side_profile": (
                "Side profile view of this exact character, "
                "{outfit}, standing upright facing left, "
                "plain grey background, full body visible, side silhouette"
            ),
            "angles/back_view": (
                "Back view of this exact character, "
                "{outfit}, standing facing away from camera, "
                "plain grey background, full body visible head to toe"
            ),
            "actions/walking": (
                "Medium shot of this exact character, "
                "{outfit}, walking forward with slow elegant stride, "
                "plain grey background, graceful pose"
            ),
            "actions/looking_back": (
                "Medium shot of this exact character, "
                "{outfit}, turning head to look over shoulder, "
                "plain grey background, dramatic elegant pose"
            ),
            "actions/leaning": (
                "Medium shot of this exact character, "
                "{outfit}, seated in a chair with legs crossed, poised, "
                "plain grey background, regal pose"
            ),
            "expressions/cold_composure": (
                "Close-up portrait of this exact character, {eyes}, "
                "cold composed expression, regal and unreadable, "
                "plain grey background, focus on face"
            ),
            "expressions/predatory_smile": (
                "Close-up portrait of this exact character, {eyes}, "
                "subtle predatory smile, one corner of mouth raised, dangerous, "
                "plain grey background, focus on face"
            ),
            "expressions/displeasure": (
                "Close-up portrait of this exact character, {eyes}, "
                "displeased expression, slightly narrowed eyes, raised chin, "
                "plain grey background, focus on face"
            ),
            "expressions/contempt": (
                "Close-up portrait of this exact character, {eyes}, "
                "contemptuous expression, looking down, dismissive gaze, "
                "plain grey background, focus on face"
            ),
            "expressions/controlled_anger": (
                "Close-up portrait of this exact character, {eyes}, "
                "controlled anger, icy stare, barely contained fury, "
                "plain grey background, focus on face"
            ),
            "expressions/possessive_satisfaction": (
                "Close-up portrait of this exact character, {eyes}, "
                "possessive satisfied expression, owning smile, calculating eyes, "
                "plain grey background, focus on face"
            ),
        },
        "outfit_variants": {},
    },
    "milo": {
        "base": (
            "orange tabby cat face, cat face, human body, "
            "orange stripes, warm features, amber eyes, "
            "average build, warm open honest-looking eyes, orange-tinted whiskers"
        ),
        "eyes": "amber eyes",
        "default_outfit": "police uniform",
        "shots": {
            "fullbody_front": (
                "Full body front view of this exact character, "
                "{outfit}, standing in a neutral upright pose facing the camera, "
                "plain grey background, full body visible head to toe"
            ),
            "angles/three_quarter": (
                "Three-quarter view of this exact character, "
                "{outfit}, standing relaxed angled slightly to camera, "
                "plain grey background, full body visible head to toe"
            ),
            "angles/side_profile": (
                "Side profile view of this exact character, "
                "{outfit}, standing upright facing left, "
                "plain grey background, full body visible, side silhouette"
            ),
            "angles/back_view": (
                "Back view of this exact character, "
                "{outfit}, standing facing away from camera, "
                "plain grey background, full body visible head to toe"
            ),
            "actions/walking": (
                "Medium shot of this exact character, "
                "{outfit}, walking forward with steady stride, "
                "plain grey background, dynamic pose"
            ),
            "actions/looking_back": (
                "Medium shot of this exact character, "
                "{outfit}, turning head to look over shoulder, body angled away, "
                "plain grey background, dramatic pose"
            ),
            "actions/leaning": (
                "Medium shot of this exact character, "
                "{outfit}, leaning against a wall with arms crossed, "
                "plain grey background, relaxed pose"
            ),
            "expressions/concern": (
                "Close-up portrait of this exact character, {eyes}, "
                "concerned expression, worried eyes, furrowed brow, "
                "plain grey background, focus on face"
            ),
            "expressions/suspicion": (
                "Close-up portrait of this exact character, {eyes}, "
                "suspicious expression, slightly narrowed eyes, studying gaze, "
                "plain grey background, focus on face"
            ),
            "expressions/quiet_disappointment": (
                "Close-up portrait of this exact character, {eyes}, "
                "quietly disappointed expression, hurt eyes, closed mouth, "
                "plain grey background, focus on face"
            ),
            "expressions/determination": (
                "Close-up portrait of this exact character, {eyes}, "
                "determined expression, firm jaw, resolute eyes, "
                "plain grey background, focus on face"
            ),
            "expressions/warmth": (
                "Close-up portrait of this exact character, {eyes}, "
                "warm expression, gentle eyes, soft caring look, "
                "plain grey background, focus on face"
            ),
            "expressions/cold_silence": (
                "Close-up portrait of this exact character, {eyes}, "
                "cold silent expression, blank stare, emotionally shut down, "
                "plain grey background, focus on face"
            ),
        },
        "outfit_variants": {
            "outfit_casual": {
                "outfit": "casual jacket and jeans",
                "shots": ["fullbody_front", "face_closeup"],
            },
        },
    },
}


def regenerate_character(name: str, cfg: dict):
    """Regenerate all images for one character using face_closeup as reference."""
    ref_img = REF_DIR / name / "face_closeup.png"
    if not ref_img.exists():
        print(f"  ERROR: {ref_img} not found! Cannot use as reference.")
        return []

    print(f"\n{'='*60}")
    print(f"  {name.upper()} - Reference: {ref_img.name}")
    print(f"{'='*60}")

    results = []
    outfit = cfg["default_outfit"]
    eyes = cfg.get("eyes", "")
    count = 0
    total = len(cfg["shots"])
    for variant_cfg in cfg.get("outfit_variants", {}).values():
        total += len(variant_cfg["shots"])

    # --- Default outfit shots ---
    for shot_key, prompt_tpl in cfg["shots"].items():
        if count > 0:
            time.sleep(DELAY)
        count += 1
        prompt = prompt_tpl.format(outfit=outfit, eyes=eyes)
        path = REF_DIR / name / f"{shot_key}.png"
        path.parent.mkdir(parents=True, exist_ok=True)
        print(f"  [{count}/{total}] {shot_key}...")
        try:
            r = generate_character_image(prompt, path, reference_image=ref_img)
            results.append(r)
        except Exception as e:
            print(f"    ERROR: {e}")

    # --- Outfit variants ---
    for variant_name, variant_cfg in cfg.get("outfit_variants", {}).items():
        variant_outfit = variant_cfg["outfit"]
        for shot_type in variant_cfg["shots"]:
            if count > 0:
                time.sleep(DELAY)
            count += 1
            out_dir = REF_DIR / name / variant_name
            out_dir.mkdir(parents=True, exist_ok=True)

            if shot_type == "fullbody_front":
                prompt = (
                    f"Full body front view of this exact character, "
                    f"{variant_outfit}, standing in a neutral pose facing the camera, "
                    "plain grey background, full body visible head to toe"
                )
            else:  # face_closeup
                prompt = (
                    f"Close-up portrait of this exact character, {eyes}, "
                    f"wearing {variant_outfit}, neutral expression, "
                    "plain grey background, focus on face"
                )

            path = out_dir / f"{shot_type}.png"
            print(f"  [{count}/{total}] {variant_name}/{shot_type}...")
            try:
                r = generate_character_image(prompt, path, reference_image=ref_img)
                results.append(r)
            except Exception as e:
                print(f"    ERROR: {e}")

    return results


def main():
    requested = [a.lower() for a in sys.argv[1:]] if len(sys.argv) > 1 else list(CHARACTERS.keys())
    targets = {k: v for k, v in CHARACTERS.items() if k in requested}

    if not targets:
        print(f"Unknown: {requested}. Available: {list(CHARACTERS.keys())}")
        sys.exit(1)

    print("=" * 60)
    print("Ember - Consistent Character Regeneration")
    print("  Using face_closeup as canonical reference")
    print("=" * 60)

    all_results = []
    for name, cfg in targets.items():
        results = regenerate_character(name, cfg)
        all_results.extend(results)

    print(f"\n{'='*60}")
    print(f"DONE! Regenerated {len(all_results)} images with consistent faces.")
    print("=" * 60)


if __name__ == "__main__":
    main()
