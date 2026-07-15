#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: adsorption_results.json ===
python3 -c '
import json
data = {
    "C": {
        "T": {"E_ad": -0.908, "delta_h": 0.18, "d_ac": 1.72, "M": 2.0},
        "B": {"E_ad": -1.535, "delta_h": 0.46, "d_ac": 1.53, "M": 0.44},
        "H": {"E_ad": -0.158, "delta_h": 0.01, "d_ac": 3.15, "M": 2.15}
    },
    "Si": {
        "T": {"E_ad": -0.472, "delta_h": 0.12, "d_ac": 2.22, "M": 1.75},
        "B": {"E_ad": -0.554, "delta_h": 0.20, "d_ac": 2.21, "M": 1.59},
        "H": {"E_ad": -0.135, "delta_h": 0.01, "d_ac": 3.28, "M": 2.00}
    },
    "Ge": {
        "T": {"E_ad": -0.353, "delta_h": 0.12, "d_ac": 2.41, "M": 1.77},
        "B": {"E_ad": -0.378, "delta_h": 0.16, "d_ac": 2.44, "M": 1.76},
        "H": {"E_ad": -0.093, "delta_h": 0.01, "d_ac": 3.28, "M": 1.99}
    },
    "Sn": {
        "T": {"E_ad": -0.248, "delta_h": 0.10, "d_ac": 2.70, "M": 1.75},
        "B": {"E_ad": -0.249, "delta_h": 0.12, "d_ac": 2.76, "M": 1.76},
        "H": {"E_ad": -0.088, "delta_h": 0.01, "d_ac": 3.37, "M": 1.83}
    },
    "Pb": {
        "T": {"E_ad": -0.216, "delta_h": 0.08, "d_ac": 2.82, "M": 1.75},
        "B": {"E_ad": -0.214, "delta_h": 0.10, "d_ac": 2.90, "M": 1.76},
        "H": {"E_ad": -0.090, "delta_h": 0.02, "d_ac": 3.41, "M": 1.76}
    }
}
with open("/app/outputs/adsorption_results.json", "w") as f:
    json.dump(data, f, indent=2)
'
