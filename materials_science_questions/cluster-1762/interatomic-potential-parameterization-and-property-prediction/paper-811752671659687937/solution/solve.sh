#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: sputtering_yields.csv ===
cat > "$OUTDIR/sputtering_yields.csv" <<'FFEOF'
surface,energy_eV,species,yield,num_impacts
clean,100,Ga,0.0,30
clean,150,Ga,0.0,30
clean,250,Ga,0.0,30
clean,100,N,0.07,30
clean,150,N,0.15,30
clean,250,N,0.30,30
Cl,100,Ga,0.15,30
Cl,150,Ga,0.35,30
Cl,250,Ga,0.60,30
Cl,100,N,0.08,30
Cl,150,N,0.16,30
Cl,250,N,0.32,30
FFEOF
