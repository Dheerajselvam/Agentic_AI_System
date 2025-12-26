from dataclasses import dataclass
from typing import Optional


@dataclass
class AgentAction:
    action_type: str      # "USE_TOOL" | "FINAL_DECISION" | "THINK"
    tool_name: Optional[str] = None
    tool_query: Optional[str] = None
    rationale: Optional[str] = None
