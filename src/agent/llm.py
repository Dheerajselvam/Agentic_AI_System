from schemas.actions import AgentAction


class LLM:
    def generate_next_action(self, context: str) -> AgentAction:
        """
        Stubbed LLM reasoning.
        In production: OpenAI / Anthropic / local model.
        """
        return AgentAction(
            action_type="USE_TOOL",
            tool_name="market_reports",
            tool_query="Market demand for Product X in Market Y",
            rationale="Need demand data before decision"
        )
