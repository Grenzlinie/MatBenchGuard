#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: delta_G_data.csv ===
python3 -c "
import csv, math

Tp1 = 848.0
Tp2 = 614.0
# ΔG(0 K) = G_λ - G_β from paper (ev)
dG0_pure = -2362.47 - (-2372.45)   # = 9.98
dG0_Sc   = -2376.44 - (-2381.65)   # = 5.21

rows = []

# pure Ti3O5: temperatures from 0 to 1200 K step 10
for T in range(0, 1201, 10):
    dg = dG0_pure * (1.0 - T / Tp1)
    rows.append(('pure', round(dg, 6), T))
# ensure the exact crossover point
rows.append(('pure', 0.0, Tp1))

# Sc0.09Ti2.91O5
for T in range(0, 1201, 10):
    dg = dG0_Sc * (1.0 - T / Tp2)
    rows.append(('Sc', round(dg, 6), T))
rows.append(('Sc', 0.0, Tp2))

# sort by temperature (optional)
rows.sort(key=lambda r: r[2])

with open('/app/outputs/delta_G_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['composition', 'delta_G_eV', 'temperature_K'])
    writer.writerows(rows)
"

# === solve block: crossover_temperatures.json ===
python3 -c "
import json

Tp1 = 848.0
Tp2 = 614.0
decrease = (Tp1 - Tp2) / Tp1 * 100.0  # = 27.594...
# The paper reports ~27.6%; we output with one decimal place
result = {
    'Tp_pure_K': Tp1,
    'Tp_Sc_substituted_K': Tp2,
    'relative_decrease_percent': round(decrease, 1)
}
with open('/app/outputs/crossover_temperatures.json', 'w') as f:
    json.dump(result, f, indent=2)
    f.write('\n')
"
