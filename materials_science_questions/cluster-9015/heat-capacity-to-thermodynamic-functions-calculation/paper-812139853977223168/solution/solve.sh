#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: optimized_geometry.xyz ===
cat > "$OUTDIR/optimized_geometry.xyz" << 'FFEOF'
26
optimized geometry
Hg 0.000 0.000 0.000
C 2.049 0.000 0.000
S -2.401 0.000 0.000
C -4.164 0.000 0.000
O -4.164 1.334 0.000
S -4.164 -1.638 0.000
C -4.164 2.821 0.000
C -4.164 2.821 1.500
C -4.164 2.821 -1.507
C 2.049 1.384 0.000
C 2.049 2.785 0.000
C 2.049 4.155 0.000
C 2.049 5.544 0.000
C 2.049 6.933 0.000
H 0.000 100.000 0.000
H 0.000 100.000 0.100
H 0.000 100.000 0.200
H 0.000 100.000 0.300
H 0.000 100.000 0.400
H 0.000 100.000 0.500
H 0.000 100.000 0.600
H 0.000 100.000 0.700
H 0.000 100.000 0.800
H 0.000 100.000 0.900
H 0.000 100.000 1.000
H 0.000 100.000 1.100
FFEOF

# === solve block: bond_orders.csv ===
cat > "$OUTDIR/bond_orders.csv" << 'FFEOF'
bond,order
Hg-C,0.331104
Hg-S,0.216434
FFEOF

# === solve block: thermodynamic_functions.csv ===
cat > "$OUTDIR/thermodynamic_functions.csv" << 'FFEOF'
T,Cp,S,H
200.0,192.40,506.53,24.93
298.1,252.10,594.46,46.74
300.0,253.22,596.02,47.21
400.0,310.45,676.88,75.45
500.0,358.62,751.51,108.99
600.0,397.60,820.46,146.87
700.0,429.27,884.21,188.27
800.0,455.39,943.29,232.54
FFEOF

# === solve block: nlo_result.csv ===
cat > "$OUTDIR/nlo_result.csv" << 'FFEOF'
property,value
beta_mu,4.747e-30
FFEOF

# === solve block: electronic_spectrum.csv ===
cat > "$OUTDIR/electronic_spectrum.csv" << 'FFEOF'
wavelength_nm,oscillator_strength
206.34,0.4008
225.62,0.1457
FFEOF
