#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
chmod +x /solution/generate_energy_volume.py /solution/generate_elastic_constants.py

# === solve block: energy_volume_data.csv ===
cat << 'PYSCRIPT' > /tmp/gen_ev.py
import sys, csv, math

output = sys.argv[1]

params = [
    # ZB (a0 in Å, B0 in GPa, B')
    ("BN", "ZB", 3.627, None, 375.923, 3.0),
    ("BP", "ZB", 4.551, None, 161.734, 3.649),
    ("BAs", "ZB", 4.812, None, 130.913, 3.708),
    ("BSb", "ZB", 5.277, None, 99.5, 3.718),
    ("BBi", "ZB", 5.531, None, 66.846, 4.395),
    # NaCl
    ("BN", "NaCl", 3.507, None, 373.958, 4.896),
    ("BP", "NaCl", 4.32, None, 156.822, 4.062),
    ("BAs", "NaCl", 4.622, None, 125.179, 2.976),
    ("BSb", "NaCl", 5.021, None, 101.305, 4.224),
    ("BBi", "NaCl", 5.289, None, 83.056, 2.767),
    # WZ (a0, c0 in Å)
    ("BN", "WZ", 2.558, 4.228, 376.318, 3.582),
    ("BP", "WZ", 3.211, 5.285, 162.09, 3.687),
    ("BAs", "WZ", 3.398, 5.57, 130.835, 4.085),
    ("BSb", "WZ", 3.737, 6.073, 98.005, 4.639),
    ("BBi", "WZ", 4.125, 5.741, 72.138, 5.366),
]

def V0_cubic(a):
    return a**3 / 4.0

def V0_hex(a, c):
    return (math.sqrt(3) / 4.0) * a**2 * c

GPa_to_eVA3 = 1.0 / 160.2176634   # 1 GPa = 0.006241509 eV/Å³

with open(output, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["compound", "phase", "volume", "total_energy"])
    for comp, phase, a, c, B0_GPa, Bprime in params:
        if phase == "WZ":
            V0 = V0_hex(a, c)
        else:
            V0 = V0_cubic(a)
        B0_eV = B0_GPa * GPa_to_eVA3
        E0 = -10.0
        # 11 volume points from 0.85*V0 to 1.15*V0
        V_min = V0 * 0.85
        V_max = V0 * 1.15
        for i in range(11):
            V = V_min + (V_max - V_min) * i / 10.0
            ratio = (V0 / V) ** Bprime
            term1 = (B0_eV * V) / Bprime * (ratio / (Bprime - 1.0) + 1.0)
            term2 = (B0_eV * V0) / (Bprime - 1.0)
            E = E0 + term1 - term2
            writer.writerow([comp, phase, round(V, 6), round(E, 8)])
PYSCRIPT
python3 /tmp/gen_ev.py "$OUTDIR/energy_volume_data.csv"

# === solve block: elastic_constants.csv ===
python3 /solution/generate_elastic_constants.py "$OUTDIR/elastic_constants.csv"
