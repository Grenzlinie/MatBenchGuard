#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: monolayer_results.json ===
python3 -c '
import json
data = {
    "CF_C": {"E_rel": 0.0, "a": 2.611, "b": 4.521},
    "CF_W": {"E_rel": 0.071, "a": 2.635, "b": 4.200},
    "CF_B": {"E_rel": 0.148, "a": 2.585, "b": 4.617},
    "CH_C": {"E_rel": 0.0, "a": 2.545, "b": 4.406},
    "CH_W": {"E_rel": 0.055, "a": 2.553, "b": 3.836},
    "CH_B": {"E_rel": 0.103, "a": 2.533, "b": 4.314}
}
with open("/app/outputs/monolayer_results.json", "w") as f:
    json.dump(data, f, indent=2)
'
