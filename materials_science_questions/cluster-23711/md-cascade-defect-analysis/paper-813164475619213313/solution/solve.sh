#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_cascade_energies.csv ===
python3 <<PYEOF
import csv, math
out_path = '$OUTDIR/step_01_cascade_energies.csv'
with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['time_ps', 'kinetic_norm', 'potential_norm'])
    t_eq = 0.35
    for i in range(201):
        t = i * 0.01
        kin = 0.5 + 0.5 / (1 + math.exp((t - t_eq) / 0.05))
        pot = 1.0 - kin
        writer.writerow([f'{t:.6f}', f'{kin:.6f}', f'{pot:.6f}'])
PYEOF

# === solve block: step_02_thermal_spike_energies.csv ===
python3 /solution/generate_outputs.py step_02 > /app/outputs/step_02_thermal_spike_energies.csv

# === solve block: step_03_max_volume_vs_energy.csv ===
python3 /solution/generate_outputs.py step_03 > /app/outputs/step_03_max_volume_vs_energy.csv
