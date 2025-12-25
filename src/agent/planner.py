from schemas.tasks import Task
from typing import List


class TaskPlanner:
    def decompose(self, goal: str) -> List[Task]:
        return [
            Task(
                id="market_demand",
                description="Analyze market demand for Product X in Market Y",
                required_tools=["market_reports"]
            ),
            Task(
                id="competition",
                description="Assess competitive landscape",
                required_tools=["competitive_analysis"]
            ),
            Task(
                id="costs_risks",
                description="Estimate costs, risks, and constraints",
                required_tools=["financial_model"]
            ),
        ]
