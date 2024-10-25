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


def enhanced_rag_analysis(context):
    return f"""
    Analyze the provided information about the report. Structure your analysis using these specific guidelines:

    1. Core Business Model
    - Start with the company's primary business definition
    - List key subsidiaries with ownership percentages
    - Detail main revenue-generating activities
    - Include any specific locations or jurisdictions

    2. Revenue Drivers
    - List specific revenue streams with their contributions if available
    - Include quantitative metrics where provided (growth rates, volumes)
    - Describe market conditions affecting revenue
    - Note any seasonal or cyclical factors

    3. Strategic Position
    - Detail competitive advantages
    - List key partnerships and ownership structures
    - Describe growth initiatives and target markets
    - Include any stated strategic goals

    4. Market Context & Risks
    - Describe relevant market trends with specific data
    - Include regulatory environment
    - List key performance indicators
    - Note major risk factors

    5. Financial Metrics (if available)
    - Trading volumes
    - Revenue figures
    - Growth rates
    - Market share data

    Guidelines:
    - Use specific numbers and percentages whenever available
    - Start each bullet point with an action verb when possible
    - Avoid generic statements without supporting details
    - Include timeframes for any metrics or goals mentioned
    - Reference source materials for key claims

    Context: {context}
    """


@tool
def defi_information(report_query: str):
    """Get financial reports regarding crypto asset for shareholders"""

    chunks = retriever.invoke(report_query)
    data = []
    for c in chunks:
        data.append(c.page_content)
    prompt = f"""
    Analyze the provided information. For each section:
        {enhanced_rag_analysis(data)}
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
