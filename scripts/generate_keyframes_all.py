#!/usr/bin/env python3
"""Generate shot keyframes for all Ember Season 1 episodes (EP02-EP10).

Each scene keyframe uses the relevant character's face_closeup as
multimodal reference to maintain face consistency.

Usage:
    python scripts/generate_keyframes_all.py              # All episodes
    python scripts/generate_keyframes_all.py ep02          # One episode
    python scripts/generate_keyframes_all.py ep02 ep05     # Specific episodes
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
KEYFRAME_DIR = project_root / "characters" / "shot_keyframes"
DELAY = 5

# ============================================================
# EP02 — "The Deal"
# ============================================================
EP02 = {
    "s1": {
        "filename": "ep02_s1_hook.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Wide shot of a rain-soaked city street at night, "
            "a calico cat-face figure in a dark long coat walking toward camera, "
            "neon signs reflecting blue and purple in puddles, "
            "single orange streetlight behind, rain streaks visible against backlight, "
            "lonely determined walk, 9:16 vertical composition"
        ),
    },
    "s2": {
        "filename": "ep02_s2_club_entry.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot of a calico cat-face figure with green eyes pushing open a heavy door, "
            "transitioning from grey rain outside to cold blue neon flooding in from club interior, "
            "dramatic lighting contrast warm-to-cold, sleek dark surfaces, "
            "9:16 vertical composition"
        ),
    },
    "s3": {
        "filename": "ep02_s3_duchess_appears.png",
        "ref_chars": ["duchess"],
        "prompt": (
            "Low-angle medium shot of a persian cat-face figure with fluffy white fur and blue eyes, "
            "seated on a dark leather sofa, blue neon backlight reflecting on white fur, "
            "luxurious dark clothing with jewelry glowing, holding a wine glass, "
            "seemingly kind but dangerous smile, cold elegant club interior, "
            "9:16 vertical composition"
        ),
    },
    "s4": {
        "filename": "ep02_s4_the_deal.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Over-the-shoulder shot from behind an elegant figure toward a calico cat-face figure "
            "with green eyes sitting opposite, cold blue neon lighting, "
            "the calico figure half in shadow holding a phone with a warm photo glowing on screen, "
            "tense negotiation atmosphere, dark club interior, "
            "9:16 vertical composition"
        ),
    },
    "s5": {
        "filename": "ep02_s5_phone_transition.png",
        "ref_chars": [],
        "prompt": (
            "Extreme close-up of a phone screen showing a warm sunny photo "
            "of two cat-face figures smiling together in sunlight, "
            "surrounded by cold blue neon darkness of a club, "
            "warm light from screen contrasting with cold environment, "
            "nostalgic and bittersweet, 9:16 vertical composition"
        ),
    },
    "s6": {
        "filename": "ep02_s6_luna_exit.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot from behind of a calico cat-face figure walking away "
            "through a dark club toward a grey exit door where rain is visible outside, "
            "figure growing smaller in the dark corridor, blue neon fading behind, "
            "lonely determined departure, 9:16 vertical composition"
        ),
    },
    "s7": {
        "filename": "ep02_s7_end.png",
        "ref_chars": ["duchess"],
        "prompt": (
            "Close-up portrait of a persian cat-face figure with fluffy white fur and blue eyes, "
            "watching an exit door with a slow possessive smile spreading across face, "
            "holding wine glass, cold blue neon lighting in club interior, "
            "predatory satisfaction, dangerous and calculating, "
            "9:16 vertical composition, focus on face"
        ),
    },
}

# ============================================================
# EP03 — "Delivery"
# ============================================================
EP03 = {
    "s1": {
        "filename": "ep03_s1_hook.png",
        "ref_chars": [],
        "prompt": (
            "High-angle shot of a dark narrow alley at night, "
            "a small silhouette figure in a dark coat walking deeper carrying a package, "
            "wet brick walls on both sides, distant neon glow reflecting on wet ground, "
            "claustrophobic and tense atmosphere, "
            "9:16 vertical composition"
        ),
    },
    "s2": {
        "filename": "ep03_s2_delivery.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot of a calico cat-face figure with green eyes in a dark coat, "
            "extending a package toward a shadowy figure at the end of a dark alley, "
            "the receiving hands trembling, minimal light from above, "
            "tense exchange atmosphere, 9:16 vertical composition"
        ),
    },
    "s3": {
        "filename": "ep03_s3_luna_exit.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot from behind of a calico cat-face figure walking away "
            "through a dark alley toward a distant orange streetlight, "
            "stepping from darkness into sodium light, "
            "anxiety visible in posture, wet brick walls, "
            "9:16 vertical composition"
        ),
    },
    "s4": {
        "filename": "ep03_s4_package_opens.png",
        "ref_chars": [],
        "prompt": (
            "Close-up of a shadowy cat-face figure opening a package in a dark alley, "
            "contents not visible but face illuminated showing pure terror, "
            "wide eyes, mouth open, hands trembling, "
            "minimal harsh overhead light, deep shadows, "
            "9:16 vertical composition"
        ),
    },
    "s5": {
        "filename": "ep03_s5_phone_call.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot of a calico cat-face figure with green eyes standing under an orange streetlight, "
            "holding a phone to ear with a forced smile that doesnt reach the eyes, "
            "orange sodium light casting warm glow on face, dark street behind, "
            "lonely and emotionally exhausted, 9:16 vertical composition"
        ),
    },
    "s6": {
        "filename": "ep03_s6_hands_trembling.png",
        "ref_chars": [],
        "prompt": (
            "Extreme close-up of trembling hands under orange streetlight, "
            "slowly clenching into tight fists, trembling stopping, "
            "orange sodium light on skin, dark background, "
            "symbolic moment of control, shallow depth of field, "
            "9:16 vertical composition"
        ),
    },
    "s7": {
        "filename": "ep03_s7_end.png",
        "ref_chars": ["milo"],
        "prompt": (
            "Medium shot from inside a patrol car, "
            "an orange tabby cat-face figure with amber eyes in the driver seat, "
            "watching a distant figure in a dark coat exiting an alley across the street, "
            "expression hardening with suspicion, "
            "orange streetlight through windshield, dashboard visible, "
            "9:16 vertical composition"
        ),
    },
}

# ============================================================
# EP04 — "The Crack"
# ============================================================
EP04 = {
    "s1": {
        "filename": "ep04_s1_hook.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Wide shot of a grey overcast street in daytime, "
            "park with benches visible in background, "
            "a small calico cat-face figure walking alone with arms crossed hugging herself, "
            "flat overcast light with no shadows, muted colors, "
            "lonely and vulnerable atmosphere, 9:16 vertical composition"
        ),
    },
    "s2": {
        "filename": "ep04_s2_milo_appears.png",
        "ref_chars": ["milo"],
        "prompt": (
            "Medium two-shot on a grey overcast street, "
            "an orange tabby cat-face figure with amber eyes grabbing the arm of a calico cat-face figure, "
            "the orange tabby showing worry mixed with anger in casual clothes, "
            "overcast daylight, muted tones, tense confrontation, "
            "9:16 vertical composition"
        ),
    },
    "s3": {
        "filename": "ep04_s3_luna_rejection.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Close-up of a calico cat-face figure with green eyes pulling her arm free, "
            "looking up with cold determination, jaw set, eyes guarded, "
            "overcast street background blurred, flat grey light, "
            "emotional wall being built, 9:16 vertical composition, focus on face"
        ),
    },
    "s4": {
        "filename": "ep04_s4_milo_shock.png",
        "ref_chars": ["milo"],
        "prompt": (
            "Medium shot of an orange tabby cat-face figure with amber eyes standing still in shock, "
            "a calico figure walking away growing smaller in the background, "
            "park bench visible behind under a tree, overcast grey light, "
            "distance widening between them, emotional separation, "
            "9:16 vertical composition"
        ),
    },
    "s5": {
        "filename": "ep04_s5_park_bench.png",
        "ref_chars": [],
        "prompt": (
            "Medium shot of an empty park bench under a large tree, "
            "fallen leaves scattered on the seat, overcast daylight filtering through bare branches, "
            "melancholic and abandoned atmosphere, no people, "
            "symbolic of lost connection, muted autumn colors, "
            "9:16 vertical composition"
        ),
    },
    "s6": {
        "filename": "ep04_s6_end.png",
        "ref_chars": ["milo"],
        "prompt": (
            "Medium shot of an orange tabby cat-face figure with amber eyes sitting at a desk, "
            "opening a case file in a dim police office, "
            "a photo of a persian cat-face figure visible inside the file, "
            "fluorescent overhead light mixed with desk lamp, "
            "eyes narrowing with suspicion, camera pushing in, "
            "9:16 vertical composition"
        ),
    },
}

# ============================================================
# EP05 — "Hands Dirty"
# ============================================================
EP05 = {
    "s1": {
        "filename": "ep05_s1_hook.png",
        "ref_chars": [],
        "prompt": (
            "Medium shot of a dark cramped room interior, "
            "door opening with bright light flooding from behind, "
            "a silhouette figure in a dark coat standing in the doorway, "
            "face hidden by backlight, imposing posture, "
            "dramatic contrast between dark room and bright doorway, "
            "9:16 vertical composition"
        ),
    },
    "s2": {
        "filename": "ep05_s2_collection.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot inside a dark room, "
            "a calico cat-face figure with green eyes seated at a table with calm steady expression, "
            "a trembling figure opposite pushing money across the table with shaking hands, "
            "a small flower vase on the table between them, "
            "harsh overhead light, tense and intimidating atmosphere, "
            "9:16 vertical composition"
        ),
    },
    "s3": {
        "filename": "ep05_s3_talent_recognition.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Close-up of a calico cat-face figure with green eyes pausing at a doorway, "
            "face partially lit by corridor light, "
            "green eyes showing a flash of surprise at her own capability, "
            "half shadow half light on face, introspective moment, "
            "9:16 vertical composition, focus on face"
        ),
    },
    "s4": {
        "filename": "ep05_s4_alley.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot of a calico cat-face figure leaning against a wet brick wall, "
            "bent forward in distress in a dark alley, "
            "distant neon glow reflecting on wet surfaces, "
            "emotional breakdown after composure, physical revulsion, "
            "9:16 vertical composition"
        ),
    },
    "s5": {
        "filename": "ep05_s5_empty_room.png",
        "ref_chars": [],
        "prompt": (
            "Extreme close-up of a small flower vase on a bare wooden table, "
            "the only object remaining in a dark empty room, "
            "overhead light casting a harsh circle of light on the table, "
            "peaceful object in an unsettling context, "
            "symbolic and haunting still life, "
            "9:16 vertical composition"
        ),
    },
    "s6": {
        "filename": "ep05_s6_end.png",
        "ref_chars": ["duchess"],
        "prompt": (
            "Medium shot of a persian cat-face figure with white fur and blue eyes, "
            "watching a CCTV monitor showing a grainy black-and-white figure exiting an alley, "
            "holding wine glass with a satisfied smile, "
            "cold blue neon lighting in club interior, "
            "surveillance and control atmosphere, "
            "9:16 vertical composition"
        ),
    },
}

# ============================================================
# EP06 — "Roots"
# ============================================================
EP06 = {
    "s1": {
        "filename": "ep06_s1_hook.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Wide shot of a dark flower shop interior at night with lights off, "
            "only moonlight through the window, silhouettes of flowers everywhere, "
            "a calico cat-face figure in the background removing an apron, "
            "a jacket draped on a chair, quiet intimate atmosphere, "
            "9:16 vertical composition"
        ),
    },
    "s2": {
        "filename": "ep06_s2_receipt_discovery.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Close-up of a calico cat-face figure with green eyes, "
            "holding a crumpled receipt, eyes widening as she reads it, "
            "moonlit flower shop interior, pale cold light on face and paper, "
            "shock and dawning realization, hands beginning to tremble, "
            "9:16 vertical composition, focus on face and receipt"
        ),
    },
    "s3": {
        "filename": "ep06_s3_receipt_closeup.png",
        "ref_chars": [],
        "prompt": (
            "Extreme close-up of a crumpled receipt held by trembling hands, "
            "pale moonlight illuminating the paper showing a date and amount, "
            "shallow depth of field, dark flower shop background, "
            "evidence of hidden truth, symbolic revelation, "
            "9:16 vertical composition"
        ),
    },
    "s4": {
        "filename": "ep06_s4_weight_of_truth.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot of a calico cat-face figure with green eyes "
            "sitting on the floor among flower silhouettes in a dark shop, "
            "holding a crumpled receipt, tears running down face, "
            "moonlight casting long shadows through the window, "
            "devastated and overwhelmed, 9:16 vertical composition"
        ),
    },
    "s5": {
        "filename": "ep06_s5_end.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Close-up of a calico cat-face figure sitting motionless on a dark flower shop floor, "
            "a single petal falling onto her still hand, "
            "tears glistening in pale moonlight, completely still, "
            "time passing indicated by moonlight shifting, "
            "9:16 vertical composition"
        ),
    },
}

# ============================================================
# EP07 — "The File"
# ============================================================
EP07 = {
    "s1": {
        "filename": "ep07_s1_hook.png",
        "ref_chars": [],
        "prompt": (
            "Extreme close-up of an elegant hand with jewelry pushing a manila envelope "
            "across a dark polished table, neon blue reflections on the glossy surface, "
            "cold club interior atmosphere, suspenseful moment, "
            "shallow depth of field, 9:16 vertical composition"
        ),
    },
    "s2": {
        "filename": "ep07_s2_instructions.png",
        "ref_chars": ["duchess"],
        "prompt": (
            "Medium two-shot in a club interior, "
            "a persian cat-face figure with white fur and blue eyes on a dark sofa holding wine glass casually, "
            "a calico cat-face figure opposite picking up a manila envelope from the table, "
            "cold blue neon lighting, tense business atmosphere, "
            "9:16 vertical composition"
        ),
    },
    "s3": {
        "filename": "ep07_s3_refusal.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Close-up of a calico cat-face figure with green eyes reading documents, "
            "eyes widening then hardening as she shakes her head in refusal, "
            "cold blue neon lighting from club interior, "
            "determination and moral conflict on face, "
            "9:16 vertical composition, focus on face"
        ),
    },
    "s4": {
        "filename": "ep07_s4_second_discovery.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Extreme close-up of documents in hands with a visible name on the paper, "
            "a phone screen briefly visible with camera interface, "
            "cold blue neon lighting, "
            "evidence being secretly recorded, desperation in the moment, "
            "9:16 vertical composition"
        ),
    },
    "s5": {
        "filename": "ep07_s5_end.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot of a calico cat-face figure exiting a club into heavy rain, "
            "holding a manila envelope getting wet, "
            "standing still in the rain on a neon-reflected street, "
            "then beginning to walk forward with resolve, "
            "rain-soaked street with colored neon reflections, "
            "9:16 vertical composition"
        ),
    },
}

# ============================================================
# EP08 — "Ash and Bone"
# ============================================================
EP08 = {
    "s1": {
        "filename": "ep08_s1_hook.png",
        "ref_chars": ["milo"],
        "prompt": (
            "Medium shot of an orange tabby cat-face figure with amber eyes "
            "standing before a large evidence board with only scattered pins remaining, "
            "photos and documents gone, eyes widening in shock, "
            "dim police office with fluorescent lighting, "
            "9:16 vertical composition"
        ),
    },
    "s2": {
        "filename": "ep08_s2_evidence_gone.png",
        "ref_chars": ["milo"],
        "prompt": (
            "Medium two-shot in a dim police office, "
            "a stern figure in uniform speaking to an orange tabby cat-face figure with amber eyes, "
            "the orange tabby's eyes hardening and fist clenching with restrained anger, "
            "fluorescent overhead light, institutional grey walls, "
            "9:16 vertical composition"
        ),
    },
    "s3": {
        "filename": "ep08_s3_park_reunion.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Wide shot of a park with a bench under a large tree, "
            "a calico cat-face figure with green eyes sitting alone on the bench with fallen leaves, "
            "an orange tabby figure walking slowly toward her from a distance, "
            "afternoon sun filtered through branches but shadow covering the bench, "
            "bittersweet reunion atmosphere, 9:16 vertical composition"
        ),
    },
    "s4": {
        "filename": "ep08_s4_milo_goodbye.png",
        "ref_chars": ["milo"],
        "prompt": (
            "Close-up two-shot at a park bench, "
            "an orange tabby cat-face figure with amber eyes filled with quiet sorrow looking down, "
            "a calico cat-face figure looking up with tears forming in green eyes, "
            "afternoon light through tree branches, dappled shadows, "
            "emotional farewell moment, 9:16 vertical composition, focus on faces"
        ),
    },
    "s5": {
        "filename": "ep08_s5_end.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot of a calico cat-face figure with green eyes "
            "sitting alone on a park bench under a tree in deep shadow, "
            "a single petal falling onto her lap, "
            "a phone on the bench glowing with missed calls, buzzing unanswered, "
            "afternoon light fading, profound loneliness, "
            "9:16 vertical composition"
        ),
    },
}

# ============================================================
# EP09 — "The Cost"
# ============================================================
EP09 = {
    "s1": {
        "filename": "ep09_s1_hook.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot of a flower shop interior with closed blinds, "
            "thin strips of light through slats creating striped pattern on flowers, "
            "a calico cat-face figure with green eyes arranging flowers in striped light, "
            "door bursting open with bright daylight and a grey tabby silhouette in the doorway, "
            "dramatic contrast, 9:16 vertical composition"
        ),
    },
    "s2": {
        "filename": "ep09_s2_ash_anger.png",
        "ref_chars": ["ash"],
        "prompt": (
            "Medium two-shot in a dim flower shop, "
            "a grey tabby cat-face figure with yellow eyes confronting a calico cat-face figure, "
            "the grey tabby showing rage mixed with despair, "
            "the calico figure looking up with calm exhaustion in green eyes, "
            "striped light through blinds, tense confrontation, "
            "9:16 vertical composition"
        ),
    },
    "s3": {
        "filename": "ep09_s3_silence.png",
        "ref_chars": ["ash"],
        "prompt": (
            "Close-up of a grey tabby cat-face figure with yellow eyes, "
            "tears forming as rage dissolves into grief, "
            "a hand reaching out slowly toward him but he steps back, "
            "dim flower shop with striped light, raw emotional moment, "
            "9:16 vertical composition, focus on face"
        ),
    },
    "s4": {
        "filename": "ep09_s4_ash_exit.png",
        "ref_chars": ["ash"],
        "prompt": (
            "Medium shot of a grey tabby cat-face figure walking to a door with back to camera, "
            "pausing at the threshold, pushing through into bright daylight outside, "
            "the flower shop falling back into dim striped light behind, "
            "emotional departure, contrast of dark interior and bright exterior, "
            "9:16 vertical composition"
        ),
    },
    "s5": {
        "filename": "ep09_s5_end.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Close-up of a calico cat-face figure with green eyes "
            "standing motionless in a dim flower shop, "
            "a phone buzzing on the counter with a name glowing on screen, "
            "green eyes shifting from grief to something harder — determination, "
            "striped light through blinds, flowers half-arranged on counter, "
            "9:16 vertical composition, focus on face"
        ),
    },
}

# ============================================================
# EP10 — "Ember" (Season Finale)
# ============================================================
EP10 = {
    "s1": {
        "filename": "ep10_s1_hook.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot of a calico cat-face figure with green eyes "
            "standing before a club entrance at night, "
            "neon sign reflecting in rain puddles, "
            "one hand in coat pocket, focused and resolute expression, "
            "taking a breath before stepping forward, "
            "9:16 vertical composition"
        ),
    },
    "s2": {
        "filename": "ep10_s2_last_job.png",
        "ref_chars": ["duchess"],
        "prompt": (
            "Medium two-shot in club interior, "
            "a persian cat-face figure with white fur and blue eyes on sofa pushing an envelope, "
            "a calico cat-face figure opposite taking the envelope "
            "while other hand subtly moves inside coat pocket, "
            "cold blue neon, tense final meeting, "
            "9:16 vertical composition"
        ),
    },
    "s3": {
        "filename": "ep10_s3_evidence_delivery.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Close-up of hands pulling a thick envelope from inside a coat, "
            "pushing the envelope into a mailbox slot, "
            "a police station address partially visible on the envelope, "
            "rain falling, single orange streetlight casting warm glow, "
            "night scene, act of courage, "
            "9:16 vertical composition"
        ),
    },
    "s4a": {
        "filename": "ep10_s4a_milo_evidence.png",
        "ref_chars": ["milo"],
        "prompt": (
            "Medium shot of an orange tabby cat-face figure with amber eyes at a desk, "
            "opening an envelope with CCTV screenshots and documents spilling out, "
            "eyes widening with realization, "
            "fluorescent office lighting, desk lamp, "
            "9:16 vertical composition"
        ),
    },
    "s4b": {
        "filename": "ep10_s4b_club_raid.png",
        "ref_chars": [],
        "prompt": (
            "Wide shot of police officers entering an upscale club, "
            "neon signs flickering and dying, blue and purple lights going dark, "
            "dramatic raid scene, flashlights cutting through darkness, "
            "cold atmosphere disrupted by authority, "
            "9:16 vertical composition"
        ),
    },
    "s4c": {
        "filename": "ep10_s4c_duchess_arrested.png",
        "ref_chars": ["duchess"],
        "prompt": (
            "Medium shot of a persian cat-face figure with white fur and blue eyes "
            "being led away by officers outside the club, "
            "blue eyes wide with shock and disbelief, "
            "neon signs dark behind, cold night air, "
            "fall from power, 9:16 vertical composition"
        ),
    },
    "s4d": {
        "filename": "ep10_s4d_luna_news.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Close-up of a calico cat-face figure with green eyes in a flower shop, "
            "looking at a phone screen showing news, "
            "warm amber daylight in the shop, "
            "quietly setting the phone down with a complex expression, "
            "relief mixed with weight of what was done, "
            "9:16 vertical composition"
        ),
    },
    "s5": {
        "filename": "ep10_s5_reopening.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot of a flower shop in warm daylight, "
            "a calico cat-face figure with green eyes behind the counter "
            "wrapping flowers for a customer, "
            "warm amber light, peaceful atmosphere, flowers everywhere, "
            "hands perfectly steady, no trembling, "
            "quiet redemption, 9:16 vertical composition"
        ),
    },
    "s6": {
        "filename": "ep10_s6_end.png",
        "ref_chars": ["luna"],
        "prompt": (
            "Medium shot of a calico cat-face figure pulling down a shop shutter at night, "
            "turning to face an empty street, walking alone under a single streetlight, "
            "across the street in darkness a small orange ember of a cigarette glows, "
            "a shadowy figure watching from the shadows, "
            "the calico figure pauses, looks toward the glow, expression unchanged, continues walking, "
            "9:16 vertical composition, ominous and cyclical"
        ),
    },
}

# ============================================================
# ALL EPISODES
# ============================================================
ALL_EPISODES = {
    "ep02": EP02,
    "ep03": EP03,
    "ep04": EP04,
    "ep05": EP05,
    "ep06": EP06,
    "ep07": EP07,
    "ep08": EP08,
    "ep09": EP09,
    "ep10": EP10,
}


def generate_keyframe(ep_key: str, scene_key: str, scene_cfg: dict):
    """Generate a single scene keyframe."""
    filename = scene_cfg["filename"]
    ref_chars = scene_cfg["ref_chars"]
    prompt = scene_cfg["prompt"]

    out_dir = KEYFRAME_DIR / ep_key
    out_dir.mkdir(parents=True, exist_ok=True)
    save_path = out_dir / filename

    ref_image = None
    if ref_chars:
        primary = ref_chars[0]
        ref_path = REF_DIR / primary / "face_closeup.png"
        if ref_path.exists():
            ref_image = ref_path

    ref_label = f"{ref_chars[0]} face_closeup" if ref_image else "none"
    print(f"  {scene_key.upper()}: {filename}  (ref: {ref_label})")

    try:
        result = generate_character_image(prompt, save_path, reference_image=ref_image)
        return result
    except Exception as e:
        print(f"    ERROR: {e}")
        return None


def main():
    requested = [a.lower() for a in sys.argv[1:]] if len(sys.argv) > 1 else list(ALL_EPISODES.keys())
    targets = {k: v for k, v in ALL_EPISODES.items() if k in requested}

    if not targets:
        print(f"Unknown: {requested}. Available: {list(ALL_EPISODES.keys())}")
        sys.exit(1)

    # Count total scenes
    total_scenes = sum(len(scenes) for scenes in targets.values())

    print("=" * 60)
    print("Ember Season 1 — Shot Keyframe Generator")
    print(f"  Episodes: {', '.join(targets.keys())}")
    print(f"  Total scenes: {total_scenes}")
    print("=" * 60)

    all_results = []
    count = 0
    for ep_key, scenes in targets.items():
        print(f"\n{'='*60}")
        print(f"  {ep_key.upper()}")
        print(f"{'='*60}")
        for scene_key, scene_cfg in scenes.items():
            if count > 0:
                time.sleep(DELAY)
            count += 1
            print(f"\n  [{count}/{total_scenes}]", end=" ")
            r = generate_keyframe(ep_key, scene_key, scene_cfg)
            if r:
                all_results.append(r)

    print(f"\n\n{'='*60}")
    print(f"DONE! Generated {len(all_results)}/{total_scenes} keyframes.")
    print("=" * 60)


if __name__ == "__main__":
    main()
