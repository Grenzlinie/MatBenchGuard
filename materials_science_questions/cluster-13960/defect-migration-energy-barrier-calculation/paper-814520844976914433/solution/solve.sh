#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_barrier.json ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -c '
import json
data = {
    "dilute_barrier_meV": 550.0,
    "concentrated_barrier_meV": 550.0
}
with open("/app/outputs/step_01_barrier.json", "w") as f:
    json.dump(data, f, indent=2)
'
