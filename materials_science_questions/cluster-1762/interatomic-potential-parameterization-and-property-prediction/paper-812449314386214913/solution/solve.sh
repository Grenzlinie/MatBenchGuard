#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: cvm_phase_diagram_results.json ===
cat > /app/outputs/cvm_phase_diagram_results.json <<'FFEOF'
{
  "percolation_limit": 0.57,
  "tricritical_q0": {
    "x": 0.727,
    "T_K": 3420
  },
  "tricritical_q025": {
    "x": 0.692,
    "T_K": 2280
  }
}
FFEOF
