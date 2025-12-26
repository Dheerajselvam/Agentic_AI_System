from agent.agent import Agent
from tools.registry import ToolRegistry
from tools.mock_tools import MarketReportTool, CompetitiveAnalysisTool, FinancialModelTool

if __name__ == "__main__":
    registry = ToolRegistry()
    registry.register(MarketReportTool())
    registry.register(CompetitiveAnalysisTool())
    registry.register(FinancialModelTool())

    agent = Agent(
        goal="Should we launch Product X in Market Y?",
        tools=registry
    )

    agent.run()
