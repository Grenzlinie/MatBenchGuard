#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: magnetic_moments.csv ===
cat > /app/outputs/magnetic_moments.csv <<'FFEOF'
system,layer_label,magnetic_moment_muB
MnAs_MnTerm,Mn(S),3.79
MnAs_MnTerm,Mn(S-2),3.02
MnAs_MnTerm,Mn(S-4),3.11
MnAs_MnTerm,Mn(S-6),3.10
MnAs_MnTerm,Mn(C),3.10
MnAs_MnTerm,As(S-1),-0.10
MnAs_MnTerm,As(S-3),-0.10
MnAs_MnTerm,As(S-5),-0.10
MnAs_MnTerm,As(S-7),-0.10
MnAs_AsTerm,Mn(S-1),3.11
MnAs_AsTerm,Mn(S-3),3.06
MnAs_AsTerm,Mn(S-5),3.11
MnAs_AsTerm,Mn(C),3.11
MnAs_AsTerm,As(S),-0.15
MnAs_AsTerm,As(S-2),-0.09
MnAs_AsTerm,As(S-4),-0.10
MnAs_AsTerm,As(S-6),-0.10
MnSb_MnTerm,Mn(S),4.04
MnSb_MnTerm,Mn(S-2),3.34
MnSb_MnTerm,Mn(S-4),3.37
MnSb_MnTerm,Mn(S-6),3.32
MnSb_MnTerm,Mn(C),3.32
MnSb_MnTerm,Sb(S-1),-0.09
MnSb_MnTerm,Sb(S-3),-0.12
MnSb_MnTerm,Sb(S-5),-0.12
MnSb_MnTerm,Sb(S-7),-0.12
MnSb_SbTerm,Mn(S-1),3.26
MnSb_SbTerm,Mn(S-3),3.25
MnSb_SbTerm,Mn(S-5),3.26
MnSb_SbTerm,Mn(C),3.31
MnSb_SbTerm,Sb(S),-0.18
MnSb_SbTerm,Sb(S-2),-0.11
MnSb_SbTerm,Sb(S-4),-0.12
MnSb_SbTerm,Sb(S-6),-0.12
FFEOF

# === solve block: center_ldos.csv ===
python3 /solution/gen_ldos.py /app/outputs/center_ldos.csv
