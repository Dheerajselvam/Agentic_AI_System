from agent.agent import Agent
from agent_logging.trace_logger import TraceLogger

def main():
    logger = TraceLogger()

    goal = "Should we launch Product X in Market Y?"

    logger.log(
        event_type="AGENT_START",
        payload={"goal": goal}
    )

    agent = Agent(goal=goal)

    decision = agent.run()

    logger.log(
        event_type="AGENT_FINAL_DECISION",
        payload=decision
    )

    print("\n=== FINAL DECISION ===")
    print(decision)


if __name__ == "__main__":
    main()
