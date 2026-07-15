#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: cluster_sizes_a_axis.csv ===
python3 /solution/generate_clusters.py a > "$OUTDIR/cluster_sizes_a_axis.csv"

# === solve block: cluster_sizes_c_axis.csv ===
python3 /solution/generate_clusters.py c > "$OUTDIR/cluster_sizes_c_axis.csv"
