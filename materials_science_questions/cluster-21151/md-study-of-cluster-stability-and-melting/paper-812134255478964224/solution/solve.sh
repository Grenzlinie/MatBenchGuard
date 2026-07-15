#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_linear_fit_and_LDM.json ===
python3 -c '
import json
data = {
  "potential_s": {
    "n55": {"A": 67.0, "B": -3.79, "epsilon_C": 68.1},
    "n135": {"A": 128.0, "B": -4.56, "epsilon_C": 128.3},
    "a_c": 4.8,
    "a_v": -80.0,
    "a_s": 132.0,
    "a_v0": -6.9,
    "a_s0": 11.5
  },
  "potential_l": {
    "n55": {"A": 119.0, "B": -11.3, "epsilon_C": 128.0},
    "n135": {"A": 278.0, "B": -21.5, "epsilon_C": 279.1},
    "a_c": 10.8,
    "a_v": -600.0,
    "a_s": 1900.0,
    "a_v0": -50.0,
    "a_s0": 148.0
  }
}
with open("/app/outputs/step_01_linear_fit_and_LDM.json", "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: step_02_fragmentation_data.json ===
python3 -c '
import json
data = {
  "fission": {
    "n_k": [[26, 1], [23, 1], [3, 1], [1, 3]],
    "total_KE": 1472.0,
    "total_IN": 1043.0,
    "n_epsilon": 2530.0
  },
  "coulomb_explosion": {
    "n_k": [[1, 31], [2, 7], [3, 2], [4, 1]],
    "total_KE": 2620.0,
    "total_IN": 140.0,
    "n_epsilon": 2778.0
  }
}
with open("/app/outputs/step_02_fragmentation_data.json", "w") as f:
    json.dump(data, f, indent=2)
'
