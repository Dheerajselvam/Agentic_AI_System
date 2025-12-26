from transformers import pipeline

class EvidenceGroundingEvaluator:
    def __init__(self, model_name="facebook/bart-large-mnli"):
        self.nli = pipeline("text-classification", model=model_name)

    def grounding_score(self, decision: str, evidence: dict) -> float:
        if not evidence:
            return 0.0

        evidence_text = " ".join(str(v) for v in evidence.values())
        result = self.nli(f"{evidence_text} </s> {decision}")[0]

        if result["label"].lower() == "entailment":
            return result["score"]
        return 0.0
