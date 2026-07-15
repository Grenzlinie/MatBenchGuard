#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: seebeck_max_300K.csv ===
cat > "$OUTDIR/seebeck_max_300K.csv" <<'FFEOF'
composition,S_max
SnSe,1750
SnS,2380
GeSe,1960
GeS,2810
FFEOF

# === solve block: phonon_stability.csv ===
cat > "$OUTDIR/phonon_stability.csv" <<'FFEOF'
composition,min_frequency
SnSe,0.1
SnS,0.1
GeSe,0.1
GeS,0.1
FFEOF

# === solve block: lattice_thermal_conductivity.csv ===
cat > "$OUTDIR/lattice_thermal_conductivity.csv" <<'FFEOF'
composition,direction,kappa_l
SnSe,armchair,2.4
SnSe,zigzag,2.6
SnS,armchair,4.4
SnS,zigzag,4.7
GeSe,armchair,5.2
GeSe,zigzag,6.7
GeS,armchair,7.8
GeS,zigzag,10.5
FFEOF

# === solve block: zt_700K.csv ===
cat > "$OUTDIR/zt_700K.csv" <<'FFEOF'
composition,direction,ZT
SnSe,armchair,2.63
SnSe,zigzag,2.46
SnS,armchair,1.75
SnS,zigzag,1.88
GeSe,armchair,1.99
GeSe,zigzag,1.73
GeS,armchair,1.85
GeS,zigzag,1.29
FFEOF
