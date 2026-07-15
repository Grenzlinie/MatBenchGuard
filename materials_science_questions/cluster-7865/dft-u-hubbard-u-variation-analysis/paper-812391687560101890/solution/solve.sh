#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: step_01_results.json ===
python3 -c '
import json, os
outdir = os.environ.get("OUTDIR", "/app/outputs")
with open(os.path.join(outdir, "step_01_results.json"), "w") as f:
    json.dump({
        "UPt3_S_q0": 4.6,
        "UPt3_S_q_pi2c": 1.9,
        "UPt3_S_q_pic": 3.1,
        "UPt3_S_q_2pic": 3.0,
        "CeAl3_S_q0": 2.9,
        "CeAl3_S_q_pi2c": 5.1,
        "CeAl3_S_q_pic": 6.3,
        "CeAl3_S_q_2pic": 3.1,
        "UPt3_chi0": 3.34,
        "CeAl3_chi0": 0.95
    }, f)
'
