from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

query = "population of Algeria"
result = search_tool.run(query)
print("Résultat de recherche :", result)