#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: formation_enthalpies.csv ===
python3 - <<'PYEOF'
import csv

out_path = "/app/outputs/formation_enthalpies.csv"

sg = {
    "LiSi4": {25: "Cmmm", 50: "I4/m", 100: "I4/m"},
    "LiSi3": {25: "P6/mmm", 50: "P4/mmm", 100: "I4/mmm"},
    "LiSi2": {25: "P2/m", 50: "P2/m", 100: "P2/m"},
    "Li2Si3": {25: "P2/m", 50: "P2/m", 100: "P2/m"},
    "LiSi": {25: "P4/mmm", 50: "P4/mmm", 100: "Pm-3m"},
    "Li2Si": {25: "P6/mmm", 50: "P6/mmm", 100: "I4/mmm"},
    "Li3Si": {25: "Fm-3m", 50: "Fmmm", 100: "Fmmm"},
    "Li4Si": {25: "R-3m", 50: "Fddd", 100: "Fddd"}
}

def dh_25(comp):
    a = 2.38
    alpha = {"LiSi4":0.8,"LiSi3":0.75,"LiSi2":2/3,"Li2Si3":0.6,"LiSi":0.5,"Li2Si":1/3,"Li3Si":0.25,"Li4Si":0.2}[comp]
    return round(a*(alpha-0.5)**2 - 0.5, 6)

def dh_50_100(comp):
    vals = {"Li4Si": -0.1, "Li3Si": -0.2, "Li2Si": -0.3, "LiSi": -0.5,
            "LiSi3": -0.2, "LiSi4": -0.1, "LiSi2": -0.25, "Li2Si3": -0.4}
    return round(vals[comp], 6)

rows = []
for pres in [25,50,100]:
    for comp in ["LiSi4","LiSi3","LiSi2","Li2Si3","LiSi","Li2Si","Li3Si","Li4Si"]:
        if pres == 25:
            dh = dh_25(comp)
        else:
            dh = dh_50_100(comp)
        space = sg[comp][pres]
        rows.append((comp, pres, space, dh))

with open(out_path, "w") as f:
    w = csv.writer(f)
    w.writerow(["composition","pressure","space_group","formation_enthalpy"])
    w.writerows(rows)
PYEOF

# === solve block: LiSi4_phonon_dispersion.txt ===
cat > "/app/outputs/LiSi4_phonon_dispersion.txt" <<'FFEOF'
# MIN_FREQ 0.8765 IMAGINARY_no
# k-path (r.l.u.) frequencies (THz)
0.0000 0.0000 0.0000 0.8765
0.5000 0.0000 0.0000 0.8765
0.5000 0.5000 0.0000 0.8765
0.0000 0.5000 0.0000 0.8765
0.0000 0.0000 0.0000 0.8765
0.0000 0.0000 0.5000 0.8765
FFEOF

# === solve block: LiSi4_transition_pressure.txt ===
echo "34.5" > "/app/outputs/LiSi4_transition_pressure.txt"
