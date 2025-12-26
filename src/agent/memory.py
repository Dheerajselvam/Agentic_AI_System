class EpisodicMemory:
    def __init__(self):
        self.history = []

    def store(self, entry: dict):
        self.history.append(entry)

    def recall(self):
        return self.history
