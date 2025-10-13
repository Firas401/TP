from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

def run_search(query: str):
    result = search_tool.run(query)
    return result
