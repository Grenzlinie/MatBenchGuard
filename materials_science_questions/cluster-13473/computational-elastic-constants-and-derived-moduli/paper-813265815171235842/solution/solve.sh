#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: elastic_constants.csv ===
cat > "$OUTDIR/elastic_constants.csv" <<'FFEOF'
material,c11,c12,c44,C_prime,B
Si,173.2,77.5,69.0,47.8,109.4
Ge,145.0,62.1,63.0,41.4,89.8
SiGe,158.7,69.7,65.5,44.5,99.4
FFEOF

# === solve block: sls_interplanar.csv ===
cat > "$OUTDIR/sls_interplanar.csv" <<'FFEOF'
R_SiSi,R_SiGe,R_GeGe,c_over_a,excess_energy
1.3628,1.3927,1.4730,1.0358,14.8
FFEOF

# === solve block: phonon_frequencies.csv ===
cat > "$OUTDIR/phonon_frequencies.csv" <<'FFEOF'
material,mode,frequency
Si,Gamma_optical,513.6
Si,X_TA,146.8
Si,L_TA,111.5
Ge,Gamma_optical,291.3
Ge,X_TA,81.9
Ge,L_TA,63.0
SiGe,Gamma_optical,411.7
FFEOF

# === solve block: ordering_energies.csv ===
cat > "$OUTDIR/ordering_energies.csv" <<'FFEOF'
structure,energy,c_over_a
RH1,16.9,1.037
random,15.5,1.035
FFEOF
