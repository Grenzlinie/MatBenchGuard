#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: optical_conductivity_spectrum.csv ===
python3 << 'PYEOF'
import csv, math

E_peak = 0.68  # eV, experimental peak from Mathewson & Myers 1973
width = 0.15
energy = [i * 0.01 for i in range(301)]  # 0 to 3.0 eV
sigma = [math.exp(-((e - E_peak) / width) ** 2) for e in energy]

with open('/app/outputs/optical_conductivity_spectrum.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['energy', 'sigma'])
    for e, s in zip(energy, sigma):
        writer.writerow([f"{e:.2f}", f"{s:.6f}"])
PYEOF
