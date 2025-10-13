from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from chat_module import chat_model

# Modèle Pydantic
class Movie(BaseModel):
    title: str = Field(description="The title of the movie.")
    genre: list[str] = Field(description="The genre of the movie.")
    year: int = Field(description="The year the movie was released.")

parser = PydanticOutputParser(pydantic_object=Movie)

# Prompt pour sortie structurée
prompt_template_text = """
Provide a movie recommendation in JSON format with title, genre (list), and year:
{format_instructions}
Query: {query}
"""

format_instructions = parser.get_format_instructions()
structured_prompt = PromptTemplate(
    template=prompt_template_text,
    input_variables=["query"],
    partial_variables={"format_instructions": format_instructions},
)

def recommend_movie(query: str):
    prompt = structured_prompt.format(query=query)
    text_output = chat_model.invoke(prompt)
    parsed_output = parser.parse(text_output.content)
    return text_output.content, parsed_output
