"""Master orchestrator flow that coordinates all language team crews."""

from crewai.flow.flow import Flow, start, listen, and_

from blog_partners_auto.state import PipelineState, Language
from blog_partners_auto.crews.ko_team.ko_crew import KoTeamCrew
from blog_partners_auto.crews.en_team.en_crew import EnTeamCrew
from blog_partners_auto.crews.es_team.es_crew import EsTeamCrew


class MasterOrchestratorFlow(Flow[PipelineState]):
    """
    Top-level Flow that orchestrates all 3 language-team crews.

    Pipeline:
      1. validate_inputs   (@start)
      2. run_ko/en/es_team (@listen - parallel)
      3. aggregate_results (@listen - waits for all)
    """

    @start()
    def validate_inputs(self):
        """Validate and normalize the incoming topic/niche inputs."""
        assert self.state.topic, "Topic is required"
        assert self.state.niche, "Niche is required"
        return {"topic": self.state.topic, "niche": self.state.niche}

    @listen(validate_inputs)
    def run_ko_team(self):
        """Kick off the Korean language crew."""
        if Language.KO not in self.state.target_languages:
            return

        result = KoTeamCrew().crew().kickoff(inputs={
            "topic": self.state.topic,
            "niche": self.state.niche,
            "language": "ko",
            "language_name": "Korean",
        })
        self.state.ko_result.blog_content = result.raw
        self.state.ko_result.status = "completed"

    @listen(validate_inputs)
    def run_en_team(self):
        """Kick off the English language crew."""
        if Language.EN not in self.state.target_languages:
            return

        result = EnTeamCrew().crew().kickoff(inputs={
            "topic": self.state.topic,
            "niche": self.state.niche,
            "language": "en",
            "language_name": "English",
        })
        self.state.en_result.blog_content = result.raw
        self.state.en_result.status = "completed"

    @listen(validate_inputs)
    def run_es_team(self):
        """Kick off the Spanish language crew."""
        if Language.ES not in self.state.target_languages:
            return

        result = EsTeamCrew().crew().kickoff(inputs={
            "topic": self.state.topic,
            "niche": self.state.niche,
            "language": "es",
            "language_name": "Spanish",
        })
        self.state.es_result.blog_content = result.raw
        self.state.es_result.status = "completed"

    @listen(and_(run_ko_team, run_en_team, run_es_team))
    def aggregate_results(self):
        """Collect results from all language teams and generate final report."""
        results = []
        for lang_result in [self.state.ko_result, self.state.en_result, self.state.es_result]:
            if lang_result.status == "completed":
                results.append(f"[{lang_result.language.value.upper()}] Completed")
            else:
                results.append(f"[{lang_result.language.value.upper()}] Skipped")

        self.state.final_report = "\n".join(results)
        return self.state.final_report
