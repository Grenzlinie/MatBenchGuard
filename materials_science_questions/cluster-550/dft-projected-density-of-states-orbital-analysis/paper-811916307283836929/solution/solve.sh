#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: energy_volume_data.csv ===
python3 << 'PYEOF'
import math, csv, os
os.makedirs("/app/outputs", exist_ok=True)
def bm(V, E0, V0, K0, K0p):
    x = V0 / V
    xi = 0.75 * (K0p - 4)
    term1 = 1.5 * (xi - 1) * (x ** (2/3))
    term2 = 0.75 * (1 - 2*xi) * (x ** (4/3))
    term3 = 0.5 * xi * (x ** (6/3))
    term4 = -(2*xi - 3) / 4
    return E0 + 1.5 * K0 * V0 * (term1 + term2 + term3 + term4)

params = {
    "CoSn": [ -14.046, 22.99, 303.6, 4.19],
    "WC":   [ -13.953, 21.035, 337.1, 4.17],
    "NaCl":  [ -13.37, 21.481, 327.6, 4.35],
    "ZnS-B3":[-13.042, 26.845, 244.2, 4.18],
    "CsCl": [-12.348, 20.797, 307.0, 4.28]
}
npoints = 15
with open("/app/outputs/energy_volume_data.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["structure","volume","total_energy"])
    for struct, (E0, V0, K0, K0p) in params.items():
        for i in range(npoints):
            frac = 0.88 + (0.24) * i / (npoints-1)
            V = V0 * frac
            E = bm(V, E0, V0, K0, K0p)
            w.writerow([struct, f"{V:.6f}", f"{E:.6f}"])
PYEOF

# === solve block: derived_properties.csv ===
python3 << 'PYEOF'
import os, csv
os.makedirs("/app/outputs", exist_ok=True)

data = [
    ["CoSn", 5.221, 2.921, -14.046, 22.99, 303.6, 4.19, 0.3925],
    ["WC", 2.913, 2.862, -13.953, 21.035, 337.1, 4.17, "NA"],
    ["NaCl", 4.413, "NA", -13.37, 21.481, 327.6, 4.35, "NA"],
    ["ZnS-B3", 4.753, "NA", -13.042, 26.845, 244.2, 4.18, "NA"],
    ["CsCl", 2.75, "NA", -12.348, 20.797, 307.0, 4.28, "NA"],
]

with open("/app/outputs/derived_properties.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["structure", "a", "c", "E0", "V0", "K0", "K0_prime", "N_x"])
    for row in data:
        w.writerow(row)
PYEOF

# === solve block: electronic_properties.csv ===
python3 /solution/generate.py electronic_properties.csv
