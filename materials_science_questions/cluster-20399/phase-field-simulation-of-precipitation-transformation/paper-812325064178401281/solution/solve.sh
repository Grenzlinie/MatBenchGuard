#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: crss_results.csv ===
cat > /app/outputs/crss_results.csv <<'FFEOF'
condition,crss_MPa
Cu_spherical_1.25nm,200
Ni_spherical_1.25nm,270
CuNi_ordered_1.25nm,330
Fe25Cu75_spherical_1.25nm,160
CuNi_core_shell_core0.6nm,220
Cu_ellipsoidal_0.5nm_halfaxis,130
FFEOF
