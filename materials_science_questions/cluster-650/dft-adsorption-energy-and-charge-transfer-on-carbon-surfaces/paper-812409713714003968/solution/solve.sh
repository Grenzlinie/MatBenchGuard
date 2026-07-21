#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: adsorption_energies.csv ===
python3 <<'PYEOF'
import csv
rows = [
    ("TO38", "(1 0 0)", "center", 0.00),
    ("TO38", "(1 1 1)", "fcc (sites B)", 0.26),
    ("TO38", "(1 1 1)", "hcp (sites A)", 0.26),
    ("Ih55", "(1 1 1)", "fcc (sites B)", 0.00),
    ("Ih55", "(1 1 1)", "hcp (sites A)", 0.02),
    ("Dh75", "truncation", "truncation", 0.00),
    ("Dh75", "(1 0 0)", "center", 0.02),
    ("Dh75", "(1 1 1)", "fcc (sites D)", 0.25),
    ("Dh75", "(1 1 1)", "fcc (sites B)", 0.27),
    ("Dh75", "(1 1 1)", "hcp (sites E)", 0.28),
    ("Dh75", "(1 1 1)", "hcp (sites C)", 0.26),
    ("Dh75", "(1 1 1)", "hcp (sites A)", 0.27),
]
outpath = "/app/outputs/adsorption_energies.csv"
with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['cluster','facet','site','energy_eV'])
    for row in rows:
        writer.writerow(row)
PYEOF

# === solve block: diffusion_barriers.csv ===
python3 <<'PYEOF'
import csv
rows = [
    ("TO38", "j(1 1 1)", 0.18),
    ("TO38", "j(1 1 1)/(1 1 1)", 0.31),
    ("TO38", "j(1 1 1)/(1 0 0)", 0.37),
    ("Ih55", "j(1 1 1)", 0.12),
    ("Ih55", "j(1 1 1)/(1 1 1)", 0.27),
    ("Ih55", "ex(1 1 1)/(1 1 1)", 0.54),
    ("Dh75", "j(1 1 1)", 0.18),
    ("Dh75", "j(1 1 1)/(1 1 1)", 0.29),
    ("Dh75", "j(1 1 1)/(1 0 0)", 0.33),
    ("Dh75", "j(1 1 1)/R", 0.30),
    ("Dh75", "ex(1 1 1)/(1 1 1)", 1.40),
]
outpath = "/app/outputs/diffusion_barriers.csv"
with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['cluster','process','barrier_eV'])
    for row in rows:
        writer.writerow(row)
PYEOF
