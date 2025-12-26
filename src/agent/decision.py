from evaluation.heuristics import HeuristicEvaluator

class DecisionController:
    def decide(self, goal, decision_obj, evidence):
        evaluation = HeuristicEvaluator.evaluate(
            goal,
            decision_obj.conclusion,  # <-- use 'conclusion' field
            evidence
        )

        if evaluation["hallucinated"]:
            return {"status": "REPLAN", "evaluation": evaluation}

        if not evaluation["goal_aligned"]:
            return {"status": "REJECT", "evaluation": evaluation}

        return {
            "status": "ACCEPT",
            "decision": decision_obj,
            "evaluation": evaluation
        }
