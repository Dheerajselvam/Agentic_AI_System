import json
from datetime import datetime

class Logger:
    @staticmethod
    def log(event: str, payload: dict):
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": event,
            "payload": payload
        }
        print(json.dumps(record, indent=2))
