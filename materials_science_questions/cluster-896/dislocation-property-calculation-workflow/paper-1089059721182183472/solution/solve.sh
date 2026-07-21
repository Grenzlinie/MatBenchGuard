#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: strain_profiles.csv ===
python3 -c "
import math, csv

OUT = '/app/outputs/strain_profiles.csv'
times = [-3.4, 3.9]
A_th = 2.0e-4
A_exp_init = 1.7e-4
A_exp_final = 1.7e-4 * 0.65  # 35% reduction

with open(OUT, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['time','angle','theoretical_eps111','experimental_eps111'])
    for t in times:
        if t == -3.4:
            A_exp = A_exp_init
        else:
            A_exp = A_exp_final
        for i in range(360):
            ang = 2.0 * math.pi * i / 360.0
            th = A_th * math.sin(2.0 * ang)
            ex = A_exp * math.sin(2.0 * ang)
            w.writerow([t, ang, th, ex])
"

# === solve block: max_min_values.csv ===
python3 -c "
import csv, math

OUT = '/app/outputs/max_min_values.csv'
avg_factor = (2.0*math.sqrt(2))/math.pi  # average of sin(2θ) over π/4 window
A_th = 2.0e-4
max_th_avg = A_th * avg_factor
min_th_avg = -max_th_avg

init_amp = 1.7e-4
max_exp_init = init_amp * avg_factor
min_exp_init = -max_exp_init

final_amp = 1.7e-4 * 0.65
max_exp_final = final_amp * avg_factor
min_exp_final = -max_exp_final

with open(OUT, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['time','max_theoretical','min_theoretical','max_experimental','min_experimental'])
    w.writerow([-3.4, max_th_avg, min_th_avg, max_exp_init, min_exp_init])
    w.writerow([3.9, max_th_avg, min_th_avg, max_exp_final, min_exp_final])
"
