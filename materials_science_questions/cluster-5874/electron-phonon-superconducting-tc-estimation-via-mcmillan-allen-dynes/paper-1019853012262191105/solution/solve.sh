#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: tc_results.json ===
cat > /app/outputs/tc_results.json <<'FFEOF'
[
  {"phase": "oS48-Mg4/5B2C2", "Tc_K": 57.0},
  {"phase": "hP7-Mg2/3B2C2", "Tc_K": 73.0},
  {"phase": "mP23-Na7/8BC", "Tc_K": 88.0},
  {"phase": "oP22-Na3/4BC", "Tc_K": 84.0},
  {"phase": "oS32-Na2/3BC", "Tc_K": 43.0}
]
FFEOF
