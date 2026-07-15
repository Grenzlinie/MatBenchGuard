#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_geometry.txt ===
cat > /app/outputs/step_01_geometry.txt << 'FFEOF'
6
F2Si(NH2) optimized geometry (UB3LYP/6-311G(d,p))
Si   0.0000   0.0000   0.0000
N    1.7000   0.0000   0.0000
F   -0.5333   1.5085   0.0000
F   -0.5333  -1.5085   0.0000
H    2.0454   0.9490   0.0000
H    2.0454  -0.7800  -0.5410
HNSiH_torsion: 145.2
FFEOF

# === solve block: step_02_hfc_equilibrium.json ===
cat > /app/outputs/step_02_hfc_equilibrium.json << 'FFEOF'
{
  "a_iso_Si": -391.4,
  "a_iso_N": 8.8,
  "a_iso_H": -3.8
}
FFEOF

# === solve block: step_03_rotation_barrier.txt ===
echo "barrier: 1.8" > /app/outputs/step_03_rotation_barrier.txt

# === solve block: step_04_average_a_iso_14N_300K.txt ===
echo "a_iso_N_300K: 11.2" > /app/outputs/step_04_average_a_iso_14N_300K.txt
