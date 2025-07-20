from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
import os

# Loading environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Agent setup
agent = Agent(
    model=Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    description="You are a helpful and polite AI assistant.",
    tools=[DuckDuckGoTools()],
    markdown=True
)

# Interactive Chat Loop
def chat():
    print("Chat with LLaMA (type 'exit' to quit):")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        agent.print_response(query)

if __name__ == "__main__":
    chat()
