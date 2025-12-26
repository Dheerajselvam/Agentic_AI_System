class AgentState:
    def __init__(self, goal: str):
        self.goal = goal
        self.observations = {}     # factual evidence
        self.completed_tasks = set()
        self.decision_ready = False
        self.failed_decisions = 0

    def add_observation(self, key: str, value: str):
        self.observations[key] = value

    def has_observation(self, key: str) -> bool:
        return key in self.observations

    def mark_task_complete(self, task: str):
        self.completed_tasks.add(task)

    def is_task_complete(self, task: str) -> bool:
        return task in self.completed_tasks

    def reset(self):
        """Clear observations, completed tasks, and decision flag."""
        self.observations.clear()
        self.completed_tasks.clear()
        self.decision_ready = False

    def register_failed_decision(self):
        self.failed_decisions += 1