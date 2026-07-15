#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: slopes.json ===
python3 <<'PYEOF'
import json
import math
pi = math.pi
# Exact analytic slopes from Table I of the paper
one_s = -4.0 / (3 * pi)
two_s = one_s * 88 / 5
two_p_xy = one_s * 16 / 5
two_p_z = -one_s * 32   # 4/(3π)*32, one_s is negative

result = {
    "1s": one_s,
    "2s": two_s,
    "2p_xy": two_p_xy,
    "2p_z": two_p_z
}
with open("/app/outputs/slopes.json", "w") as f:
    json.dump(result, f, indent=2)
PYEOF
