#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_bond_geometry.csv ===
cat > /app/outputs/step_01_bond_geometry.csv <<'FFEOF'
type,label,value
bond,Co1-O1,1.8955
bond,Co1-O2,1.8824
bond,Co1-O3,1.8818
bond,Co1-O4,1.8818
bond,Co2-O2,1.92581
bond,Co2-O5,1.92581
bond,Co2-O6,1.92581
bond,Co2-O7,1.96010
angle,O1-Co1-O2,109.3700
angle,O1-Co1-O3,109.3755
angle,O1-Co1-O4,109.3755
angle,O2-Co1-O3,109.5612
angle,O2-Co1-O4,109.5612
angle,O3-Co1-O4,109.5833
angle,O2-Co2-O5,113.9086
angle,O2-Co2-O6,113.9086
angle,O2-Co2-O7,108.3735
angle,O5-Co2-O6,104.8207
angle,O5-Co2-O7,107.7532
angle,O6-Co2-O7,107.7533
FFEOF

# === solve block: step_02_cdft_magnetic_moments.csv ===
cat > /app/outputs/step_02_cdft_magnetic_moments.csv <<'FFEOF'
site,mu_B
Co1,-3.3055
Co2,1.9974
FFEOF
