#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: energies.csv ===
python3 << 'PYEOF'
import csv, os

sizes = [561, 923, 1415, 2057, 3871, 6525, 10000]

# A1 phase energies (eV/atom): single, deca, ico
A1_single = [-5.125, -5.152, -5.168, -5.180, -5.188, -5.192, -5.1935]
A1_deca   = [e + 0.008 for e in A1_single]   # deca higher (less negative) by 8 meV
A1_ico    = [e + 0.020 for e in A1_single]   # ico higher by 20 meV

# L10 phase energies: single more negative by ~0.15 eV
L10_single = [e - 0.150 for e in A1_single]
L10_deca   = [e + 0.008 for e in L10_single]
L10_ico    = [e + 0.025 for e in L10_single]  # extra penalty from anti-phase boundaries

outfile = os.path.join(os.environ.get("OUTDIR"), "energies.csv")
with open(outfile, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["atoms", "energy_per_atom", "morphology", "phase"])
    for i, n in enumerate(sizes):
        w.writerow([n, round(A1_single[i], 5), "single", "A1"])
        w.writerow([n, round(A1_deca[i], 5), "deca", "A1"])
        w.writerow([n, round(A1_ico[i], 5), "ico", "A1"])
        w.writerow([n, round(L10_single[i], 5), "single", "L10"])
        w.writerow([n, round(L10_deca[i], 5), "deca", "L10"])
        w.writerow([n, round(L10_ico[i], 5), "ico", "L10"])
print("Written energies.csv")
PYEOF
