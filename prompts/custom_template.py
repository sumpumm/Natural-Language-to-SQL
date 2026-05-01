from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from prompts.fewshots_template import few_shot_prompt

final_template = ChatPromptTemplate([
    ("system",
     """You are a PostgreSQL expert.

Return only SQL query.

Here is the database schema:
{table_info}

Limit results to {top_k} rows if applicable.

\n\nThe Below 3 pairs of User and AI messages are examples of questions and their corresponding SQL queries.  \n
"""),
    few_shot_prompt,
    ("system","END OF EXAMPLEs. Below are the chat history. You must answer the follow up questions if asked using these messages."),
    MessagesPlaceholder(variable_name='chat_history'),
    ("human", "{input}")
])