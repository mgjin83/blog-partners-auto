#!/usr/bin/env python3
"""Generate character reference images for Harem S1 using Gemini.

Usage:
    python generate_characters.py                    # Generate all (reports count first)
    python generate_characters.py ethan tasha        # Specific characters
    python generate_characters.py --batch 1          # Batch 1: Ethan+Tasha
    python generate_characters.py --batch 2          # Batch 2: Mika+Serena
    python generate_characters.py --batch 3          # Batch 3: Lily+Diana
"""

import sys
import time
from pathlib import Path

project_root = Path(__file__).resolve().parent
repo_root = project_root.parent.parent
sys.path.insert(0, str(repo_root / "src"))

from dotenv import load_dotenv
load_dotenv(repo_root / ".env")

import importlib.util
_spec = importlib.util.spec_from_file_location(
    "image_generator",
    repo_root / "src" / "blog_partners_auto" / "tools" / "image_generator.py",
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
generate_character_image = _mod.generate_character_image

# ─── Output ───
OUTPUT_DIR = project_root / "characters" / "reference_images"
DELAY = 8  # seconds between API calls

# ─── Generation Rule ───
# 1. face_closeup 먼저 생성
# 2. fullbody_diagonal 생성 시 face_closeup을 reference_image로 전달
#    → 같은 얼굴 유지 (얼굴 일관성)
#
# ─── Prompt 기본 원칙 ───
# - 여성 전원: 극도로 예쁘고 날씬하고 가슴 큰 체형
#   남자 독자가 시간 가는 줄 모르고, 여자 독자가 부러워하는 수준
# - 금지 단어: strong features, defined cheekbones, thick, curvy(단독사용), stocky
#   → 얼굴 늙어보이거나 뚱뚱해보이는 원인
# - 필수 키워드: slim, slender, thin waist, long legs, large/prominent bust
# - 비율: 7.5+ head-to-body ratio, small head, long legs
# - 얼굴: youthful, soft, delicate, feminine → 젊고 예쁜 인상 유지

# ─── Common Style Suffix ───
FACE_STYLE = (
    "photorealistic, studio lighting, plain light grey background, "
    "detailed facial features, sharp focus, magazine cover quality, 85mm portrait lens"
)
BODY_STYLE = (
    "photorealistic, fashion editorial photography, plain light grey background, "
    "85mm lens, 7.5 head-to-body ratio, small head proportional to body, "
    "full body visible from head to toe"
)

# ─── Character Prompts ───

CHARACTERS = {
    "ethan": {
        "face_closeup": (
            "Close-up portrait of an incredibly handsome 17-year-old male, "
            "dark brown short neat hair with forehead exposed, deep brown eyes with long thick eyelashes, "
            "soft slim V-line jaw with short compact face proportions, high straight nose bridge, fair clear skin, "
            "strikingly handsome youthful baby-faced look with refined features, shorter oval face shape, "
            "Western Caucasian, bright cheerful natural smile with gentle eyes, "
            + FACE_STYLE
        ),
        "fullbody_diagonal": (
            "Full body three-quarter view of an incredibly handsome 17-year-old male, "
            "175cm slim lean build, slender but toned frame, "
            "dark brown short neat hair, deep brown eyes, slim V-line jaw, "
            "wearing heather grey oversized hoodie and black jogger pants, white sneakers, "
            "standing in natural relaxed pose with one hand in hoodie pocket, "
            + BODY_STYLE
        ),
    },
    "tasha": {
        "face_closeup": (
            "Close-up portrait of a stunningly gorgeous 22-year-old woman, "
            "platinum blonde wavy hair below collarbone, ice blue eyes with long lashes, "
            "fair porcelain skin, full red lips, soft delicate feminine face, "
            "youthful beautiful face, Western Caucasian, Russian-American mixed, "
            "gentle warm inviting expression with soft smile, "
            + FACE_STYLE
        ),
        "fullbody_diagonal": (
            "Full body three-quarter view of a stunningly gorgeous 22-year-old woman, "
            "170cm, slim body with very thin waist and very large F-cup breasts and wide hips, long slender legs, "
            "platinum blonde wavy hair, ice blue eyes, "
            "wearing thin cream knit top clinging tightly to body showing clear bust shape and curves, "
            "very short denim shorts exposing most of thighs and bare legs, "
            "standing with one hip slightly out in relaxed pose, "
            + BODY_STYLE
        ),
    },
    "mika": {
        "face_closeup": (
            "DSLR photograph taken with Canon EOS R5, 85mm f/1.4 lens. "
            "Close-up portrait of a 20-year-old woman with honey brown hair in high ponytail, "
            "bright vivid green eyes with long lashes, light freckles across nose and cheeks, "
            "fair healthy glowing skin with visible pores and natural skin texture, "
            "soft youthful feminine face, small nose, full lips, "
            "Western Caucasian, Russian-American mixed heritage, "
            "confident bright sporty smile, "
            "shot in professional photo studio, single softbox lighting from upper left, "
            "plain light grey seamless paper background, shallow depth of field, "
            "subtle film grain, natural color grading, no retouching, raw unedited look"
        ),
        "fullbody_diagonal": (
            "DSLR photograph taken with Canon EOS R5, 50mm f/1.8 lens. "
            "Full body three-quarter view of a 20-year-old athletic woman, "
            "173cm, slim toned body with thin waist and flat stomach and long slender legs, "
            "large D-cup bust prominent and visible through tight sports bra, bust stretching the fabric, "
            "honey brown hair in high ponytail, bright green eyes, light freckles, "
            "soft youthful baby face, "
            "wearing tight black crop sports bra with bust slightly spilling over the top edge, "
            "low-rise grey biker shorts sitting below hip bones exposing hip line, white running shoes, "
            "standing in confident athletic pose with one hand on hip, bright sporty smile, "
            "shot in professional photo studio, plain light grey seamless paper background, "
            "natural studio lighting, visible skin texture, subtle film grain, "
            "fashion editorial for magazine, raw photo"
        ),
    },
    "serena": {
        "face_closeup": (
            "Close-up portrait of an extremely gorgeous 22-year-old woman, "
            "long straight jet black hair, dark brown eyes with slight cat-eye shape and long lashes, "
            "full red lips, fair smooth skin, elegant feminine face, "
            "youthful beautiful face, Western Caucasian, Italian-American heritage, "
            "confident slight smirk with one eyebrow slightly raised, "
            + FACE_STYLE
        ),
        "fullbody_diagonal": (
            "Full body three-quarter view of an extremely gorgeous 22-year-old woman, "
            "170cm, slim model body with very thin waist and large E-cup bust and very long slender legs, "
            "long straight black hair to waist, dark brown eyes, "
            "wearing deep V-neck black bodycon dress showing deep cleavage, ending mid-thigh, "
            "black strappy heels, thin gold necklace resting on exposed chest, "
            "standing with one hand on hip in confident seductive model pose, "
            + BODY_STYLE
        ),
    },
    "lily": {
        "face_closeup": (
            "DSLR photograph taken with Canon EOS R5, 85mm f/1.4 lens. "
            "Close-up portrait of a 20-year-old woman with short wavy copper-brown bob cut at jawline, "
            "big round hazel eyes, deep dimples on both cheeks, light freckles across nose and cheeks, "
            "fair skin with visible pores and natural skin texture, small upturned nose, full soft lips, "
            "heart-shaped face, youthful face, Western Caucasian Irish-American, "
            "bright natural smile showing dimples, "
            "shot in professional photo studio, single softbox lighting from upper left, "
            "plain light grey seamless paper background, shallow depth of field, "
            "subtle film grain, natural color grading, no retouching, raw unedited look"
        ),
        "fullbody_diagonal": (
            "DSLR photograph taken with Canon EOS R5, 50mm f/1.8 lens. "
            "Full body three-quarter view of a 20-year-old petite woman, "
            "160cm, extremely slim skinny body with very thin waist and thin arms and thin legs, "
            "large heavy bust prominent on her small skinny frame, bust stretching the fabric, "
            "short wavy copper-brown bob, big hazel eyes, dimples, freckles, "
            "wearing oversized light pink hoodie slipping off one shoulder exposing bare shoulder and bra strap, "
            "very short shorts barely visible under the long hoodie, white knee-high socks, pink sneakers, "
            "playful cute pose with slight body tilt, "
            "shot in professional photo studio, plain light grey seamless paper background, "
            "natural studio lighting, visible skin texture, subtle film grain, "
            "fashion editorial for magazine, raw photo, "
            "skinny thin body like a K-pop idol, NO chubby, NO thick thighs, NO round body"
        ),
    },
    "diana": {
        "face_closeup": (
            "Close-up portrait of an extremely beautiful 28-year-old woman, "
            "black sleek bob cut, dark brown elegant eyes with long lashes, "
            "soft youthful feminine face, minimal natural makeup, smooth glowing skin, "
            "photorealistic, East Asian heritage, "
            "warm playful smile with a hint of mischief, "
            + FACE_STYLE
        ),
        "fullbody_diagonal": (
            "Full body three-quarter view of an extremely beautiful 28-year-old woman, "
            "168cm, slim body with very thin waist and very large G-cup breasts extremely prominent and visible through clothing, "
            "deep cleavage visible through open blouse, long slender legs, "
            "black sleek bob cut, "
            "wearing white silk blouse with top three buttons open showing deep cleavage and bra outline visible through thin fabric, "
            "tight cream pencil skirt hugging hips and butt, ending above knee, nude pointed-toe heels, "
            "standing in confident relaxed pose with one hand on hip, "
            + BODY_STYLE
        ),
    },
    "valencia": {
        "face_closeup": (
            "Close-up portrait of an extremely beautiful 21-year-old woman, "
            "voluminous wavy bright red hair past shoulders, warm brown eyes with long lashes, "
            "light golden tan skin, soft youthful feminine baby face, full lips, "
            "photorealistic, Bolivian heritage, Miranda Kerr-like features, "
            "warm confident radiant smile, "
            + FACE_STYLE
        ),
        "fullbody_diagonal": (
            "Full body three-quarter view of an extremely beautiful 21-year-old woman, "
            "168cm, very thin skinny body with extremely thin waist and large F-cup breasts, long slender legs, "
            "voluminous wavy bright red hair past shoulders, warm brown eyes, "
            "light golden tan skin, soft youthful feminine baby face, Bolivian heritage, "
            "wearing deep V-neck fitted red mini dress ending mid-thigh showing cleavage and long bare legs, "
            "nude strappy heels, "
            "standing in confident relaxed pose with one hand on hip, "
            + BODY_STYLE
        ),
    },
}

# ─── Batches (max 5 images per batch) ───
BATCHES = {
    1: ["ethan", "tasha"],       # 4 images
    2: ["mika", "serena"],       # 4 images
    3: ["lily", "diana"],        # 4 images
    4: ["valencia"],             # 2 images
}


def generate_one(name, shot, prompt, reference_image=None):
    """Generate a single image, optionally using a reference for face consistency."""
    out_dir = OUTPUT_DIR / name
    out_dir.mkdir(parents=True, exist_ok=True)
    save_path = out_dir / f"{shot}.png"
    if reference_image:
        print(f"  Generating {name}/{shot} (with face reference)...")
    else:
        print(f"  Generating {name}/{shot}...")
    result = generate_character_image(prompt, save_path, reference_image=reference_image)
    return result


def run(targets: dict):
    """Generate images for given targets.

    Rule: face_closeup is generated first, then used as reference_image
    for all subsequent shots (fullbody_diagonal etc.) to maintain face consistency.
    """
    total = sum(len(shots) for shots in targets.values())
    print("=" * 60)
    print("Harem S1 - Character Reference Image Generator")
    print("=" * 60)
    print(f"Output: {OUTPUT_DIR}")
    print(f"Characters: {', '.join(targets.keys())}")
    print(f"Total images: {total}")
    print(f"Face consistency: ON (face_closeup -> reference for other shots)")
    print("=" * 60)

    if total > 5:
        print(f"WARNING: {total} images exceeds 5-image safety limit!")
        print("Use --batch flag or specify fewer characters.")
        sys.exit(1)

    results = []
    count = 0
    for name, shots in targets.items():
        face_ref = None
        # Ensure face_closeup is generated first
        ordered_shots = sorted(shots.items(), key=lambda x: 0 if x[0] == "face_closeup" else 1)
        for shot_name, prompt in ordered_shots:
            if count > 0:
                print(f"  Waiting {DELAY}s...")
                time.sleep(DELAY)
            try:
                ref = face_ref if shot_name != "face_closeup" else None
                r = generate_one(name, shot_name, prompt, reference_image=ref)
                results.append(r)
                # Save face_closeup path as reference for subsequent shots
                if shot_name == "face_closeup":
                    face_ref = r
            except Exception as e:
                print(f"  ERROR generating {name}/{shot_name}: {e}")
            count += 1

    print("\n" + "=" * 60)
    print(f"Done! Generated {len(results)}/{total} images.")
    for p in results:
        print(f"  {p}")
    print("=" * 60)
    return results


def main():
    args = sys.argv[1:]

    # --batch mode
    if "--batch" in args:
        idx = args.index("--batch")
        batch_num = int(args[idx + 1])
        if batch_num not in BATCHES:
            print(f"Invalid batch: {batch_num}. Available: {list(BATCHES.keys())}")
            sys.exit(1)
        names = BATCHES[batch_num]
        targets = {n: CHARACTERS[n] for n in names}
        run(targets)
        return

    # Specific characters
    if args:
        names = [a.lower() for a in args]
        invalid = [n for n in names if n not in CHARACTERS]
        if invalid:
            print(f"Unknown: {invalid}. Available: {list(CHARACTERS.keys())}")
            sys.exit(1)
        targets = {n: CHARACTERS[n] for n in names}
    else:
        # No args = report only
        total = len(CHARACTERS) * 2
        print("=" * 60)
        print(f"Total characters: {len(CHARACTERS)}")
        print(f"Images per character: 2 (face_closeup + fullbody_diagonal)")
        print(f"Total images: {total}")
        print()
        for batch_num, names in BATCHES.items():
            count = len(names) * 2
            print(f"  Batch {batch_num}: {', '.join(names)} ({count} images)")
        print()
        print("Run with: python generate_characters.py --batch 1")
        print("=" * 60)
        return

    run(targets)


if __name__ == "__main__":
    main()
