import os
from crewai import Process, Crew
from langchain.agents import load_tools

import Agents.agents  # import <Directory>.<File_Name>
import Tasks.tasks  # import <Directory>.<File_Name>

# Loading Human Tools
human_tools = load_tools(["human"])

crew = Crew(
    agents=[Agents.agents.forum_research_analyst],  # List of all Agents <Directory>.<File_Name>.<Function>
    tasks=[Tasks.tasks.task1],  # List of all Tasks <Directory>.<File_Name>.<Function>
    verbose=2,
    process=Process.sequential,
    # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed
    # as extra content into this next.
)

# Get your crew to work!
result = crew.kickoff()
print("######################")
print(result)
