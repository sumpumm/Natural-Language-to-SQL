from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from prompts.fewshots_template import few_shot_prompt

final_template = ChatPromptTemplate([
    ("system",
     """You are a PostgreSQL expert.

Return only SQL query.

Here is the database schema:
{table_info}

Limit results to {top_k} rows if applicable.

\n\nBelow are a number of examples of questions and their corresponding SQL queries. \n\n
Below is given the chat history. You must answer the follow up questions if asked using these messages.
"""),
    few_shot_prompt,
    MessagesPlaceholder(variable_name='chat_history'),
    ("human", "{input}")
])