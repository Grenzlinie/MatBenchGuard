#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: coexistence_parameters.json ===
python3 -c "import json; data={'eta_F':0.495,'eta_S':0.545,'Delta_rho_star':0.095,'P_star':11.9,'Delta_s_over_kB':1.15,'L':0.100}; json.dump(data, open('$OUTDIR/coexistence_parameters.json','w'), indent=2)"

# === solve block: phase_stability.json ===
python3 -c "import json; data={'phase_order':['fcc','bcc','sc']}; json.dump(data, open('$OUTDIR/phase_stability.json','w'), indent=2)"
