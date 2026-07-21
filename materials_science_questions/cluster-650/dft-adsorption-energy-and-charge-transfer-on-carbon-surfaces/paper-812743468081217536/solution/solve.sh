#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_angle_vs_time.csv ===
python3 /solution/generate.py step_01_angle_vs_time.csv

# === solve block: step_02_basepair_distance.csv ===
python3 /solution/generate.py step_02_basepair_distance.csv

# === solve block: step_03_interaction_energy.csv ===
python3 /solution/generate.py step_03_interaction_energy.csv

# === solve block: step_04_final_angles.csv ===
python3 /solution/generate.py step_04_final_angles.csv
