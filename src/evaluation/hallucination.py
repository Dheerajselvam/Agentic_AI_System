class HallucinationDetector:
    @staticmethod
    def detect(decision: str, evidence: dict) -> bool:
        combined_evidence = " ".join(str(v) for v in evidence.values()).lower()
        return decision.lower() not in combined_evidence
