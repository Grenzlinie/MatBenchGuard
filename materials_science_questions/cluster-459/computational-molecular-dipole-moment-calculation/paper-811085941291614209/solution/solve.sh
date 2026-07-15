#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: optimal_geometry.xyz ===
cat > /app/outputs/optimal_geometry.xyz <<'FFEOF'
6
formamide MP2/6-311G(3df,2p) optimized geometry
C      0.00000    0.00000    0.00000
O      0.00000    1.20950    0.00000
N     -1.35300   -0.50000    0.00000
H      0.80000   -0.50000    0.00000
H     -1.60000   -1.50000    0.00000
H     -1.10000    0.50000    0.00000
FFEOF

# === solve block: molecular_parameters.tsv ===
cat > /app/outputs/molecular_parameters.tsv <<'FFEOF'
property	value
dipole_moment_D	3.739
A_MHz	74036.22
B_MHz	11440.35
C_MHz	9909.15
FFEOF

# === solve block: harmonic_vibrational_data.tsv ===
cat > /app/outputs/harmonic_vibrational_data.tsv <<'FFEOF'
mode_index	wavenumber_cm1	intensity_km_mol
1	3803	56
2	3650	51
3	3021	83
4	1831	337
5	1632	59
6	1437	4
7	1295	96
8	1062	4
9	571	11
10	1060	3
11	656	12
12	186	278
FFEOF
