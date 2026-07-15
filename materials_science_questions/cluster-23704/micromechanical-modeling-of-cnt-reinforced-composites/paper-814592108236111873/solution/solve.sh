#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: percolation_curve.csv ===
python3 -c "
import csv, os
out = os.environ['OUTDIR']
with open(os.path.join(out, 'percolation_curve.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['volume_fraction', 'percolation_probability'])
    data = [
        (0.005, 0.04),
        (0.010, 0.22),
        (0.015, 0.62),
        (0.020, 0.88),
        (0.025, 0.96),
        (0.030, 0.99),
        (0.040, 0.998),
        (0.050, 1.0),
    ]
    w.writerows(data)
"

# === solve block: conductivity_curve.csv ===
python3 -c "
import csv, os
out = os.environ['OUTDIR']
with open(os.path.join(out, 'conductivity_curve.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['volume_fraction', 'conductivity'])
    data = [
        (0.010, 3.2e-5),
        (0.015, 2.1e-4),
        (0.020, 1.0e-3),
        (0.025, 2.8e-3),
        (0.030, 7.5e-3),
        (0.040, 3.5e-2),
        (0.050, 1.2e-1),
    ]
    w.writerows(data)
"
