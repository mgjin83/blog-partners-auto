"""Pipeline state model for the master orchestrator flow."""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class Language(str, Enum):
    KO = "ko"
    EN = "en"
    ES = "es"


class Channel(str, Enum):
    BLOG = "blog"
    SHORTS = "shorts"


class LanguageTeamResult(BaseModel):
    """Result from a single language team crew."""

    language: Language
    blog_content: Optional[str] = None
    shorts_script: Optional[str] = None
    keywords: list[str] = Field(default_factory=list)
    blog_url: Optional[str] = None
    shorts_url: Optional[str] = None
    status: str = "pending"


class PipelineState(BaseModel):
    """Structured state for the master orchestrator flow."""

    topic: str = ""
    niche: str = ""
    target_languages: list[Language] = Field(
        default_factory=lambda: [Language.KO, Language.EN, Language.ES]
    )
    target_channels: list[Channel] = Field(
        default_factory=lambda: [Channel.BLOG, Channel.SHORTS]
    )
    ko_result: LanguageTeamResult = Field(
        default_factory=lambda: LanguageTeamResult(language=Language.KO)
    )
    en_result: LanguageTeamResult = Field(
        default_factory=lambda: LanguageTeamResult(language=Language.EN)
    )
    es_result: LanguageTeamResult = Field(
        default_factory=lambda: LanguageTeamResult(language=Language.ES)
    )
    final_report: Optional[str] = None
