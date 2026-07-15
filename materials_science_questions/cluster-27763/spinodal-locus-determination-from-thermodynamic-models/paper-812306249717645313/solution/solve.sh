#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: chi_qs_vs_DeltaH.csv ===
python3 /solution/generate_data.py /app/outputs/chi_qs_vs_DeltaH.csv chi_qs

# === solve block: mean_cluster_size_vs_DeltaH.csv ===
python3 /solution/generate_data.py /app/outputs/mean_cluster_size_vs_DeltaH.csv mean_cluster_size

# === solve block: droplet_radius_vs_DeltaH.csv ===
python3 /solution/generate_data.py /app/outputs/droplet_radius_vs_DeltaH.csv droplet_radius

# === solve block: droplet_mass_vs_DeltaH.csv ===
python3 /solution/generate_data.py /app/outputs/droplet_mass_vs_DeltaH.csv droplet_mass
