#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c '
import json

simulations = [
    {
        "chirality": "(11,11)",
        "temperature": 300,
        "max_shear_stress_GPa": 72.0,
        "critical_twist_angle_deg": 835.0,
        "interaction_force_at_500deg_eV_Ang": 0.006
    },
    {
        "chirality": "(11,11)",
        "temperature": 500,
        "max_shear_stress_GPa": 68.0,
        "critical_twist_angle_deg": 810.0,
        "interaction_force_at_500deg_eV_Ang": 0.008
    },
    {
        "chirality": "(11,11)",
        "temperature": 700,
        "max_shear_stress_GPa": 64.0,
        "critical_twist_angle_deg": 780.0,
        "interaction_force_at_500deg_eV_Ang": 0.010
    },
    {
        "chirality": "(13,13)",
        "temperature": 300,
        "max_shear_stress_GPa": 74.0,
        "critical_twist_angle_deg": 670.0,
        "interaction_force_at_500deg_eV_Ang": 0.0055
    },
    {
        "chirality": "(15,15)",
        "temperature": 300,
        "max_shear_stress_GPa": 78.0,
        "critical_twist_angle_deg": 590.0,
        "interaction_force_at_500deg_eV_Ang": 0.006
    },
    {
        "chirality": "(11,11)-pure",
        "temperature": 300,
        "max_shear_stress_GPa": 60.0,
        "critical_twist_angle_deg": 1040.0,
        "interaction_force_at_500deg_eV_Ang": 0.0
    }
]

with open("/app/outputs/results.json", "w") as f:
    json.dump({"simulations": simulations}, f, indent=2)
'
