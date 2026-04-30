from langchain_core.prompts import ChatPromptTemplate
from prompts.fewshots_template import few_shot_prompt

final_template = ChatPromptTemplate([
    ("system",
     """You are a PostgreSQL expert.

Return only SQL query.

Here is the database schema:
{table_info}

Limit results to {top_k} rows if applicable.

\n\nBelow are a number of examples of questions and their corresponding SQL queries.
"""),
    few_shot_prompt,
    ("human", "{input}")
])