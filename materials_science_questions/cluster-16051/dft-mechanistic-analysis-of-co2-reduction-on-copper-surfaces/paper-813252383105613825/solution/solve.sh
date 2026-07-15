#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_barriers.json ===
cat > "$OUTDIR/step_01_barriers.json" <<'FFEOF'
{
  "CH3O_to_CH3OH": 0.15,
  "CH3O_to_CH4": 1.21,
  "CO_to_CHO": 0.39,
  "CO_to_COH": 0.21,
  "CH2_dimer_ethylene": 0.21
}
FFEOF

# === solve block: step_02_selectivity.json ===
python3 -c "
import json, math
kb = 8.617333262145e-5
T = 300.0
kT = kb * T
diff_pathI = 1.21 - 0.15
sel_pathI = math.exp(diff_pathI / kT)
diff_CO = 0.39 - 0.21
sel_CO = math.exp(diff_CO / kT)
data = {
    'selectivity_ratio_pathI': sel_pathI,
    'barrier_difference_pathI': diff_pathI,
    'selectivity_pathII_over_I': sel_CO,
    'barrier_difference_CO_reduction': diff_CO
}
with open('/app/outputs/step_02_selectivity.json', 'w') as f:
    json.dump(data, f, indent=2)
"
