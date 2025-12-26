from schemas.actions import AgentAction
from schemas.decision import Decision

class LLM:
    def generate_next_action(self, context: str) -> AgentAction:
        # Planner-level LLM
        return AgentAction(
            action_type="USE_TOOL",
            tool_name="rag_search",
            tool_query="Market Y demand growth",
            rationale="Need demand data"
        )

    def generate_decision(self, goal: str, reasoning: list, evidence: dict[str, any]) -> Decision:
        """
        Generates a structured decision based on the current reasoning context and evidence.
        """

        # For demonstration, we create a simple heuristic conclusion
        # In production: call LLM API and parse structured JSON

        # Example logic (stub):
        if "Market Y" in goal or "Product X" in goal:
            conclusion = "Launch cautiously"
            confidence = 0.7
        else:
            conclusion = "Cannot determine"
            confidence = 0.3

        # Include all available evidence
        evidence_used = evidence.copy()

        return Decision(
            conclusion=conclusion,
            confidence=confidence,
            evidence_used=evidence_used
        )
