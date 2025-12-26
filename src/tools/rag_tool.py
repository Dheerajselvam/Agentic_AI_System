from tools.base import Tool
from rag.pipeline import RAGPipeline

class RAGSearchTool(Tool):
    name = "rag_search"

    def __init__(self):
        self.pipeline = RAGPipeline()

    def run(self, query: str):
        return self.pipeline.query(query)
