from tools.base import Tool
from rag.retriever import SimpleRetriever


class RAGSearchTool(Tool):
    name = "rag_search"

    def __init__(self, retriever: SimpleRetriever):
        self.retriever = retriever

    def run(self, query: str) -> str:
        results = self.retriever.retrieve(query)
        if not results:
            return "No relevant documents found."
        return " ".join(results)
