#!/usr/bin/env python3
"""Generate all pre-production assets for Ember.

Covers: additional angles, action poses, outfit variants, environment references.

Usage:
    python scripts/generate_preproduction.py                # All tasks
    python scripts/generate_preproduction.py angles          # Character angles only
    python scripts/generate_preproduction.py actions         # Action poses only
    python scripts/generate_preproduction.py outfits         # Outfit variants only
    python scripts/generate_preproduction.py environments    # Environment refs only
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
ENV_DIR = project_root / "characters" / "environment_references"
DELAY = 5

# ============================================================
# CHARACTER BASE DESCRIPTIONS
# ============================================================
CHARS = {
    "luna": (
        "++calico cat face, cat face, human body++, "
        "white base with orange and black patches, green eyes, "
        "average build, florist apron over simple dark clothes, "
        "almond-shaped expressive eyes, thin white whiskers"
    ),
    "ash": (
        "++grey tabby cat face, cat face, human body++, "
        "grey stripes, yellow eyes, "
        "larger build, casual clothes with hoodie, "
        "round warm-looking eyes, grey whiskers"
    ),
    "duchess": (
        "++persian cat face, cat face, human body++, "
        "fluffy white fur, flat face, blue eyes, "
        "elegant build, luxurious dark clothing, jewelry, "
        "large piercing slightly narrowed eyes, white delicate whiskers"
    ),
    "milo": (
        "++orange tabby cat face, cat face, human body++, "
        "orange stripes, warm features, amber eyes, "
        "average build, police uniform, "
        "warm open honest-looking eyes, orange-tinted whiskers"
    ),
}

# ============================================================
# TASK 1: ADDITIONAL ANGLES (3/4, side, back)
# ============================================================
def generate_angles():
    print("\n" + "=" * 60)
    print("PHASE 1: Additional Character Angles")
    print("=" * 60)
    results = []
    count = 0
    total = len(CHARS) * 3

    for name, desc in CHARS.items():
        out = REF_DIR / name / "angles"
        out.mkdir(parents=True, exist_ok=True)

        angles = {
            "three_quarter": (
                f"Three-quarter view of {desc}, "
                "standing in a relaxed pose angled slightly to camera, "
                "plain grey background, character concept art, "
                "full body visible from head to toe"
            ),
            "side_profile": (
                f"Side profile view of {desc}, "
                "standing upright facing left, "
                "plain grey background, character concept art, "
                "full body visible from head to toe, side silhouette"
            ),
            "back_view": (
                f"Back view of {desc}, "
                "standing facing away from camera, showing back of head and body, "
                "plain grey background, character concept art, "
                "full body visible from head to toe"
            ),
        }

        for shot, prompt in angles.items():
            if count > 0:
                time.sleep(DELAY)
            count += 1
            path = out / f"{shot}.png"
            print(f"  [{count}/{total}] {name}/{shot}...")
            try:
                r = generate_character_image(prompt, path)
                results.append(r)
            except Exception as e:
                print(f"    ERROR: {e}")

    print(f"  Angles done: {len(results)}/{total}")
    return results

# ============================================================
# TASK 2: ACTION POSES (walking, looking back, leaning)
# ============================================================
def generate_actions():
    print("\n" + "=" * 60)
    print("PHASE 2: Action Poses")
    print("=" * 60)
    results = []
    count = 0
    total = len(CHARS) * 3

    for name, desc in CHARS.items():
        out = REF_DIR / name / "actions"
        out.mkdir(parents=True, exist_ok=True)

        actions = {
            "walking": (
                f"Medium shot of {desc}, "
                "walking forward with natural stride, "
                "plain grey background, dynamic pose, "
                "full body visible"
            ),
            "looking_back": (
                f"Medium shot of {desc}, "
                "turning head to look over shoulder, body angled away from camera, "
                "plain grey background, dramatic pose, "
                "three-quarter back view"
            ),
            "leaning": (
                f"Medium shot of {desc}, "
                "leaning against a wall with arms crossed, "
                "plain grey background, relaxed but guarded pose"
            ),
        }

        for shot, prompt in actions.items():
            if count > 0:
                time.sleep(DELAY)
            count += 1
            path = out / f"{shot}.png"
            print(f"  [{count}/{total}] {name}/{shot}...")
            try:
                r = generate_character_image(prompt, path)
                results.append(r)
            except Exception as e:
                print(f"    ERROR: {e}")

    print(f"  Actions done: {len(results)}/{total}")
    return results

# ============================================================
# TASK 3: OUTFIT VARIANTS
# ============================================================
OUTFIT_VARIANTS = {
    "luna": {
        "desc": (
            "++calico cat face, cat face, human body++, "
            "white base with orange and black patches, green eyes, "
            "average build, wearing a dark long coat over dark pants, "
            "almond-shaped expressive eyes, thin white whiskers"
        ),
        "outfit_name": "dark_coat",
    },
    "ash": {
        "desc": (
            "++grey tabby cat face, cat face, human body++, "
            "grey stripes, yellow eyes, "
            "larger build, torn dirty clothes with bloodstains, "
            "round warm-looking eyes, grey whiskers, injured appearance"
        ),
        "outfit_name": "torn_clothes_ep01",
    },
    "milo": {
        "desc": (
            "++orange tabby cat face, cat face, human body++, "
            "orange stripes, warm features, amber eyes, "
            "average build, casual jacket and jeans, "
            "warm open honest-looking eyes, orange-tinted whiskers"
        ),
        "outfit_name": "casual",
    },
}

def generate_outfits():
    print("\n" + "=" * 60)
    print("PHASE 3: Outfit Variants")
    print("=" * 60)
    results = []
    count = 0
    total = len(OUTFIT_VARIANTS) * 2  # fullbody + closeup per outfit

    for name, cfg in OUTFIT_VARIANTS.items():
        desc = cfg["desc"]
        outfit = cfg["outfit_name"]
        out = REF_DIR / name / f"outfit_{outfit}"
        out.mkdir(parents=True, exist_ok=True)

        shots = {
            "fullbody_front": (
                f"Full body front view of {desc}, "
                "standing in a neutral pose facing the camera, "
                "plain grey background, character concept art, "
                "full body visible from head to toe"
            ),
            "face_closeup": (
                f"Close-up portrait of {desc}, "
                "neutral expression, face centered in frame, "
                "plain grey background, detailed facial features, focus on face"
            ),
        }

        for shot, prompt in shots.items():
            if count > 0:
                time.sleep(DELAY)
            count += 1
            path = out / f"{shot}.png"
            print(f"  [{count}/{total}] {name}/{outfit}/{shot}...")
            try:
                r = generate_character_image(prompt, path)
                results.append(r)
            except Exception as e:
                print(f"    ERROR: {e}")

    print(f"  Outfits done: {len(results)}/{total}")
    return results

# ============================================================
# TASK 4: ENVIRONMENT REFERENCES
# ============================================================
ENVIRONMENTS = {
    "L1_flower_shop": (
        "Interior of a small flower shop at night, "
        "warm amber lighting from overhead practical lamp, "
        "flowers arranged on shelves and counters, "
        "small cozy space, tungsten warmth, "
        "intimate atmosphere, slightly melancholic, "
        "no people, empty shop interior"
    ),
    "L1_flower_shop_dark": (
        "Interior of a small flower shop at night with lights dimmed, "
        "shadows across wilting flowers, cold undertones creeping in, "
        "dim lighting, moonlight through window, "
        "oppressive and lonely atmosphere, "
        "no people, empty dark shop"
    ),
    "L2_duchess_club": (
        "Interior of an upscale underground club, "
        "neon signs casting blue and purple reflections, "
        "cold backlight, dark leather furniture, "
        "elegant and dangerous atmosphere, "
        "empty VIP booth area, low-key lighting, "
        "no people, predatory elegance"
    ),
    "L3_rainy_street": (
        "Rain-soaked city street at night, "
        "orange sodium streetlight reflecting on wet pavement, "
        "rain streaks visible against backlight, "
        "puddles reflecting neon signs in distance, "
        "lonely and tense atmosphere, "
        "no people, empty wet street"
    ),
    "L4_park_bench": (
        "Park bench under a tree during afternoon, "
        "soft natural daylight, dappled shadows through leaves, "
        "faded green grass, warm golden tones, "
        "peaceful but bittersweet atmosphere, "
        "no people, empty park bench"
    ),
    "L5_dark_alley": (
        "Narrow dark alley at night, "
        "minimal light, distant neon glow reflecting on wet brick walls, "
        "claustrophobic and secretive atmosphere, "
        "deep shadows, single distant light source, "
        "no people, empty dark passage"
    ),
    "L6_police_office": (
        "Police detective desk area, "
        "fluorescent overhead lighting mixed with desk lamp, "
        "case files and papers on desk, "
        "institutional grey walls, functional furniture, "
        "serious professional atmosphere, "
        "no people, empty office"
    ),
}

def generate_environments():
    print("\n" + "=" * 60)
    print("PHASE 4: Environment References")
    print("=" * 60)
    ENV_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    count = 0
    total = len(ENVIRONMENTS)

    for loc_name, prompt in ENVIRONMENTS.items():
        if count > 0:
            time.sleep(DELAY)
        count += 1
        path = ENV_DIR / f"{loc_name}.png"
        print(f"  [{count}/{total}] {loc_name}...")
        try:
            r = generate_character_image(prompt, path)
            results.append(r)
        except Exception as e:
            print(f"    ERROR: {e}")

    print(f"  Environments done: {len(results)}/{total}")
    return results

# ============================================================
# MAIN
# ============================================================
TASKS = {
    "angles": generate_angles,
    "actions": generate_actions,
    "outfits": generate_outfits,
    "environments": generate_environments,
}

def main():
    requested = [a.lower() for a in sys.argv[1:]] if len(sys.argv) > 1 else list(TASKS.keys())
    to_run = {k: v for k, v in TASKS.items() if k in requested}

    if not to_run:
        print(f"Unknown task(s): {requested}")
        print(f"Available: {list(TASKS.keys())}")
        sys.exit(1)

    print("=" * 60)
    print("Ember - Pre-Production Asset Generator")
    print("=" * 60)
    print(f"Tasks: {', '.join(to_run.keys())}")
    print("=" * 60)

    all_results = []
    for task_name, fn in to_run.items():
        results = fn()
        all_results.extend(results)

    print("\n" + "=" * 60)
    print(f"ALL DONE! Generated {len(all_results)} images total.")
    print("=" * 60)


if __name__ == "__main__":
    main()
