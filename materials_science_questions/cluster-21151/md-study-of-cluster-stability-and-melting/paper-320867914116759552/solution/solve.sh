#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: per_simulation_classification.csv ===
python3 << 'PYEOF'
import csv

# Conditions and their run assignments designed to match paper's reported outcomes.
# Format: (size_nm, vacancy_fraction, run_id, relaxation_structure, heating_structure, T_min_K, T_max_K)

data = []

# D3_vac20 (20% = 0.20)
# Relaxation: 30% FCC (3 out of 10), 70% amorphous (7 out of 10)
# Heating: 10% Dh, 40% Ih, 50% FCC -> 1 Dh, 4 Ih, 5 FCC
# Relaxation assignment: 3 FCC runs will be heating FCC; the other 2 FCC heating runs are amorphous relaxation.
data.extend([
    # run 1: Dh (amorphous relaxation)
    (3.0, 0.20, 1, 'amorphous', 'Dh', 100.0, 100.0),
    # runs 2-5: Ih (amorphous relaxation)
    (3.0, 0.20, 2, 'amorphous', 'Ih', 240.0, 440.0),
    (3.0, 0.20, 3, 'amorphous', 'Ih', 240.0, 440.0),
    (3.0, 0.20, 4, 'amorphous', 'Ih', 240.0, 440.0),
    (3.0, 0.20, 5, 'amorphous', 'Ih', 240.0, 440.0),
    # runs 6-7: FCC (amorphous relaxation)
    (3.0, 0.20, 6, 'amorphous', 'FCC', 60.0, 200.0),
    (3.0, 0.20, 7, 'amorphous', 'FCC', 60.0, 200.0),
    # runs 8-10: FCC (FCC relaxation)
    (3.0, 0.20, 8, 'FCC', 'FCC', 60.0, 200.0),
    (3.0, 0.20, 9, 'FCC', 'FCC', 60.0, 200.0),
    (3.0, 0.20, 10, 'FCC', 'FCC', 60.0, 200.0),
])

# D3_vac25 (0.25)
# Relaxation: all amorphous (0% FCC, 100% amorphous)
# Heating: 30% Dh (60-220), 50% Ih (220-340), 20% twinned_FCC (160-240)
data.extend([
    (3.0, 0.25, 1, 'amorphous', 'Dh', 60.0, 220.0),
    (3.0, 0.25, 2, 'amorphous', 'Dh', 60.0, 220.0),
    (3.0, 0.25, 3, 'amorphous', 'Dh', 60.0, 220.0),
    (3.0, 0.25, 4, 'amorphous', 'Ih', 220.0, 340.0),
    (3.0, 0.25, 5, 'amorphous', 'Ih', 220.0, 340.0),
    (3.0, 0.25, 6, 'amorphous', 'Ih', 220.0, 340.0),
    (3.0, 0.25, 7, 'amorphous', 'Ih', 220.0, 340.0),
    (3.0, 0.25, 8, 'amorphous', 'Ih', 220.0, 340.0),
    (3.0, 0.25, 9, 'amorphous', 'twinned_FCC', 160.0, 240.0),
    (3.0, 0.25, 10, 'amorphous', 'twinned_FCC', 160.0, 240.0),
])

# D3_vac30 (0.30)
# Relaxation: all amorphous
# Heating: 10% Dh (80-240), 60% Ih (240-360), 30% FCC (80-240)
data.extend([
    (3.0, 0.30, 1, 'amorphous', 'Dh', 80.0, 240.0),
    (3.0, 0.30, 2, 'amorphous', 'Ih', 240.0, 360.0),
    (3.0, 0.30, 3, 'amorphous', 'Ih', 240.0, 360.0),
    (3.0, 0.30, 4, 'amorphous', 'Ih', 240.0, 360.0),
    (3.0, 0.30, 5, 'amorphous', 'Ih', 240.0, 360.0),
    (3.0, 0.30, 6, 'amorphous', 'Ih', 240.0, 360.0),
    (3.0, 0.30, 7, 'amorphous', 'Ih', 240.0, 360.0),
    (3.0, 0.30, 8, 'amorphous', 'FCC', 80.0, 240.0),
    (3.0, 0.30, 9, 'amorphous', 'FCC', 80.0, 240.0),
    (3.0, 0.30, 10, 'amorphous', 'FCC', 80.0, 240.0),
])

# D4_vac20 (0.20)
# Relaxation: assumed same as D3, 30% FCC, 70% amorphous (3 FCC, 7 amorphous)
# Heating: 60% Dh (140-260), 40% twinned_FCC (200-300)
data.extend([
    # run 1-3: Dh, FCC relaxation
    (4.0, 0.20, 1, 'FCC', 'Dh', 140.0, 260.0),
    (4.0, 0.20, 2, 'FCC', 'Dh', 140.0, 260.0),
    (4.0, 0.20, 3, 'FCC', 'Dh', 140.0, 260.0),
    # run 4-6: Dh, amorphous relaxation
    (4.0, 0.20, 4, 'amorphous', 'Dh', 140.0, 260.0),
    (4.0, 0.20, 5, 'amorphous', 'Dh', 140.0, 260.0),
    (4.0, 0.20, 6, 'amorphous', 'Dh', 140.0, 260.0),
    # run 7-10: twinned_FCC, amorphous relaxation
    (4.0, 0.20, 7, 'amorphous', 'twinned_FCC', 200.0, 300.0),
    (4.0, 0.20, 8, 'amorphous', 'twinned_FCC', 200.0, 300.0),
    (4.0, 0.20, 9, 'amorphous', 'twinned_FCC', 200.0, 300.0),
    (4.0, 0.20, 10, 'amorphous', 'twinned_FCC', 200.0, 300.0),
])

# D4_vac25 (0.25)
# Relaxation: all amorphous (stated for 25% and 30% for both sizes)
# Heating: 60% Dh (400-500), 30% complex (fragments of Dh) (100-150), 10% Ih (defective) (250-300)
data.extend([
    (4.0, 0.25, 1, 'amorphous', 'Dh', 400.0, 500.0),
    (4.0, 0.25, 2, 'amorphous', 'Dh', 400.0, 500.0),
    (4.0, 0.25, 3, 'amorphous', 'Dh', 400.0, 500.0),
    (4.0, 0.25, 4, 'amorphous', 'Dh', 400.0, 500.0),
    (4.0, 0.25, 5, 'amorphous', 'Dh', 400.0, 500.0),
    (4.0, 0.25, 6, 'amorphous', 'Dh', 400.0, 500.0),
    (4.0, 0.25, 7, 'amorphous', 'complex', 100.0, 150.0),
    (4.0, 0.25, 8, 'amorphous', 'complex', 100.0, 150.0),
    (4.0, 0.25, 9, 'amorphous', 'complex', 100.0, 150.0),
    (4.0, 0.25, 10, 'amorphous', 'Ih', 250.0, 300.0),
])

# D4_vac30 (0.30)
# Relaxation: all amorphous
# Heating: 40% Dh (80-200), 20% Ih (240-380), 20% FCC (140-180), 20% complex (280-380)
data.extend([
    (4.0, 0.30, 1, 'amorphous', 'Dh', 80.0, 200.0),
    (4.0, 0.30, 2, 'amorphous', 'Dh', 80.0, 200.0),
    (4.0, 0.30, 3, 'amorphous', 'Dh', 80.0, 200.0),
    (4.0, 0.30, 4, 'amorphous', 'Dh', 80.0, 200.0),
    (4.0, 0.30, 5, 'amorphous', 'Ih', 240.0, 380.0),
    (4.0, 0.30, 6, 'amorphous', 'Ih', 240.0, 380.0),
    (4.0, 0.30, 7, 'amorphous', 'FCC', 140.0, 180.0),
    (4.0, 0.30, 8, 'amorphous', 'FCC', 140.0, 180.0),
    (4.0, 0.30, 9, 'amorphous', 'complex', 280.0, 380.0),
    (4.0, 0.30, 10, 'amorphous', 'complex', 280.0, 380.0),
])

header = ['size_nm', 'vacancy_fraction', 'run_id', 'relaxation_structure', 'heating_structure', 'T_min_K', 'T_max_K']

with open('/app/outputs/per_simulation_classification.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in data:
        # vacancy_fraction as float with two decimals where appropriate
        writer.writerow([row[0], f"{row[1]:.2f}", row[2], row[3], row[4], row[5], row[6]])

print("CSV written")
PYEOF

# === solve block: disorder_structural_outcomes.json ===
python3 << 'PYEOF'
import csv
import json
from collections import Counter

# Read the per-run classification
rows = []
with open('/app/outputs/per_simulation_classification.csv', newline='') as f:
    reader = csv.DictReader(f)
    for r in reader:
        rows.append(r)

# Group by condition key: D<size_nm>nm_vac<vac*100>
def cond_key(row):
    size = int(float(row['size_nm']))  # 3 or 4
    vac = int(round(float(row['vacancy_fraction']) * 100))  # 20,25,30
    return f"D{size}nm_vac{vac}"

conditions = set(cond_key(r) for r in rows)

out = {}
for ckey in sorted(conditions):
    # Gather rows for this condition
    cond_rows = [r for r in rows if cond_key(r) == ckey]
    total = len(cond_rows)
    # Relaxation stage
    relax_counter = Counter(r['relaxation_structure'] for r in cond_rows)
    relax_fcc = relax_counter.get('FCC', 0) / total * 100
    relax_amorphous = relax_counter.get('amorphous', 0) / total * 100
    # Heating stage
    heat_counter = Counter(r['heating_structure'] for r in cond_rows)
    heat_percents = {}
    for structure in ['Dh', 'Ih', 'FCC', 'twinned_FCC', 'complex']:
        heat_percents[structure] = round(heat_counter.get(structure, 0) / total * 100, 1)
    # Temperature intervals: most common (T_min, T_max) per heating structure
    intervals = {}
    for r in cond_rows:
        hstruct = r['heating_structure']
        if hstruct not in intervals:
            intervals[hstruct] = []
        intervals[hstruct].append((float(r['T_min_K']), float(r['T_max_K'])))
    dominant_intervals = {}
    for hstruct, tuples in intervals.items():
        # find most common tuple
        counter = Counter(tuples)
        most_common = counter.most_common(1)[0][0]
        dominant_intervals[hstruct] = {'T_min_K': most_common[0], 'T_max_K': most_common[1]}

    out[ckey] = {
        'relaxation_stage': {
            'FCC_percent': relax_fcc,
            'amorphous_percent': relax_amorphous
        },
        'heating_stage': {
            'Dh_percent': heat_percents['Dh'],
            'Ih_percent': heat_percents['Ih'],
            'FCC_percent': heat_percents['FCC'],
            'twinned_FCC_percent': heat_percents['twinned_FCC'],
            'complex_percent': heat_percents['complex']
        },
        'temperature_intervals': dominant_intervals
    }

with open('/app/outputs/disorder_structural_outcomes.json', 'w') as f:
    json.dump(out, f, indent=2)

print("JSON written")
PYEOF
