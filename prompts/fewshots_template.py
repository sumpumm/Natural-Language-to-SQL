from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_huggingface import HuggingFaceEmbeddings
from prompts.examples import data

vector_store = Chroma()
embedding_model = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

example_prompt = ChatPromptTemplate([
    ('human','{input}'),
    ('ai','{result}')
])

example_selector = SemanticSimilarityExampleSelector.from_examples(
    data,
    embedding_model,
    vector_store,
    k=3,
    input_keys=['input']

)

few_shot_prompt=FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    example_selector = example_selector,
    input_variables=['input']
)

