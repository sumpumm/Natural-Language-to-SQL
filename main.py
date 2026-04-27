from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_classic.chains import create_sql_query_chain
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic_models.query import Query
from dotenv import load_dotenv
import os

load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token= os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm)

parser = PydanticOutputParser(pydantic_object=Query)

db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_name = os.getenv("db_name")
db_port = os.getenv("db_port")

connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

db= SQLDatabase.from_uri(connection_string)

template=PromptTemplate(
    template=" extract only the sql query from the given text: \n {text} \n{format_instruction}",
    input_variables=["text"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

query_generator= create_sql_query_chain(model,db) 

query = query_generator.invoke({"question":"what is the price of 1968 ford mustang?"})

chain = template | model | parser 

cleaned_query=chain.invoke(query)
print(cleaned_query.sql)