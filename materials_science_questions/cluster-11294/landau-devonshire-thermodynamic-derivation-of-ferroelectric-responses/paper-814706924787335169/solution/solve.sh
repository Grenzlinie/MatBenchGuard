#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: epsilon_vs_field.csv ===
python3 -c '
import csv, math
fields = [-4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
epsilon0 = 8.85e-12
Q13 = -0.0431
d31 = -274e-12
s11E = 8.33e-12
epsilon3_0 = 5554

with open("/app/outputs/epsilon_vs_field.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["E_kV_per_cm", "epsilon_3"])
    for E_kv in fields:
        E = E_kv * 1e5  # convert kV/cm to V/m
        denom = -3 * epsilon0 * Q13 * d31 * E / s11E + 1.0 / (epsilon3_0 - 1.0)
        eps = 1.0 / denom + 1.0
        writer.writerow([E_kv, eps])
'
