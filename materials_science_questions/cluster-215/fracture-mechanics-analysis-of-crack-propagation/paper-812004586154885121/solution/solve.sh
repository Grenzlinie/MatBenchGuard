#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: rotated_matrix.json ===
python3 <<'PYEOF'
import json, math
phi = 3 * math.pi / 8
c = math.cos(phi)
s = math.sin(phi)
ZN, Z1, Z2, Z12 = 1.0, 2.0, 3.0, 0.5
Z13, Z23 = 0.3, 0.4
Z1p = s**2 * Z2 + c**2 * Z1 + 2*c*s * Z12
Z2p = c**2 * Z2 + s**2 * Z1 - 2*c*s * Z12
Z23p = c * Z23 - s * Z13
Z13p = s * Z23 + c * Z13
data = {
    "rotation_angle": phi,
    "Z_N_prime": ZN,
    "Z1_prime": Z1p,
    "Z2_prime": Z2p,
    "Z12_prime": 0.0,
    "Z23_prime": Z23p,
    "Z13_prime": Z13p
}
with open('/app/outputs/rotated_matrix.json', 'w') as f:
    json.dump(data, f)
PYEOF
