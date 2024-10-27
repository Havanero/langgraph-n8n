from app.tools.template_loader import load_prompt
from langchain.tools.base import StructuredTool
from langchain_core.documents import Document


class NormalTool:
    def __init__(self):
        self.weather = StructuredTool.from_function(self.get_weather)
        self.city = StructuredTool.from_function(self.get_coolest_cities)

    def get_weather(self, location: str):
        """Call to get the current weather."""
        if location.lower() in ["sf", "san francisco", "san francisco, ca"]:
            return "It's 60 degrees and foggy."
        else:
            return "It's 90 degrees and sunny."

    def get_coolest_cities(self):
        """Get a list of coolest cities"""
        return "nyc, sf, berlin"


class RagTool:
    def __init__(self, store):
        self.vector = store
        self.defi = StructuredTool.from_function(self.defi_information)

    def defi_information(self, report_query: str):
        """Get financial reports regarding crypto asset for shareholders"""

        chunks = self.vector.get(report_query)
        data = []
        for c in chunks:
            data.append(c.page_content)
        prompt = f"""
        Analyze the provided information. For each section:
            {load_prompt(data)}
        """
        return prompt


class ToolSet:
    def __init__(self, vector_db):
        self.vector = vector_db

    @property
    def get_tools(self):
        normal_tool = NormalTool()
        rag_tool = RagTool(self.vector)

        return {
            "1": normal_tool.weather,
            "2": normal_tool.city,
            "3": rag_tool.defi,
        }


def create_tool_documents(tool_dict):
    return [
        Document(
            page_content=current_tool.description,
            id=id,
            metadata={"tool_name": current_tool.name},
        )
        for id, current_tool in tool_dict.items()
    ]
