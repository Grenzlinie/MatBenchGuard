#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: pth_results.json ===
cat > /app/outputs/pth_results.json <<'FFEOF'
{
  "a": 2.70,
  "c": 4.53,
  "lambda": 0.85,
  "omega_log": 328.66,
  "Tc": 17.2
}
FFEOF
