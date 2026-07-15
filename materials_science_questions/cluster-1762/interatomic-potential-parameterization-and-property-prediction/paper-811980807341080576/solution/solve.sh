#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: activation_energies.csv ===
cat > $OUTDIR/activation_energies.csv <<'EOF'
compound,cation_single,anion_single,cation_pair,anion_pair
LiF,0.69,0.86,0.70,0.73
LiCl,0.70,1.34,0.61,1.00
LiBr,0.63,1.54,0.57,1.14
LiI,0.70,2.40,0.63,1.68
NaF,0.60,0.67,0.73,0.74
NaCl,0.85,1.19,0.90,1.02
NaBr,0.68,1.11,0.59,0.86
NaI,0.74,1.52,0.71,1.16
KF,0.73,0.64,0.62,0.67
KCl,0.84,0.84,0.63,0.64
KBr,0.90,0.94,0.79,0.66
KI,0.87,1.16,0.71,0.76
RbF,0.75,0.70,0.57,0.63
RbCl,0.79,0.84,0.62,0.61
RbBr,0.84,0.93,0.65,0.62
RbI,0.95,1.13,0.71,0.69
EOF

# === solve block: nacl_diffusion_energies.csv ===
cat > $OUTDIR/nacl_diffusion_energies.csv <<'EOF'
formation_vacancy_pair,formation_schottky_pair,diffusion_vacancy_pair,diffusion_anion_vacancy
1.55,2.35,2.57,2.37
EOF
