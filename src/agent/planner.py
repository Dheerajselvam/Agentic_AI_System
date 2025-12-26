from agent.llm import LLM
from schemas.actions import AgentAction


class TaskPlanner:
    def __init__(self):
        self.llm = LLM()

    def next_action(self, context: str) -> AgentAction:
        return self.llm.generate_next_action(context)
