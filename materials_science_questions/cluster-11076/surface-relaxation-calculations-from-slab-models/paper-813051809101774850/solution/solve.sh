#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: lattice_constants.csv ===
cat > "$OUTDIR/lattice_constants.csv" <<'FFEOF'
metal,structure,a,c_ratio
Li,bcc,3.44,
Na,bcc,4.19,
K,bcc,5.28,
Rb,bcc,5.67,
Cs,bcc,6.15,
Be,hcp,2.26,1.58
Mg,hcp,3.19,1.62
Ca,fcc,5.52,
Sr,fcc,6.02,
Ba,bcc,5.03,
Y,hcp,3.65,1.55
Zr,hcp,3.23,1.61
Nb,bcc,3.31,
Mo,bcc,3.17,
Tc,hcp,2.76,1.60
Ru,hcp,2.73,1.58
Rh,fcc,3.85,
Pd,fcc,3.96,
Ag,fcc,4.16,
Cd,hcp,3.05,1.87
FFEOF

# === solve block: surface_properties.csv ===
cat > "$OUTDIR/surface_properties.csv" <<'FFEOF'
metal,surface,gamma,tau
Li,bcc(110),0.49,-0.13
Na,bcc(110),0.21,0.12
K,bcc(110),0.11,-0.29
Rb,bcc(110),0.08,0.03
Cs,bcc(110),0.06,0.04
Be,hcp(0001),1.77,2.99
Mg,hcp(0001),0.55,0.88
Ca,fcc(111),0.41,-0.85
Sr,fcc(111),0.35,-0.48
Ba,bcc(110),0.31,0.03
Y,hcp(0001),1.00,1.00
Zr,hcp(0001),1.57,1.15
Nb,bcc(110),2.06,2.99
Mo,bcc(110),2.73,2.96
Tc,hcp(0001),2.21,2.59
Ru,hcp(0001),2.52,3.15
Rh,fcc(111),2.01,2.73
Pd,fcc(111),1.33,2.57
Ag,fcc(111),0.76,0.79
Cd,hcp(0001),0.21,1.07
FFEOF
