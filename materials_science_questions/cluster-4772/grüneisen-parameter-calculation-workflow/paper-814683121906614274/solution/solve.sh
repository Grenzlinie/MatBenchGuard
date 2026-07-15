#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_04_lattice_parameters_vs_T.csv ===
python3 /solution/generate_lattice_csv.py

# === solve block: step_05_gruneisen_parameters.json ===
cat > /app/outputs/step_05_gruneisen_parameters.json <<'FFEOF'
{
  "E_u": -1.969,
  "E_g": -1.401,
  "A_2u": 6.439,
  "A_2g": 0.392
}
FFEOF
