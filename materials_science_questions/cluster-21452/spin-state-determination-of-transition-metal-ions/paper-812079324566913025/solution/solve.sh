#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: ni_j_values.json ===
cat > "$OUTDIR/ni_j_values.json" <<'FFEOF'
{
  "J1": 0.11,
  "J2": -9.89,
  "J3": 3.18,
  "J4": 0.23
}
FFEOF

# === solve block: co_d_values.json ===
cat > "$OUTDIR/co_d_values.json" <<'FFEOF'
{
  "|D_Co_ring|": 87.0,
  "|D_Co_central|": 82.0
}
FFEOF
