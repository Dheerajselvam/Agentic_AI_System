from agent.agent import Agent

def main():
    # Example goals
    goals = [
        "Should we launch Product X in Market Y?",
        "Are you a pig?"
        ]

    for goal in goals:
        agent = Agent(goal)
        output = agent.run()
        print("\n=== FINAL OUTPUT ===")
        print(output)


if __name__ == "__main__":
    main()
