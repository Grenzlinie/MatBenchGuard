#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: energy_release_rates.csv ===
cat > "$OUTDIR/energy_release_rates.csv" <<'CSVEOF'
crack_length_nm,mode,method,normalized_G
2.009,I,global_energy,0.498
2.009,I,local_force,0.482
4.018,I,global_energy,1.029
4.018,I,local_force,0.992
6.53,I,global_energy,1.918
6.53,I,local_force,1.849
2.009,II,global_energy,1.139
2.009,II,local_force,1.12
4.018,II,global_energy,2.156
4.018,II,local_force,2.164
6.53,II,global_energy,3.649
6.53,II,local_force,3.747
CSVEOF
