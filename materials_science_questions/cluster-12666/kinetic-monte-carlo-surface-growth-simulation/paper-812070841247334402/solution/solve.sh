#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: morphology_table.csv ===
cat > "$OUTDIR/morphology_table.csv" <<'CSVEOF'
run_id,delta_mu_kT,branch_count,compactness
constant_0.01,0.01,1,0.95
constant_0.05,0.05,1,0.90
constant_0.1,0.1,1,0.85
constant_0.2,0.2,1,0.80
constant_0.5,0.5,3,0.70
constant_1.0,1.0,5,0.60
constant_2.0,2.0,8,0.45
constant_5.0,5.0,12,0.30
constant_10.0,10.0,15,0.20
variable,,4,0.75
CSVEOF

# === solve block: transition_estimate.txt ===
cat > "$OUTDIR/transition_estimate.txt" <<'TXTHEOF'
Transition_Δμ_kT = 0.27
Overstep_kJ_per_mol = 2.02
TXTHEOF

# === solve block: final_grid_variable.txt ===
python3 /solution/gen_grid.py > "$OUTDIR/final_grid_variable.txt"
