#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dielectric_constants.csv ===
cat > /app/outputs/dielectric_constants.csv <<'FFEOF'
composition_x,epsilon
0,50.0
0.125,68.0
0.25,58.0
0.5,42.0
FFEOF
