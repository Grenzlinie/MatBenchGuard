#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: step_01_center_displacement.csv ===
python3 /solution/compute.py step_01_center_displacement.csv

# === solve block: step_02_mode_shape.csv ===
python3 /solution/compute.py step_02_mode_shape.csv

# === solve block: step_03_resonance_frequencies.csv ===
python3 -c '
import csv
rows = [
    (1.15, False, 390.0),
    (1.15, True,  346.0),
    (1.38, False, 530.0),
    (1.38, True,  444.0),
]
with open("/app/outputs/step_03_resonance_frequencies.csv", "w") as f:
    w = csv.writer(f)
    w.writerow(["prestretch", "with_electrode", "frequency_Hz"])
    for prestretch, we, freq in rows:
        w.writerow([prestretch, we, freq])
'

# === solve block: step_04_voltage_dependence.csv ===
python3 /solution/compute.py step_04_voltage_dependence.csv

# === solve finalize ===
true
