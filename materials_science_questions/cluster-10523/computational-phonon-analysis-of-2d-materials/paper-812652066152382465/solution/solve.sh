#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_mlg_tensile.csv ===
python3 /solution/generate_tensile.py --output /app/outputs/step_01_mlg_tensile.csv --material MLG

# === solve block: step_02_gh_tensile.csv ===
python3 /solution/generate_tensile.py --output /app/outputs/step_02_gh_tensile.csv --material GH

# === solve block: step_03_strain_summary.json ===
cat > "/app/outputs/step_03_strain_summary.json" <<'FFEOF'
{
  "mlg_failure_strain": 0.1,
  "gh_max_strain": 12.5
}
FFEOF
