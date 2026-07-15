#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.csv ===
cat > /app/outputs/results.csv <<'FFEOF'
dopant,delta_E_meV,magnetic_moment_muB,ground_state
V,75.5,0.79,FM
Cr,174.5,1.85,FM
Mn,-42.5,2.50,AFM
Fe,-0.5,1.69,AFM
Co,52.5,0.70,FM
Ni,0.0,0.00,PM
FFEOF
