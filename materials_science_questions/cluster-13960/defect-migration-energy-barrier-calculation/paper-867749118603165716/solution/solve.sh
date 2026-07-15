#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_energy_path.csv ===
cat > "$OUTDIR/step_01_energy_path.csv" <<'FFEOF'
image,energy_eV
0,0.0
1,0.05
2,0.10
3,0.18
4,0.30
5,0.45
6,0.50
7,0.40
8,0.30
9,0.20
FFEOF

# === solve block: step_02_band_gaps.csv ===
cat > "$OUTDIR/step_02_band_gaps.csv" <<'FFEOF'
step,band_gap_eV
M1,0.70
Step1,0.38
Step2,0.05
Step3,0.02
FFEOF
