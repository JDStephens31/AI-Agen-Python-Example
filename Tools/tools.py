import os
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.agents import Tool
os.environ["SERPER_API_KEY"] = "f9d634cd11c08dc8f6796ca7510bf92e68279b65"
search = GoogleSerperAPIWrapper()

search_tool = Tool(
    name="Scrape google searches",
    func=search.run,
    description="useful for when you need to ask the agent to search the internet",
)