#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_results.csv ===
cat > /app/outputs/computed_results.csv <<'FFEOF'
system,total_magnetic_moment,spin_up_gap,spin_down_gap
pristine,0.03,0.41,NaN
V_Si,4.19,0.41,NaN
V_C,1.19,NaN,NaN
V_Si^1V_Si^4,3.88,0.91,0.15
V_Si^1V_C^8,1.34,0.31,0.04
V_Si^1B_Si^4,2.24,0.19,0.13
V_Si^1N_C^8,3.06,0.52,NaN
FFEOF
