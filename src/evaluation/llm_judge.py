class LLMJudge:
    def __init__(self, llm):
        self.llm = llm

    def judge(self, goal: str, decision: str, evidence: dict) -> dict:
        prompt = {
            "goal": goal,
            "decision": decision,
            "evidence": evidence,
            "instruction": (
                "Judge if the decision answers the goal and if it is supported "
                "by the evidence. Return JSON with keys: goal_alignment (0-1), "
                "grounding (0-1), hallucinated (true/false)."
            )
        }

        return self.llm.raw_generate(prompt)
