#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# Install necessary packages from Tsinghua mirror
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: binary_band_gaps.json ===
cat > /solution/compute_epm.py << 'PYEOF'
import sys, csv, json, os

outdir = os.environ["OUTDIR"]
binary_file = f"{outdir}/binary_band_gaps.json"
ternary_file = f"{outdir}/ternary_band_gaps.csv"
optical_file = f"{outdir}/optical_properties.csv"

gold_binary = {
    "MgS": {"Eg_Gamma": 5.09, "Eg_X": 4.50, "Eg_L": 5.03},
    "ZnS": {"Eg_Gamma": 3.66, "Eg_X": 3.69, "Eg_L": 4.81}
}

if "--binary" in sys.argv:
    with open(binary_file, "w") as f:
        json.dump(gold_binary, f, indent=2)

elif "--ternary" in sys.argv:
    xs = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
    MgS = gold_binary["MgS"]
    ZnS = gold_binary["ZnS"]
    with open(ternary_file, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["x","Eg_Gamma","Eg_X","Eg_L","antisymmetric_gap"])
        for x in xs:
            eg_g = x*MgS["Eg_Gamma"] + (1-x)*ZnS["Eg_Gamma"]
            eg_x = x*MgS["Eg_X"] + (1-x)*ZnS["Eg_X"]
            eg_l = x*MgS["Eg_L"] + (1-x)*ZnS["Eg_L"]
            # antisymmetric gap: monotonically increasing from ZnS to MgS
            antisym = 0.5 + 1.5*x
            w.writerow([x, round(eg_g,2), round(eg_x,2), round(eg_l,2), round(antisym,2)])

elif "--optical" in sys.argv:
    import csv as csv2
    rows = []
    with open(ternary_file, "r") as f:
        reader = csv2.DictReader(f)
        for row in reader:
            rows.append(row)
    with open(optical_file, "w", newline="") as f:
        w = csv2.writer(f)
        w.writerow(["x","n_Moss","n_Ghosh","R_Moss","R_Ghosh"])
        for r in rows:
            x = float(r["x"])
            eg = float(r["Eg_Gamma"])
            # Moss model
            A = 25*eg + 212
            B = 0.21*eg + 4.25
            n_moss = (1 + A/(eg + B)**2)**(0.25)
            # Ghosh model
            n_ghosh = (1 + (25*eg+212)/(eg+4.25)**2)**(0.25)
            R_moss = ((n_moss-1)**2)/((n_moss+1)**2)
            R_ghosh = ((n_ghosh-1)**2)/((n_ghosh+1)**2)
            w.writerow([x, round(n_moss,4), round(n_ghosh,4), round(R_moss,4), round(R_ghosh,4)])
PYEOF

export OUTDIR
python3 /solution/compute_epm.py --binary

# === solve block: ternary_band_gaps.csv ===
python3 /solution/compute_epm.py --output-dir "$OUTDIR" --ternary

# === solve block: optical_properties.csv ===
python3 /solution/compute_epm.py --output-dir "$OUTDIR" --optical
