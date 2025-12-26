from evaluation.goal_alignment import GoalAlignmentEvaluator
from evaluation.hallucination import HallucinationDetector

class HeuristicEvaluator:
    @staticmethod
    def evaluate(goal, decision, evidence):
        return {
            "goal_aligned": GoalAlignmentEvaluator.evaluate(goal, decision),
            "hallucinated": HallucinationDetector.detect(decision, evidence)
        }
