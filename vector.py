from typing import List

import bs4
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

# system_prompt = (
#    "You are an assistant for question-answering tasks. "
#    "Use the following pieces of retrieved context to answer "
#    "the question. If you don't know the answer, say that you "
#    "don't know. Use three sentences maximum and keep the "
#    "answer concise."
#    "\n\n"
#    "{context}"
# )
#
# prompt = ChatPromptTemplate.from_messages(
#    [
#        ("system", system_prompt),
#        ("human", "{input}"),
#    ]
# )
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")


vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    collection_name="financial_report",
    url="http://localhost:6333",
    content_payload_key="content",
    metadata_payload_key="metadata",
)
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={
        "k": 6,
    },
)
