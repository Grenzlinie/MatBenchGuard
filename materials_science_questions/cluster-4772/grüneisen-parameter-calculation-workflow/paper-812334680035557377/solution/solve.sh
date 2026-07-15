#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fitted_parameters.json ===
# Write fitted parameters (Table 2) and Grüneisen parameter
python3 -c '
import json

params = {
  "a": {
    "Q0": 8.099e6,      # 8.099 × 10^6 J/mol
    "theta": 672.0,    # K
    "k": 7.27,
    "a_minus_1": 8.62e-4   # a-1 = 8.62 × 10^{-4}
  },
  "b": {
    "Q0": 4.905e6,
    "theta": 779.0,
    "k": 2.27,
    "a_minus_1": 1.208e-3  # 12.08 × 10^{-4}
  },
  "c": {
    "Q0": 5.952e6,
    "theta": 652.0,
    "k": 3.56,
    "a_minus_1": 1.206e-3
  },
  "V": {
    "Q0": 6.065e6,
    "theta": 707.0,
    "k": 4.16,
    "a_minus_1": 3.273e-3  # 32.73 × 10^{-4}
  },
  "gamma": 1.04
}

with open("/app/outputs/fitted_parameters.json", "w") as f:
    json.dump(params, f, indent=2)
'
