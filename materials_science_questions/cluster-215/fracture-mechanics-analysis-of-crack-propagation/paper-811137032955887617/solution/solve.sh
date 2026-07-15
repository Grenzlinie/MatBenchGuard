#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: effective_moduli.json ===
python3 - <<'PY'
import json
data = {
  "base_case": {
    "fracture_nu": 0.0,
    "E11": 6.25e9,
    "E22": 100.0e9,
    "E33": 100.0e9,
    "G12": 3.067e9,
    "G13": 3.067e9,
    "G23": 38.46153846e9
  },
  "nonzero_nu_case": {
    "fracture_nu": 0.3,
    "E11": 8.125e9,
    "E22": 100.0e9,
    "E33": 100.0e9,
    "G12": 2.404e9,
    "G13": 2.404e9,
    "G23": 38.46153846e9
  },
  "percent_change_E11": 30.0
}
with open("/app/outputs/effective_moduli.json", "w") as f:
    json.dump(data, f, indent=2)
PY
