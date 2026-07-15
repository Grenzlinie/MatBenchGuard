#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: saddle_plane_probabilities.csv ===
cat > /app/outputs/saddle_plane_probabilities.csv <<'FFEOF'
T,P0
995,9.6e-9
1368,1.6e-6
1520,7.8e-6
1760,2.3e-5
FFEOF

# === solve block: transmission_coefficients.csv ===
cat > /app/outputs/transmission_coefficients.csv <<'FFEOF'
T,S
995,0.37
1368,0.32
1520,0.54
1760,0.33
FFEOF

# === solve block: migration_results.csv ===
cat > /app/outputs/migration_results.csv <<'FFEOF'
T,P_0_Angstrom_inv,transmission_coeff,Gamma_per_s,nu_bar_1e12_per_s
995,9.6e-9,0.37,1.8e4,5.2
1368,1.6e-6,0.32,3.0e6,4.2
1520,7.8e-6,0.54,2.6e7,8.8
1760,2.3e-5,0.33,5.0e7,3.0
FFEOF
