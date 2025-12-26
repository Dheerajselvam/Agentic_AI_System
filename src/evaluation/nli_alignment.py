from transformers import pipeline

class NLIAlignmentEvaluator:
    def __init__(self, model_name="facebook/bart-large-mnli"):
        self.nli = pipeline("text-classification", model=model_name)

    def entails(self, premise: str, hypothesis: str) -> float:
        result = self.nli(f"{premise} </s> {hypothesis}")[0]
        if result["label"].lower() == "entailment":
            return result["score"]
        return result["score"]
