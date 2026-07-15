#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 << 'PYEOF'
import json, os

data = {
  "Model_I_alpha_1": {
    "malonate": {"mu_rms": 2.44, "d_ln_mu_dT": 0.2},
    "succinate": {"mu_rms": 2.39, "d_ln_mu_dT": 0.02, "delta_E": 0.23},
    "glutarate": {"mu_rms": 2.32, "d_ln_mu_dT": 0.1},
    "adipate": {"mu_rms": 2.45, "d_ln_mu_dT": 0.03},
    "sebacate": {"mu_rms": 2.47, "d_ln_mu_dT": 0.01}
  },
  "Model_II_Ebeta_1_2": {
    "malonate": {"mu_rms": 2.44, "d_ln_mu_dT": -0.1},
    "succinate": {"mu_rms": 2.20, "d_ln_mu_dT": 0.7, "delta_E": 0.21},
    "glutarate": {"mu_rms": 2.49, "d_ln_mu_dT": -0.2},
    "adipate": {"mu_rms": 2.48, "d_ln_mu_dT": 0.2},
    "sebacate": {"mu_rms": 2.49, "d_ln_mu_dT": 0.02}
  }
}

os.makedirs("/app/outputs", exist_ok=True)
with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
