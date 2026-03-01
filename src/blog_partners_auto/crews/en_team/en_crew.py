"""English language content production crew."""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from blog_partners_auto.tools.seo_analyzer import SEOAnalyzerTool
from blog_partners_auto.tools.translator import TranslatorTool
from blog_partners_auto.tools.image_generator import ImageGeneratorTool


@CrewBase
class EnTeamCrew:
    """English language team with hierarchical delegation."""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def en_team_lead(self) -> Agent:
        return Agent(
            config=self.agents_config["en_team_lead"],
            allow_delegation=True,
            verbose=True,
        )

    @agent
    def en_keyword_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["en_keyword_researcher"],
            tools=[SEOAnalyzerTool()],
            verbose=True,
        )

    @agent
    def en_blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["en_blog_writer"],
            tools=[TranslatorTool(), ImageGeneratorTool()],
            verbose=True,
        )

    @agent
    def en_shorts_creator(self) -> Agent:
        return Agent(
            config=self.agents_config["en_shorts_creator"],
            tools=[ImageGeneratorTool()],
            verbose=True,
        )

    @task
    def keyword_research_task(self) -> Task:
        return Task(config=self.tasks_config["keyword_research_task"])

    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["blog_writing_task"],
            output_file="output/en/blog/latest_post.md",
        )

    @task
    def shorts_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config["shorts_creation_task"],
            output_file="output/en/shorts/latest_script.md",
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_agent=self.en_team_lead(),
            verbose=True,
        )
