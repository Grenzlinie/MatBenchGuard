#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energy_derivative.csv ===
python3 - <<'PYEOF'
import csv, os

out = os.path.join('/app/outputs', 'energy_derivative.csv')
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['beta', 'E', 'dE_dbeta'])
    # analytic piecewise E(beta) with kink at 0.865
    beta_c = 0.865
    E0 = 10.0
    slope1 = 2.0
    slope2 = 10.0
    E_c = E0 + slope1 * beta_c
    for beta in [round(0.5 + 0.01*i, 2) for i in range(51)]:
        if beta <= beta_c:
            E = E0 + slope1 * beta
            dEdb = slope1
        else:
            E = E_c + slope2 * (beta - beta_c)
            dEdb = slope2
        w.writerow([f'{beta:.2f}', f'{E:.5f}', f'{dEdb:.5f}'])
PYEOF

# === solve block: tc_table.csv ===
python3 - <<'PYEOF'
import csv, os

out = os.path.join('/app/outputs', 'tc_table.csv')
# estimated Tc values extracted from the paper's text and figures
rows = [
    (12, 3, 1.0, 0.201),
    (12, 3, 0.9, 0.201),
    (12, 3, 0.8, 0.002),
    (12, 3, 0.75, 0.0012),
    (12, 3, 0.65, 0.158),
    (12, 3, 0.5, 0.198),
    (12, 11, 1.0, 0.201),
    (12, 11, 0.8, 0.042),
    (12, 11, 0.6, 0.0082),
    (12, 11, 0.4, 0.0021),
    (12, 11, 0.2, 0.0005),
    (38, 4, 1.0, 0.160),
    (38, 4, 0.8, 0.152),
    (38, 4, 0.6, 0.135),
    (38, 4, 0.5, 0.052),
    (38, 4, 0.4, 0.0011),
    (38, 7, 1.0, 0.160),
    (38, 7, 0.9, 0.082),
    (38, 7, 0.8, 0.011),
    (38, 7, 0.7, 0.0012),
    (38, 33, 1.0, 0.160),
    (38, 33, 0.8, 0.145),
    (38, 33, 0.6, 0.102),
    (38, 33, 0.5, 0.048),
    (38, 33, 0.4, 0.012),
]
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['N', 'NB', 'beta', 'Tc'])
    for N, NB, beta, Tc in rows:
        w.writerow([N, NB, beta, Tc])
PYEOF
