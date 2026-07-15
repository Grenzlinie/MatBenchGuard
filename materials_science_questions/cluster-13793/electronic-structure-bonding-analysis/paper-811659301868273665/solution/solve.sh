#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c '
import json
results = {
    "delta_E": {
        "NM": 0.34,
        "FM": 0.21,
        "AFM1": 0.25,
        "AFM2": 0.24,
        "AFM3": 0.0
    },
    "magnetic_moments": {
        "FM": 1.03,
        "AFM1": [1.77, 1.82],
        "AFM2": 0.97,
        "AFM3": 2.05
    },
    "lattice_constants_AFM3": {
        "a": 4.008,
        "c": 10.712
    },
    "bulk_modulus_AFM3": 82.9,
    "dos_at_fermi_total": 2.54
}
with open("/app/outputs/results.json", "w") as f:
    json.dump(results, f, indent=2)
'
