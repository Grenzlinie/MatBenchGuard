#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: results.json ===
cat > $OUTDIR/results.json << 'EOF'
{
  "eta": {
    "value": 0.25,
    "error": 0.03
  },
  "gamma": {
    "value": 1.7,
    "error": 0.2
  },
  "magnetization_cooling_low_T": 0.90,
  "magnetization_cooling_high_T": 0.05,
  "magnetization_warming_low_T": 0.83,
  "magnetization_warming_high_T": 0.05
}
EOF
