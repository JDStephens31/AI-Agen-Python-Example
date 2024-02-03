from crewai import Task
import Agents.agents  # import <Directory>.<File_Name>

# Example Task
task1 = Task(
    description=""" How do I import modules in python? Show me with a code example""",
    agent=Agents.agents.forum_research_analyst, # Agent that starts the task <Directory>.<File_Name>.<Function>
)
