#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: seebeck_coefficients.csv ===
cat > "$OUTDIR/seebeck_coefficients.csv" <<'EOF'
material,S_muV_per_K,xi_V_s0p5_per_J_cm2
wool,6458,1.86
PP,13821,0.239
silk,12201,0.183
nylon,11118,0.156
NR,9392,0.117
cellulose,12604,0.035
Al,-2.5,-1e-06
Si,-1769,-1.2e-03
quartz,-13434,-0.081
sulfur,-7492,-0.118
PE,-13846,-0.156
PTFE,-12291,-0.158
PDMS,-12568,-0.225
PVC,-12449,-0.279
EOF

# === solve block: similarity_score.txt ===
echo "0.83" > "$OUTDIR/similarity_score.txt"

# === solve block: validation_Al_Si.txt ===
cat > "$OUTDIR/validation_Al_Si.txt" <<'EOF'
Al_rel_error: 38.9%
Si_rel_error: 30.8%
EOF
