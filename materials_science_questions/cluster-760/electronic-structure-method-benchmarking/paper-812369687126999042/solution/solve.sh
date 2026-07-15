#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: direct_exchange_energies.csv ===
cat > "$OUTDIR/direct_exchange_energies.csv" <<'FFEOF'
dimer,method,direct_exchange_energy_eV
Sc2,HF,-1.381
Sc2,SVWN,-0.961
Sc2,MPW1PW91,-1.086
Sc2,B3PW91,-0.643
Ti2,HF,0.478
Ti2,SVWN,0.415
Ti2,MPW1PW91,0.443
Ti2,B3PW91,-5.251
V2,HF,-13.04
V2,SVWN,-1.992
V2,MPW1PW91,-8.258
V2,B3PW91,-1.150
Cr2,HF,22.97
Cr2,SVWN,7.727
Cr2,MPW1PW91,12.40
Cr2,B3PW91,8.770
Mn2,HF,22.51
Mn2,SVWN,10.04
Mn2,MPW1PW91,13.36
Mn2,B3PW91,10.96
Fe2,HF,-0.645
Fe2,SVWN,3.292
Fe2,MPW1PW91,2.829
Fe2,B3PW91,3.330
Co2,HF,2.535
Co2,SVWN,1.850
Co2,MPW1PW91,0.899
Co2,B3PW91,0.840
Ni2,HF,3.230
Ni2,SVWN,1.799
Ni2,MPW1PW91,2.763
Ni2,B3PW91,2.590
Cu2,HF,-0.301
Cu2,SVWN,-1.679
Cu2,MPW1PW91,-1.366
Cu2,B3PW91,-1.401
Zn2,HF,-2.839
Zn2,SVWN,-3.541
Zn2,MPW1PW91,-3.311
Zn2,B3PW91,-3.385
FFEOF
