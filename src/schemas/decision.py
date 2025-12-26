from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Decision:
    conclusion: str
    confidence: float
    evidence_used: Dict[str, Any]
    
    def to_dict(self):
        return {
            "conclusion": self.conclusion,
            "confidence": self.confidence,
            "evidence_used": self.evidence_used
        }