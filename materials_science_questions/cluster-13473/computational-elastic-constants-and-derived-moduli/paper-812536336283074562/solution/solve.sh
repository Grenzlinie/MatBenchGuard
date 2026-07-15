#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_elastic_constants.json ===
cat > /app/outputs/dft_elastic_constants.json <<'FFEOF'
{
  "poissons_ratio": -0.096,
  "youngs_modulus_GPa_nm": 257.6
}
FFEOF

# === solve block: md_stress_strain.csv ===
python3 /solution/generate_md_csv.py > /app/outputs/md_stress_strain.csv
