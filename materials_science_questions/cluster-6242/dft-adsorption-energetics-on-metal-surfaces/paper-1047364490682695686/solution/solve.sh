#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: adsorption_energies.json ===
python3 -c '
import json
data = {"Ph-OH": 1.85, "Ph-COOH": -62.19, "Ph-CO-CH3": -25.39, "Ph-O-CH3": 1.9}
with open("/app/outputs/adsorption_energies.json", "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: mulliken_analysis.json ===
python3 -c '
import json
data = {
    "Ph-OH/FeS2": [{"interaction": "H-S", "population": 0.0, "length_Angstrom": 2.990}],
    "Ph-COOH/FeS2": [
        {"interaction": "H-S", "population": 0.05, "length_Angstrom": 2.475},
        {"interaction": "Fe-O", "population": 0.13, "length_Angstrom": 2.797}
    ],
    "Ph-CO-CH3/FeS2": [
        {"interaction": "Fe-O", "population": 0.13, "length_Angstrom": 2.820},
        {"interaction": "H-S", "population": 0.0, "length_Angstrom": 2.895}
    ],
    "Ph-O-CH3/FeS2": [
        {"interaction": "H-S", "population": -0.01, "length_Angstrom": 2.597},
        {"interaction": "H-S", "population": 0.0, "length_Angstrom": 2.595}
    ]
}
with open("/app/outputs/mulliken_analysis.json", "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: charge_transfer.json ===
python3 -c '
import json
data = {
    "Ph-OH/FeS2": [
        {"atom": "H", "charge_before": 0.54, "charge_after": 0.52},
        {"atom": "S", "charge_before": -0.11, "charge_after": -0.11}
    ],
    "Ph-COOH/FeS2": [
        {"atom": "H", "charge_before": 0.55, "charge_after": 0.48},
        {"atom": "S", "charge_before": -0.12, "charge_after": -0.01},
        {"atom": "Fe", "charge_before": 0.07, "charge_after": 0.10},
        {"atom": "O", "charge_before": -0.57, "charge_after": -0.54}
    ],
    "Ph-CO-CH3/FeS2": [
        {"atom": "H", "charge_before": 0.33, "charge_after": 0.27},
        {"atom": "S", "charge_before": -0.11, "charge_after": -0.09},
        {"atom": "Fe", "charge_before": 0.07, "charge_after": 0.10},
        {"atom": "O", "charge_before": -0.52, "charge_after": -0.49}
    ],
    "Ph-O-CH3/FeS2": [
        {"atom": "H", "charge_before": 0.31, "charge_after": 0.23},
        {"atom": "S", "charge_before": -0.11, "charge_after": -0.11}
    ]
}
with open("/app/outputs/charge_transfer.json", "w") as f:
    json.dump(data, f, indent=2)
'
