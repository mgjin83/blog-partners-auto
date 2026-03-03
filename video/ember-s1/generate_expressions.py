#!/usr/bin/env python3
"""Generate expression sheet images for Ember characters.

Usage:
    python scripts/generate_expressions.py              # All characters
    python scripts/generate_expressions.py luna          # One character
    python scripts/generate_expressions.py luna duchess   # Specific characters
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

# --- Character base descriptions (same as generate_characters.py) ---

CHARACTER_BASE_DESC = {
    "luna": (
        "++young woman with auburn hair++, "
        "auburn hair, green eyes, fair skin with freckles, "
        "average build, florist apron over simple dark clothes, "
        "almond-shaped expressive eyes"
    ),
    "ash": (
        "++young man with dark brown hair++, "
        "dark brown messy hair, hazel eyes, "
        "tall broad build, casual clothes with hoodie, "
        "round warm-looking eyes"
    ),
    "duchess": (
        "++elegant woman with platinum blonde hair++, "
        "platinum blonde hair, ice blue eyes, porcelain skin, "
        "elegant build, luxurious dark clothing, jewelry, "
        "large piercing slightly narrowed eyes"
    ),
    "milo": (
        "++young man with sandy blonde hair++, "
        "sandy blonde hair, warm features, warm brown eyes, "
        "average build, police uniform, "
        "warm open honest-looking eyes"
    ),
}

# --- Character-specific expressions (from character_sheets/*.md) ---

EXPRESSIONS = {
    "luna": [
        ("determination", "determined expression, jaw set, eyes focused forward"),
        ("fear", "fearful expression, wide eyes, brow furrowed"),
        ("anger", "angry expression, narrowed eyes, tense face"),
        ("sadness", "sad expression, downcast eyes, subtle grief"),
        ("resignation", "resigned expression, weary eyes, hollow gaze"),
        ("cold_composure", "cold composed expression, emotionless face, guarded eyes"),
    ],
    "ash": [
        ("determination", "determined expression, jaw set, eyes focused forward"),
        ("fear", "fearful expression, wide eyes, brow furrowed"),
        ("anger", "angry expression, narrowed eyes, bared teeth slightly"),
        ("sadness", "sad expression, downcast eyes, heavy grief"),
        ("resignation", "resigned expression, weary eyes, slumped"),
        ("cold_composure", "cold composed expression, emotionless stare"),
    ],
    "duchess": [
        ("cold_composure", "cold composed expression, regal and unreadable"),
        ("predatory_smile", "subtle predatory smile, one corner of mouth raised, dangerous elegance"),
        ("displeasure", "displeased expression, slightly narrowed eyes, raised chin"),
        ("contempt", "contemptuous expression, looking down, dismissive gaze"),
        ("controlled_anger", "controlled anger, icy stare, barely contained fury"),
        ("possessive_satisfaction", "possessive satisfied expression, owning smile, calculating eyes"),
    ],
    "milo": [
        ("concern", "concerned expression, worried eyes, furrowed brow"),
        ("suspicion", "suspicious expression, slightly narrowed eyes, studying gaze"),
        ("quiet_disappointment", "quietly disappointed expression, hurt eyes, closed mouth"),
        ("determination", "determined expression, firm jaw, resolute eyes"),
        ("warmth", "warm expression, gentle eyes, soft caring look"),
        ("cold_silence", "cold silent expression, blank stare, emotionally shut down"),
    ],
}

OUTPUT_DIR = project_root / "characters" / "reference_images"
DELAY_BETWEEN = 5  # seconds between API calls


def main():
    requested = [a.lower() for a in sys.argv[1:]] if len(sys.argv) > 1 else list(CHARACTER_BASE_DESC.keys())
    targets = [k for k in CHARACTER_BASE_DESC if k in requested]

    if not targets:
        print(f"Unknown character(s): {requested}")
        print(f"Available: {list(CHARACTER_BASE_DESC.keys())}")
        sys.exit(1)

    total = sum(len(EXPRESSIONS[c]) for c in targets)
    print("=" * 60)
    print("Ember - Expression Sheet Generator")
    print("=" * 60)
    print(f"Characters: {', '.join(targets)}")
    print(f"Total images to generate: {total}")
    print("=" * 60)

    all_results = []
    img_count = 0

    for char_name in targets:
        base_desc = CHARACTER_BASE_DESC[char_name]
        expressions = EXPRESSIONS[char_name]
        char_dir = OUTPUT_DIR / char_name / "expressions"
        char_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n--- {char_name.upper()} ({len(expressions)} expressions) ---")

        for expr_name, expr_desc in expressions:
            if img_count > 0:
                time.sleep(DELAY_BETWEEN)

            prompt = (
                f"Close-up portrait of {base_desc}, "
                f"{expr_desc}, "
                "face centered in frame, plain grey background, "
                "detailed facial features, focus on face"
            )
            path = char_dir / f"{expr_name}.png"
            img_count += 1
            print(f"  [{img_count}/{total}] {char_name}/{expr_name}...")

            try:
                result = generate_character_image(prompt, path)
                all_results.append(result)
            except Exception as e:
                print(f"    ERROR: {e}")

    print("\n" + "=" * 60)
    print(f"Done! Generated {len(all_results)}/{total} expression images.")
    for p in all_results:
        print(f"  {p}")
    print("=" * 60)


if __name__ == "__main__":
    main()
