#!/usr/bin/env python3
"""Generate character reference images for Ember using Gemini image generation.

Usage:
    python scripts/generate_characters.py              # Generate all characters
    python scripts/generate_characters.py luna          # Generate one character
    python scripts/generate_characters.py luna ash      # Generate specific characters
"""

import sys
import time
from pathlib import Path

# Add project root to path
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
generate_character_pack = _mod.generate_character_pack

# --- Character Configs (from character_sheets/*.md + style_guide.md) ---

CHARACTERS = {
    "luna": {
        "breed": "calico cat face, white base with orange and black patches",
        "eyes": "green eyes",
        "build": "average build",
        "outfit": "florist apron over simple dark clothes",
        "extras": "almond-shaped expressive eyes, thin white whiskers",
    },
    "ash": {
        "breed": "grey tabby cat face, grey stripes",
        "eyes": "yellow eyes",
        "build": "larger build",
        "outfit": "casual clothes with hoodie",
        "extras": "round warm-looking eyes, grey whiskers",
    },
    "duchess": {
        "breed": "persian cat face, fluffy white fur, flat face",
        "eyes": "blue eyes",
        "build": "elegant build",
        "outfit": "luxurious dark clothing, jewelry",
        "extras": "large piercing slightly narrowed eyes, white delicate whiskers",
    },
    "milo": {
        "breed": "orange tabby cat face, orange stripes, warm features",
        "eyes": "amber eyes",
        "build": "average build",
        "outfit": "police uniform",
        "extras": "warm open honest-looking eyes, orange-tinted whiskers",
    },
}

OUTPUT_DIR = project_root / "characters" / "reference_images"


DELAY_BETWEEN_CHARACTERS = 10  # seconds between characters to avoid rate limits


def main():
    # Filter characters by CLI args
    requested = [a.lower() for a in sys.argv[1:]] if len(sys.argv) > 1 else list(CHARACTERS.keys())
    targets = {k: v for k, v in CHARACTERS.items() if k in requested}

    if not targets:
        print(f"Unknown character(s): {requested}")
        print(f"Available: {list(CHARACTERS.keys())}")
        sys.exit(1)

    print("=" * 60)
    print("Ember - Character Reference Image Generator")
    print("=" * 60)
    print(f"Output: {OUTPUT_DIR}")
    print(f"Characters: {', '.join(targets.keys())}")
    print("Shots per character: fullbody_front, face_closeup")
    print("=" * 60)

    all_results = []

    for i, (name, config) in enumerate(targets.items()):
        if i > 0:
            print(f"\nWaiting {DELAY_BETWEEN_CHARACTERS}s before next character...")
            time.sleep(DELAY_BETWEEN_CHARACTERS)
        print(f"\n--- {name.upper()} ---")
        results = generate_character_pack(name, config, OUTPUT_DIR)
        all_results.extend(results)

    print("\n" + "=" * 60)
    print(f"Done! Generated {len(all_results)} images.")
    for p in all_results:
        print(f"  {p}")
    print("=" * 60)


if __name__ == "__main__":
    main()
