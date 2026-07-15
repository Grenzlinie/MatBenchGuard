#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: step_01_total_irrep.json ===
cat > "$OUTDIR/step_01_total_irrep.json" << 'EOF'
{
  "a1": 18.5,
  "a2": 15,
  "b1": 14.5,
  "b2": 18,
  "e": 34.5,
  "total_df": 135
}
EOF
