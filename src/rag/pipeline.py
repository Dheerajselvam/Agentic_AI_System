from rag.loader import load_documents
from rag.chunker import chunk_text
from rag.embedder import Embedder
from rag.vector_store import VectorStore
from rag.retriever import SemanticRetriever

class RAGPipeline:
    def __init__(self):
        docs = load_documents()
        chunks = []

        for doc in docs:
            for chunk in chunk_text(doc["text"]):
                chunks.append(chunk)

        self.embedder = Embedder()
        embeddings = self.embedder.embed(chunks)

        self.store = VectorStore(dim=len(embeddings[0]))
        self.store.add(embeddings, chunks)

        self.retriever = SemanticRetriever(self.embedder, self.store)

    def query(self, query):
        results = self.retriever.retrieve(query)
        return [text for text, score in results]
