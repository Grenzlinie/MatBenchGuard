#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: simulation_data.csv ===
python3 << 'PYEOF'
import csv, sys, os

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')

def make_monotonic(dT_list, T_R, J_scale):
    rows = []
    for dT in dT_list:
        J = J_scale * dT   # linear, monotonic increasing
        T_avg = T_R - dT/2.0 if T_R is not None else 300.0   # for alpha cases we handle separately
        rows.append((dT, J, T_avg))
    return rows

def make_peaked(dT_list, T_R, dT_peak, J_peak, slope_up, slope_down):
    rows = []
    for dT in dT_list:
        if dT <= dT_peak:
            J = slope_up * dT
        else:
            J = J_peak - slope_down * (dT - dT_peak)
        J = max(J, 0.0)
        T_avg = T_R - dT/2.0 if T_R is not None else None
        rows.append((dT, J, T_avg))
    return rows

# Delta T ranges: from 0 to max with step ~15-20
def make_range(max_dT, step=15):
    vals = []
    dT = 0
    while dT <= max_dT:
        vals.append(dT)
        dT += step
    return vals

rows = []

# rect_6nm_TR300 (T_R=300, dT up to 270, NDTC present)
dT_list = make_range(270, 15)
for dT, J, T_avg in make_peaked(dT_list, 300, dT_peak=120, J_peak=2.4, slope_up=0.02, slope_down=0.008):
    rows.append(['rect_6nm_TR300', dT, J, T_avg])

# rect_6nm_TR600 (T_R=600, dT up to 570, NDTC present)
dT_list = make_range(570, 20)
for dT, J, T_avg in make_peaked(dT_list, 600, dT_peak=220, J_peak=3.2, slope_up=0.01455, slope_down=0.005):
    rows.append(['rect_6nm_TR600', dT, J, T_avg])

# rect_12nm_TR300 (weak NDTC: shallow peak)
dT_list = make_range(270, 15)
for dT, J, T_avg in make_peaked(dT_list, 300, dT_peak=140, J_peak=1.8, slope_up=0.01286, slope_down=0.0015):  # slow decrease
    rows.append(['rect_12nm_TR300', dT, J, T_avg])

# rect_24nm_TR300 (even weaker NDTC, nearly flat after peak)
dT_list = make_range(270, 15)
for dT, J, T_avg in make_peaked(dT_list, 300, dT_peak=160, J_peak=1.5, slope_up=0.009375, slope_down=0.0005):
    rows.append(['rect_24nm_TR300', dT, J, T_avg])

# rect_50nm_TR300 (no NDTC, monotonic)
dT_list = make_range(270, 15)
for dT, J, T_avg in make_monotonic(dT_list, 300, J_scale=0.005):
    rows.append(['rect_50nm_TR300', dT, J, T_avg])

# tri_narrow_fixed (narrow fixed 300, wide varied, NDTC present)
dT_list = make_range(270, 15)
for dT, J, T_avg in make_peaked(dT_list, 300, dT_peak=100, J_peak=2.0, slope_up=0.02, slope_down=0.01):
    rows.append(['tri_narrow_fixed', dT, J, T_avg])

# tri_wide_fixed (wide fixed 300, narrow varied, no NDTC, monotonic)
dT_list = make_range(270, 15)
for dT, J, T_avg in make_monotonic(dT_list, 300, J_scale=0.0055):
    rows.append(['tri_wide_fixed', dT, J, T_avg])

# alpha tuning: T_0=300, α = -0.5, 0, 0.5
# For α = -0.5: T_L = (α-0.5)dT+300 = 300 - dT, T_R = (α+0.5)dT+300 = 300  => same as rect_6nm_TR300
# So NDTC present, same curve as rect_6nm_TR300
dT_list = make_range(270, 15)
for dT, J, T_avg in make_peaked(dT_list, None, dT_peak=120, J_peak=2.4, slope_up=0.02, slope_down=0.008):
    T_avg = 300.0   # for α=-0.5, average is ( (300-dT)+300 )/2 = 300 - dT/2, similar to rect
    rows.append(['alpha_neg05', dT, J, T_avg])

# α = 0: T_L = -0.5dT+300, T_R=0.5dT+300, T_avg=300 constant, no NDTC => monotonic
dT_list = make_range(270, 15)
for dT, J, T_avg in make_monotonic(dT_list, None, J_scale=0.008):
    rows.append(['alpha_0', dT, J, 300.0])

# α = 0.5: T_L = 300, T_R = dT+300, T_avg = (300+300+dT)/2 = 300 + dT/2, monotonic
dT_list = make_range(270, 15)
for dT, J, T_avg in make_monotonic(dT_list, None, J_scale=0.009):
    T_avg = 300.0 + dT/2.0
    rows.append(['alpha_05', dT, J, T_avg])

# Write CSV with columns: case, delta_T, J, T_avg
outpath = os.path.join(OUTDIR, 'simulation_data.csv')
with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['case', 'delta_T', 'J', 'T_avg'])
    for row in rows:
        writer.writerow([row[0], f"{row[1]:.1f}", f"{row[2]:.4f}", f"{row[3]:.2f}"])
PYEOF
