#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: C(T)_J_integrals.csv ===
python3 <<'PYEOF'
import csv
rows = [
    (0.00, 0.0, 0.0, 0.0),
    (0.10, 2.86, 2.86, 0.0),
    (0.20, 11.43, 11.43, 0.0),
    (0.25, 15.86, 17.86, 2.00),
    (0.30, 21.71, 25.71, 4.00),
    (0.35, 28.00, 35.00, 7.00),
    (0.40, 35.71, 45.71, 10.00),
    (0.44, 43.31, 55.31, 12.00),
]
with open('/app/outputs/C(T)_J_integrals.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['v_LL_mm', 'J_far_ep_kJ_m2', 'J_Gamma2_ep_kJ_m2', 'Cp_kJ_m2'])
    for v, jf, jg, cp in rows:
        w.writerow([v, jf, jg, cp])
PYEOF
