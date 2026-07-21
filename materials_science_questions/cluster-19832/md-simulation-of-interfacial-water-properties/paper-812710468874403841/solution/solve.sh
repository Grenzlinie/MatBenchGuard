#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: surface_excess_properties.csv ===
python3 -c '
import csv

T = 300.0

# (x_M, gamma [mN/m], u_s [kJ/m^2], outermost_x_M)
rows_raw = [
    (0.0,   50.0, 0.08,  0.0),
    (0.045, 42.0, 0.07,  0.95),
    (0.089, 37.0, 0.062, 0.91),
    (0.195, 30.0, 0.05,  0.88),
    (0.275, 28.0, 0.042, 0.85),
    (0.320, 27.0, 0.041, 0.83),
    (0.468, 28.0, 0.045, 0.81),
    (0.747, 29.0, 0.042, 0.80),
    (1.0,   30.0, 0.04,  1.0),
]

# get pure-ends for mixing excess
x_0, g_0, u_0, ox_0 = rows_raw[0]
s_0 = (u_0 - g_0 * 1e-6) / T
x_1, g_1, u_1, ox_1 = rows_raw[-1]
s_1 = (u_1 - g_1 * 1e-6) / T

out = []
for x, gamma, u_s, ox in rows_raw:
    s_s = (u_s - gamma * 1e-6) / T
    ideal_u = (1 - x) * u_0 + x * u_1
    ideal_s = (1 - x) * s_0 + x * s_1
    delta_u = u_s - ideal_u
    delta_s = s_s - ideal_s
    out.append([x, gamma, u_s, s_s, delta_u, delta_s, ox])

with open("/app/outputs/surface_excess_properties.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["x_M", "gamma (mN/m)", "u_s (kJ/m^2)", "s_s (kJ/(m^2*K))", "Delta_u_s (kJ/m^2)", "Delta_s_s (kJ/(m^2*K))", "outermost_x_M"])
    for row in out:
        w.writerow(row)
'
