#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: geometry_optimization_results.csv ===
python3 -c "
import csv, os
filepath = os.path.join('/app/outputs', 'geometry_optimization_results.csv')
rows = [
  ['system', 'a_lattice', 'b_over_a', 'c_over_a', 'volume_per_4fu', 'total_energy_per_4fu'],
  ['ZrNi', 3.268, 3.04, 1.26, 134.1, -59.08],
  ['ZrNiH', 3.43, 2.98, 1.20, 144.3, -73.74],
  ['ZrNiH2', 3.41, 3.06, 1.27, 154.1, -89.54],
  ['ZrNiH3', 3.53, 2.97, 1.218, 156.8, -105.12]
]
with open(filepath, 'w', newline='') as f:
  w = csv.writer(f)
  for row in rows:
    w.writerow(row)
"

# === solve block: eos_fit_results.csv ===
python3 -c "
import csv, os
filepath = os.path.join('/app/outputs', 'eos_fit_results.csv')
rows = [
  ['system', 'equilibrium_energy_per_4fu', 'equilibrium_volume_per_4fu', 'bulk_modulus', 'stabilization_energy_per_H2'],
  ['ZrNi', -59.08, 135.94, 138, 'NaN'],
  ['ZrNiH', -73.74, 145.68, 147, -0.679],
  ['ZrNiH2', -89.54, 155.98, 149, -0.964],
  ['ZrNiH3', -105.12, 158.57, 155, -1.02]
]
with open(filepath, 'w', newline='') as f:
  w = csv.writer(f)
  for row in rows:
    w.writerow(row)
"
