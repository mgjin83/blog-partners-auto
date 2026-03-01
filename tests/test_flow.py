"""Tests for the master orchestrator flow."""

from blog_partners_auto.state import PipelineState, Language, Channel


def test_pipeline_state_defaults():
    state = PipelineState()
    assert state.target_languages == [Language.KO, Language.EN, Language.ES]
    assert state.target_channels == [Channel.BLOG, Channel.SHORTS]
    assert state.ko_result.status == "pending"
    assert state.en_result.status == "pending"
    assert state.es_result.status == "pending"


def test_pipeline_state_custom():
    state = PipelineState(
        topic="test topic",
        niche="tech",
        target_languages=[Language.KO],
    )
    assert state.topic == "test topic"
    assert state.target_languages == [Language.KO]
