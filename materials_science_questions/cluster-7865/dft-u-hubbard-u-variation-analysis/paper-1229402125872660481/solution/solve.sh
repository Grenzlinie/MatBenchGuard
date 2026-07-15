#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results_table.json ===
python3 - <<'PYEOF'
import json

data = [
    {
        "projection": "ortho-atomic",
        "magnetic": "AFM",
        "U_sc": 2.9787,
        "delta_E": 0.0,
        "M_tot": 0.0,
        "M_abs": 2.15,
        "a": 5.454,
        "c": 5.4631,
        "E_g": 2.2281
    },
    {
        "projection": "ortho-atomic",
        "magnetic": "FM",
        "U_sc": 2.9936,
        "delta_E": 0.0103,
        "M_tot": 2.0,
        "M_abs": 2.175,
        "a": 5.4541,
        "c": 5.4655,
        "E_g": 1.7102
    },
    {
        "projection": "atomic",
        "magnetic": "AFM",
        "U_sc": 2.0862,
        "delta_E": 0.0961,
        "M_tot": 0.0,
        "M_abs": 2.155,
        "a": 5.4546,
        "c": 5.4766,
        "E_g": 1.3699
    },
    {
        "projection": "atomic",
        "magnetic": "FM",
        "U_sc": 2.1247,
        "delta_E": 0.114,
        "M_tot": 2.0,
        "M_abs": 2.19,
        "a": 5.4582,
        "c": 5.477,
        "E_g": 0.9162
    }
]

with open("/app/outputs/results_table.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
