#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: ag3n_equilibrium_properties.json ===
# Write the equilibrium properties JSON for the three Ag3N phases
# using the paper's reported values.
python3 -c '
import json

data = {
    "phases": [
        {
            "name": "D0_9",
            "a": 4.328,
            "V0": 20.27,
            "Ecoh": -2.513,
            "B0": 71.980,
            "B0_prime": 5.386,
            "band_gap": 0.134,
            "band_gap_type": "indirect"
        },
        {
            "name": "D0_2",
            "a": 8.662,
            "V0": 20.31,
            "Ecoh": -2.514,
            "B0": 72.230,
            "B0_prime": 5.335,
            "band_gap": 0.130,
            "band_gap_type": "indirect"
        },
        {
            "name": "RhF3",
            "a": 6.126,
            "V0": 20.31,
            "Ecoh": -2.514,
            "B0": 72.237,
            "B0_prime": 5.396,
            "band_gap": 0.129,
            "band_gap_type": "direct"
        }
    ]
}

with open("/app/outputs/ag3n_equilibrium_properties.json", "w") as f:
    json.dump(data, f, indent=2)
'
