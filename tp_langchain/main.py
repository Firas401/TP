import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun

# Charger les variables d'environnement
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialisation modèle
chat_model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=500,
    api_key=api_key
)

# Fonctions TP
def chat_pirate(question: str):
    system_message = SystemMessage(content="You are a friendly pirate ☠️")
    messages = [system_message, HumanMessage(content=question)]
    response = chat_model.invoke(messages)
    return response.content

def generate_meal_titles(n: int, cuisine: str):
    prompt_template = PromptTemplate.from_template(
        "List {n} cooking/meal titles for {cuisine} cuisine (name only)."
    )
    prompt = prompt_template.format(n=n, cuisine=cuisine)
    response = chat_model.invoke(prompt)
    return prompt, response.content

def web_search(query: str):
    search_tool = DuckDuckGoSearchRun()
    return search_tool.run(query)

# Test rapide
if __name__ == "__main__":
    print("=== Chat Pirate ===")
    print(chat_pirate("Ahoy! What treasure have ye found today?"))
    print("\n=== Generate Meal Titles ===")
    prompt, meals = generate_meal_titles(3, "Italian")
    print(prompt)
    print(meals)
    print("\n=== DuckDuckGo Search ===")
    result = web_search("population of Algeria")
    print(result)
