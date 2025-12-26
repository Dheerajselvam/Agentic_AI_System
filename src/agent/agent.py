from agent.state import AgentState
from agent.planner import Planner
from tools.registry import ToolRegistry
from tools.rag_tool import RAGSearchTool
from rag.retriever import SimpleRetriever
from rag.documents import load_documents
from evaluation.heuristics import HeuristicEvaluator
from observability.logger import Logger


class Agent:
    def __init__(self, goal: str):
        self.state = AgentState(goal)
        self.planner = Planner()
        self.tools = ToolRegistry()
        self.logger = Logger()

        documents = load_documents()
        retriever = SimpleRetriever(documents)
        self.tools.register(RAGSearchTool(retriever))

    def run(self):
        self.logger.log("AGENT_START", {"goal": self.state.goal})

        while not self.state.decision_ready:
            plan = self.planner.plan(self.state)
            self.logger.log("PLAN", plan)

            if plan["action"] == "USE_TOOL":
                tool = self.tools.get(plan["tool"])
                result = tool.run(plan["query"])

                self.logger.log("TOOL_RESULT", {
                    "tool": plan["tool"],
                    "result": result
                })

                if "demand" in plan["query"].lower():
                    self.state.add_observation("market_demand", result)
                elif "risk" in plan["query"].lower():
                    self.state.add_observation("risk", result)

            elif plan["action"] == "DECIDE":
                decision = self.make_decision()

                evaluation = HeuristicEvaluator.evaluate(
                    goal=self.state.goal,
                    decision=decision["decision"],
                    evidence=decision["evidence"]
                )

                self.logger.log("EVALUATION_RESULT", evaluation)
                self.logger.log("AGENT_FINAL_DECISION", decision)

                return {
                    "decision": decision,
                    "evaluation": evaluation
                }

    def make_decision(self):
        return {
            "decision": "Launch cautiously",
            "evidence": self.state.observations
        }
