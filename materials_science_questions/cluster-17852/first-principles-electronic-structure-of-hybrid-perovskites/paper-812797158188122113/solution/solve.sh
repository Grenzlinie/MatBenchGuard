#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "delta_E_PbI": 2.00,
  "delta_E_I": 5.20,
  "l1": 2.89,
  "l2": 3.16,
  "band_gap_PbI": 0.22,
  "band_gap_I": 1.73
}
FFEOF
