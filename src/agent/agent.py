from agent.state import AgentState
from agent.planner import TaskPlanner
from tools.registry import ToolRegistry
from agent_logging.trace_logger import TraceLogger
from schemas.actions import AgentAction
from agent.decision import LaunchDecision


class Agent:
    def __init__(self, goal: str, tools: ToolRegistry):
        self.state = AgentState(goal)
        self.planner = TaskPlanner()
        self.tools = tools
        self.logger = TraceLogger()

    def run(self):
        self.logger.log("AGENT_START", {"goal": self.state.goal})

        for step in range(3):  # bounded loop
            action: AgentAction = self.planner.next_action(
                context=str(self.state.memory)
            )

            self.logger.log("LLM_ACTION", action.__dict__)

            if action.action_type == "USE_TOOL":
                tool = self.tools.get(action.tool_name)
                result = tool.run(action.tool_query)
                self.state.memory[action.tool_name] = result

                self.logger.log("TOOL_RESULT", {
                    "tool": action.tool_name,
                    "result": result
                })

            elif action.action_type == "FINAL_DECISION":
                decision = LaunchDecision(
                    recommendation="YES",
                    rationale="Sufficient demand and acceptable risk",
                    risks="Competitive pressure",
                    assumptions="Cost projections hold"
                )
                self.logger.log("FINAL_DECISION", decision.__dict__)
                break
