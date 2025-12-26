from evaluation.evaluator import DecisionEvaluator

class DecisionController:
    def __init__(self):
        self.evaluator = DecisionEvaluator()

    def decide(self, goal, decision_obj, evidence):
        evaluation = self.evaluator.evaluate(
            goal,
            decision_obj.conclusion,
            evidence
        )

        if evaluation["hallucinated"]:
            return {"status": "REPLAN", "evaluation": evaluation}

        if not evaluation["goal_aligned"]:
            return {"status": "REPLAN", "evaluation": evaluation}

        return {
            "status": "ACCEPT",
            "decision": decision_obj,
            "evaluation": evaluation
        }
