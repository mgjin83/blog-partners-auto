"""Character reference image generator using Google Gemini (Nano Banana)."""

import base64
import os
import re
import time
from pathlib import Path

from google import genai
from google.genai.types import GenerateContentConfig


# --- Style Lock & Negative Prompt (style_guide.md Section 1) ---

STYLE_LOCK = (
    "cinematic, shallow depth of field, film noir aesthetic, "
    "desaturated color palette, high contrast, low-key lighting, "
    "anamorphic lens, professional color grading"
)

NEGATIVE_PROMPT = (
    "blur, distortion, watermark, text overlay, low quality, flickering, "
    "morphing faces, extra limbs, bright colors, cartoon, anime, pixar, "
    "smiling, oversaturated, plastic look, CGI artifacts, inconsistent lighting"
)

CHARACTER_BASE = "cat face, human body"

# Model fallback order for image generation
IMAGE_MODELS = [
    "gemini-2.0-flash-exp-image-generation",
    "gemini-2.5-flash-image",
    "nano-banana-pro-preview",
    "imagen-4.0-generate-001",
]

MAX_RETRIES = 3
BASE_DELAY = 20  # seconds


def _build_prompt(raw_prompt: str) -> str:
    """Append Style Lock and Negative Prompt to raw prompt."""
    lines = [
        raw_prompt.strip(),
        STYLE_LOCK,
        f"Negative prompt: {NEGATIVE_PROMPT}",
    ]
    return "\n".join(lines)


def _get_client() -> genai.Client:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY not set in environment")
    return genai.Client(api_key=api_key)


def _extract_retry_delay(error_msg: str) -> float:
    """Extract retry delay from API error message."""
    match = re.search(r"retry in (\d+\.?\d*)s", str(error_msg))
    if match:
        return float(match.group(1)) + 2  # add buffer
    return BASE_DELAY


def _load_reference_image(ref_path: str | Path) -> "genai.types.Part":
    """Load a reference image as a Gemini Part for multimodal input."""
    from google.genai.types import Part

    ref_path = Path(ref_path)
    data = ref_path.read_bytes()
    ext = ref_path.suffix.lower()
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "webp": "image/webp"}.get(ext.lstrip("."), "image/png")
    return Part.from_bytes(data=data, mime_type=mime)


def generate_character_image(
    prompt: str,
    save_path: str | Path,
    model: str | None = None,
    reference_image: str | Path | None = None,
) -> Path:
    """Generate a single character image and save it.

    Args:
        prompt: Raw image generation prompt (Style Lock will be appended).
        save_path: File path to save the generated image.
        model: Model name override. Defaults to first available IMAGE_MODELS.
        reference_image: Path to a reference image for character consistency.

    Returns:
        Path to the saved image file.
    """
    client = _get_client()
    full_prompt = _build_prompt(prompt)
    models_to_try = [model] if model else IMAGE_MODELS

    # Build contents: reference image + text prompt
    if reference_image:
        ref_part = _load_reference_image(reference_image)
        contents = [
            ref_part,
            (
                "Using the character in the reference image above as the EXACT SAME character "
                "(same face pattern, same eye color, same fur markings, same color palette), "
                "generate a new image. Keep the same colors as the reference — do NOT convert to black and white.\n\n"
                + full_prompt
            ),
        ]
    else:
        contents = full_prompt

    save_path = Path(save_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)

    last_error = None
    for model_name in models_to_try:
        for attempt in range(MAX_RETRIES):
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
                        print(f"  Saved: {save_path} (model: {model_name})")
                        return save_path

                raise RuntimeError(
                    f"No image in response. Text: "
                    f"{[p.text for p in response.candidates[0].content.parts if p.text]}"
                )

            except Exception as e:
                last_error = e
                error_str = str(e)

                if "429" in error_str or "RESOURCE_EXHAUSTED" in error_str:
                    if "limit: 0" in error_str:
                        print(f"  Model {model_name}: quota is 0 (not available on current tier)")
                        break  # skip retries, try next model

                    delay = _extract_retry_delay(error_str)
                    print(f"  Rate limited (attempt {attempt+1}/{MAX_RETRIES}), waiting {delay:.0f}s...")
                    time.sleep(delay)
                    continue

                if "404" in error_str or "NOT_FOUND" in error_str:
                    print(f"  Model {model_name}: not found, trying next...")
                    break  # try next model

                raise  # unexpected error, don't retry

    raise RuntimeError(
        f"All models failed. Last error: {last_error}"
    )


def generate_character_pack(
    character_name: str,
    character_config: dict,
    output_dir: str | Path = "characters/reference_images",
    delay_between: float = 5.0,
) -> list[Path]:
    """Generate a character reference image pack.

    Args:
        character_name: Character name (e.g., "luna").
        character_config: Dict with keys: breed, eyes, build, outfit, extras.
        output_dir: Base directory for reference images.
        delay_between: Delay between API calls in seconds.

    Returns:
        List of paths to generated images.
    """
    output_dir = Path(output_dir) / character_name
    output_dir.mkdir(parents=True, exist_ok=True)

    breed = character_config["breed"]
    eyes = character_config["eyes"]
    build = character_config["build"]
    outfit = character_config.get("outfit", "")
    extras = character_config.get("extras", "")

    base_desc = f"++{breed}, {CHARACTER_BASE}++, {eyes}, {build}"
    if outfit:
        base_desc += f", {outfit}"
    if extras:
        base_desc += f", {extras}"

    prompts = {
        "fullbody_front": (
            f"Full body front view of {base_desc}, "
            "standing in a neutral pose facing the camera, "
            "plain grey background, character concept art, "
            "full body visible from head to toe"
        ),
        "face_closeup": (
            f"Close-up portrait of {base_desc}, "
            "neutral expression, face centered in frame, "
            "plain grey background, detailed facial features, "
            "focus on face"
        ),
    }

    saved = []
    for i, (shot_name, prompt) in enumerate(prompts.items()):
        if i > 0:
            time.sleep(delay_between)
        path = output_dir / f"{shot_name}.png"
        print(f"Generating {character_name}/{shot_name}...")
        try:
            result = generate_character_image(prompt, path)
            saved.append(result)
        except Exception as e:
            print(f"  ERROR: {e}")

    return saved
