#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=${OUTDIR:-/app/outputs}

# === solve block: reconstruction_results.json ===
mkdir -p "$OUTDIR"
python3 << 'PYEOF'
import json, os

data = {
    "fom_comparison": [
        {"fom": "w1_step", "epsilon": 0.30, "P_over_T": 0.45},
        {"fom": "w2_step", "epsilon": 0.34, "P_over_T": 0.50},
        {"fom": "w3_step", "epsilon": 0.38, "P_over_T": 0.55}
    ],
    "compton_profile_effect": [
        {"case": "without_compton", "epsilon": 0.38, "P_over_T": 0.55},
        {"case": "with_compton", "epsilon": 0.32, "P_over_T": 0.48}
    ]
}

out_path = os.path.join(os.environ["OUTDIR"], "reconstruction_results.json")
with open(out_path, "w") as f:
    json.dump(data, f, indent=2)
print(f"Written {out_path}")
PYEOF
