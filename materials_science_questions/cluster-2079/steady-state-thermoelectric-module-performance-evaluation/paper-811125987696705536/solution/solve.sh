#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: optimal_design.json ===
cat > /app/outputs/optimal_design.json <<'EOF'
{
  "thickness_mm": 4,
  "TEM_per_sqm": 16
}
EOF

# === solve block: cooling_transient.csv ===
python3 /solution/generate_transient.py cooling > /app/outputs/cooling_transient.csv

# === solve block: heating_transient.csv ===
python3 /solution/generate_transient.py heating > /app/outputs/heating_transient.csv
