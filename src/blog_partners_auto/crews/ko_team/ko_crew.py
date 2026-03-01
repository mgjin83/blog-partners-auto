"""Korean language content production crew."""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from blog_partners_auto.tools.seo_analyzer import SEOAnalyzerTool
from blog_partners_auto.tools.translator import TranslatorTool
from blog_partners_auto.tools.image_generator import ImageGeneratorTool


@CrewBase
class KoTeamCrew:
    """Korean language team with hierarchical delegation.

    Team Lead (manager) delegates to:
    - Keyword Researcher
    - Blog Writer
    - Shorts Creator
    """

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # -- Manager Agent (Team Lead) --
    @agent
    def ko_team_lead(self) -> Agent:
        return Agent(
            config=self.agents_config["ko_team_lead"],
            allow_delegation=True,
            verbose=True,
        )

    # -- Worker Agents --
    @agent
    def ko_keyword_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["ko_keyword_researcher"],
            tools=[SEOAnalyzerTool()],
            verbose=True,
        )

    @agent
    def ko_blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["ko_blog_writer"],
            tools=[TranslatorTool(), ImageGeneratorTool()],
            verbose=True,
        )

    @agent
    def ko_shorts_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["ko_shorts_creator"],
            tools=[ImageGeneratorTool()],
            verbose=True,
        )

    # -- Tasks --
    @task
    def keyword_research_task(self) -> Task:
        return Task(config=self.tasks_config["keyword_research_task"])

    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["blog_writing_task"],
            output_file="output/ko/blog/latest_post.md",
        )

    @task
    def shorts_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config["shorts_creation_task"],
            output_file="output/ko/shorts/latest_script.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Korean language team crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_agent=self.ko_team_lead(),
            verbose=True,
        )
