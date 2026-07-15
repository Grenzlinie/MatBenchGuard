#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: acoustic_contributions.json ===
cat > /app/outputs/acoustic_contributions.json <<'FFEOF'
{
  "B11_ac_E": 0.20,
  "B33_ac_E": 0.29,
  "B11_ac_P": 0.17,
  "B33_ac_P": 0.20
}
FFEOF

# === solve block: optic_contribution.json ===
cat > /app/outputs/optic_contribution.json <<'FFEOF'
{
  "B11_op": 0.52
}
FFEOF

# === solve block: final_results.json ===
cat > /app/outputs/final_results.json <<'FFEOF'
{
  "B11_E": 0.72,
  "B33_E": 0.29,
  "B11_P": 0.69,
  "B33_P": 0.20
}
FFEOF
