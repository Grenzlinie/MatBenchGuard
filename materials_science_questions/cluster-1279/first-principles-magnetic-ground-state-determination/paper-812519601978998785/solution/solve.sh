#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: magnetization_plateaus.csv ===
python3 - <<'SCRIPT'
import sys, csv

# fixed output path (no variable expansion)
outfile = '/app/outputs/magnetization_plateaus.csv'

# critical d_s thresholds from the paper
thresholds_r1_05 = [-23.2, -19.1, -14.7]
thresholds_r1_5  = [-77.3, -73.2, -32.8]

def mag_for(ds, thresholds):
    # plateau 1: both zero
    if ds < thresholds[0]:
        return 0.0, 0.0
    # plateau 2: spin states 0.33 / -0.33
    if ds < thresholds[1]:
        return 0.33, -0.33
    # plateau 3: spin states 1.0 / -1.0
    if ds < thresholds[2]:
        return 1.0, -1.0
    # plateau 4: spin states 2.0 / -2.0
    return 2.0, -2.0

# sweep d_s from -80 to 0 with step 0.1
ds_values = [round(x * 0.1, 1) for x in range(-800, 1)]
rows = []

for r1 in [0.5, 5.0]:
    thres = thresholds_r1_05 if r1 == 0.5 else thresholds_r1_5
    for ds in ds_values:
        mp, mm = mag_for(ds, thres)
        rows.append((r1, ds, mp, mm))

with open(outfile, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['R1', 'd_s', 'M_Mn_plus', 'M_Mn_minus'])
    w.writerows(rows)

print(f"Wrote {len(rows)} rows to {outfile}")
SCRIPT

# === solve block: critical_ds.txt ===
python3 /solution/write_all.py critical_ds.txt

# === solve block: rcp_vs_field.csv ===
python3 /solution/write_all.py rcp_vs_field.csv

# === solve block: rcp_vs_ds.csv ===
python3 /solution/write_all.py rcp_vs_ds.csv

# === solve block: rcp_vs_R1.csv ===
python3 /solution/write_all.py rcp_vs_R1.csv

# === solve block: rcp_vs_R2.csv ===
python3 /solution/write_all.py rcp_vs_R2.csv
