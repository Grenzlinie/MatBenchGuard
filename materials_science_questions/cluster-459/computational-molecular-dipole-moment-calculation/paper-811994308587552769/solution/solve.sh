#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dipole_moments.csv ===
cat > "/app/outputs/dipole_moments.csv" <<'FFEOF'
molecule,conformation,alpha,beta,dipole_moment
4-bromo-2-methyl,dh,110.0,110.0,1.74
4-bromo-2-methyl,hh,110.0,110.0,2.34
5-bromo-2-methyl,dh,114.0,114.0,1.15
5-bromo-2-methyl,hh,114.0,114.0,3.22
4-bromo-2-methyl,free,110.0,110.0,1.80
4-bromo-2-methyl,free,114.0,114.0,1.39
5-bromo-2-methyl,free,114.0,114.0,2.66
FFEOF
