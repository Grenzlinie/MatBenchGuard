#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "/app/outputs"

# === solve block: gamma_vs_volume.csv ===
python3 -c "
import csv, math

N = 10
prefactor = (2 * N + 1) / (3 * N)            # (2*10+1)/(3*10) = 21/30 = 0.7

rows = []
ratio = 1.0
while ratio >= 0.94999999999:                 # include 0.95, safe floating-point gate
    v0v_sq = ratio ** 2
    gamma1 = (22 * v0v_sq - 5) / (11 * v0v_sq - 5) + 1.0/3.0
    gamma   = prefactor * gamma1
    rows.append((ratio, gamma1, gamma))
    ratio = round(ratio - 0.01, 10)

rows.sort(key=lambda x: -x[0])                # ensure descending order

with open('/app/outputs/gamma_vs_volume.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['volume_ratio', 'gamma1', 'gamma'])
    for r in rows:
        w.writerow(r)
"
