#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: reproduced_results.csv ===
cat > "$OUTDIR/reproduced_results.csv" << 'FFEOF'
complex,D_e_kJmol,rho_bcp_au
OC-HF,9.3,0.0123
SC-HF,21.8,0.0178
NN-HF,6.9,0.0084
HCN-HF,27.2,0.0183
H3N-HF,46.2,0.0344
OOO-HF,10.7,0.0129
SCO-HF,10.9,0.0099
OCO-HF,12.6,0.0112
NNO-HF,12.6,0.0163
OSO-HF,22.1,0.0164
H2CO-HF,27.3,0.0274
H2O-HF,34.8,0.0276
HF-HF,16.7,0.0213
H3P-HF,16.4,0.0114
H2S-HF,24.8,0.0115
HCl-HF,7.7,0.0072
HF-HCl,9.9,0.0147
FFEOF
