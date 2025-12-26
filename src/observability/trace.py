class Trace:
    def __init__(self):
        self.steps = []

    def add(self, step_type: str, content: dict):
        self.steps.append({
            "type": step_type,
            "content": content
        })

    def export(self):
        return self.steps
