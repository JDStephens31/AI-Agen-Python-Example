import os
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool
# to get your api key for free, visit and signup: https://serper.dev/
os.environ["SERPER_API_KEY"] = "<SERPER API KEY>"
search = GoogleSerperAPIWrapper()

search_tool = Tool(
    name="Scrape google searches",
    func=search.run,
    description="useful for when you need to ask the agent to search the internet",
)