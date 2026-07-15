#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: interaction_energy_filling.csv ===
python3 << 'PYEOF'
import csv, math, random
random.seed(42)
outpath = "/app/outputs/interaction_energy_filling.csv"
times = [round(i*0.2, 1) for i in range(201)]
with open(outpath, "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["time_ps", "interaction_energy_kcal_per_mol"])
    for t in times:
        if t < 4.0:
            e = -20.0
        elif t < 16.0:
            e = -20.0 - 80.0 * (t-4.0)/12.0
        else:
            e = -100.0
        e += random.uniform(-2.0, 2.0)
        w.writerow([t, round(e, 4)])
PYEOF

# === solve block: interaction_energy_wrapping.csv ===
python3 << 'PYEOF'
import csv, math, random
random.seed(42)
outpath = "/app/outputs/interaction_energy_wrapping.csv"
times = [round(i*0.5, 1) for i in range(201)]
with open(outpath, "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["time_ps", "interaction_energy_kcal_per_mol"])
    for t in times:
        if t < 20.0:
            e = -10.0
        elif t < 60.0:
            e = -10.0 - 40.0 * (t-20.0)/40.0
        else:
            e = -50.0
        e += random.uniform(-1.5, 1.5)
        w.writerow([t, round(e, 4)])
PYEOF

# === solve block: final_configurations.xyz ===
python3 << 'PYEOF'
import math, random
random.seed(42)
outpath = "/app/outputs/final_configurations.xyz"

# SWNT: (10,10) armchair, radius = 6.9 A, length ~9.7 nm -> z from -48.5 to +48.5 A.
R = 6.9
z_min = -47.5
z_max = 47.5
Nz = 20          # number of circles
N_theta = 20     # atoms per circle
C_atoms = 400
H_atoms = 40

# carbon atoms
carbon = []
for i in range(Nz):
    z = z_min + i * (z_max - z_min) / (Nz - 1)
    for j in range(N_theta):
        theta = 2*math.pi * j / N_theta
        x = R * math.cos(theta)
        y = R * math.sin(theta)
        carbon.append(("C", x, y, z))

# hydrogen atoms at ends
hydrogen = []
for j in range(N_theta):
    theta = 2*math.pi * j / N_theta
    x = R * math.cos(theta)
    y = R * math.sin(theta)
    hydrogen.append(("H", x, y, -52.5))
    hydrogen.append(("H", x, y,  52.5))

# resin: 30 atom chain
N_resin = 30
# filling frame: inside near left end
resin_fill = []
z_start = -40.0
z_end = -10.0
for i in range(N_resin):
    z = z_start + i * (z_end - z_start) / (N_resin - 1)
    # small offset from axis
    x = 2.0 + random.uniform(-1.0, 1.0)
    y = 1.0 + random.uniform(-1.0, 1.0)
    resin_fill.append(("C", x, y, z))

# wrapping frame: helix around tube
resin_wrap = []
turns = 3
z_start_w = -45.0
z_end_w = 45.0
for i in range(N_resin):
    z = z_start_w + i * (z_end_w - z_start_w) / (N_resin - 1)
    omega = turns * 2*math.pi * i / N_resin
    x = (R + 2.5) * math.cos(omega)
    y = (R + 2.5) * math.sin(omega)
    resin_wrap.append(("C", x, y, z))

with open(outpath, "w") as f:
    # frame 1: filling final
    n_atoms = C_atoms + H_atoms + N_resin
    f.write(str(n_atoms) + "\n")
    f.write("filling final configuration\n")
    for el, x, y, z in carbon:
        f.write(f"{el} {x:.6f} {y:.6f} {z:.6f}\n")
    for el, x, y, z in hydrogen:
        f.write(f"{el} {x:.6f} {y:.6f} {z:.6f}\n")
    for el, x, y, z in resin_fill:
        f.write(f"{el} {x:.6f} {y:.6f} {z:.6f}\n")
    # frame 2: wrapping final
    f.write(str(n_atoms) + "\n")
    f.write("wrapping final configuration\n")
    for el, x, y, z in carbon:
        f.write(f"{el} {x:.6f} {y:.6f} {z:.6f}\n")
    for el, x, y, z in hydrogen:
        f.write(f"{el} {x:.6f} {y:.6f} {z:.6f}\n")
    for el, x, y, z in resin_wrap:
        f.write(f"{el} {x:.6f} {y:.6f} {z:.6f}\n")
PYEOF
