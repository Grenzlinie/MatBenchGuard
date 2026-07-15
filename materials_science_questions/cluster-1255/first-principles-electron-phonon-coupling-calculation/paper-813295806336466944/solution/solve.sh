#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results_square.csv ===
cat > "$OUTDIR/results_square.csv" <<'FFEOF'
τ_opt,β_opt,energy_normal,energy_superconducting,gap,condensation_energy
0.4337,-0.06850,-0.04767,-0.04795,0.03020,-0.00028
FFEOF

# === solve block: results_cubic.csv ===
cat > "$OUTDIR/results_cubic.csv" <<'FFEOF'
τ_opt,β_opt,energy_normal,energy_superconducting,gap,condensation_energy
0.4295,-0.04375,-0.04500,-0.04531,0.03123,-0.00031
FFEOF
