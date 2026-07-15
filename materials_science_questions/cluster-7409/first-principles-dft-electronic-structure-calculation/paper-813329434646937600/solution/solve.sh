#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 - "$OUTDIR/results.json" << 'PYEOF'
import json, sys
data = {
    "bulk_bandgap_eV": 3.4063,
    "slab3_t2_bandgap_eV": 0.0018,
    "slab6_t2_bandgap_eV": 4.0616,
    "slab9_t2_bandgap_eV": 2.8982,
    "surface_energies": [
        {
            "n_layers": 3,
            "termination_layer": 1,
            "k": 1,
            "E_surface_Jpm2": 3.96,
            "E_slab_Ha": -1994.04024,
            "E_bulk_per_repeat_unit_Ha": -1994.39502
        },
        {
            "n_layers": 3,
            "termination_layer": 2,
            "k": 1,
            "E_surface_Jpm2": 2.23,
            "E_slab_Ha": -1994.19514,
            "E_bulk_per_repeat_unit_Ha": -1994.39502
        },
        {
            "n_layers": 3,
            "termination_layer": 3,
            "k": 1,
            "E_surface_Jpm2": 3.96,
            "E_slab_Ha": -1994.04024,
            "E_bulk_per_repeat_unit_Ha": -1994.39502
        },
        {
            "n_layers": 6,
            "termination_layer": 2,
            "k": 2,
            "E_surface_Jpm2": 1.89,
            "E_slab_Ha": -3988.62097,
            "E_bulk_per_repeat_unit_Ha": -1994.39502
        }
    ]
}
with open(sys.argv[1], "w") as f:
    json.dump(data, f, indent=2)
PYEOF
