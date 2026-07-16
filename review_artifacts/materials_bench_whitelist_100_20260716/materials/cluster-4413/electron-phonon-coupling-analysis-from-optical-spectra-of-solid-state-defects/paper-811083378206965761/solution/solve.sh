#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_deltaE_CP.json ===
python3 -c '
import json
params = {
    "x0": {"E5d1Ex": 34542, "SS": 2896, "E3P2Ex": 21618},
    "x1": {"E5d1Ex": 34843, "SS": 2689, "E3P2Ex": 22186},
    "x2": {"E5d1Ex": 35335, "SS": 2735, "E3P2Ex": 22185},
    "x3": {"E5d1Ex": 35747, "SS": 2798, "E3P2Ex": 22181},
    "x4": {"E5d1Ex": 35939, "SS": 2744, "E3P2Ex": 22183},
    "x5": {"E5d1Ex": 36331, "SS": 2947, "E3P2Ex": 22295},
}
results = {}
for k, p in params.items():
    SS = p["SS"]
    S_hbar_omega = SS / 2.0
    u = (p["E5d1Ex"] - p["E3P2Ex"]) / SS
    results[k] = S_hbar_omega * (u - 1) ** 2
with open("/app/outputs/step_01_deltaE_CP.json", "w") as f:
    json.dump(results, f)
'

# === solve finalize ===
echo "All artifacts written."
