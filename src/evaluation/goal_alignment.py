class GoalAlignmentEvaluator:
    @staticmethod
    def evaluate(goal: str, decision: str) -> bool:
        goal_words = set(goal.lower().split())
        decision_words = set(decision.lower().split())
        return len(goal_words & decision_words) > 0
