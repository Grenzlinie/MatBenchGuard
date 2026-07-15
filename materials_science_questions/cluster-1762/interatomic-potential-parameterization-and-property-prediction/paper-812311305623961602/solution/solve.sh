#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: polarizabilities.csv ===
cat > /app/outputs/polarizabilities.csv <<'FFEOF'
Ion,Polarizability
H-,98.81
F-,10.35
Cl-,28.76
Br-,37.53
I-,55.90
FFEOF
