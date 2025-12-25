from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Task:
    id: str
    description: str
    required_tools: List[str]
    status: str = "PENDING"
    result: Optional[str] = None
