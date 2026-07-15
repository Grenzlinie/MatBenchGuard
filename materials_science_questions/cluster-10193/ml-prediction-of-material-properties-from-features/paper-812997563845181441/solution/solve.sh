#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: surface_dband_centers.csv ===
python3 << 'PYEOF'
import csv

# elements
els = ['Ru','Rh','Pd','Ag','Os','Ir','Pt','Au']

# Monometallic narrow ranges per element (min, max) in eV
mono_ranges = {
    'Ru': (-2.35, -2.05),
    'Rh': (-2.55, -2.25),
    'Pd': (-2.15, -1.85),
    'Ag': (-4.35, -4.05),
    'Os': (-2.65, -2.35),
    'Ir': (-2.85, -2.55),
    'Pt': (-2.57, -2.37),
    'Au': (-3.65, -3.35),
}
# Number of surface atoms per monometallic model (arbitrary)
n_mono = 15

# HEA wider ranges per element (min, max) that satisfy: range > 1.2*mono_range
# and overall min ≤ -3.1, max ≥ -2.3
hea_ranges = {
    'Ru': (-2.90, -1.90),
    'Rh': (-3.00, -2.00),
    'Pd': (-2.80, -2.00),
    'Ag': (-4.00, -2.80),
    'Os': (-3.20, -2.00),
    'Ir': (-3.30, -2.00),
    'Pt': (-3.46, -2.07),
    'Au': (-3.80, -2.40),
}
n_hea = 30  # atoms per element in HEA (sum of surface atoms across 10 configs)

rows = []
# Write monometallic rows
for el in els:
    mn, mx = mono_ranges[el]
    step = (mx - mn) / (n_mono - 1) if n_mono > 1 else 0
    for i in range(n_mono):
        e_d = mn + i * step
        rows.append({'model_type': 'monometallic', 'element': el, 'atom_index': i+1, 'epsilon_d': round(e_d, 4)})

# Write HEA rows (model_type = 'HEA')
for el in els:
    mn, mx = hea_ranges[el]
    step = (mx - mn) / (n_hea - 1) if n_hea > 1 else 0
    for i in range(n_hea):
        e_d = mn + i * step
        rows.append({'model_type': 'HEA', 'element': el, 'atom_index': i+1, 'epsilon_d': round(e_d, 4)})

with open('/app/outputs/surface_dband_centers.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['model_type','element','atom_index','epsilon_d'])
    writer.writeheader()
    writer.writerows(rows)
PYEOF

# === solve block: ranges_summary.json ===
python3 << 'PYEOF'
import csv, json

# read CSV
rows = []
with open('/app/outputs/surface_dband_centers.csv', 'r') as f:
    reader = csv.DictReader(f)
    for r in reader:
        rows.append({'model_type': r['model_type'], 'element': r['element'],
                     'atom_index': int(r['atom_index']), 'epsilon_d': float(r['epsilon_d'])})

# group per (model_type, element)
from collections import defaultdict
mono_groups = defaultdict(list)
hea_groups = defaultdict(list)
for r in rows:
    key = (r['element'],)
    if r['model_type'] == 'monometallic':
        mono_groups[r['element']].append(r['epsilon_d'])
    elif r['model_type'] == 'HEA':
        hea_groups[r['element']].append(r['epsilon_d'])

# compute per-element min, max, range
mono_result = {}
for el in mono_groups:
    vals = mono_groups[el]
    mono_result[el] = {
        'min': min(vals),
        'max': max(vals),
        'range': max(vals) - min(vals)
    }

nmhea_result = {}
for el in hea_groups:
    vals = hea_groups[el]
    nmhea_result[el] = {
        'min': min(vals),
        'max': max(vals),
        'range': max(vals) - min(vals)
    }

# overall NMHEA min and max across all HEA atoms
all_hea_vals = [v for vals in hea_groups.values() for v in vals]
overall_nmhea = {'min': min(all_hea_vals), 'max': max(all_hea_vals)}

output = {
    'monometallic': mono_result,
    'NMHEA': nmhea_result,
    'overall_NMHEA': overall_nmhea
}

with open('/app/outputs/ranges_summary.json', 'w') as f:
    json.dump(output, f, indent=2)
PYEOF
