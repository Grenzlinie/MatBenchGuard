#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy

# === solve block: step_01_md_results.csv ===
python3 -c "
import csv, math
thicknesses = [5.67, 10.21, 17.00, 22.67, 28.34, 34.01, 39.68, 45.35, 50.92]
rows = []
for d in thicknesses:
    # Eq. (12) normal: k_N = 1/(0.017 + 3.08*d^{-2.37})
    k_n = 1.0 / (0.017 + 3.08 * (d ** (-2.37)))
    # tangential: k_T = 1/(0.017 + 20.87*d^{-2.82})
    k_t = 1.0 / (0.017 + 20.87 * (d ** (-2.82)))
    rows.append([f'{d:.2f}', f'{k_n:.6f}', f'{k_t:.6f}'])
with open('/app/outputs/step_01_md_results.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['thickness_nm', 'k_normal_WmK', 'k_tangential_WmK'])
    w.writerows(rows)
"

# === solve block: step_02_theory_results.csv ===
python3 /solution/theory.py
