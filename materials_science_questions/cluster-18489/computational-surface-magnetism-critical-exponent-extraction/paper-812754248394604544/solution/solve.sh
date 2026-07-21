#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c '
import math, json

S = 2
J = 1.0
gmuB_HA = 0.1
c_k_abs = 0.01

bulk_energy = math.sqrt(gmuB_HA * (gmuB_HA + 16 * S * J))
surface_energy = math.sqrt(gmuB_HA * (gmuB_HA + 8 * S * J))
intensity_ratio = 4 * math.pi * c_k_abs * math.sqrt((S * J) / gmuB_HA)

result = {
    "bulk_energy": round(bulk_energy, 15),
    "surface_energy": round(surface_energy, 15),
    "intensity_ratio": round(intensity_ratio, 15)
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(result, f)
'
