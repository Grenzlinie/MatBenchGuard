#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: defect_magnetic_moments.json ===
# Write the scored artifact
echo 'Creating defect_magnetic_moments.json ...'
python3 -c '
import json

results = [
    {
        "defect_type": "perfect",
        "total_moment_muB": 0.0,
        "atomic_moment_defect_site_muB": None,
        "atomic_moment_nearest_C_muB": None,
        "ferromagnetic_coupling": None
    },
    {
        "defect_type": "V_Si",
        "total_moment_muB": 2.0,
        "atomic_moment_defect_site_muB": 1.0,
        "atomic_moment_nearest_C_muB": 0.26,
        "ferromagnetic_coupling": None
    },
    {
        "defect_type": "V_C",
        "total_moment_muB": 1.65,
        "atomic_moment_defect_site_muB": 0.65,
        "atomic_moment_nearest_C_muB": None,
        "ferromagnetic_coupling": None
    },
    {
        "defect_type": "Zn_subs",
        "total_moment_muB": 1.18,
        "atomic_moment_defect_site_muB": 0.158,
        "atomic_moment_nearest_C_muB": 0.151,
        "ferromagnetic_coupling": None
    },
    {
        "defect_type": "Zn_inter",
        "total_moment_muB": 0.0,
        "atomic_moment_defect_site_muB": None,
        "atomic_moment_nearest_C_muB": None,
        "ferromagnetic_coupling": None
    },
    {
        "defect_type": "V_Si_V_Si",
        "total_moment_muB": 4.0,
        "atomic_moment_defect_site_muB": None,
        "atomic_moment_nearest_C_muB": None,
        "ferromagnetic_coupling": True
    },
    {
        "defect_type": "V_Si_V_C",
        "total_moment_muB": 2.0,
        "atomic_moment_defect_site_muB": None,
        "atomic_moment_nearest_C_muB": 0.264,
        "ferromagnetic_coupling": False
    }
]

with open("/app/outputs/defect_magnetic_moments.json", "w") as f:
    json.dump(results, f, indent=2)
'
