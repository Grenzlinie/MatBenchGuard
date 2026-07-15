#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: nucleation_constants.json ===
python3 -c "import json, math; d={'alpha_3':1.952,'beta_3':math.sqrt(3)/4,'alpha_5':2.52,'beta_5':0.93}; json.dump(d, open('/app/outputs/nucleation_constants.json','w'))"

# === solve block: barrier_prefactors.json ===
python3 -c "import json; d={'G3_over_h_DeltaMu':2.21,'G5_over_h_DeltaMu':1.74}; json.dump(d, open('/app/outputs/barrier_prefactors.json','w'))"
