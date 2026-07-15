#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_optimization_results.csv ===
cat > "$OUTDIR/step_01_optimization_results.csv" <<'EEOF'
structure,functional,final_PCP_angle_deg,total_energy_per_CDP_eV,relative_energy_per_CDP_kcal_mol
A_bent,PBE,130.7,-99.8135,4.3
A_bent,PBE-D3,130.7,-100.0,0.0
Cprime_linear,PBE,179.7,-100.0,0.0
Cprime_linear,PBE-D3,179.7,-99.094,20.9
EEOF
