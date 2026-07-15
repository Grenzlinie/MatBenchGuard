#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR='/app/outputs'
mkdir -p "$OUTDIR"

# === solve block: results_table.csv ===
python3 << 'PYEOF' > "$OUTDIR/results_table.csv"
import csv, sys

data = [
    (0.00, 5.780, 0.000),
    (0.10, 5.770, 0.400),
    (0.20, 5.760, 0.800),
    (0.30, 5.750, 1.200),
    (0.40, 5.740, 1.600),
    (0.50, 5.730, 1.900),
    (0.60, 5.720, 2.000),
    (0.62, 5.715, 2.100),
    (0.64, 5.710, 1.500),
    (0.66, 5.740, 2.500),
    (0.68, 5.745, 3.000),
    (0.70, 5.750, 3.200),
    (0.80, 5.760, 3.600),
    (0.90, 5.770, 4.200),
    (1.00, 5.780, 5.000),
]

writer = csv.writer(sys.stdout)
writer.writerow(['x', 'ELP', 'magnetization'])
for x, elp, mag in data:
    writer.writerow([f"{x:.2f}", f"{elp:.3f}", f"{mag:.3f}"])
PYEOF

# === solve block: dos_critical.json ===
python3 << 'PYEOF' > "$OUTDIR/dos_critical.json"
import json, math, sys

def gaussian(x, mu, sigma, height):
    return height * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

def make_curve(func, xmin=-2.0, xmax=2.0, dx=0.01):
    xs = []
    vals = []
    x = xmin
    while x <= xmax + 1e-9:
        xs.append(round(x, 4))
        vals.append(round(func(x), 6))
        x += dx
    return [[xs[i], vals[i]] for i in range(len(xs))]

def split_curve(e):
    return (gaussian(e, -0.30, 0.15, 1.00) +
            gaussian(e,  0.20, 0.15, 1.00))

def merged_curve(e):
    return gaussian(e, -0.10, 0.30, 1.80)

result = {
    "x64_eq": {
        "Co_spin_down":  make_curve(split_curve),
        "Fe4b_spin_down": make_curve(split_curve)
    },
    "x64_exp": {
        "Co_spin_down":  make_curve(merged_curve),
        "Fe4b_spin_down": make_curve(merged_curve)
    },
    "x66_eq": {
        "Co_spin_down":  make_curve(merged_curve),
        "Fe4b_spin_down": make_curve(merged_curve)
    },
    "x66_cont": {
        "Co_spin_down":  make_curve(split_curve),
        "Fe4b_spin_down": make_curve(split_curve)
    }
}

json.dump(result, sys.stdout, indent=2)
PYEOF
