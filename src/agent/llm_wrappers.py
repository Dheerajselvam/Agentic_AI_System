from gpt4all import GPT4All
from schemas.decision import Decision

class GPT4AllLLM:
    def __init__(self, model_name: str = "orca-mini-3b-gguf2-q4_0.gguf"):
        self.model = GPT4All(model_name)

    def generate_decision(self, goal: str, reasoning: list, evidence: dict) -> Decision:
        prompt = f"""
                        Goal:
                        {goal}

                        Reasoning:
                        {reasoning}

                        Evidence:
                        {evidence}

                        Instruction:
                        Return STRICT JSON with keys:
                        - conclusion (string)
                        - confidence (float 0-1)
                        - evidence_used (object)
                        """

        output = self.model.generate(prompt)

        try:
            import json
            decision_json = json.loads(output)
            return Decision(
                conclusion=decision_json["conclusion"],
                confidence=float(decision_json["confidence"]),
                evidence_used=decision_json.get("evidence_used", {})
            )
        except Exception:
            return Decision(
                conclusion="Cannot determine",
                confidence=0.3,
                evidence_used=evidence
            )

    def plan_next_action(self, state_context: dict):
        prompt = f"""
                    You are an autonomous planning agent.

                    GOAL:
                    {state_context.get("goal")}

                    CURRENT OBSERVATIONS:
                    {state_context.get("observations")}

                    RULES (FOLLOW STRICTLY):
                    - You MUST gather evidence before making a decision.
                    - Required evidence keys:
                    - market_demand
                    - risk
                    - If ANY required evidence is missing, you MUST choose USE_TOOL.
                    - You may ONLY choose DECIDE when ALL required evidence is present.

                    AVAILABLE TOOL:
                    - rag_search(query: str)

                    OUTPUT FORMAT (STRICT JSON ONLY):
                    {{
                    "action": "USE_TOOL" or "DECIDE",
                    "tool": "rag_search" (ONLY if action is USE_TOOL),
                    "query": "search query" (ONLY if action is USE_TOOL)
                    }}
                    """

        output = self.model.generate(prompt)

        try:
            import json
            return json.loads(output)
        except Exception:
            return {"action": "DECIDE"}


'''
Other Advanced LLMs like OpenAI can be also used, based on budget and swapped
'''
# import openai
# from schemas.decision import Decision

# class OpenAILLM:
#     def __init__(self, model: str = "gpt-3.5-turbo"):
#         self.model = model

#     def generate_decision(self, goal: str, reasoning: list, evidence: dict) -> Decision:
#         prompt = f"""
#         Goal: {goal}
#         Reasoning: {reasoning}
#         Evidence: {evidence}
#         Instruction: Produce JSON with conclusion, confidence (0-1), and evidence_used
#         """
#         response = openai.ChatCompletion.create(
#             model=self.model,
#             messages=[{"role": "user", "content": prompt}]
#         )
#         import json
#         try:
#             decision_json = json.loads(response.choices[0].message.content)
#             return Decision(
#                 conclusion=decision_json["conclusion"],
#                 confidence=float(decision_json["confidence"]),
#                 evidence_used=decision_json.get("evidence_used", {})
#             )
#         except Exception:
#             return Decision(
#                 conclusion="Cannot determine",
#                 confidence=0.3,
#                 evidence_used=evidence
#             )
