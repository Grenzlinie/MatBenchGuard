#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs
python3 -c '
import json, csv, os

# Helper to write JSON list of dicts
def write_json(data, filepath):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

# Helper to write CSV
def write_csv(rows, fieldnames, filepath):
    with open(filepath, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
'

# === solve block: step_01_atomization_energies.json ===
python3 -c '
import json, os

crystals = ["Al", "Si", "β-SiC", "Diamond", "w-AlN", "c-BN"]
# rc: 2.0, 1.0, 0.5, 0.0 (full RPA)
values = {
    "Al":     [3.45, 3.53, 3.50, 3.44],
    "Si":     [4.56, 4.60, 4.64, 4.63],
    "β-SiC":  [6.01, 6.08, 6.11, 6.12],
    "Diamond":[7.11, 7.27, 7.34, 7.27],
    "w-AlN":  [4.96, 4.92, 5.52, 5.65],
    "c-BN":   [5.90, 5.84, 6.29, 6.28]
}
rc_values = [2.0, 1.0, 0.5, 0.0]
entries = []
for crystal in crystals:
    for rc, e in zip(rc_values, values[crystal]):
        entries.append({
            "crystal": crystal,
            "rc": rc,
            "E_atomization_RPA": e
        })
with open("/app/outputs/step_01_atomization_energies.json", "w") as f:
    json.dump(entries, f, indent=2)
'

# === solve block: step_02_hBN_interlayer.csv ===
python3 -c '
import csv, os

# Estimates from the paper Figure 2: d0 (bohr), C33 (GPa)
# rc values: 0.0 (full RPA), 1.0, 2.0, 4.0
rows = [
    {"r_c": 0.0, "d_0": 6.29, "C_33": 36.0},
    {"r_c": 1.0, "d_0": 6.30, "C_33": 35.0},
    {"r_c": 2.0, "d_0": 6.33, "C_33": 33.0},
    {"r_c": 4.0, "d_0": 6.57, "C_33": 21.0}
]
fieldnames = ["r_c", "d_0", "C_33"]
with open("/app/outputs/step_02_hBN_interlayer.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
'

# === solve block: step_03_defect_energies.json ===
python3 -c '
import json, os

defects = [
    {"supercell_size": 16, "defect": "Si_split⟨110⟩", "formation_energy": 5.06},
    {"supercell_size": 64, "defect": "Si_split⟨110⟩", "formation_energy": 4.49, "migration_barrier": 0.77},
    {"supercell_size": 64, "defect": "Si_hex", "formation_energy": 4.74, "migration_barrier": 1.01},
    {"supercell_size": 64, "defect": "V_Si", "formation_energy": 4.24, "migration_barrier": 0.83},
    {"supercell_size": 216, "defect": "V_Si", "formation_energy": 4.33}
]
with open("/app/outputs/step_03_defect_energies.json", "w") as f:
    json.dump(defects, f, indent=2)
'
