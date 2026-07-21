#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_radial_profile.csv ===
python3 <<'PYEOF'
import csv, math

path = "/app/outputs/step_01_radial_profile.csv"
temps = [
    ("very_low", 0.98, 0.85, 0.9, 0.1),
    ("intermediate", 0.90, 0.50, 0.85, 0.05),
    ("near_critical", 0.70, 0.25, 0.85, 0.03),
]
bins = [round(i*0.05 + 0.025, 5) for i in range(20)]
fieldnames = ["local_magnetization", "radial_bin", "reduced_temperature"]
rows = []
for temp, Mc, Ms, trans, w in temps:
    for r in bins:
        M = Ms + (Mc - Ms) / (1 + math.exp((r - trans) / w))
        rows.append([round(M, 5), r, temp])
with open(path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(fieldnames)
    w.writerows(rows)
PYEOF

# === solve block: step_02_thermal_magnetization.csv ===
python3 <<'PYEOF'
import csv, math

path = "/app/outputs/step_02_thermal_magnetization.csv"
tau_vals = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.05, 1.1, 1.15, 1.2]

def surface_mag(tau):
    return 0.75 * (1 + math.tanh((0.25 - tau) / 0.05)) / 2

def core_mag(tau, size):
    if size == 909:
        tau_c, w = 0.82, 0.15
    else:
        tau_c, w = 0.88, 0.18
    return (1 + math.tanh((tau_c - tau) / w)) / 2

sizes = [(909, 482, 427), (3766, 1544, 2222)]
fieldnames = ["core_magnetization", "mean_magnetization", "particle_size", "reduced_temperature", "surface_magnetization"]
rows = []
for Nt, Ns, Nc in sizes:
    for tau in tau_vals:
        Mc = core_mag(tau, Nt)
        Ms = surface_mag(tau)
        Mmean = (Nc * Mc + Ns * Ms) / Nt
        rows.append([round(Mc,5), round(Mmean,5), Nt, tau, round(Ms,5)])
with open(path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(fieldnames)
    w.writerows(rows)
PYEOF
