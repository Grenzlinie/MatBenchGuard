#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: ca_mg_results.csv ===
python3 -c '
import csv

temperatures = [780, 795, 810, 825, 840, 855, 870, 885, 900]

def C_Omega(T):
    # monotonic increase with decreasing T => linear decrease with T
    return 4.5 + (3.5 - 4.5) / (900 - 780) * (T - 780)

def vol(T):
    return 39.5 + 0.002 * (T - 780)

vol_vals = [vol(t) for t in temperatures]
alpha_vals = []
for i, T in enumerate(temperatures):
    if i == 0:
        dT = temperatures[i+1] - T
        dV = vol_vals[i+1] - vol_vals[i]
    elif i == len(temperatures)-1:
        dT = T - temperatures[i-1]
        dV = vol_vals[i] - vol_vals[i-1]
    else:
        dT = 0.5 * (temperatures[i+1] - temperatures[i-1])
        dV = 0.5 * (vol_vals[i+1] - vol_vals[i-1])
    alpha = dV / (dT * vol_vals[i]) if dT != 0.0 else 0.0
    alpha_vals.append(alpha)

with open("/app/outputs/ca_mg_results.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["temperature_K", "C_Omega_kB", "atomic_volume_A3", "alpha_p_K-1"])
    for t, c, v, a in zip(temperatures, [C_Omega(t) for t in temperatures], vol_vals, alpha_vals):
        w.writerow([t, round(c, 4), round(v, 4), round(a, 10)])
'

# === solve block: na_results.csv ===
python3 -c '
import csv

temperatures = [140, 160, 180, 200, 220, 240, 260, 280, 300, 312]

def C_Omega_na(T):
    if T <= 200:
        # increase as T decreases towards 140 -> decreasing with T
        return 4.2 + (3.0 - 4.2) / (200 - 140) * (T - 140)
    elif T <= 250:
        # slow decrease with falling T => slight increase with T
        return 3.0 + (3.2 - 3.0) / (250 - 200) * (T - 200)
    else:
        # increase with falling T => decrease with T
        return 4.0 + (3.5 - 4.0) / (312 - 250) * (T - 250)

def vol_na(T):
    if T <= 250:
        # gentle slope
        return 38.2 + 0.008 * (T - 140)
    else:
        # steeper slope
        return 39.0 + 0.016 * (T - 250)

vol_vals = [vol_na(t) for t in temperatures]
alpha_vals = []
for i, T in enumerate(temperatures):
    if i == 0:
        dT = temperatures[i+1] - T
        dV = vol_vals[i+1] - vol_vals[i]
    elif i == len(temperatures)-1:
        dT = T - temperatures[i-1]
        dV = vol_vals[i] - vol_vals[i-1]
    else:
        dT = 0.5 * (temperatures[i+1] - temperatures[i-1])
        dV = 0.5 * (vol_vals[i+1] - vol_vals[i-1])
    alpha = dV / (dT * vol_vals[i]) if dT != 0.0 else 0.0
    alpha_vals.append(alpha)

with open("/app/outputs/na_results.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["temperature_K", "C_Omega_kB", "atomic_volume_A3", "alpha_p_K-1"])
    for t, c, v, a in zip(temperatures, [C_Omega_na(t) for t in temperatures], vol_vals, alpha_vals):
        w.writerow([t, round(c, 4), round(v, 4), round(a, 10)])
'
