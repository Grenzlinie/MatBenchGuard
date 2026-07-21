#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: bulk_exchange_constants.json ===
python3 <<PYEOF
import json
data = {
    "J1": 0.37,
    "J2": -0.11,
    "J3": 0.18,
    "units": "mRy"
}
with open("$OUTDIR/bulk_exchange_constants.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: surface_moments_and_charges.json ===
python3 <<'PYEOF'
import json
import os

out_dir = os.environ.get("OUTDIR", "/app/outputs")
data = {
    "FM(100)": {
        "Layer1": {"Mn_moment": 4.17, "Pt_moment": 0.18},
        "Layer2": {"Pt_moment": 0.10},
        "Layer3": {"Mn_moment": 3.82, "Pt_moment": 0.11},
        "Layer4": {"Pt_moment": 0.12},
        "Layer5": {"Mn_moment": 3.82, "Pt_moment": 0.13}
    },
    "AFM(100)": {
        "Layer1": {"Mn_moment": -4.20, "Pt_moment": -0.11},
        "Layer2": {"Pt_moment": 0.02},
        "Layer3": {"Mn_moment": 3.80, "Pt_moment": 0.16},
        "Layer4": {"Pt_moment": 0.16},
        "Layer5": {"Mn_moment": 3.80, "Pt_moment": 0.16}
    },
    "FM(111)": {
        "Layer1": {"Mn_moment": 4.06, "Pt_moment": 0.12},
        "Layer2": {"Mn_moment": 3.87, "Pt_moment": 0.16},
        "Layer3": {"Mn_moment": 3.85, "Pt_moment": 0.16}
    },
    "AFM(111)": {
        "Layer1": {"Mn_moment": -4.02, "Pt_moment": -0.08},
        "Layer2": {"Mn_moment": -3.89, "Pt_moment": -0.04},
        "Layer3": {"Mn_moment": 3.80, "Pt_moment": 0.05}
    },
    "charge_transfer_FM(100)": {
        "Layer1": {"Mn_charge": -0.32, "Pt_charge": -0.35},
        "Layer2": {"Pt_charge": -0.02},
        "Layer3": {"Mn_charge": 0.12, "Pt_charge": -0.05},
        "Layer4": {"Pt_charge": -0.04},
        "Layer5": {"Mn_charge": 0.13, "Pt_charge": -0.04}
    },
    "charge_transfer_FM(111)": {
        "Layer1": {"Mn_charge": -0.21, "Pt_charge": -0.27},
        "Layer2": {"Mn_charge": 0.12, "Pt_charge": -0.03},
        "Layer3": {"Mn_charge": 0.12, "Pt_charge": -0.05}
    }
}
with open(out_dir + "/surface_moments_and_charges.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
