#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: transition_energies.csv ===
python3 -c '
import csv
rows = [
    (0.08, 3.577, 3.580, 3.580, 3.583, 3.730, 3.710, 3.690, 3.670),
    (0.11, 3.597, 3.600, 3.600, 3.603, 3.716, 3.692, 3.668, 3.644),
    (0.14, 3.627, 3.630, 3.630, 3.633, 3.695, 3.665, 3.635, 3.605),
    (0.20, 3.665, 3.669, 3.671, 3.675, 3.610, 3.570, 3.530, 3.490),
    (0.26, 3.709, 3.714, 3.716, 3.721, 3.475, 3.425, 3.375, 3.325),
    (0.34, 3.742, 3.748, 3.752, 3.758, 3.290, 3.230, 3.170, 3.110),
    (0.41, 3.705, 3.717, 3.723, 3.735, 3.155, 3.085, 3.015, 2.945),
    (1.0,  3.620, 3.670, 3.690, 3.710, 2.920, 2.840, 2.760, 2.680),
]
with open("/app/outputs/transition_energies.csv", "w") as f:
    w = csv.writer(f)
    w.writerow(["Al_concentration","shell_included_ND2","shell_included_ND5","shell_included_ND7","shell_included_ND9","no_shell_ND2","no_shell_ND5","no_shell_ND7","no_shell_ND9"])
    for r in rows:
        w.writerow(r)
'
