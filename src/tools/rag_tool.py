from tools.base import Tool


class RAGSearchTool(Tool):
    name = "rag_search"

    def __init__(self, retriever):
        self.retriever = retriever

    def run(self, query: str) -> str:
        results = self.retriever.retrieve(query)
        return " ".join(results) if results else "No relevant information found."
