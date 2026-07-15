#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# Install required packages (fast lightweight miniconda-style install)
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: static_results.csv ===
# Fix alpha_list to use explicit values (avoid np.arange floating-point precision issues)
sed -i 's/alpha_list\s*=\s*np\.arange(\s*2\.8\s*,\s*4\.1\s*,\s*0\.1\s*)/alpha_list = [2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0]/g' /solution/compute.py

# Prevent KeyError from floating-point dict keys by rounding alpha in all dict accesses
sed -i 's/\(opt_params\|results\|params\|all_data\|data\)\[\s*alpha\s*\]/\1[round(alpha,1)]/g' /solution/compute.py

python3 /solution/compute.py --static

# === solve block: lattice_frequencies.csv ===
python3 /solution/compute.py --freqs
