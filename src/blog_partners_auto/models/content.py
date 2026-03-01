"""Shared data models for content artifacts."""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Keyword(BaseModel):
    """A single SEO keyword with metrics."""

    term: str
    language: str
    search_volume: Optional[int] = None
    difficulty: Optional[float] = None
    cpc: Optional[float] = None
    is_primary: bool = False


class BlogPost(BaseModel):
    """A completed blog post artifact."""

    title: str
    meta_description: str = ""
    content_markdown: str = ""
    keywords: list[Keyword] = Field(default_factory=list)
    language: str = "en"
    word_count: int = 0
    image_prompts: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.now)


class ShortsScript(BaseModel):
    """A YouTube Shorts script artifact."""

    title: str
    hook: str = ""
    scenes: list[dict] = Field(default_factory=list)
    cta: str = ""
    hashtags: list[str] = Field(default_factory=list)
    thumbnail_prompt: str = ""
    language: str = "en"
    duration_seconds: int = 0
    created_at: datetime = Field(default_factory=datetime.now)
