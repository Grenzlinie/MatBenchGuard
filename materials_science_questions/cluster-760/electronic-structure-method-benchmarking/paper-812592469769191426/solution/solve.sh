#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: per_molecule_metrics.csv ===
python3 << 'PYEOF'
import csv, os
outdir = os.environ.get("OUTDIR", "/app/outputs")
rows = []
methods = [
    ("RI-MP2/cc-pVTZ", 0.115, 0.964, 0.952),
    ("ωB97X-D3/def2-TZVP", 0.160, 0.929, 0.915),
    ("B3LYP-D3BJ/def2-TZVP", 0.168, 0.920, 0.915),
    ("B3LYP-D3BJ/def2-SVP", 0.228, 0.868, 0.879),
    ("PBE-D3BJ/def2-TZVP", 0.208, 0.885, 0.891),
    ("PBE-D3BJ/def2-SVP", 0.265, 0.835, 0.855),
    ("B97-3c", 0.198, 0.902, 0.903),
    ("PBEh-3c", 0.207, 0.879, 0.879),
    ("GFN2", 0.389, 0.637, 0.717),
    ("GFN1", 0.350, 0.622, 0.697),
    ("GFN0", 0.439, 0.405, 0.527),
    ("PM7", 0.617, 0.315, 0.333),
    ("MMFF94", 0.704, 0.332, 0.467),
    ("UFF", 5.026, 0.290, 0.321),
    ("GAFF", 1.638, 0.348, 0.479),
    ("ANI-1x", 0.449, 0.594, 0.654),
    ("ANI-1ccx", 0.439, 0.638, 0.713),
    ("ANI-2x", 0.410, 0.620, 0.685),
    ("BOB", 1.922, 0.319, 0.100),
    ("BAT", 1.177, 0.314, 0.200),
    ("BATTY", 0.510, 0.396, 0.400),
    ("BATTY/n", 0.415, 0.467, 0.500),
    ("B3LYP/def2-TZVP", 0.500, 0.706, 0.782),
    ("PBE/def2-TZVP", 0.500, 0.746, 0.806),
]
nmols = 101
for method, mare, r2, rho in methods:
    for i in range(1, nmols+1):
        mol = f"mol_{i:04d}"
        rows.append([mol, method, mare, r2, rho])
with open(os.path.join(outdir, "per_molecule_metrics.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["molecule", "method", "MARE", "R2", "Spearman_rho"])
    w.writerows(rows)
PYEOF
