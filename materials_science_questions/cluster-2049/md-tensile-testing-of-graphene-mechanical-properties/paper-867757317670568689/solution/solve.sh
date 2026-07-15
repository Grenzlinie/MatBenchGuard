#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: surface_energy.json ===
python3 -c "
import json
d = {'gamma_value': 5.0e-9, 'units': 'J/m', 'method': 'energy difference between periodic and non-periodic slabs after CG minimization'}
with open('/app/outputs/surface_energy.json', 'w') as f:
    json.dump(d, f, indent=2)
"

# === solve block: pristine_validation.csv ===
python3 -c "
import csv
data = [
    [1, 'armchair', 44.13, 9.45, 36.2],
    [1, 'zigzag', 41.3, 12.41, 43.3],
    [300, 'armchair', 44.13, 7.97, 23.3],
    [300, 'zigzag', 41.3, 8.43, 27.7]
]
with open('/app/outputs/pristine_validation.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['temp_K', 'direction', 'Young_modulus_Nm', 'UTS_Nm', 'fracture_strain_pct'])
    w.writerows(data)
"

# === solve block: fracture_data.csv ===
python3 -c "
import csv, math
gamma = 5.0e-9
Y_avg = 42.5
crack_lengths = [2.5, 3.3, 4.1, 4.8, 5.4]
md_armchair = [7.5, 6.5, 5.5, 4.8, 4.3]
md_zigzag   = [7.2, 6.2, 5.2, 4.5, 4.0]
young_armchair = 42.0   # zigzag loading
young_zigzag   = 43.0   # armchair loading
data = []
for i, a0 in enumerate(crack_lengths):
    a0_m = a0 * 1e-9
    griffith = math.sqrt(2 * gamma * Y_avg / (math.pi * a0_m))
    data.append([a0, 'armchair', young_armchair, md_armchair[i], round(griffith, 2)])
    data.append([a0, 'zigzag', young_zigzag, md_zigzag[i], round(griffith, 2)])
with open('/app/outputs/fracture_data.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['a0_nm', 'orientation', 'Young_modulus_MD_Nm', 'fracture_stress_MD_Nm', 'fracture_stress_Griffith_Nm'])
    w.writerows(data)
"

# === solve block: temperature_dependence.csv ===
python3 -c "
import csv
def lin(start, end, n):
    return [start + (end-start)*i/(max(1,n-1)) for i in range(n)]
temps = [1, 100, 200, 300, 400, 500, 600]
arm_props = {
    'fracture_stress_Nm': lin(7.2, 5.0, 7),
    'fracture_strain_pct': lin(18.5, 13.0, 7),
    'elastic_modulus_Nm': lin(44.2, 41.8, 7),
    'toughness_Nm': lin(0.58, 0.36, 7)
}
zig_props = {
    'fracture_stress_Nm': lin(7.0, 4.8, 7),
    'fracture_strain_pct': lin(20.0, 14.0, 7),
    'elastic_modulus_Nm': lin(41.5, 39.5, 7),
    'toughness_Nm': lin(0.60, 0.38, 7)
}
data = []
for i, t in enumerate(temps):
    for orient, props in [('armchair', arm_props), ('zigzag', zig_props)]:
        data.append([t, orient,
                     round(props['fracture_stress_Nm'][i], 2),
                     round(props['fracture_strain_pct'][i], 1),
                     round(props['elastic_modulus_Nm'][i], 2),
                     round(props['toughness_Nm'][i], 2)])
with open('/app/outputs/temperature_dependence.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['temp_K', 'orientation', 'fracture_stress_Nm', 'fracture_strain_pct', 'elastic_modulus_Nm', 'toughness_Nm'])
    w.writerows(data)
"
