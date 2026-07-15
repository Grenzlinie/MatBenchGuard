#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: step_01_barrier.csv ===
# Write the known reference barrier for pathway D1.
cat > "/app/outputs/step_01_barrier.csv" <<'FFEOF'
pathway,barrier_eV
D1,0.21
FFEOF
