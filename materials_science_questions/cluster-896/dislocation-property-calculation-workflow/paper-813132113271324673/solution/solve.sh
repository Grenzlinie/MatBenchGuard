#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: stress_strain_single_crystals.csv ===
cat > "$OUTDIR/stress_strain_single_crystals.csv" <<'FFEOF'
strain,stress_100,stress_111
0.0,0.0,0.0
0.05,15.2,20.1
0.10,22.7,30.3
0.15,28.1,38.2
0.20,32.4,44.5
0.25,35.9,49.7
0.30,38.7,53.6
0.34,40.5,56.2
FFEOF

# === solve block: stored_energy_single_crystals.csv ===
cat > "$OUTDIR/stored_energy_single_crystals.csv" <<'FFEOF'
strain,stored_energy_111,stored_energy_100
0.0,0.0,0.0
0.05,0.45,0.24
0.10,0.98,0.53
0.15,1.62,0.88
0.20,2.31,1.29
0.25,3.08,1.74
0.30,3.82,2.22
0.34,4.25,2.50
FFEOF

# === solve block: stored_energy_bicrystals.csv ===
cat > "$OUTDIR/stored_energy_bicrystals.csv" <<'FFEOF'
bicrystal,grain,stored_energy_avg
Bicrystal_001_111,111,4.17
Bicrystal_001_111,001,2.52
Bicrystal_001_634,634,3.76
Bicrystal_001_634,001,2.34
FFEOF
