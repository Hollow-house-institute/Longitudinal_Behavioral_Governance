#!/usr/bin/env python3
import json
with open("telemetry/GOVERNANCE_LOG.jsonl") as f:
    for line in f:
        event=json.loads(line)
        print(f"[REPLAY] {event['timestamp']} :: {event['action']} :: {event['outcome']}")
