from langchain_core.tools import tool

from vector import retriever


@tool
def get_weather(location: str):
    """Call to get the current weather."""
    if location.lower() in ["sf", "san francisco", "san francisco, ca"]:
        return "It's 60 degrees and foggy."
    else:
        return "It's 90 degrees and sunny."


@tool
def get_coolest_cities():
    """Get a list of coolest cities"""
    return "nyc, sf, berlin"


@tool
def defi_informatiion(crypto: str):
    """Get financial reports regarding crypto asset for shareholders"""
    result = retriever.invoke(crypto)
    return "\n".join([doc.page_content for doc in result])


tool_registry = {"1": get_weather, "2": get_coolest_cities, "3": defi_informatiion}
