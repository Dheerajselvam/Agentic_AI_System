from .loader import DOCUMENTS

class SimpleIndexer:
    def __init__(self):
        self.index = DOCUMENTS

    def get_index(self):
        return self.index
