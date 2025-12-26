class ReasoningEngine:
    def derive(self, state):
        return {
            "goal": state.goal,
            "observations": state.observations,
            "completed_tasks": list(state.completed_tasks)
        }
