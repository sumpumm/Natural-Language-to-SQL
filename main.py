from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_ollama import ChatOllama
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.tools import QuerySQLDataBaseTool
from langchain_classic.chains import create_sql_query_chain
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_classic.schema.runnable import RunnablePassthrough
from pydantic_models.query import Query
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


parser = PydanticOutputParser(pydantic_object=Query)

db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_name = os.getenv("db_name")
db_port = os.getenv("db_port")

connection_string = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

db= SQLDatabase.from_uri(connection_string)

extraction_template=PromptTemplate(
    template=" extract only the sql query from the given text: \n {text} \n{format_instruction}",
    input_variables=["text"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

rephraser_template=PromptTemplate(
    template="""
            Given the following user question, corresponding sql query and sql result, answer the user question:
            Question:{question}
            SQL Query:{query}
            SQL Result:{result}
            Answer:
""",
input_variables=['question', 'query', 'result']
)

query_generator= create_sql_query_chain(model1,db) 

query_executor = QuerySQLDataBaseTool(db=db)

question = "what is the most expensive order and from whom?"

rephraser_chain = rephraser_template | model2 | StrOutputParser()

chain = ( RunnablePassthrough.assign(query= (query_generator | extraction_template | model1 | parser | (lambda x: x.sql))).assign(result =itemgetter("query") | query_executor) ) | rephraser_chain

print(chain.invoke({"question":question}))