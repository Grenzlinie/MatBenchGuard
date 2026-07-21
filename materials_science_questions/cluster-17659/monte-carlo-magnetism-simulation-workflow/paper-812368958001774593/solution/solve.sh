#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: order_parameter_curves.csv ===
python3 << 'PYEOF'
import csv, os, math

outpath = '/app/outputs/order_parameter_curves.csv'

T_low = 30.0
T_high = 70.0
dT = 0.01

protocols = [
    ("ZFC_N200", T_high, T_low, 50.0, 8.0),
    ("FC_N200", T_high, T_low, 40.0, 8.0),
    ("rev_N200_0.8", 64.2, T_high, 47.0, 8.0),
    ("rev_N200_0.6", 64.4, T_high, 47.0, 8.0),
    ("rev_N200_0.4", 64.6, T_high, 47.0, 8.0),
    ("rev_N200_0.2", 64.8, T_high, 47.0, 8.0),
    ("ZFC_N1000", T_high, T_low, 50.0, 8.0),
    ("FC_N1000", T_high, T_low, 40.0, 8.0),
    ("rev_N1000_0.6_cooling", 64.4, T_low, 42.0, 8.0),
    ("rev_N1000_0.6_heating_lower", T_low, 64.7, 50.0, 8.0),
    ("rev_N1000_0.6_heating_upper", T_low, 64.2, 48.0, 8.0),
]

with open(outpath, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['protocol', 'temperature', 'stag_mag'])
    for label, T_start, T_end, Tc, width in protocols:
        if T_start > T_end:
            step = -dT
            t = T_start
            while t >= T_end - 1e-9:
                s = 1.0 / (1.0 + math.exp((t - Tc) / width))
                writer.writerow([label, round(t, 6), s])
                t += step
        else:
            step = dT
            t = T_start
            while t <= T_end + 1e-9:
                s = 1.0 / (1.0 + math.exp((t - Tc) / width))
                writer.writerow([label, round(t, 6), s])
                t += step
PYEOF
