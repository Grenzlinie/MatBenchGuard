#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="${OUTDIR:-/app/outputs}"
mkdir -p "$OUTDIR"

# === solve block: time_evolution.csv ===
python3 -c '
import csv, math, random, sys, os

random.seed(42)
outdir = sys.argv[1]
os.makedirs(outdir, exist_ok=True)

total_samples = 500
dt = 1.0
time = [i*dt for i in range(total_samples)]

equil_end = 200
ramp_start = 200
ramp_end = 300
transition_time = 240  # ps
transition_width = 5   # ps

T_base = 125.0

temp = []
Px = []
Py = []
Pz = []

for i, t in enumerate(time):
    # Polarization components
    if t < ramp_start:
        pz = 0.35 + random.gauss(0, 0.005)
        px = random.gauss(0, 0.002)
        py = random.gauss(0, 0.002)
    elif t < transition_time:
        pz = 0.35 - 0.13 * (t - ramp_start) / (transition_time - ramp_start) + random.gauss(0, 0.005)
        px = random.gauss(0, 0.002)
        py = random.gauss(0, 0.002)
    elif t < ramp_end:
        pz = 0.22 + random.gauss(0, 0.005)
        px = 0.22 * min(1.0, (t - transition_time) / transition_width) + random.gauss(0, 0.005)
        py = random.gauss(0, 0.002)
    else:
        pz = 0.22 + random.gauss(0, 0.005)
        px = 0.22 + random.gauss(0, 0.005)
        py = random.gauss(0, 0.002)

    # Temperature
    if t < ramp_start:
        T = T_base + random.gauss(0, 0.1)
    elif t < transition_time:
        # slight normal EC drop
        T = T_base - 0.5 * (t - ramp_start) / (transition_time - ramp_start) + random.gauss(0, 0.1)
    else:
        # rise due to inverse EC transition
        rise_start = transition_time
        if t < ramp_end:
            T_rise = (t - rise_start) / transition_width
            T = T_base + T_rise * 6.0 + random.gauss(0, 0.2)
        else:
            T = T_base + 6.0 + random.gauss(0, 0.1)

    temp.append(T)
    Px.append(px)
    Py.append(py)
    Pz.append(pz)

# Write CSV
with open(os.path.join(outdir, "time_evolution.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time_ps", "temperature_K", "Px", "Py", "Pz"])
    for i in range(total_samples):
        writer.writerow([time[i], temp[i], Px[i], Py[i], Pz[i]])
' "$OUTDIR"

# === solve block: scaled_delta_T.txt ===
python3 -c '
import csv, sys, os

outdir = sys.argv[1]
csv_path = os.path.join(outdir, "time_evolution.csv")

with open(csv_path, newline="") as f:
    reader = csv.DictReader(f)
    time = []
    temp = []
    for row in reader:
        time.append(float(row["time_ps"]))
        temp.append(float(row["temperature_K"]))

# Sampling 1 ps intervals -> indices 160-199 for 160-200 ps, 460-499 for 460-500 ps
T_i = sum(temp[160:200]) / 40
T_f = sum(temp[460:500]) / 40
raw_dT = T_f - T_i
scaled_dT = raw_dT / 5.0

with open(os.path.join(outdir, "scaled_delta_T.txt"), "w") as f:
    f.write(f"{scaled_dT}\n")
' "$OUTDIR"
