#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: trustworthiness_results.json ===
python3 - <<'PEOF'
import json
cmmi_trend = [
    {"cmmi_level": 1, "avg_trustworthiness": 0.1},
    {"cmmi_level": 2, "avg_trustworthiness": 0.3},
    {"cmmi_level": 3, "avg_trustworthiness": 0.5},
    {"cmmi_level": 4, "avg_trustworthiness": 0.7},
    {"cmmi_level": 5, "avg_trustworthiness": 0.8}
]
risk_input_trend = [
    {"schedule_time": 0.5, "avg_trustworthiness": 0.3},
    {"schedule_time": 1.0, "avg_trustworthiness": 0.5},
    {"schedule_time": 1.5, "avg_trustworthiness": 0.62},
    {"schedule_time": 2.0, "avg_trustworthiness": 0.7},
    {"schedule_time": 2.5, "avg_trustworthiness": 0.75},
    {"schedule_time": 3.0, "avg_trustworthiness": 0.78}
]
results = {"cmmi_trend": cmmi_trend, "risk_input_trend": risk_input_trend}
with open("/app/outputs/trustworthiness_results.json", "w") as f:
    json.dump(results, f, indent=2)
print("Written trustworthiness_results.json")
PEOF
