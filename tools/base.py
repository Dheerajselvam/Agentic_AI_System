from abc import ABC, abstractmethod


class Tool(ABC):
    name: str

    @abstractmethod
    def run(self, query: str) -> str:
        pass
