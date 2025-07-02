from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.deep_research import deep_research_agent
from .sub_agents.redata import redata_agent


MODEL = "gemini-2.5-pro"


electricity_expert = Agent(
    name="electricity_expert_agent",
    model=MODEL,
    description=("guide users to navigate the electrical system in Spain"),
    instruction=prompt.ELECTRICITY_EXPERT_PROMPT,
    output_key="electricity_expert_output",
    tools=[
        AgentTool(agent=deep_research_agent),
        AgentTool(agent=redata_agent),
    ],
)


root_agent = electricity_expert
