#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 /solution/generate_xyz.py /app/outputs/gold_clusters_structures.xyz

# === solve block: gold_clusters_structures.xyz ===
echo 'Generating gold_clusters_structures.xyz'
