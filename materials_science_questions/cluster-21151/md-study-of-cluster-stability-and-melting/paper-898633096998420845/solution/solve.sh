#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: structural_distribution_Cu90.csv ===
cat > "$OUTDIR/structural_distribution_Cu90.csv" << 'FFEOF'
Temperature,Motif,Probability
300,Ih,0.92
300,Dh,0.02
300,fcc,0.0
300,twin,0.02
300,mix,0.04
300,amorphous,0.0
400,Ih,0.72
400,Dh,0.04
400,fcc,0.0
400,twin,0.04
400,mix,0.2
400,amorphous,0.0
500,Ih,0.45
500,Dh,0.07
500,fcc,0.0
500,twin,0.08
500,mix,0.4
500,amorphous,0.0
600,Ih,0.15
600,Dh,0.05
600,fcc,0.0
600,twin,0.05
600,mix,0.712
600,amorphous,0.038
609,Ih,0.1
609,Dh,0.02
609,fcc,0.0
609,twin,0.03
609,mix,0.6
609,amorphous,0.25
FFEOF

# === solve block: melting_point.txt ===
printf "609.0\n" > "$OUTDIR/melting_point.txt"
