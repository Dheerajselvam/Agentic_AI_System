from agent.state import AgentState
from agent.planner import Planner
from tools.registry import ToolRegistry
from tools.rag_tool import RAGSearchTool
from rag.retriever import SimpleRetriever
from rag.documents import load_documents

class Agent:
    def __init__(self, goal):
        self.state = AgentState(goal)
        self.planner = Planner()
        self.tools = ToolRegistry()

        documents = load_documents()
        retriever = SimpleRetriever(documents)
        self.tools.register(RAGSearchTool(retriever))

    def run(self):
        while not self.state.decision_ready:
            plan = self.planner.plan(self.state)

            if plan["action"] == "USE_TOOL":
                tool = self.tools.get(plan["tool"])
                result = tool.run(plan["query"])


                if "growth" in plan["query"].lower():
                    self.state.add_observation("market_demand", result)
                elif "risk" in plan["query"].lower():
                    self.state.add_observation("risk", result)

            elif plan["action"] == "DECIDE":
                return self.make_decision()

    def make_decision(self):
        return {
            "decision": "Launch cautiously",
            "evidence": self.state.observations
        }
