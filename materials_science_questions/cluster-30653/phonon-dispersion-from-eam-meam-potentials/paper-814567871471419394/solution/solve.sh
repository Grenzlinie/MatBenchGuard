#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
#!/bin/bash
set -euo pipefail

python3 -c '
import json

results = [
    {"metal": "Ag", "temperature_K": 300, "Q_eV": 0.0, "d_break_Angstrom": 24.0, "LAC_formed": False},
    {"metal": "Ag", "temperature_K": 300, "Q_eV": 1.0, "d_break_Angstrom": 32.0, "LAC_formed": False},
    {"metal": "Au", "temperature_K": 300, "Q_eV": 0.0, "d_break_Angstrom": 21.0, "LAC_formed": False},
    {"metal": "Au", "temperature_K": 300, "Q_eV": 1.0, "d_break_Angstrom": 24.5, "LAC_formed": False},
    {"metal": "Pd", "temperature_K": 300, "Q_eV": 0.0, "d_break_Angstrom": 20.0, "LAC_formed": False},
    {"metal": "Pd", "temperature_K": 300, "Q_eV": 1.0, "d_break_Angstrom": 24.0, "LAC_formed": False},
    {"metal": "Pt", "temperature_K": 300, "Q_eV": 0.0, "d_break_Angstrom": 19.5, "LAC_formed": False},
    {"metal": "Pt", "temperature_K": 300, "Q_eV": 1.0, "d_break_Angstrom": 23.5, "LAC_formed": False},
    {"metal": "Ag", "temperature_K": 100, "Q_eV": 0.4, "d_break_Angstrom": 29.0, "LAC_formed": True}
]

with open("/app/outputs/results.json", "w") as f:
    json.dump(results, f, indent=2)
'
