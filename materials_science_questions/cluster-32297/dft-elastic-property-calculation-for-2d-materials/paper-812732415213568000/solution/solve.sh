#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: phonon_stability.csv ===
cat > "$OUTDIR/phonon_stability.csv" <<'FFEOF'
system,layer_type,stable
C,bulk,true
C,1L,true
C,2L,true
Si,bulk,true
Si,1L,false
Si,2L,true
Ge,bulk,true
Ge,1L,true
Ge,2L,true
Sn,bulk,true
Sn,1L,true
Sn,2L,true
Pb,bulk,true
Pb,1L,true
Pb,2L,true
FFEOF

# === solve block: cleavage_energies.csv ===
cat > "$OUTDIR/cleavage_energies.csv" <<'FFEOF'
system,layer_type,cleavage_energy
C,1L,0.78
C,2L,0.75
Si,1L,1.36
Si,2L,0.88
Ge,1L,0.95
Ge,2L,0.72
Sn,1L,0.71
Sn,2L,0.52
Pb,1L,0.88
Pb,2L,0.82
FFEOF

# === solve block: band_gaps.csv ===
cat > "$OUTDIR/band_gaps.csv" <<'FFEOF'
system,layer_type,functional,band_gap,gap_type,classification
C,bulk,PBE,0.0,metallic,metallic
C,1L,PBE,0.0,metallic,metallic
C,2L,PBE,0.0,metallic,metallic
Si,bulk,PBE,0.0,metallic,metallic
Si,1L,PBE,0.0,metallic,metallic
Si,2L,PBE,0.20,indirect,semiconducting
Ge,bulk,PBE,0.0,metallic,metallic
Ge,1L,PBE,0.56,indirect,semiconducting
Ge,2L,PBE,0.35,indirect,semiconducting
Sn,bulk,PBE,0.0,metallic,metallic
Sn,1L,PBE,0.42,indirect,semiconducting
Sn,2L,PBE,0.30,indirect,semiconducting
Pb,bulk,PBE,0.0,metallic,metallic
Pb,1L,PBE,0.28,indirect,semiconducting
Pb,2L,PBE,0.038,indirect,semiconducting
C,bulk,HSE06,0.0,metallic,metallic
C,1L,HSE06,0.0,metallic,metallic
C,2L,HSE06,0.0,metallic,metallic
Si,bulk,HSE06,0.0,metallic,metallic
Si,1L,HSE06,0.0,metallic,metallic
Si,2L,HSE06,0.32,indirect,semiconducting
Ge,bulk,HSE06,0.0,metallic,metallic
Ge,1L,HSE06,0.90,indirect,semiconducting
Ge,2L,HSE06,0.58,indirect,semiconducting
Sn,bulk,HSE06,0.0,metallic,metallic
Sn,1L,HSE06,0.68,indirect,semiconducting
Sn,2L,HSE06,0.50,indirect,semiconducting
Pb,bulk,HSE06,0.0,metallic,metallic
Pb,1L,HSE06,0.45,indirect,semiconducting
Pb,2L,HSE06,0.05,indirect,semiconducting
FFEOF
