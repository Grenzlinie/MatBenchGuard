#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: h_flip_defect_data.csv ===
python3 <<'PYEOF'
import csv, math

rows = [
    {"H_site_id": "55", "delta_E_eV": 0.69, "e_d_star_original": 0.21, "e_d_star_defect": 0.46, "volume_change_percent": 0.613, "avg_bond_angle_deg": 100.0},
    {"H_site_id": "56", "delta_E_eV": 0.56, "e_d_star_original": 0.21, "e_d_star_defect": 0.40, "volume_change_percent": 0.088, "avg_bond_angle_deg": 102.0},
    {"H_site_id": "57", "delta_E_eV": 0.48, "e_d_star_original": 0.24, "e_d_star_defect": 0.39, "volume_change_percent": 0.516, "avg_bond_angle_deg": 105.0},
    {"H_site_id": "58", "delta_E_eV": 0.60, "e_d_star_original": 0.30, "e_d_star_defect": 0.48, "volume_change_percent": 0.074, "avg_bond_angle_deg": 103.0},
    {"H_site_id": "59", "delta_E_eV": 0.18, "e_d_star_original": 0.38, "e_d_star_defect": 0.45, "volume_change_percent": 0.000, "avg_bond_angle_deg": 115.0},
    {"H_site_id": "60", "delta_E_eV": 0.28, "e_d_star_original": 0.25, "e_d_star_defect": 0.30, "volume_change_percent": 0.306, "avg_bond_angle_deg": 110.0},
]

output_path = "/app/outputs/h_flip_defect_data.csv"
fieldnames = ["H_site_id", "delta_E_eV", "e_d_star_original", "e_d_star_defect", "volume_change_percent", "avg_bond_angle_deg"]

with open(output_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
PYEOF

# === solve block: energy_barrier.json ===
python3 <<'PYEOF'
import json

data = {
    "site_id": "55",
    "barrier_eV": 1.8,
    "method": "nudged elastic band (NEB)"
}

with open("/app/outputs/energy_barrier.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
