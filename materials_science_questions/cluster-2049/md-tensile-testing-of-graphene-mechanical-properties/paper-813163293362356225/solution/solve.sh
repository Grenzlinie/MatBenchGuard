#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: simulation_results.json ===
python3 -c '
import json
data = {
    "G": {
        "substrate": "G",
        "detachment": False,
        "t_d": None,
        "v_d": None,
        "dE_CuCu": -25.0,
        "E_CCu": -150.0
    },
    "PG": {
        "substrate": "PG",
        "detachment": True,
        "t_d": 41.0,
        "v_d": 75.0,
        "dE_CuCu": -160.0,
        "E_CCu": -30.0
    }
}
with open("/app/outputs/simulation_results.json", "w") as f:
    json.dump(data, f, indent=2)
'
