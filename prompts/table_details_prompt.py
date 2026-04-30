from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic_models.models import Table
from utils import get_table_details
from langchain_ollama import ChatOllama

model1 = ChatOllama(
    model="hf.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF:UD-Q4_K_XL",
    temperature=0
)

table_details=get_table_details()

parser = PydanticOutputParser(pydantic_object= Table)

table_details_prompt1 = f"""Return the names of ALL the SQL tables that MIGHT be relevant to the user question. \n

User question:
{{question}} 
The tables are:

{table_details}

Remember to include ALL POTENTIALLY RELEVANT tables, even if you're not sure that they're needed.\n
{{format_instruction}}
"""

table_details_prompt2 = PromptTemplate(
    template=table_details_prompt1,
    input_variables=['question'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)


