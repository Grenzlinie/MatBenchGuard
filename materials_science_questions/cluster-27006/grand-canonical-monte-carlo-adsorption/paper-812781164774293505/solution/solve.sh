#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: gamma_caso4_gibbs_polynomial.json ===
python3 - "$OUTDIR" << 'PYEOF'
import sys, json
outdir = sys.argv[1]
with open(f"{outdir}/gamma_caso4_gibbs_polynomial.json", 'w') as f:
    json.dump({"a": -1417.12, "b": 0.3253}, f)
PYEOF

# === solve block: phase_boundary_curves.csv ===
python3 /solution/generate_outputs.py phase_boundary_curves.csv

# === solve block: mc_isotherm_298K.csv ===
python3 /solution/generate_outputs.py mc_isotherm_298K.csv

# === solve block: mc_isotherm_215K.csv ===
python3 /solution/generate_outputs.py mc_isotherm_215K.csv
