#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: defect_properties.json ===
python3 << 'PYEOF'
import json, os

data = {
    "stoichiometric": {
        "Fe_vacancy": {"Delta_V": -0.2, "effective_Omega": 0.5},
        "Al_vacancy": {"Delta_V": -0.7, "effective_Omega": 0.6},
        "Fe_antisite": {"Delta_V": -0.4, "effective_Omega": -0.2},
        "Al_antisite": {"Delta_V": 0.4, "effective_Omega": 0.2}
    },
    "off_stoichiometric": {
        "Fe_vacancy": {"Delta_V": -0.2, "effective_Omega": 0.55},
        "Al_vacancy": {"Delta_V": -0.7, "effective_Omega": 0.5},
        "Fe_antisite": {"Delta_V": -0.4, "effective_Omega": 0.0},
        "Al_antisite": {"Delta_V": 0.4, "effective_Omega": 0.05}
    }
}

outdir = os.environ.get("OUTDIR", "/app/outputs")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "defect_properties.json"), "w") as f:
    json.dump(data, f, indent=2)
PYEOF
