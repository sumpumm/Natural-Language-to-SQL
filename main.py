from langchain_ollama import ChatOllama
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.tools import QuerySQLDataBaseTool
from langchain_classic.chains import create_sql_query_chain
from langchain_core.output_parsers import  StrOutputParser,PydanticOutputParser
from langchain_classic.schema.runnable import RunnablePassthrough, RunnableLambda
from prompts.table_details_prompt import table_details_prompt2
from prompts.rephraser import rephraser_template
from prompts.custom_template import final_template
from pydantic_models.models import Table
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

db= SQLDatabase.from_uri(connection_string,sample_rows_in_table_info=1)

query_generator = create_sql_query_chain(
    model1,
    db,
    prompt=final_template,
    k=3
)

query_executor = QuerySQLDataBaseTool(db=db)

question = "can you get me  name of any 5 customers"

parser = PydanticOutputParser(pydantic_object= Table)

table_chain = table_details_prompt2 | model1 | parser

rephraser_chain = rephraser_template | model1 | StrOutputParser()

chain = ( RunnablePassthrough.assign(table_names_to_use=table_chain | RunnableLambda(lambda x :x.name)).assign(query= query_generator ).assign(result =itemgetter("query") | query_executor) ) | rephraser_chain

print(chain.invoke({"question":question}))