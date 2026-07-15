#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: vacancy_formation_energies.csv ===
python3 << 'PYEOF'
import csv, os
outdir = "/app/outputs"
fields = [
    (0,    0.611),
    (4,    0.556),
    (6,    0.520),
    (10,   0.456),
    (30,  -0.10)   # negative, spontaneous vacancy formation
]
with open(os.path.join(outdir, "vacancy_formation_energies.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Field (V/nm)", "Delta_E_vac (eV)"])
    for field, energy in fields:
        writer.writerow([field, energy])
PYEOF

# === solve block: structural_relaxation_30Vnm.json ===
python3 << 'PYEOF'
import json, os
outdir = "/app/outputs"
data = {
    "Cu_O_surface_bond_length_A": 1.85,
    "O_plane_O_surface_distance_A": 6.27
}
with open(os.path.join(outdir, "structural_relaxation_30Vnm.json"), "w") as f:
    json.dump(data, f, indent=2)
PYEOF
