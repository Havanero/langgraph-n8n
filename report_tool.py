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


def structured_rag_prompt():
    return """
    Organize the analysis into these sections:

    ### Core Business Model
    - State the primary business activities
    - Highlight key subsidiaries and ownership
    - Describe main services offered

    ### Revenue Drivers
    - Focus on unique/primary revenue sources
    - Include market-dependent factors
    - Avoid repeating business model details

    ### Strategic Position
    - Emphasize competitive advantages
    - Include market share/dominance
    - Highlight strategic relationships

    ### Market Context
    - Industry-specific factors
    - Market trends affecting business
    - Relevant performance metrics

    Format Guidelines:
    - Start each point with an action verb when possible
    - Avoid repeating information across sections
    - Include specific numbers/metrics where available
    """


@tool
def defi_information(report_query: str):
    """Get financial reports regarding crypto asset for shareholders"""

    chunks = retriever.invoke(report_query)
    data = []
    for c in chunks:
        data.append(c.page_content)
    prompt = f"""
    Analyze the provided information about {data}. For each section:
        {structured_rag_prompt()}
    """
    return prompt


def format_analysis_report(text):
    sections = text.split("###")[1:]  # Skip empty first split

    formatted_sections = []
    for section in sections:
        title, *content = section.strip().split("\n")

        points = [point.strip("- ").strip() for point in content if point.strip()]

        formatted_section = f"### {title.strip()}\n" + "\n".join(
            f"• {point}" for point in points
        )
        formatted_sections.append(formatted_section)

    return "\n\n".join(formatted_sections)


tool_registry = {"1": get_weather, "2": get_coolest_cities, "3": defi_information}
