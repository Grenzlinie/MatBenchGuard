#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs

# === solve block: antioxidant_properties.json ===
python3 -c '
import json, sys
data = {
  "PANI-L": {
    "bde": [85.09, 78.04, 78.10, 79.92],
    "adiabatic_IE": 130.36,
    "adiabatic_EA": 0.58,
    "HOMO_energy": -4.64,
    "LUMO_energy": -1.21
  },
  "PANI-E": {
    "bde": [86.83, 78.66],
    "adiabatic_IE": 140.74,
    "adiabatic_EA": 45.62,
    "HOMO_energy": -5.13,
    "LUMO_energy": -2.87
  },
  "C60-L1": {
    "bde": [81.85, 78.14, 78.31, 80.21],
    "adiabatic_IE": 130.98,
    "adiabatic_EA": 65.10,
    "HOMO_energy": -4.71,
    "LUMO_energy": -3.78
  },
  "C60-L2": {
    "bde": [89.78, 79.75, 81.14],
    "adiabatic_IE": 133.97,
    "adiabatic_EA": 61.74,
    "HOMO_energy": -4.84,
    "LUMO_energy": -3.68
  },
  "C60-E1": {
    "bde": [83.86, 78.93],
    "adiabatic_IE": 140.56,
    "adiabatic_EA": 66.46,
    "HOMO_energy": -5.26,
    "LUMO_energy": -4.01
  },
  "C60-E2": {
    "bde": [90.88],
    "adiabatic_IE": 143.84,
    "adiabatic_EA": 65.18,
    "HOMO_energy": -5.39,
    "LUMO_energy": -3.90
  }
}
json.dump(data, open(sys.argv[1], "w"))
' "$OUTDIR/antioxidant_properties.json"

# === solve block: fedor_analysis.json ===
python3 -c '
import json, sys
IE_Na = 118.5
EA_F  = 78.4
ie_vals = {
    "PANI-L": 130.36,
    "PANI-E": 140.74,
    "C60-L1": 130.98,
    "C60-L2": 133.97,
    "C60-E1": 140.56,
    "C60-E2": 143.84
}
ea_vals = {
    "PANI-L": 0.58,
    "PANI-E": 45.62,
    "C60-L1": 65.10,
    "C60-L2": 61.74,
    "C60-E1": 66.46,
    "C60-E2": 65.18
}
compounds = {}
for c in ["PANI-L","PANI-E","C60-L1","C60-L2","C60-E1","C60-E2"]:
    compounds[c] = {"RIE": ie_vals[c]/IE_Na, "REA": ea_vals[c]/EA_F}
output = {"compounds": compounds, "best_antioxidant": "C60-L1"}
json.dump(output, open(sys.argv[1], "w"))
' "$OUTDIR/fedor_analysis.json"
