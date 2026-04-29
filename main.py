from langchain_ollama import ChatOllama
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.tools import QuerySQLDataBaseTool
from langchain_classic.chains import create_sql_query_chain
from langchain_core.output_parsers import  StrOutputParser
from langchain_classic.schema.runnable import RunnablePassthrough, RunnableLambda
from utils import extract_sql_query
from prompts.templates import rephraser_template
from operator import itemgetter
from dotenv import load_dotenv
import os

load_dotenv()

model1 = ChatOllama(
    model="hf.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF:UD-Q4_K_XL",
    temperature=0
)
model2=ChatOllama(
    model="gpt-oss:latest"
)

db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_name = os.getenv("db_name")
db_port = os.getenv("db_port")

connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

db= SQLDatabase.from_uri(connection_string)


query_generator= create_sql_query_chain(model1,db) 

query_executor = QuerySQLDataBaseTool(db=db)

question = "what is the most expensive order and from whom?"

rephraser_chain = rephraser_template | model1 | StrOutputParser()

chain = ( RunnablePassthrough.assign(query= (query_generator | RunnableLambda(extract_sql_query))).assign(result =itemgetter("query") | query_executor) ) | rephraser_chain

print(chain.invoke({"question":question}))