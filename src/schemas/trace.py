from dataclasses import dataclass
from typing import List, Dict

@dataclass
class ReasoningTrace:
    steps: List[Dict]
