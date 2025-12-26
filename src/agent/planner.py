class Planner:
    def plan(self, state, llm):
        # If no evidence, DO NOT DECIDE
        if not state.observations:
            return {
                "action": "USE_TOOL",
                "tool": "rag_search",
                "query": f"Market demand and risks for {state.goal}"
            }

        if state.failed_decisions > 0:
            return {
                "action": "USE_TOOL",
                "tool": "rag_search",
                "query": f"Risks, competition, and feasibility of {state.goal}"
            }

        return {"action": "DECIDE"}
