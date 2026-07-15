#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: optical_gaps.json ===
cat > /app/outputs/optical_gaps.json <<'FFEOF'
{
  "Cd17Se17": 2.92,
  "Cd26Se26": 2.38,
  "Cd38Se38": 2.10
}
FFEOF
