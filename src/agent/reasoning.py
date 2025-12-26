class ReasoningEngine:
    def derive(self, state):
        reasoning = []

        for key, value in state.observations.items():
            reasoning.append({
                "observation": key,
                "summary": value
            })

        return reasoning
