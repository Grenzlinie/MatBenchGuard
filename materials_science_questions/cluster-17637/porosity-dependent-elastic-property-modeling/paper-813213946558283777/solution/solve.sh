#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: predicted_properties.csv ===
python3 > "$OUTDIR/predicted_properties.csv" << 'PYEOF'
import sys

Es = 110.0
sigma_ys = 220.0

data = [
    (900, 0.61, 19.33, 22.80),
    (1000, 0.62, 19.52, 23.25),
    (1100, 0.60, 19.57, 22.88),
    (1200, 0.62, 19.69, 24.20),
    (1300, 0.64, 19.33, 24.43),
]

print("FST,E_oc_predicted,E_dc_predicted,sigma_standard_predicted,sigma_modified_predicted")
for fst, rhor, d, t in data:
    l_oct = d / 2.41
    l_dc = d / 3.08
    C1_oct = 1.0 / (rhor**2 * (t / l_oct)**4)
    C1_dc = 1.0 / (rhor**2 * (t / l_dc)**4)
    E_oct = C1_oct * rhor**2 * Es
    E_dc = C1_dc * rhor**2 * Es
    sigma_std = sigma_ys * 0.3 * rhor ** 1.5
    sigma_mod = sigma_ys * rhor ** 2.5
    print(f"{fst},{E_oct:.2f},{E_dc:.2f},{sigma_std:.2f},{sigma_mod:.2f}")
PYEOF
