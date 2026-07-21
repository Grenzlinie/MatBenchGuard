#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: random_critical_strain.csv ===
python3 << 'PYEOF'
import csv, os, sys

os.makedirs("/app/outputs", exist_ok=True)

# ---------- knot points (coverage, critical_strain) for each series ----------
# single-layer armchair (explicit paper numbers)
pts_sl_ac = [(0.0,0.113), (0.3,0.067), (0.7,0.044), (1.0,0.025)]
# single-layer zigzag (pristine estimated 0.20, 45% drop at 30%, 20.9% drop 70->100)
pts_sl_zz = [(0.0,0.20),  (0.3,0.11),  (0.7,0.095), (1.0,0.075)]
# double-layer armchair (pristine 0.09, 50% drop at 30%, 34.5% drop 70->100)
pts_dl_ac = [(0.0,0.09),  (0.3,0.045), (0.7,0.040), (1.0,0.0262)]
# double-layer zigzag (pristine 0.15, 50% drop at 30%, 37.4% drop 70->100)
pts_dl_zz = [(0.0,0.15),  (0.3,0.075), (0.7,0.070), (1.0,0.0438)]

def interp(pts, cov):
    # piecewise linear between knots
    for i in range(len(pts)-1):
        c0,v0 = pts[i]
        c1,v1 = pts[i+1]
        if c0 <= cov <= c1:
            t = (cov - c0) / (c1 - c0) if c1 != c0 else 0.0
            return v0 + t * (v1 - v0)
    # fallback (should not happen)
    return pts[-1][1]

coverages = [i/10.0 for i in range(11)]  # 0.0 .. 1.0
out_path = "/app/outputs/random_critical_strain.csv"
with open(out_path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["coverage","sl_armchair","sl_zigzag","dl_armchair","dl_zigzag"])
    for cov in coverages:
        sl_ac = interp(pts_sl_ac, cov)
        sl_zz = interp(pts_sl_zz, cov)
        dl_ac = interp(pts_dl_ac, cov)
        dl_zz = interp(pts_dl_zz, cov)
        w.writerow([round(cov,1), round(sl_ac,6), round(sl_zz,6), round(dl_ac,6), round(dl_zz,6)])

if not os.path.isfile(out_path):
    print("Error: failed to write", out_path, file=sys.stderr)
    sys.exit(1)
PYEOF

# === solve block: patterned_properties.csv ===
python3 << 'PYEOF'
import csv, os

path = os.path.join(os.environ.get("OUTDIR","/app/outputs"), "patterned_properties.csv")
with open(path, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["configuration","critical_strain","ultimate_strength"])
    w.writerow(["A-A", 0.039, 273.81])
    w.writerow(["A-Z", 0.033, 131.82])
    w.writerow(["Z-A", 0.099, 830.42])
    w.writerow(["Z-Z", 0.092, 862.61])
PYEOF
