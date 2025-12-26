from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Decision:
    conclusion: str
    confidence: float
    evidence_used: Dict[str, Any]
