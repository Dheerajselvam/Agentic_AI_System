from tools.base import Tool


class MarketReportTool(Tool):
    name = "market_reports"

    def run(self, query: str) -> str:
        return "Market demand appears moderate with 12% YoY growth."


class CompetitiveAnalysisTool(Tool):
    name = "competitive_analysis"

    def run(self, query: str) -> str:
        return "Two strong incumbents, moderate differentiation."


class FinancialModelTool(Tool):
    name = "financial_model"

    def run(self, query: str) -> str:
        return "Projected break-even in 24 months, medium risk."
