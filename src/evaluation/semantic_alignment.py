from sentence_transformers import SentenceTransformer, util

class SemanticAlignmentEvaluator:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def score(self, goal: str, decision: str) -> float:
        goal_emb = self.model.encode(goal, convert_to_tensor=True)
        decision_emb = self.model.encode(decision, convert_to_tensor=True)
        return float(util.cos_sim(goal_emb, decision_emb))
