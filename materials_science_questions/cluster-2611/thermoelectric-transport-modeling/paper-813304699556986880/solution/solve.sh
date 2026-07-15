#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: transport_parameters.csv ===
python3 <<'PYEOF'
import csv

outpath = "/app/outputs/transport_parameters.csv"
with open(outpath, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sample", "Ef_eV", "lambda", "n_cm3", "mu_cm2Vs", "P_uW_K2m"])
    writer.writerow(["P3HT", -0.72, 1.13, 1.3e20, 0.45, 0.5])
    writer.writerow(["P3HT-Bi2Te3", -0.70, 2.99, 0.9e20, 0.31, 6.3])
PYEOF
