from typing import Dict, List
from schemas.tasks import Task


class AgentState:
    def __init__(self, goal: str):
        self.goal = goal
        self.tasks: List[Task] = []
        self.completed_tasks: Dict[str, Task] = {}
        self.memory: Dict[str, str] = {}

    def add_task(self, task: Task):
        self.tasks.append(task)

    def mark_done(self, task_id: str, result: str):
        task = next(t for t in self.tasks if t.id == task_id)
        task.status = "DONE"
        task.result = result
        self.completed_tasks[task_id] = task
