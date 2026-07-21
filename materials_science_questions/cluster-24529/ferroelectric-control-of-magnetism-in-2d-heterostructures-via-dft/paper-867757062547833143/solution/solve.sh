#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: phase_diagram.csv ===
python3 <<'PYEOF'
import csv

def phase_label(e, eps):
    if eps <= 7:
        if e > 0.15:
            return 0  # NI
        elif e > -0.1:
            return 2  # MES
        else:
            return 5  # QAH
    else:
        ni_bound = 0.15 - 0.005 * eps
        if e > ni_bound:
            return 0  # NI
        elif e > -0.08:
            return 1  # ES
        elif e > -0.18:
            return 3  # QAH-ES
        else:
            return 4  # QSH

with open('/app/outputs/phase_diagram.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Eg','epsilon_perp','phase'])
    for eg in [round(-0.4 + 0.02*i, 2) for i in range(41)]:
        for eps in range(2, 21):
            w.writerow([eg, eps, phase_label(eg, eps)])
PYEOF
