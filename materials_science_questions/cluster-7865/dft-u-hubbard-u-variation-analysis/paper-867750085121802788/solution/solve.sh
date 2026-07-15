#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: inter_site_matrix_M.json ===
python3 <<'PYEOF'
import json, os
out = os.environ['OUTDIR']
M = {
    "M11": -4.8,
    "M22": 39.5,
    "M23": 49.0,
    "M32": -44.5,
    "M33": -26.0
}
intra = {
    "P1xx": [0.0, 0.0, 0.0],
    "P1yy": [2.5, 0.0, 0.0],
    "P1zz": [-2.5, 0.0, 0.0],
    "P1xy": [5.0, 7.5, 0.0],
    "P1xz": [0.0, -5.0, 0.0],
    "P1yz": [7.5, -2.5, 0.0]
}
data = {
    "M": M,
    "intra_site_coefficients": intra,
    "units": "M in 10^-5 eÅ, intra-site coefficients in 10^-6 eÅ"
}
with open(os.path.join(out, "inter_site_matrix_M.json"), 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: total_polarization_helical_states.csv ===
python3 <<'PYEOF'
import csv, math, os
out = os.environ['OUTDIR']
q1 = "1/3,0,0"
P1 = (58.8, 0.0, 0.0)
q2 = "1/3,1/3,0"
a = 71.4 / math.sqrt(2)
P2 = (a, a, 0.0)
with open(os.path.join(out, "total_polarization_helical_states.csv"), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["q_vec", "Px", "Py", "Pz"])
    writer.writerow([q1, P1[0], P1[1], P1[2]])
    writer.writerow([q2, P2[0], P2[1], P2[2]])
PYEOF
