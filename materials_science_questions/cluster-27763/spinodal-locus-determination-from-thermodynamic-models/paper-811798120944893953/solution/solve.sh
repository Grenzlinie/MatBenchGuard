#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p $OUTDIR
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: analytical_hcc.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from compute_analytical import compute_analytical_hcc; compute_analytical_hcc('$OUTDIR/analytical_hcc.csv')"

# === solve block: effective_potentials.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from compute_analytical import compute_effective_potentials; compute_effective_potentials('$OUTDIR/effective_potentials.csv')"

# === solve block: simulation_hcc.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from compute_analytical import compute_simulation_hcc; compute_simulation_hcc('$OUTDIR/simulation_hcc.csv')"

# === solve block: structure_factor_analytical.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from compute_analytical import compute_structure_factor; compute_structure_factor('$OUTDIR/structure_factor_analytical.csv')"
