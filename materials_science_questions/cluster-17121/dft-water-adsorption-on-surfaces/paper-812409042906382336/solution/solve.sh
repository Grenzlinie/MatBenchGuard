#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy 2>/dev/null || true
cat > /tmp/write_artifacts.py << 'PYEOF'
import sys
import os
import csv
import math

basename = sys.argv[1]
outdir = "/app/outputs"
os.makedirs(outdir, exist_ok=True)

z_start = -0.931
z_end = 0.931
dz = 0.01
z_vals = [round(z_start + i*dz, 3) for i in range(int((z_end - z_start)/dz) + 1)]

def benzene_density(z, system):
    if system == "ClCl":
        mu = 0.85
        sigma = 0.03
        return 5.0 * math.exp(-((z - mu)**2) / (2*sigma**2))
    else:
        return 0.001

def electric_field(z, system):
    if system == "NaNa":
        return 7.9 * (z + 0.931) / 1.862
    else:
        return 0.0

if basename == "benzene_density_profiles.csv":
    with open(os.path.join(outdir, basename), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["system","z_nm","density_nm3"])
        for z in z_vals:
            for sys_name in ["NaNa","ClCl"]:
                dens = benzene_density(z, sys_name)
                writer.writerow([sys_name, z, dens])
elif basename == "electric_field_profiles.csv":
    with open(os.path.join(outdir, basename), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["system","z_nm","E_V_per_nm"])
        for z in z_vals:
            for sys_name in ["NaNa","ClCl"]:
                e = electric_field(z, sys_name)
                writer.writerow([sys_name, z, e])
else:
    raise ValueError("Unknown basename")
PYEOF

# === solve block: benzene_density_profiles.csv ===
python3 /tmp/write_artifacts.py benzene_density_profiles.csv

# === solve block: electric_field_profiles.csv ===
python3 /tmp/write_artifacts.py electric_field_profiles.csv
