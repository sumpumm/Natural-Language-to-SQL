from langchain_core.prompts import PromptTemplate

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
