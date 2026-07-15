#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: fitted_coefficients.csv ===
python3 << 'BLOCK_EOF'
import csv

# Reference values from Table 3, with sign conversions:
#   A·10³  =>  A = value/1000
#   -D     =>  D = -value
#   -E     =>  E = -value
#   -b     =>  b = -value
# Solid phases have A,B,C,D,E; a,b empty. Liquid phases have a,b; A,B,C,D,E empty.

rows = [
    # (phase,            A,        B,      C,         D,       E,      a,      b)
    ("Gd5Ge3_solid",     0.001436, 234.67, 1958350,   -76664,  -905.22, "", ""),
    ("Gd5Ge3_liquid",    "",       "",     "",        "",      "",      371.77, -110843),
    ("GdGe_solid",       0.005774, 45.87,  34755,     -14305,  -174.41, "", ""),
    ("GdGe_liquid",      "",       "",     "",        "",      "",      87.67,  -26139),
    ("alpha_GdGe1.5",    0.000182, 64.17,  211039,    -19855,  -268.64, "", ""),
    ("beta_GdGe1.5",     0.00168,  61.75,  -376500,   -17298,  -253.64, "", ""),
    ("gamma_GdGe1.5",    0.005159, 52.38,  -2855310,  -6498,   -108.58, "", ""),
    ("GdGe1.5_liquid",   "",       "",     "",        "",      "",      107.90, -32169),
]

with open("/app/outputs/fitted_coefficients.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["phase", "A", "B", "C", "D", "E", "a", "b"])
    for row in rows:
        writer.writerow(row)
BLOCK_EOF

# === solve block: phase_transformations.csv ===
python3 << 'BLOCK_EOF'
import csv

# Reference values from Table 4 (temperatures, enthalpies, entropies).
# Unit conversions follow the paper:
#   ΔH in kJ·mol⁻¹, ΔS in J·K⁻¹·mol⁻¹.

rows = [
    # (compound,    transformation_type, temperature_K, deltaH_kJ_per_mol, deltaS_J_per_K_per_mol)
    ("Gd5Ge3",     "melting",           2051,           240.0,              117.0),
    ("GdGe",       "melting",           1841,           45.5,               24.7),
    ("GdGe1.5",    "polymorphic",       1114,           1.2,                1.1),
    ("GdGe1.5",    "polymorphic",       1442,           2.8,                1.9),
    ("GdGe1.5",    "melting",           1719,           56.3,               32.8),
]

with open("/app/outputs/phase_transformations.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["compound", "transformation_type", "temperature_K", "deltaH_kJ_per_mol", "deltaS_J_per_K_per_mol"])
    for row in rows:
        writer.writerow(row)
BLOCK_EOF
