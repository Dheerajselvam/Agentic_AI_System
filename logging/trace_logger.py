import json
from datetime import datetime


class TraceLogger:
    def log(self, event_type: str, payload: dict):
        record = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": event_type,
            "payload": payload
        }
        print(json.dumps(record, indent=2))
