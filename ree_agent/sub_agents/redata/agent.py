"""This module defines the redata_agent."""
from google.adk import Agent

from . import prompt
from .tools import fetch_api
from .tools import get_date


MODEL = "gemini-2.5-pro"


redata_agent = Agent(
    name="redata_agent",
    model=MODEL,
    description=("gets generation data from the Spanish electrical grid"),
    instruction=prompt.REDATA_PROMPT,
    output_key="redata_output",
    tools=[
        fetch_api,
        get_date,
    ],
)
