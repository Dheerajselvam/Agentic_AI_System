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
        if not evidence:
            return {"status": "REPLAN", "evaluation": evaluation}
        elif evaluation["hallucinated"]:
            return {"status": "REPLAN", "evaluation": evaluation}
        elif not evaluation["goal_aligned"]:
            return {"status": "REPLAN", "evaluation": evaluation}
        else:
            return {
                "status": "ACCEPT",
                "decision": decision_obj,
                "evaluation": evaluation
            }
