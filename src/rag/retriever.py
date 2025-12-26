class SemanticRetriever:
    def __init__(self, embedder, store):
        self.embedder = embedder
        self.store = store

    def retrieve(self, query, top_k=3):
        q_emb = self.embedder.embed([query])
        return self.store.search(q_emb, top_k)
