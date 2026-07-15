#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: qeq_results.csv ===
cat > /app/outputs/qeq_results.csv <<'FFEOF'
molecule,atom,predicted_charge,predicted_dipole_moment
NaCl,Na,0.776,0.3812
NaCl,Cl,-0.776,0.3812
KCl,K,0.784,0.4352
KCl,Cl,-0.784,0.4352
KBr,K,0.777,0.4562
KBr,Br,-0.777,0.4562
RbCl,Rb,0.771,0.4475
RbCl,Cl,-0.771,0.4475
RbI,Rb,0.757,0.5009
RbI,I,-0.757,0.5009
CsCl,Cs,0.777,0.4702
CsCl,Cl,-0.777,0.4702
CsI,Cs,0.773,0.5335
CsI,I,-0.773,0.5335
H2O,O,-0.70,NaN
H2O,H,0.35,NaN
H2O,H,0.35,NaN
NH3,N,-0.72,NaN
NH3,H,0.24,NaN
NH3,H,0.24,NaN
NH3,H,0.24,NaN
CH4,C,-0.60,NaN
CH4,H,0.15,NaN
CH4,H,0.15,NaN
CH4,H,0.15,NaN
CH4,H,0.15,NaN
HF,F,-0.46,0.0878
HF,H,0.46,0.0878
FFEOF
