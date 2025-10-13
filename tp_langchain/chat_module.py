import os
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate

# Clé API Groq
os.environ["GROQ_API_KEY"] = "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"

# Initialisation modèle
chat_model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=500,
)

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
