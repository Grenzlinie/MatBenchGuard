#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: binding_energies.csv ===
cat > "$OUTDIR/binding_energies.csv" <<'CSVEOF'
system,Eb,d_Cu_O
P-CNT,-0.53,-1
SW-CNT,-1.26,-1
MV-CNT,-3.08,-1
P-CNT-O,-0.73,2.43
P-CNT-OH,-1.35,2.18
P-CNT-COOH,-1.37,2.06
SW-CNT-O,-2.70,1.96
SW-CNT-OH,-1.48,2.20
SW-CNT-COOH,-1.95,1.97
MV-CNT-O,-1.82,2.00
MV-CNT-OH,-1.04,2.14
MV-CNT-COOH,-2.15,1.97
CSVEOF
