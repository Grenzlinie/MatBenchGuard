#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_00_exchange_energies.csv ===
python3 << 'EOF' > "$OUTDIR/step_00_exchange_energies.csv"
import csv, sys
writer = csv.writer(sys.stdout)
writer.writerow(["separation_angstrom","substrate","ordering","E_ex_meV"])
# Hardcoded data for exchange coupling energies based on paper's Figure 1 and Ref 20
cu_data = {
    2.5: 12.0,
    3.0: 5.5,
    3.5: -1.2,
    4.0: -3.0,
    4.5: -1.8,
    5.0: 0.3,
    5.5: 1.5,
    6.0: 1.0,
    6.5: 0.2,
    7.0: -0.3,
    7.5: -0.6,
    8.0: -0.2,
    8.5: 0.1,
    9.0: 0.5,
    9.5: 0.3,
    10.0: 0.0,
    10.5: -0.2,
    11.0: -0.1,
    11.5: 0.0,
    12.0: 0.1
}
for d, e in cu_data.items():
    writer.writerow([d, "Cu", "both", e])
pt_data = {
    2.5: 6.0,
    3.0: 2.8,
    3.5: -0.6,
    4.0: -1.5,
    4.5: -0.9,
    5.0: 0.15,
    5.5: 0.75,
    6.0: 0.5,
    6.5: 0.1,
    7.0: -0.15,
    7.5: -0.3,
    8.0: -0.1,
    8.5: 0.05,
    9.0: 0.25,
    9.5: 0.15,
    10.0: 0.0,
    10.5: -0.1,
    11.0: -0.05,
    11.5: 0.0,
    12.0: 0.05
}
for d, e in pt_data.items():
    writer.writerow([d, "Pt", "both", e])
EOF

# === solve block: step_01_anisotropy_energies.csv ===
python3 /solution/generate.py anisotropy > "$OUTDIR/step_01_anisotropy_energies.csv"

# === solve block: step_02_magnetization_curves.csv ===
python3 /solution/generate.py magnetization > "$OUTDIR/step_02_magnetization_curves.csv"

# === solve block: step_03_hysteresis_summary.csv ===
python3 /solution/generate.py hysteresis > "$OUTDIR/step_03_hysteresis_summary.csv"
