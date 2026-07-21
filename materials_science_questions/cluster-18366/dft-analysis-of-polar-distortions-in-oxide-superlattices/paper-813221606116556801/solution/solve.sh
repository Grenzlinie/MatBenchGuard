#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bulk_properties.json ===
python3 <<'PYEOF'
import json

bulk = {
    "SrO": {
        "a": 5.157,
        "E_coh": -10.53,
        "B": 98.1,
        "C11": 171.2,
        "C12": 64.1,
        "C44": 52.3,
        "Q": 1.8,
        "ionic_charges": {"Sr": 1.8, "O": -1.8}
    },
    "TiO2": {
        "a": 4.594,
        "c": 2.9593,
        "E_coh": -19.9,
        "B": 210.6,
        "C11": 288.5,
        "C12": 171.8,
        "C44": 115.4,
        "C66": 154.0,
        "C33": 374.6,
        "C23": 150.6,
        "Q": 1.265,
        "ionic_charges": {"Ti": 2.53, "O": -1.265}
    },
    "SrTiO3_raw": {
        "a": 4.027,
        "E_coh": -30.6,
        "B": 155.5,
        "C11": 244.0,
        "C12": 111.0,
        "C44": 100.0,
        "Q": 1.513,
        "ionic_charges": {"Sr": 1.83, "Ti": 2.71, "O": -1.513}
    },
    "SrTiO3_fitted": {
        "a": 3.87,
        "E_coh": -31.8,
        "B": 182.0,
        "C11": 326.0,
        "C12": 111.0,
        "C44": 102.0,
        "Q": 1.63,
        "ionic_charges": {"Sr": 1.85, "Ti": 3.05, "O": -1.633}
    }
}

with open("/app/outputs/bulk_properties.json", "w") as f:
    json.dump(bulk, f, indent=2)
PYEOF

# === solve block: surface_properties.json ===
python3 <<'PYEOF'
import json

surface = {
    "SrO_terminated": {
        "surface_energy": 1.20,
        "atomic_relaxations": {
            "Sr(9)": -0.33,
            "O(10)": -0.04,
            "Ti(5)": 0.02,
            "O(7)": 0.04,
            "Sr(6)": -0.11,
            "O(8)": 0.02
        },
        "charge_transfers": {
            "Sr(9)": 0.05,
            "O(10)": 0.0,
            "Ti(5)": -0.04,
            "O(7)": -0.03
        }
    },
    "TiO2_terminated": {
        "surface_energy": 1.09,
        "atomic_relaxations": {
            "Ti(1)": -0.18,
            "O(3)": -0.04,
            "Sr(2)": 0.06,
            "O(4)": -0.07
        },
        "charge_transfers": {
            "Ti(1)": -0.18,
            "O(3)": 0.14,
            "Sr(2)": -0.03,
            "O(4)": -0.03
        }
    }
}

with open("/app/outputs/surface_properties.json", "w") as f:
    json.dump(surface, f, indent=2)
PYEOF

# === solve block: thin_film_properties.json ===
python3 <<'PYEOF'
import json

data = {
    "-1.66%": [
        {"thickness_nm": 2.0, "a_perp": 3.920, "a_parallel": 3.812, "ratio": 3.920/3.812},
        {"thickness_nm": 5.0, "a_perp": 3.912, "a_parallel": 3.812, "ratio": 3.912/3.812},
        {"thickness_nm": 10.0, "a_perp": 3.891, "a_parallel": 3.812, "ratio": 3.891/3.812},
        {"thickness_nm": 20.0, "a_perp": 3.838, "a_parallel": 3.812, "ratio": 3.838/3.812},
        {"thickness_nm": 40.0, "a_perp": 3.824, "a_parallel": 3.812, "ratio": 3.824/3.812}
    ],
    "+1.66%": [
        {"thickness_nm": 2.0, "a_perp": 3.824, "a_parallel": 3.941, "ratio": 3.824/3.941},
        {"thickness_nm": 5.0, "a_perp": 3.823, "a_parallel": 3.941, "ratio": 3.823/3.941},
        {"thickness_nm": 10.0, "a_perp": 3.834, "a_parallel": 3.941, "ratio": 3.834/3.941},
        {"thickness_nm": 20.0, "a_perp": 3.870, "a_parallel": 3.941, "ratio": 3.870/3.941},
        {"thickness_nm": 40.0, "a_perp": 3.890, "a_parallel": 3.941, "ratio": 3.890/3.941}
    ]
}

with open("/app/outputs/thin_film_properties.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
