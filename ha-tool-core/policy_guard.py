#!/usr/bin/env python3
import json
from datetime import datetime

TOOL_CLASSES = {
    "READ":     {"auto": True,  "auto_safe": True,  "locked": False},
    "WRITE":    {"auto": True,  "auto_safe": True,  "locked": True},
    "SYSTEM":   {"auto": False, "auto_safe": True,  "locked": True},
    "CRITICAL": {"auto": False, "auto_safe": False, "locked": True},
}

def validate(tool, tool_class, autonomy_level="auto"):
    policy = TOOL_CLASSES.get(tool_class, {})
    allowed = policy.get(autonomy_level, False)
    return {
        "allowed": allowed,
        "tool": tool,
        "class": tool_class,
        "autonomy": autonomy_level,
        "reason": "OK" if allowed else "Validation humaine requise",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

if __name__ == "__main__":
    print(json.dumps(validate("nvidia-smi", "SYSTEM", "auto_safe"), indent=2))
