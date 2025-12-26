from agent.agent import Agent


def main():
    agent = Agent(goal="Are you a pig?")
    result = agent.run()

    print("\n=== FINAL OUTPUT ===")
    print(result)


if __name__ == "__main__":
    main()
