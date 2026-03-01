#!/usr/bin/env python
"""Blog Partners Automation - Entry point."""

import os
import sys

from blog_partners_auto.flow import MasterOrchestratorFlow


def run():
    """Run the full multi-language content production pipeline."""
    flow = MasterOrchestratorFlow()
    flow.state.topic = os.getenv("BLOG_TOPIC", "AI productivity tools for remote workers")
    flow.state.niche = os.getenv("BLOG_NICHE", "technology")

    result = flow.kickoff()

    print("\n=== Pipeline Complete ===")
    print(flow.state.final_report)
    return result


def plot():
    """Generate a visualization of the orchestration flow."""
    flow = MasterOrchestratorFlow()
    flow.plot("blog_partners_flow")
    print("Flow diagram saved to blog_partners_flow.html")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "plot":
        plot()
    else:
        run()
