from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()


os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


agent=Agent(
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    description="You are an assistant please reply based on the question",
    tools=[DuckDuckGoTools()],
    markdown=True
)

# agent.print_response("When will world war 3 happen?")
# agent.print_response("Based on the news around the world and situations these days what do you predict When will world war 3 happen?")
agent.print_response("How is the weather in karachi City today?")