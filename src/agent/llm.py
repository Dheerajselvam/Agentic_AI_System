from agent.llm_wrappers import GPT4AllLLM
from schemas.decision import Decision


class LLM:
    """
    High-level LLM interface used by Agent.
    Delegates actual model calls to llm_wrapper.
    """

    def __init__(self):
        self.backend = GPT4AllLLM()

    # ----------------------------
    # PLANNING
    # ----------------------------
    def plan_next_action(self, state) -> dict:
        """
        Decide the next action based on agent state.
        """
        state_context = {
            "goal": state.goal,
            "observations": state.observations,
            "completed_tasks": list(state.completed_tasks),
        }

        return self.backend.plan_next_action(state_context)

    # ----------------------------
    # DECISION MAKING
    # ----------------------------
    def generate_decision(
        self,
        goal: str,
        reasoning: list,
        evidence: dict
    ) -> Decision:
        """
        Produce a structured Decision object.
        """
        return self.backend.generate_decision(
            goal=goal,
            reasoning=reasoning,
            evidence=evidence
        )
