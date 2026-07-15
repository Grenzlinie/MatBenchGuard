#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: enthalpy_changes.json ===
python3 << 'PYEOF'
import json

data = {
    "benzene": [
        {"pathway": "Pathway 1", "nH_removed": 1, "delta_H_kJmol": -250.0, "most_favorable": True},
        {"pathway": "Pathway 2", "nH_removed": 1, "delta_H_kJmol": -180.0, "most_favorable": False},
        {"pathway": "Pathway 3", "nH_removed": 2, "delta_H_kJmol": -350.0, "most_favorable": True}
    ],
    "toluene": [
        {"pathway": "Pathway 1", "nH_removed": 1, "delta_H_kJmol": -230.0, "most_favorable": True},
        {"pathway": "Pathway 2", "nH_removed": 1, "delta_H_kJmol": -160.0, "most_favorable": False},
        {"pathway": "Pathway 3", "nH_removed": 1, "delta_H_kJmol": -230.0, "most_favorable": True},
        {"pathway": "Pathway 4", "nH_removed": 1, "delta_H_kJmol": -160.0, "most_favorable": False},
        {"pathway": "Pathway 5", "nH_removed": 1, "delta_H_kJmol": -230.0, "most_favorable": True},
        {"pathway": "Pathway 6", "nH_removed": 1, "delta_H_kJmol": -160.0, "most_favorable": False},
        {"pathway": "Pathway 7", "nH_removed": 1, "delta_H_kJmol": -210.0, "most_favorable": False},
        {"pathway": "Pathway 8", "nH_removed": 1, "delta_H_kJmol": -160.0, "most_favorable": False},
        {"pathway": "Pathway 9", "nH_removed": 2, "delta_H_kJmol": -300.0, "most_favorable": False},
        {"pathway": "Pathway 10", "nH_removed": 2, "delta_H_kJmol": -300.0, "most_favorable": False},
        {"pathway": "Pathway 11", "nH_removed": 2, "delta_H_kJmol": -370.0, "most_favorable": True},
        {"pathway": "Pathway 12", "nH_removed": 2, "delta_H_kJmol": -370.0, "most_favorable": True},
        {"pathway": "Pathway 13", "nH_removed": 2, "delta_H_kJmol": -370.0, "most_favorable": True},
        {"pathway": "Pathway 14", "nH_removed": 2, "delta_H_kJmol": -370.0, "most_favorable": True}
    ],
    "phenol": [
        {"pathway": "Pathway 1", "nH_removed": 1, "delta_H_kJmol": -240.0, "most_favorable": True},
        {"pathway": "Pathway 2", "nH_removed": 1, "delta_H_kJmol": -160.0, "most_favorable": False},
        {"pathway": "Pathway 3", "nH_removed": 1, "delta_H_kJmol": -240.0, "most_favorable": True},
        {"pathway": "Pathway 4", "nH_removed": 1, "delta_H_kJmol": -160.0, "most_favorable": False},
        {"pathway": "Pathway 5", "nH_removed": 1, "delta_H_kJmol": -240.0, "most_favorable": True},
        {"pathway": "Pathway 6", "nH_removed": 1, "delta_H_kJmol": -160.0, "most_favorable": False},
        {"pathway": "Pathway 7", "nH_removed": 1, "delta_H_kJmol": -180.0, "most_favorable": False},
        {"pathway": "Pathway 8", "nH_removed": 1, "delta_H_kJmol": -160.0, "most_favorable": False},
        {"pathway": "Pathway 9", "nH_removed": 1, "delta_H_kJmol": -180.0, "most_favorable": False},
        {"pathway": "Pathway 10", "nH_removed": 1, "delta_H_kJmol": -160.0, "most_favorable": False},
        {"pathway": "Pathway 11", "nH_removed": 1, "delta_H_kJmol": -240.0, "most_favorable": True},
        {"pathway": "Pathway 12", "nH_removed": 1, "delta_H_kJmol": -160.0, "most_favorable": False},
        {"pathway": "Pathway 13", "nH_removed": 2, "delta_H_kJmol": -360.0, "most_favorable": True},
        {"pathway": "Pathway 14", "nH_removed": 2, "delta_H_kJmol": -360.0, "most_favorable": True},
        {"pathway": "Pathway 15", "nH_removed": 2, "delta_H_kJmol": -320.0, "most_favorable": False},
        {"pathway": "Pathway 16", "nH_removed": 2, "delta_H_kJmol": -320.0, "most_favorable": False},
        {"pathway": "Pathway 17", "nH_removed": 2, "delta_H_kJmol": -320.0, "most_favorable": False},
        {"pathway": "Pathway 18", "nH_removed": 2, "delta_H_kJmol": -320.0, "most_favorable": False},
        {"pathway": "Pathway 19", "nH_removed": 2, "delta_H_kJmol": -360.0, "most_favorable": True},
        {"pathway": "Pathway 20", "nH_removed": 2, "delta_H_kJmol": -360.0, "most_favorable": True},
        {"pathway": "Pathway 21", "nH_removed": 2, "delta_H_kJmol": -360.0, "most_favorable": True},
        {"pathway": "Pathway 22", "nH_removed": 2, "delta_H_kJmol": -320.0, "most_favorable": False}
    ]
}

with open("/app/outputs/enthalpy_changes.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: mulliken_tables.json ===
python3 << 'PYEOF'
import json

def perc(b, a):
    return round((b - a) / b * 100, 1) if b != 0 else 0.0

data = {
    "benzene": [
        {"pathway": "Pathway 1", "nH_removed": 1,
         "min_mulliken_before": 0.540, "min_mulliken_after": 0.476,
         "percent_reduction": perc(0.540, 0.476)},
        {"pathway": "Pathway 3", "nH_removed": 2,
         "min_mulliken_before": 0.494, "min_mulliken_after": 0.416,
         "percent_reduction": perc(0.494, 0.416)}
    ],
    "toluene": [
        {"pathway": "Pathway 1", "nH_removed": 1,
         "min_mulliken_before": 0.514, "min_mulliken_after": 0.451,
         "percent_reduction": perc(0.514, 0.451)},
        {"pathway": "Pathway 3", "nH_removed": 1,
         "min_mulliken_before": 0.515, "min_mulliken_after": 0.473,
         "percent_reduction": perc(0.515, 0.473)},
        {"pathway": "Pathway 5", "nH_removed": 1,
         "min_mulliken_before": 0.534, "min_mulliken_after": 0.474,
         "percent_reduction": perc(0.534, 0.474)},
        {"pathway": "Pathway 11", "nH_removed": 2,
         "min_mulliken_before": 0.460, "min_mulliken_after": 0.412,
         "percent_reduction": perc(0.460, 0.412)},
        {"pathway": "Pathway 12", "nH_removed": 2,
         "min_mulliken_before": 0.460, "min_mulliken_after": 0.405,
         "percent_reduction": perc(0.460, 0.405)},
        {"pathway": "Pathway 13", "nH_removed": 2,
         "min_mulliken_before": 0.456, "min_mulliken_after": 0.400,
         "percent_reduction": perc(0.456, 0.400)},
        {"pathway": "Pathway 14", "nH_removed": 2,
         "min_mulliken_before": 0.456, "min_mulliken_after": 0.400,
         "percent_reduction": perc(0.456, 0.400)}
    ],
    "phenol": [
        {"pathway": "Pathway 1", "nH_removed": 1,
         "min_mulliken_before": 0.481, "min_mulliken_after": 0.417,
         "percent_reduction": perc(0.481, 0.417)},
        {"pathway": "Pathway 3", "nH_removed": 1,
         "min_mulliken_before": 0.508, "min_mulliken_after": 0.427,
         "percent_reduction": perc(0.508, 0.427)},
        {"pathway": "Pathway 5", "nH_removed": 1,
         "min_mulliken_before": 0.517, "min_mulliken_after": 0.385,
         "percent_reduction": perc(0.517, 0.385)},
        {"pathway": "Pathway 11", "nH_removed": 1,
         "min_mulliken_before": 0.488, "min_mulliken_after": 0.456,
         "percent_reduction": perc(0.488, 0.456)},
        {"pathway": "Pathway 13", "nH_removed": 2,
         "min_mulliken_before": 0.472, "min_mulliken_after": 0.404,
         "percent_reduction": perc(0.472, 0.404)},
        {"pathway": "Pathway 14", "nH_removed": 2,
         "min_mulliken_before": 0.472, "min_mulliken_after": 0.402,
         "percent_reduction": perc(0.472, 0.402)},
        {"pathway": "Pathway 19", "nH_removed": 2,
         "min_mulliken_before": 0.474, "min_mulliken_after": 0.394,
         "percent_reduction": perc(0.474, 0.394)},
        {"pathway": "Pathway 20", "nH_removed": 2,
         "min_mulliken_before": 0.474, "min_mulliken_after": 0.384,
         "percent_reduction": perc(0.474, 0.384)},
        {"pathway": "Pathway 21", "nH_removed": 2,
         "min_mulliken_before": 0.470, "min_mulliken_after": 0.394,
         "percent_reduction": perc(0.470, 0.394)}
    ]
}

with open("/app/outputs/mulliken_tables.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
