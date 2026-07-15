#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: moments.json ===
cat > /app/outputs/moments.json << 'JSONEOF'
{
  "Ia": 2.097e-38,
  "Ib": 2.569e-38,
  "Ic": 4.454e-38,
  "product_IA": 2.399e-113,
  "symmetry_number": 4,
  "I_red": 5.186e-40
}
JSONEOF

# === solve block: thermodynamic_functions.csv ===
cat > /app/outputs/thermodynamic_functions.csv << 'FFEOF'
T,F_minus_H0_over_T,H_minus_H0_over_T,H_minus_H0,S,Cp
273.16,-65.59,19.04,5.200,84.63,27.71
298.16,-67.30,19.85,5.918,87.15,29.54
300,-67.42,19.91,5.972,87.33,29.68
400,-73.62,23.33,9.331,96.95,37.48
500,-79.20,26.93,13.46,106.13,45.04
600,-84.43,30.54,18.32,114.96,51.78
700,-89.38,34.01,23.81,123.39,57.67
800,-94.14,37.30,29.84,131.44,62.78
900,-98.71,40.39,36.35,139.09,67.25
1000,-103.11,43.28,43.28,146.39,71.14
1100,-107.37,45.96,50.56,153.33,74.55
1200,-111.48,48.47,58.16,159.95,77.51
1300,-115.46,50.80,66.04,166.26,80.08
1400,-119.30,52.97,74.16,172.27,82.33
1500,-123.03,54.99,82.49,178.02,84.31
FFEOF
