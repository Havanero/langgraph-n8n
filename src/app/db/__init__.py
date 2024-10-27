from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore


class MemStore:
    def __init__(self):
        self.tool_store = InMemoryVectorStore(embedding=OpenAIEmbeddings())

    def add_tools(self, tool_documents):
        self.tool_store.add_documents(tool_documents)

    def get_tool_from_db(self, tool):
        return self.tool_store.similarity_search(tool)


class VectorStore:
    def __init__(self):
        self.vector_store = QdrantVectorStore.from_existing_collection(
            embedding=OpenAIEmbeddings(model="text-embedding-ada-002"),
            collection_name="financial_report",
            url="http://localhost:6333",
            content_payload_key="content",
            metadata_payload_key="metadata",
        )

    def get(self, query, qty: int = 400):
        return self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": qty,
            },
        ).invoke(query)
