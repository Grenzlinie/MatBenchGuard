#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_summary_table.csv ===
python3 /solution/generate_all.py summary_table --out /app/outputs/step_01_summary_table.csv

# === solve block: step_02_band_gaps_zero_strain.json ===
python3 /solution/generate_all.py zero_strain_gaps --out /app/outputs/step_02_band_gaps_zero_strain.json

# === solve block: step_03_strain_band_gap_PBE.csv ===
python3 /solution/generate_all.py strain_gaps --out /app/outputs/step_03_strain_band_gap_PBE.csv

# === solve block: step_04_dielectric_function_MgS.csv ===
python3 /solution/generate_all.py dielectric --material MgS --out /app/outputs/step_04_dielectric_function_MgS.csv

# === solve block: step_05_dielectric_function_MgSe.csv ===
python3 /solution/generate_all.py dielectric --material MgSe --out /app/outputs/step_05_dielectric_function_MgSe.csv

# === solve block: step_06_absorption_reflectivity_MgS.csv ===
python3 /solution/generate_all.py absorption_reflectivity --material MgS --out /app/outputs/step_06_absorption_reflectivity_MgS.csv

# === solve block: step_07_absorption_reflectivity_MgSe.csv ===
python3 /solution/generate_all.py absorption_reflectivity --material MgSe --out /app/outputs/step_07_absorption_reflectivity_MgSe.csv
