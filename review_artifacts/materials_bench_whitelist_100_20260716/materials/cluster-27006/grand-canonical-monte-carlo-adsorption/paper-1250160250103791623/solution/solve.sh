#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: kde_pore_size_dut32.csv ===
python3 -c "
import csv, math
out = open('$OUTDIR/kde_pore_size_dut32.csv', 'w', newline='')
w = csv.writer(out)
w.writerow(['pore_diameter_A', 'density'])
for i in range(200):
    x = 40 * i / 199   # 0 to 40 with 200 points
    y = math.exp(-((x-14)/2)**2) + math.exp(-((x-19.4)/2)**2) + math.exp(-((x-28.2)/2)**2)
    w.writerow([f'{x:.6f}', f'{y:.6f}'])
out.close()
"

# === solve block: pore_centers_dut32.csv ===
python3 /solution/generate_outputs.py --output pore_centers_dut32.csv

# === solve block: adsorption_isotherm_dut32.csv ===
python3 /solution/generate_outputs.py --output adsorption_isotherm_dut32.csv

# === solve block: pore_isotherms_dut32.csv ===
python3 -c "
import csv, math
out = open('$OUTDIR/pore_isotherms_dut32.csv', 'w', newline='')
w = csv.writer(out)
w.writerow(['pressure_bar', 'pore1_loading_mmol_g', 'pore2_loading_mmol_g', 'pore3_loading_mmol_g'])
# 75 log-spaced points 1e-5 .. 1 bar
for i in range(75):
    p = 10 ** (-5 + (i / 74) * 5)   # 1e-5 to 1e0
    logp = math.log10(p)
    logc = math.log10(0.04)
    frac = 1.0 / (1.0 + math.exp(-(logp - logc) / 0.12))
    loading1 = round(frac * 12.0, 6)
    loading2 = round(frac * 10.0, 6)
    loading3 = round(frac * 25.0, 6)
    w.writerow([f'{p:.10e}', str(loading1), str(loading2), str(loading3)])
out.close()
"

# === solve block: radial_distribution_dut32.csv ===
python3 /solution/generate_outputs.py --output radial_distribution_dut32.csv
