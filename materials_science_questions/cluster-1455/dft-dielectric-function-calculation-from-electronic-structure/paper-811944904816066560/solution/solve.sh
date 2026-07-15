#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: elastic_constants.json ===
cat > "/app/outputs/elastic_constants.json" <<'FFEOF'
{
  "C11": 181.00667,
  "C12": 37.28050,
  "C44": 38.86243,
  "B0": 85.18922,
  "v": 0.1708
}
FFEOF

# === solve block: dielectric_function.csv ===
python3 /solution/generate_dielectric.py
