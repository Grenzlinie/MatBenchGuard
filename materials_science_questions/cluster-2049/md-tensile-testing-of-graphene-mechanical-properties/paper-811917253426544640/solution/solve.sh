#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: potential_energy_curves.csv ===
python3 -c '
import csv, math

def morse(d, De, re, a=1.5):
    return De * (1 - math.exp(-a * (d - re)))**2 - De

registries = [
    ("SFR-1", 0.185, 4.7),
    ("H-1",  0.0835, 7.3),
]

with open("/app/outputs/potential_energy_curves.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["registry", "distance_bohr", "energy_relative_eV"])
    for reg, De, re in registries:
        for i in range(161):  # 18.0 - 2.0 = 16.0, steps of 0.1 -> 161 points
            d = 2.0 + i * 0.1
            e = morse(d, De, re)
            writer.writerow([reg, f"{d:.1f}", f"{e:.6f}"])
'
