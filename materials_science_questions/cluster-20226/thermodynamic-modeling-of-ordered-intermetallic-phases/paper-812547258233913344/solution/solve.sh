#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_02_v_sublattice_occupation.csv ===
cat > "$OUTDIR/step_02_v_sublattice_occupation.csv" <<'EOF'
sublattice_number,occupancy_V
1,0.95
2,0.0167
3,0.0167
4,0.0167
EOF

# === solve block: step_03_sro_parameters.csv ===
python3 /solution/generate_outputs.py step_03_sro_parameters.csv

# === solve block: step_04_specific_heat.csv ===
python3 /solution/generate_outputs.py step_04_specific_heat.csv

# === solve block: step_06_relaxation_and_msad.csv ===
python3 /solution/generate_outputs.py step_06_relaxation_and_msad.csv
