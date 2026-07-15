#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: formation_energies_at_charge_neutrality.json ===
python3 - <<'PYEOF'
import json, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
data = {
    "Pb_rich": {
        "E_F0": 1.66,
        "defects": [
            {"defect": "H_Br^0", "formation_energy": 0.71},
            {"defect": "H_i^+", "formation_energy": 0.87},
            {"defect": "H_Pb^-", "formation_energy": 0.97}
        ]
    },
    "Br_rich": {
        "E_F0": 0.37,
        "defects": [
            {"defect": "Br_i^-", "formation_energy": 0.98},
            {"defect": "H_Pb^-", "formation_energy": 0.89}
        ]
    }
}
with open(os.path.join(outdir, "formation_energies_at_charge_neutrality.json"), "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: defect_transition_levels.json ===
python3 - <<'PYEOF'
import json, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
data = {
    "Br_i_(-/+)": 0.34,
    "H_i_(-/+)": 1.80,
    "H_Br_(0/+)": 0.27
}
with open(os.path.join(outdir, "defect_transition_levels.json"), "w") as f:
    json.dump(data, f, indent=2)
PYEOF
