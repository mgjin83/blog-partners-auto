"""Image generation tool for blog and shorts content."""

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class ImageGeneratorInput(BaseModel):
    prompt: str = Field(..., description="Image generation prompt")
    style: str = Field(
        default="blog_header",
        description="Image style: blog_header, thumbnail, infographic",
    )
    aspect_ratio: str = Field(
        default="16:9",
        description="Aspect ratio (16:9 for blog, 9:16 for shorts, 1:1 for square)",
    )


class ImageGeneratorTool(BaseTool):
    name: str = "Image Generator"
    description: str = (
        "Generates images for blog posts and YouTube Shorts thumbnails. "
        "Supports various styles and aspect ratios."
    )
    args_schema: Type[BaseModel] = ImageGeneratorInput

    def _run(
        self, prompt: str, style: str = "blog_header", aspect_ratio: str = "16:9"
    ) -> str:
        # TODO: Integrate with DALL-E 3, Stable Diffusion, or Midjourney API
        return (
            f"[Image Generated]\n"
            f"- Style: {style}\n"
            f"- Aspect Ratio: {aspect_ratio}\n"
            f"- Prompt: {prompt[:100]}...\n"
            f"- File: [API integration needed]"
        )
