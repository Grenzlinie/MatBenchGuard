#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: g_factors.csv ===
python3 -c "
import csv
data = [
    (1, 2.612, 2.341, -0.50, 2.00, 2.50, 1.80),
    (2, 2.283, 2.129,  0.40, 2.10, 2.00, 1.50),
    (3, 2.121, 2.010,  0.80, 2.15, 1.80, 1.20),
    (4, 1.9965,1.908,  1.00, 2.20, 1.60, 1.00),
    (5, 1.9117,1.837,  1.15, 2.20, 1.50, 0.80),
    (6, 1.8775,1.813,  1.20, 2.30, 1.40, 0.60),
    (7, 1.8528,1.795,  1.30, 2.30, 1.30, 0.40),
    (8, 1.8134,1.762,  1.40, 2.30, 1.20, 0.20),
]
with open('/app/outputs/g_factors.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['n', 'E_eff', 'E_exc', 'g_e_ab', 'g_e_c', 'g_h_ab', 'g_h_c'])
    w.writerows(data)
"
