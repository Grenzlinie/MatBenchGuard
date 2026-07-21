#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: renormalization_factors.csv ===
cat > "$OUTDIR/renormalization_factors.csv" <<'FFEOF'
k_label,mode,r_value
Gamma,0,1.0
Gamma,1,0.95
Gamma,2,0.95
M,0,0.70
M,1,0.55
M,2,0.30
FFEOF

# === solve block: magnon_dispersion.csv ===
python3 /solution/generate_dispersion.py > "$OUTDIR/magnon_dispersion.csv"
