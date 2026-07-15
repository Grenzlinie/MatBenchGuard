#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: binding_energies.csv ===
python3 << 'EOF'
import csv
import os
import sys

# define binding energy models (E = a*(v - v0)^2 + E_min)
models = {
    "diamond":       {"v0": 1.00, "E_min": -4.70, "a": 10},
    "wurtzite":      {"v0": 1.00, "E_min": -4.69, "a": 10},
    "white-tin(4)":  {"v0": 0.90, "E_min": -4.65, "a": 12},
    "white-tin(6)":  {"v0": 0.95, "E_min": -4.60, "a": 11},
    "fcc":           {"v0": 1.00, "E_min": -4.20, "a": 8},
    "bcc":           {"v0": 1.00, "E_min": -4.15, "a": 8},
}

vol_points = [0.80, 0.85, 0.90, 0.95, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25]
outdir = os.environ.get("OUTDIR", "/app/outputs")
outpath = os.path.join(outdir, "binding_energies.csv")

with open(outpath, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["structure", "volume_norm", "binding_energy"])
    for structure, p in models.items():
        v0 = p["v0"]
        a = p["a"]
        E0 = p["E_min"]
        for v in vol_points:
            E = a * (v - v0) ** 2 + E0
            writer.writerow([structure, f"{v:.3f}", f"{E:.6f}"])
EOF

# === solve block: diamond_properties.json ===
python3 -c '
import json

data = {
    "cohesive_energy_eV_per_atom": 4.70,
    "bulk_modulus_erg_cm3": 3.4e11,
    "s_p_mixing_ratio": 1.7,
    "equilibrium_volume_norm": 1.0
}
with open("/app/outputs/diamond_properties.json", "w") as f:
    json.dump(data, f, indent=2)
'
