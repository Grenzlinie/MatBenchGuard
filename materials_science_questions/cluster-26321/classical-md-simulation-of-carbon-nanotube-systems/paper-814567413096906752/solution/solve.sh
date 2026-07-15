#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_02_water_energy.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from generate import write_water_energy; write_water_energy('$OUTDIR/step_02_water_energy.csv')"

# === solve block: step_03_U_NP_volume.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from generate import write_U_NP_volume; write_U_NP_volume('$OUTDIR/step_03_U_NP_volume.csv')"

# === solve block: step_01_zcoord.dat ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from generate import write_np_trajectory; write_np_trajectory('$OUTDIR/step_01_zcoord.dat')"
