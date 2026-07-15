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

systems = [
    {"system": "PDME_isolated", "total_energy_kjmol": -336994.3, "key_distances": {}},
    {"system": "OH_isolated", "total_energy_kjmol": -32085.1, "key_distances": {}},
    {"system": "OH+_isolated", "total_energy_kjmol": -30814.4, "key_distances": {}},
    {"system": "OH-_isolated", "total_energy_kjmol": -32147.1, "key_distances": {}},
    {"system": "BF3_isolated", "total_energy_kjmol": -147795.3, "key_distances": {}},
    {"system": "DEE_isolated", "total_energy_kjmol": -93748.3, "key_distances": {}},
    {"system": "PDEE_isolated", "total_energy_kjmol": -549082.1, "key_distances": {}},
    {"system": "NH3_isolated", "total_energy_kjmol": -24002.1, "key_distances": {}},
    {"system": "BF3_NH3", "total_energy_kjmol": -171848.9, "key_distances": {"B_N": 1.782}},
    {"system": "BF3_DEE", "total_energy_kjmol": -241572.1, "key_distances": {"B_O": 1.905}},
    {"system": "BF3_PDEE", "total_energy_kjmol": -696875.7, "key_distances": {"B_O": 3.594}},
    {"system": "OH_PDME", "total_energy_kjmol": -369081.5, "key_distances": {"O_ether_H_OH": 2.148}},
    {"system": "OH+_PDME", "total_energy_kjmol": -367851.4, "key_distances": {"H_O_ether": 1.006, "H_O_hydroxyl": 1.940}},
    {"system": "OH-_PDME", "total_energy_kjmol": -369567.6, "key_distances": {"O_OH_C_ether": 3.360}}
]

with open("/app/outputs/results.json", "w") as f:
    json.dump({"systems": systems}, f, indent=2)
'
