#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: defect_formation_energy_difference.csv ===
python3 << 'PYEOF'
import csv
pressures = [25, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]
concentrations = ['283_ppb', '732_ppm']
a283, b283 = -0.015, 0.3
a732, b732 = -0.02, 0.2
with open('/app/outputs/defect_formation_energy_difference.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['pressure_GPa', 'concentration', 'delta_G_eV'])
    for p in pressures:
        writer.writerow([p, '283_ppb', round(a283 * p + b283, 6)])
        writer.writerow([p, '732_ppm', round(a732 * p + b732, 6)])
PYEOF

# === solve block: hafnium_partition_coefficient.csv ===
python3 << 'PYEOF'
import csv
data = [
    (31, 3000, 0.56),
    (50, 3000, 0.76),
    (93, 3000, 1.41),
    (129, 3000, 2.01),
    (31, 4000, 0.40),
    (58, 4000, 0.64),
    (101, 4000, 1.14),
    (140, 4000, 1.21),
    (66, 5000, 0.47),
    (109, 5000, 0.92),
    (144, 5000, 1.20),
]
with open('/app/outputs/hafnium_partition_coefficient.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['pressure_GPa', 'temperature_K', 'D_Hf'])
    for p, T, log10 in data:
        writer.writerow([p, T, round(10**log10, 6)])
PYEOF

# === solve block: tungsten_anomaly_evolution.csv ===
python3 << 'PYEOF'
import csv, math
t_i = 50.0
tau = 390.0
max_solid = 18.0
max_liquid = -14.0
t_vals = list(range(0, 4501, 50))
with open('/app/outputs/tungsten_anomaly_evolution.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time_Myr', 'mu182W_solid_ppm', 'mu182W_liquid_ppm'])
    for t in t_vals:
        if t <= t_i:
            frac = t / t_i
            solid = max_solid * frac
            liquid = max_liquid * frac
        else:
            solid = max_solid * math.exp(-(t - t_i) / tau)
            liquid = max_liquid
        writer.writerow([t, round(solid, 6), round(liquid, 6)])
PYEOF
