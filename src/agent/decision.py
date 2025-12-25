from dataclasses import dataclass


@dataclass
class LaunchDecision:
    recommendation: str  # YES / NO / DEFER
    rationale: str
    risks: str
    assumptions: str
