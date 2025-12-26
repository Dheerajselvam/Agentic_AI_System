class Planner:
    def plan(self, state):
        if not state.has_observation("market_demand"):
            return {
                "action": "USE_TOOL",
                "tool": "rag_search",
                "query": "Market Y demand growth"
            }

        if not state.has_observation("risk"):
            return {
                "action": "USE_TOOL",
                "tool": "rag_search",
                "query": "Risks in Market Y"
            }

        state.decision_ready = True
        return {"action": "DECIDE"}
