class SimpleRetriever:
    def __init__(self, index):
        self.index = index

    def retrieve(self, query: str):
        results = []
        for doc in self.index:
            if any(word.lower() in doc["content"].lower() for word in query.split()):
                results.append(doc["content"])
        return results
