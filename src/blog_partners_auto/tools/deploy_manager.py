"""Content deployment tool for blog and YouTube platforms."""

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class DeployManagerInput(BaseModel):
    content: str = Field(..., description="Content to deploy (markdown or script)")
    channel: str = Field(..., description="Target channel: 'blog' or 'shorts'")
    language: str = Field(..., description="Content language code (ko, en, es)")
    title: str = Field(default="", description="Content title")


class DeployManagerTool(BaseTool):
    name: str = "Deploy Manager"
    description: str = (
        "Deploys finished content to the appropriate platform. "
        "Blog: WordPress, Tistory, Naver Blog. "
        "Shorts: YouTube Studio staging."
    )
    args_schema: Type[BaseModel] = DeployManagerInput

    def _run(
        self, content: str, channel: str, language: str, title: str = ""
    ) -> str:
        # TODO: Integrate with WordPress REST API, Tistory API, YouTube Data API
        return (
            f"[Deployed to {channel}/{language}]\n"
            f"- Title: {title}\n"
            f"- Content Length: {len(content)} chars\n"
            f"- URL: [API integration needed]"
        )
