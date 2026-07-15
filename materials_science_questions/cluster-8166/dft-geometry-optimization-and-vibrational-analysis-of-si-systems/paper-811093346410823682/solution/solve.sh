#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_bond_lengths.csv ===
# Write bond lengths from Table 1 (MP2/6-311G(d) column)
cat > "$OUTDIR/step_01_bond_lengths.csv" <<'EOF'
bond,value_angstrom
SiC1,1.704
C1C2,1.285
C2C3,1.303
C3C4,1.294
EOF

# === solve block: step_02_harmonic_frequencies.csv ===
# Write harmonic frequencies and intensities from Table 2
cat > "$OUTDIR/step_02_harmonic_frequencies.csv" <<'EOF'
mode,frequency_cm1,intensity_kmol,symmetry
1,2227,1808,Σ
2,1837,0,Σ
3,1164,50,Σ
4,568,15,Σ
5,404,4,Π
6,236,12,Π
7,82,0,Π
EOF
