#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_02_results.json ===
python3 << 'PYEOF'
import json, math
lam = 2.0
phi = math.pi / 4
ecc = math.sqrt(1 - 1/(lam*lam))
longi = lam + 1/lam
trans = math.sin(2*phi) * (lam - 1/lam)
angle = abs(trans / longi)
data = {
    "parameters": {"lambda": lam, "phi": phi},
    "longitudinal_current": longi,
    "transverse_valley_current": trans,
    "valley_hall_angle": angle,
    "derived_eccentricity": ecc
}
with open("/app/outputs/step_02_results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
