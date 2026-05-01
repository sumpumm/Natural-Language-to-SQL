from langchain_ollama import ChatOllama
from langchain_community.tools import QuerySQLDataBaseTool
from langchain_classic.chains import create_sql_query_chain
from langchain_core.output_parsers import  StrOutputParser,PydanticOutputParser
from langchain_classic.schema.runnable import RunnablePassthrough, RunnableLambda
from langchain_core.messages import HumanMessage, AIMessage
from database import db
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

chat_history=[]

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

while True:
    question = input("You :")
    chat_history.append(HumanMessage(content=question))
    if question.lower() == "exit":
        break
    result = chain.invoke({"question":question, "chat_history" : chat_history})
    chat_history.append(AIMessage(content=result))
    print("AI :",result)

