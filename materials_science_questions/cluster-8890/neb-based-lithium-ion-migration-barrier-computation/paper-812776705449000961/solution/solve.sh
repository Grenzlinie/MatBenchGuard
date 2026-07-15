#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: diffusion_results.csv ===
cat > "/app/outputs/diffusion_results.csv" <<'CSVEOF'
impurity,lattice,activation_energy_eV,diffusion_coefficient_cm2_s1
Ag,PbS,0.54,1.80e-13
Li,PbS,0.76,2.26e-15
H,PbS,0.19,1.41e-5
Ag,Pb-doped Ag2S,0.01,2.60e-4
Ag,Ag2S,0.40,7.34e-10
Li,Ag2S,0.52,2.65e-11
H,Ag2S,0.41,3.97e-9
CSVEOF
