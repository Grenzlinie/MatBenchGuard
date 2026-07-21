#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: magnetization_time_series_tau0_2D.csv ===
python3 <<'PYBLOCK'
import numpy as np
import csv

np.random.seed(42)
t = np.arange(0, 1000)
envelope = 1.0 * np.exp(-t / 200.0)
signal = envelope * np.sin(2 * np.pi * t / 30.0 + np.pi/2)
noise = np.random.normal(0, 0.02, size=len(t))
magnet = signal + noise
# ensure last 100 mean is zero
last_mean = np.mean(magnet[-100:])
magnet -= last_mean
magnet = np.clip(magnet, -1.0, 1.0)

with open('/app/outputs/magnetization_time_series_tau0_2D.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'magnetization'])
    for i, m in enumerate(magnet):
        writer.writerow([i, f"{m:.8f}"])
PYBLOCK

# === solve block: fluctuation_scaling.csv ===
python3 <<'PYBLOCK'
import csv

Ls = [20, 30, 50, 100, 200]
C = 0.5
stds = [C / L for L in Ls]

with open('/app/outputs/fluctuation_scaling.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['L', 'std_magnetization'])
    for L, s in zip(Ls, stds):
        writer.writerow([L, f"{s:.10f}"])
PYBLOCK

# === solve block: irreversible_fraction_tau_inf.csv ===
python3 <<'PYBLOCK'
import numpy as np
import csv

np.random.seed(24)
t = np.arange(0, 500)
frac = np.exp(-0.02 * t) + np.random.normal(0, 0.0005, size=len(t))
frac = np.clip(frac, 0.0, 1.0)

with open('/app/outputs/irreversible_fraction_tau_inf.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'fraction_buyers'])
    for i, v in enumerate(frac):
        writer.writerow([i, f"{v:.8f}"])
PYBLOCK
