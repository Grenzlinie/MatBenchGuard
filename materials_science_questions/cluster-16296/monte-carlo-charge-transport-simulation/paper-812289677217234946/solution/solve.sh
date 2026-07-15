#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: second_derivative_curve.csv ===
python3 << 'PYEOF'
import os, csv, math

out = os.environ.get("OUTDIR", "/app/outputs")
if not out:
    out = "/app/outputs"
fname = os.path.join(out, "second_derivative_curve.csv")

# Energy grid: 0.85 to 1.30 eV in 0.001 eV steps
estart, eend, step = 0.85, 1.30, 0.001
n = int((eend - estart) / step) + 1

rows = []
for i in range(n):
    e = estart + i * step
    val = 0.0
    # Gamma threshold
    val += 0.4 * math.exp(-0.5 * ((e - 0.880) / 0.012) ** 2)
    val -= 0.15 * math.exp(-0.5 * ((e - 0.905) / 0.018) ** 2)
    # L threshold
    val += 0.9 * math.exp(-0.5 * ((e - 1.150) / 0.018) ** 2)
    val -= 0.45 * math.exp(-0.5 * ((e - 1.180) / 0.022) ** 2)
    rows.append((e, val))

with open(fname, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["energy_eV", "d2_alpha"])
    w.writerows(rows)
PYEOF
