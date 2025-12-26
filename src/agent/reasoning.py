class ReasoningEngine:
    """
    LLM-based reasoning engine.
    Converts raw observations into structured reasoning.
    """

    def __init__(self):
        pass

    def derive(self, state, llm) -> list:
        """
        Ask LLM to produce reasoning from current state.
        """
        prompt_context = {
            "goal": state.goal,
            "observations": state.observations,
            "instruction": (
                "Analyze the observations and produce a list of reasoning steps. "
                "Each step should explain why the observation matters for the goal."
            )
        }

        reasoning = llm.backend.model.generate(str(prompt_context))

        try:
            import json
            parsed = json.loads(reasoning)
            if isinstance(parsed, list):
                return parsed
        except Exception:
            pass

        # Safe fallback
        return [
            {
                "observation": k,
                "summary": v
            }
            for k, v in state.observations.items()
        ]
