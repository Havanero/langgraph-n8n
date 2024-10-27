from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition

from app.nodes import report_agent, select_tools, tool_node
from app.state import State

builder = StateGraph(State)


builder.add_node("report_agent", report_agent)
builder.add_node("select_tools", select_tools)

builder.add_node("tools", tool_node)

builder.add_conditional_edges(
    "report_agent", tools_condition, path_map=["tools", "__end__"]
)
builder.add_edge("tools", "report_agent")
builder.add_edge("select_tools", "report_agent")

builder.add_edge(START, "select_tools")
app = builder.compile()
