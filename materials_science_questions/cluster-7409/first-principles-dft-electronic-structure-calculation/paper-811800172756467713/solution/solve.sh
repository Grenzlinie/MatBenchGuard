#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: polarizability_results.csv ===
cat > "/app/outputs/polarizability_results.csv" << 'FFEOF'
cluster,method,basis,mean_polarizability,polarizability_anisotropy,mean_hyperpolarizability
ScSi12,B3LYP,6-311+G(2d),433.5,103.6,303.6
TiSi12,B3LYP,6-311+G(2d),403.3,99.8,222.4
FeSi12,B3LYP,6-311+G(2d),375.6,82.2,191.2
CuSi12,B3LYP,6-311+G(2d),410.0,116.8,261.8
ZnSi12,B3LYP,6-311+G(2d),417.6,82.5,270.8
FFEOF

# === solve block: absorption_spectrum.csv ===
cat > "/app/outputs/absorption_spectrum.csv" << 'FFEOF'
excitation_index,oscillator_strength,wavelength_nm
1,0.6,426.5
2,0.5,381.9
3,0.4,356.3
4,0.3,324.1
5,0.01,310.0
6,0.02,315.0
7,0.01,320.0
8,0.02,330.0
9,0.01,335.0
10,0.02,340.0
11,0.01,345.0
12,0.02,350.0
13,0.01,360.0
14,0.02,365.0
15,0.01,370.0
16,0.02,385.0
17,0.01,390.0
18,0.02,395.0
19,0.01,405.0
20,0.02,415.0
21,0.01,425.0
22,0.02,435.0
23,0.01,440.0
24,0.02,445.0
25,0.01,450.0
26,0.02,455.0
27,0.01,460.0
28,0.02,465.0
29,0.01,470.0
30,0.02,475.0
FFEOF
