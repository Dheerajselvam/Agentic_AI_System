from evaluation.semantic_alignment import SemanticAlignmentEvaluator
from evaluation.nli_alignment import NLIAlignmentEvaluator
from evaluation.grounding import EvidenceGroundingEvaluator

class DecisionEvaluator:
    def __init__(
        self,
        semantic_threshold=0.6,
        entailment_threshold=0.5,
        grounding_threshold=0.5
    ):
        self.semantic = SemanticAlignmentEvaluator()
        self.nli = NLIAlignmentEvaluator()
        self.grounding = EvidenceGroundingEvaluator()

        self.semantic_threshold = semantic_threshold
        self.entailment_threshold = entailment_threshold
        self.grounding_threshold = grounding_threshold

    def evaluate(self, goal: str, decision: str, evidence: dict) -> dict:
        semantic_score = self.semantic.score(goal, decision)
        entailment_score = self.nli.entails(goal, decision)
        grounding_score = self.grounding.grounding_score(decision, evidence)

        goal_aligned = (
            semantic_score >= self.semantic_threshold
            or entailment_score >= self.entailment_threshold
        )

        hallucinated = grounding_score < self.grounding_threshold

        return {
            "semantic_score": semantic_score,
            "entailment_score": entailment_score,
            "grounding_score": grounding_score,
            "goal_aligned": goal_aligned,
            "hallucinated": hallucinated
        }
