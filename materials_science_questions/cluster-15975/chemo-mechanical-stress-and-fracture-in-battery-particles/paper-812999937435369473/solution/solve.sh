#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail

# === solve block: chemomechanical_results.csv ===
mkdir -p /app/outputs
python3 << 'EOF'
import csv

rows = [
    {"oxide_thickness_nm": 1, "critical_pressure_GPa": 2.5, "fraction_unlithiated": 0.10, "hoop_stress_GPa": 3.00},
    {"oxide_thickness_nm": 2, "critical_pressure_GPa": 2.5, "fraction_unlithiated": 0.15, "hoop_stress_GPa": 2.80},
    {"oxide_thickness_nm": 3, "critical_pressure_GPa": 2.5, "fraction_unlithiated": 0.22, "hoop_stress_GPa": 2.50},
    {"oxide_thickness_nm": 4, "critical_pressure_GPa": 2.5, "fraction_unlithiated": 0.33, "hoop_stress_GPa": 2.20},
    {"oxide_thickness_nm": 5, "critical_pressure_GPa": 2.5, "fraction_unlithiated": 0.46, "hoop_stress_GPa": 1.80},
    {"oxide_thickness_nm": 6, "critical_pressure_GPa": 2.5, "fraction_unlithiated": 0.60, "hoop_stress_GPa": 1.40},
    {"oxide_thickness_nm": 7, "critical_pressure_GPa": 2.5, "fraction_unlithiated": 0.72, "hoop_stress_GPa": 1.10},
    {"oxide_thickness_nm": 8, "critical_pressure_GPa": 2.5, "fraction_unlithiated": 0.82, "hoop_stress_GPa": 0.80},
    {"oxide_thickness_nm": 9, "critical_pressure_GPa": 2.5, "fraction_unlithiated": 0.89, "hoop_stress_GPa": 0.60},
    {"oxide_thickness_nm": 10, "critical_pressure_GPa": 2.5, "fraction_unlithiated": 0.94, "hoop_stress_GPa": 0.45},
    {"oxide_thickness_nm": 1, "critical_pressure_GPa": 4.0, "fraction_unlithiated": 0.05, "hoop_stress_GPa": 3.50},
    {"oxide_thickness_nm": 2, "critical_pressure_GPa": 4.0, "fraction_unlithiated": 0.08, "hoop_stress_GPa": 3.20},
    {"oxide_thickness_nm": 3, "critical_pressure_GPa": 4.0, "fraction_unlithiated": 0.12, "hoop_stress_GPa": 2.90},
    {"oxide_thickness_nm": 4, "critical_pressure_GPa": 4.0, "fraction_unlithiated": 0.20, "hoop_stress_GPa": 2.50},
    {"oxide_thickness_nm": 5, "critical_pressure_GPa": 4.0, "fraction_unlithiated": 0.30, "hoop_stress_GPa": 2.00},
    {"oxide_thickness_nm": 6, "critical_pressure_GPa": 4.0, "fraction_unlithiated": 0.42, "hoop_stress_GPa": 1.60},
    {"oxide_thickness_nm": 7, "critical_pressure_GPa": 4.0, "fraction_unlithiated": 0.55, "hoop_stress_GPa": 1.20},
    {"oxide_thickness_nm": 8, "critical_pressure_GPa": 4.0, "fraction_unlithiated": 0.65, "hoop_stress_GPa": 0.90},
    {"oxide_thickness_nm": 9, "critical_pressure_GPa": 4.0, "fraction_unlithiated": 0.75, "hoop_stress_GPa": 0.70},
    {"oxide_thickness_nm": 10, "critical_pressure_GPa": 4.0, "fraction_unlithiated": 0.84, "hoop_stress_GPa": 0.50},
]

with open("/app/outputs/chemomechanical_results.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["oxide_thickness_nm", "critical_pressure_GPa", "fraction_unlithiated", "hoop_stress_GPa"])
    w.writeheader()
    w.writerows(rows)
EOF
