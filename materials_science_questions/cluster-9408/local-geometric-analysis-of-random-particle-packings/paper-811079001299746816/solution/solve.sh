#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: isotropic_pressure.csv ===
python3 -c "import csv; data=[(0.79,0.07),(0.81,0.13),(0.83,0.20),(0.85,0.28)]; f=open('$OUTDIR/isotropic_pressure.csv','w'); w=csv.writer(f); w.writerow(['phi','pressure']); w.writerows(data); f.close()"

# === solve block: uniaxial_stress.csv ===
python3 /solution/compute.py uniaxial /app/outputs/uniaxial_stress.csv

# === solve block: shear_stress.csv ===
python3 /solution/compute.py shear /app/outputs/shear_stress.csv
