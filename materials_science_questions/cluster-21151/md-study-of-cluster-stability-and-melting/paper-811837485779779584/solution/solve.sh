#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_exafs_data.json ===
python3 /solution/gen_outputs.py exafs "$OUTDIR/step_01_exafs_data.json"

# === solve block: step_02_voronoi_statistics.csv ===
python3 /solution/gen_outputs.py voronoi "$OUTDIR/step_02_voronoi_statistics.csv"

# === solve block: step_03_ag_coordination.json ===
python3 /solution/gen_outputs.py ag_coord "$OUTDIR/step_03_ag_coordination.json"
