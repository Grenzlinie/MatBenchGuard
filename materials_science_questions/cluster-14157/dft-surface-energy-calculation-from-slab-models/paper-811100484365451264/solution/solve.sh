#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
# No heavy dependencies; compute.py uses Python3 stdlib only.

# === solve block: bulk_energy.txt ===
python3 /app/solution/compute.py bulk > "$OUTDIR/bulk_energy.txt"

# === solve block: slab_energies.csv ===
python3 /app/solution/compute.py slab > "$OUTDIR/slab_energies.csv"

# === solve block: surface_energies.csv ===
python3 /app/solution/compute.py surface > "$OUTDIR/surface_energies.csv"