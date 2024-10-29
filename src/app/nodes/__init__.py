from functools import lru_cache

from app.config import GraphConfig
from app.db import MemStore, VectorStore
from app.state import State
from app.tools import ToolSet, create_tool_documents
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode

tool_db = MemStore()
rag_db = VectorStore()

tool_set = ToolSet(rag_db)
current_tools = tool_set.get_tools

tool_db.add_tools(create_tool_documents(current_tools))

tools = list(current_tools.values())


@lru_cache(maxsize=4)
def _get_open_ai(model="gpt-4o"):
    return ChatOpenAI(temperature=0, model_name="gpt-4o").bind_tools(tools)


def report_agent(state: State, config: GraphConfig):
    selected_tools = [current_tools.get(id) for id in state["selected_tools"]]

    llm_with_tools = _get_open_ai().bind_tools(selected_tools)
    #    breakpoint()
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


def select_tools(state: State):
    last_user_message = state["messages"][-1]
    query = last_user_message.content
    tool_documents = tool_db.get_tool_from_db(query)
    return {"selected_tools": [document.id for document in tool_documents]}


tool_node = ToolNode(tools=tools)
