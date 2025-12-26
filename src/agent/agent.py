from agent.state import AgentState
from agent.planner import Planner
from agent.reasoning import ReasoningEngine
from agent.llm import LLM
from agent.decision import DecisionController

from tools.registry import ToolRegistry
from tools.rag_tool import RAGSearchTool

from rag.loader import load_documents
from rag.retriever import SimpleRetriever

from observability.logger import Logger
from agent.llm_wrappers import GPT4AllLLM



class Agent:
    def __init__(self, goal: str):
        self.state = AgentState(goal)
        self.planner = Planner()
        self.reasoning_engine = ReasoningEngine()
        self.llm = LLM()
        self.decision_controller = DecisionController()

        self.logger = Logger()
        self.tools = ToolRegistry()

        # --- RAG setup (already existed conceptually) ---
        documents = load_documents()
        retriever = SimpleRetriever(documents)
        self.tools.register(RAGSearchTool(retriever))

        self.MAX_REPLANS = 3
        self.replans_done = 0

    def run(self):
        self.logger.log("AGENT_START", {"goal": self.state.goal})

        while not self.state.decision_ready:
            plan = self.planner.plan(self.state, self.llm)
            self.logger.log("PLAN", plan)

            if plan["action"] == "USE_TOOL":
                tool = self.tools.get(plan["tool"])
                result = tool.run(plan["query"])

                self.logger.log("TOOL_RESULT", {
                    "tool": plan["tool"],
                    "result": result
                })

                # --- state update (Day 3 logic preserved) ---
                if "demand" in plan["query"].lower():
                    self.state.add_observation("market_demand", result)
                elif "risk" in plan["query"].lower():
                    self.state.add_observation("risk", result)

            elif plan["action"] == "DECIDE":
                self.state.decision_ready = True

            # ===============================
            # DECISION PHASE (DAY 5 CORE)   
            # ===============================

            reasoning_context = self.reasoning_engine.derive(self.state, self.llm)

            # LLM now returns a Decision object (schema-compliant)
            llm_decision = self.llm.generate_decision(
                goal=self.state.goal,
                reasoning=reasoning_context,
                evidence=self.state.observations
            )

            decision_result = self.decision_controller.decide(
                goal=self.state.goal,
                decision_obj=llm_decision,
                evidence=self.state.observations
            )

            self.logger.log("EVALUATION_RESULT", decision_result)

            # --- Control behavior based on evaluation ---
            if decision_result["status"] == "REPLAN":
                self.replans_done += 1
                if self.replans_done >= self.MAX_REPLANS:
                    # Stop replanning, accept last decision even if hallucinated
                    self.logger.log("REPLAN_STOPPED", {"reason": "max_replans reached"})
                    final_output = {
                        "decision": llm_decision,
                        "evaluation": decision_result["evaluation"]
                    }
                    self.logger.log("AGENT_FINAL_DECISION", {
                            "conclusion": llm_decision.conclusion,
                            "confidence": llm_decision.confidence,
                            "evidence_used": llm_decision.evidence_used
                        })
                    return final_output
                self.logger.log("REPLAN_TRIGGERED", {})
                self.state.reset()
                continue

            if decision_result["status"] == "REJECT":
                self.logger.log("DECISION_REJECTED", decision_result)
                return {
                    "error": "Decision rejected",
                    "evaluation": decision_result
                }

            self.logger.log("AGENT_FINAL_DECISION", {
                "conclusion": llm_decision.conclusion,
                "confidence": llm_decision.confidence,
                "evidence_used": llm_decision.evidence_used
            })

            return {
                "decision": llm_decision,
                "evaluation": decision_result["evaluation"]
            }

