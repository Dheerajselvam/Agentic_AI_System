class HallucinationDetector:
    @staticmethod
    def detect(decision: str, evidence: dict) -> bool:
        # simple relevance-based check
        combined_text = " ".join(str(v) for v in evidence.values()).lower()
        keywords = decision.lower().split()
        relevance_score = sum(1 for word in keywords if word in combined_text) / len(keywords)
        # if less than threshold, mark hallucinated
        return relevance_score < 0.5
