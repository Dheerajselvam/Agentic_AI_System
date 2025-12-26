from evaluation.semantic_alignment import SemanticAlignmentEvaluator
from evaluation.nli_alignment import NLIAlignmentEvaluator
from evaluation.grounding import EvidenceGroundingEvaluator


class DecisionEvaluator:
    def __init__(
        self,
        semantic_threshold=0.4,
        entailment_threshold=0.5,
        grounding_threshold=0.5
    ):
        self.semantic = SemanticAlignmentEvaluator()
        self.nli = NLIAlignmentEvaluator()
        self.grounding = EvidenceGroundingEvaluator()

        self.semantic_threshold = semantic_threshold
        self.entailment_threshold = entailment_threshold
        self.grounding_threshold = grounding_threshold

    def _build_decision_text(self, decision, evidence: dict) -> str:
        """
        Construct a semantically meaningful evaluation target.
        """

        # Case 1: decision is already a string (fallback)
        if isinstance(decision, str):
            decision_text = decision
        else:
            # Case 2: structured Decision object
            decision_text = getattr(decision, "conclusion", "")

        # 🔑 Always append evidence used
        evidence_text = " ".join(
            str(item)
            for values in evidence.values()
            for item in (values if isinstance(values, list) else [values])
        )

        return f"{decision_text} {evidence_text}".strip()

    def evaluate(self, goal: str, decision, evidence: dict) -> dict:
        decision_text = self._build_decision_text(decision, evidence)

        semantic_score = self.semantic.score(goal, decision_text)
        entailment_score = self.nli.entails(goal, decision_text)
        grounding_score = self.grounding.grounding_score(decision_text, evidence)

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
