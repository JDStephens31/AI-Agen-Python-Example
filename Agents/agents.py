import os
from langchain_community.chat_models import ChatOpenAI
from crewai import Agent

import Tools.tools # import <Directory>.<File_Name>

os.environ["OPENAI_API_KEY"] = "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"
api = os.environ.get("OPENAI_API_KEY")

# Example Agent
forum_research_analyst = Agent(
    role="Forum Research Analyst", # Job Title
    goal="Find out an answer to a question I have by searching forums, blogs, and other websites.", # Job Goal
    backstory="""You are an expert at finding specific answers by searching forums, blogs, and other websites. """, # Job Description
    verbose=True,  # enable more detailed or extensive output
    allow_delegation=False,  # enable collaboration between agent
    tools=[Tools.tools.search_tool], # List of Tools the agent is allowed to use
    llm=ChatOpenAI(model_name="gpt-3.5-turbo-1106", temperature=0.7) # AI model used. For GPT-4 use just comment out this line.
)