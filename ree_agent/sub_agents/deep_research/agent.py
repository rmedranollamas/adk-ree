"""This module defines the deep_research_agent."""
from google.adk import Agent
from google.adk.tools import google_search

from . import prompt


MODEL = "gemini-2.5-pro"


deep_research_agent = Agent(
    name="deep_research_agent",
    model=MODEL,
    description=("an expert agent to find information on the web"),
    instruction=prompt.DEEP_RESEARCH_PROMPT,
    output_key="deep_research_output",
    tools=[
        google_search,
    ],
)
