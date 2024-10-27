import pytest
from app.db import MemStore, VectorStore
from app.tools import ToolSet, create_tool_documents


@pytest.fixture
def setup_environment():
    tool_db = MemStore()
    rag_db = VectorStore()
    tool_set = ToolSet(rag_db)
    current_tools = tool_set.get_tools

    tool_db.add_tools(create_tool_documents(current_tools))
    tools = list(current_tools.values())

    return tool_db, rag_db, tools, current_tools
