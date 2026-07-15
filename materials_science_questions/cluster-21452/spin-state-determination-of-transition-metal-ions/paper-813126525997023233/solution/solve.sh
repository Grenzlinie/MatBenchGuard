#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: rotational_strengths.json ===
cat > /app/outputs/rotational_strengths.json <<'FFEOF'
{
  "R(6A1->4A1)": 1.66,
  "R(6A1->a4Eu)": -0.17,
  "R(6A1->a4Ev)": 2.49
}
FFEOF
