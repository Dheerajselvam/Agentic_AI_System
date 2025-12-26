from observability.logger import Logger

class RunRecorder:
    def __init__(self, goal: str):
        self.goal = goal
        self.events = []

        Logger.log("AGENT_START", {"goal": goal})

    def record(self, event: str, payload: dict):
        self.events.append((event, payload))
        Logger.log(event, payload)

    def finalize(self, decision: dict):
        Logger.log("AGENT_FINAL_DECISION", decision)
