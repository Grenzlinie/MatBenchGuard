#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
# No downloads or external data; the helper script computes everything from equations.

# === solve block: phase_diagram_3d.csv ===
echo "Computing phase diagram (binodal and spinodal) for λ=1 3D lattice gas..."
python3 /solution/compute_curves.py --phase-diagram > "$OUTDIR/phase_diagram_3d.csv"

# === solve block: density_maxima_3d.csv ===
echo "Computing density maxima locus for λ=1 3D lattice gas..."
python3 /solution/compute_curves.py --density-maxima > "$OUTDIR/density_maxima_3d.csv"

# === solve finalize ===
echo "All outputs written."
