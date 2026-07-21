#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: binding_energies.csv ===
cat > /app/outputs/binding_energies.csv <<'FFEOF'
complex,medium,Eb_kcal_per_mol
C20+1-ap (C=O),gas,-1.77
C20+1-ap (NH),gas,-19.42
BC19+1-ap (C=O),gas,-36.02
BC19+1-ap (NH),gas,-45.39
SiC19+1-ap (C=O),gas,-53.65
SiC19+1-ap (NH),gas,-54.42
C20+1-ap (C=O),water,-10.49
C20+1-ap (NH),water,-28.09
BC19+1-ap (C=O),water,-41.65
BC19+1-ap (NH),water,-50.58
SiC19+1-ap (C=O),water,-64.13
SiC19+1-ap (NH),water,-63.42
FFEOF

# === solve block: electronic_properties.csv ===
cat > /app/outputs/electronic_properties.csv <<'FFEOF'
complex,medium,EHOMO_eV,ELUMO_eV,Egap_eV,eta_eV,omega_eV
C20+1-ap (C=O),gas,-4.838,-0.875,3.953,1.977,2.057
C20+1-ap (NH),gas,-5.261,-1.384,3.877,1.939,2.847
BC19+1-ap (C=O),gas,-4.780,-0.971,3.809,1.905,2.171
BC19+1-ap (NH),gas,-5.266,-1.484,3.782,1.891,3.012
SiC19+1-ap (C=O),gas,-4.719,-0.990,3.729,1.865,2.185
SiC19+1-ap (NH),gas,-5.240,-1.469,3.775,1.888,2.984
C20+1-ap (C=O),water,-5.366,-1.327,4.039,2.020,2.773
C20+1-ap (NH),water,-5.454,-1.479,3.975,1.989,3.023
BC19+1-ap (C=O),water,-5.305,-1.512,3.793,1.897,3.063
BC19+1-ap (NH),water,-5.410,-1.620,3.790,1.895,3.260
SiC19+1-ap (C=O),water,-5.356,-1.497,3.859,1.930,3.042
SiC19+1-ap (NH),water,-5.493,-1.660,3.833,1.917,3.337
FFEOF
