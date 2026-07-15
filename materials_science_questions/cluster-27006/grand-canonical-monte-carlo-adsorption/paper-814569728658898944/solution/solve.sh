#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple pyiast pandas numpy scipy

# === solve block: step_01_langmuir_predictions.csv ===
python3 << 'PYEOF'
import csv
M = 1.0
K = [2.0, 10.0, 20.0]
points = []
for i in range(0, 11):
    xA = i / 10.0
    for j in range(0, 11 - i):
        xB = j / 10.0
        xC = 1.0 - xA - xB
        points.append((xA, xB, xC))
with open('/app/outputs/step_01_langmuir_predictions.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['xA','xB','xC','predicted_loading_A','predicted_loading_B','predicted_loading_C'])
    for xA, xB, xC in points:
        p = [xA, xB, xC]
        denom = 1.0 + sum(K[i] * p[i] for i in range(3))
        loads = [M * K[i] * p[i] / denom for i in range(3)]
        writer.writerow([xA, xB, xC] + loads)
PYEOF

# === solve block: step_02_binary_predictions.csv ===
python3 /solution/run.py --step 2

# === solve block: step_03_reverse_predictions.csv ===
python3 /solution/run.py --step 3

# === solve block: step_04_ternary_predictions.csv ===
python3 /solution/run.py --step 4
