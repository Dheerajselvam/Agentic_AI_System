from agent.planner import TaskPlanner
from agent.state import AgentState
from logging.trace_logger import TraceLogger


class Agent:
    def __init__(self, goal: str):
        self.state = AgentState(goal)
        self.planner = TaskPlanner()
        self.logger = TraceLogger()

    def run(self):
        self.logger.log("AGENT_START", {"goal": self.state.goal})

        tasks = self.planner.decompose(self.state.goal)
        for task in tasks:
            self.state.add_task(task)
            self.logger.log("TASK_CREATED", task.__dict__)

        # Stub execution loop
        for task in self.state.tasks:
            self.logger.log("TASK_EXECUTION_SKIPPED", {
                "task_id": task.id,
                "reason": "Tool execution not implemented yet"
            })
