"""Global settings loaded from .env file."""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings - all values loaded from .env."""

    # LLM
    openai_api_key: str = ""
    openai_model_name: str = "gpt-4o"

    # Search / SEO
    serper_api_key: str = ""

    # Image Generation
    image_gen_provider: str = "openai"

    # Blog Platforms
    wordpress_url: Optional[str] = None
    wordpress_api_key: Optional[str] = None
    tistory_api_key: Optional[str] = None
    ghost_api_key: Optional[str] = None

    # YouTube
    youtube_api_key: Optional[str] = None

    # Translation
    deepl_api_key: Optional[str] = None

    # General
    output_dir: str = "output"
    log_level: str = "INFO"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
