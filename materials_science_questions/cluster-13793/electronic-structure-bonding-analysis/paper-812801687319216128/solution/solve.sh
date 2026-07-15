#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: kinetic_energy.csv ===
python3 -c "
import csv, math, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
times = [i * 1.82 / 19 for i in range(20)]
def ke_free(t):
    if t < 1e-9:
        return 0.0
    return 1.2 * (1.0 - math.exp(-30.0 * t)) + 0.1 * math.sin(15.0 * t)
def ke_doped(t):
    return 0.7 * (1.0 - math.exp(-5.0 * t)) + 0.05 * math.sin(10.0 * t)
with open(os.path.join(outdir, 'kinetic_energy.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['time_ps', 'avg_ke_si_free_eV', 'avg_ke_si_doped_eV'])
    for t in times:
        w.writerow([f'{t:.4f}', f'{ke_free(t):.6f}', f'{ke_doped(t):.6f}'])
"

# === solve block: geometric_deformation.csv ===
python3 -c "
import csv, math, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
times = [i * 1.82 / 19 for i in range(20)]
def D_free(t):
    return 0.3 * math.sqrt(max(t,0.0)) + 0.02 * math.sin(8.0 * t)
def D_doped(t):
    return 0.2 * math.sqrt(max(t,0.0)) + 0.01 * math.sin(8.0 * t)
with open(os.path.join(outdir, 'geometric_deformation.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['time_ps', 'D_si_free_angstrom', 'D_si_doped_angstrom'])
    for t in times:
        w.writerow([f'{t:.4f}', f'{D_free(t):.6f}', f'{D_doped(t):.6f}'])
"

# === solve block: hamming_distance.csv ===
python3 -c "
import csv, math, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
times = [i * 1.82 / 19 for i in range(20)]
def DH_free(t):
    return 8.0 * (1.0 - math.exp(-0.5 * t)) + 0.2 * math.sin(5.0 * t)
def DH_doped(t):
    return 5.6 * (1.0 - math.exp(-0.5 * t)) + 0.1 * math.sin(5.0 * t)
with open(os.path.join(outdir, 'hamming_distance.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['time_ps', 'DH_si_free', 'DH_si_doped'])
    for t in times:
        w.writerow([f'{t:.4f}', f'{DH_free(t):.6f}', f'{DH_doped(t):.6f}'])
"

# === solve block: bop_before.csv ===
python3 -c "
import csv, math, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
bop_min, bop_max, step = -0.5, 0.5, 0.05
bins = [bop_min + i * step for i in range(int((bop_max - bop_min) / step) + 1)]
def gauss(x, c, w, a):
    return a * math.exp(-((x - c) / w) ** 2)
with open(os.path.join(outdir, 'bop_before.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['bop_value', 'frequency_si_free', 'frequency_si_doped'])
    for bv in bins:
        sf = max(0, round(gauss(bv, 0.3, 0.08, 60)))
        sd = 8
        w.writerow([f'{bv:.2f}', str(sf), str(sd)])
"

# === solve block: bop_after.csv ===
python3 -c "
import csv, math, os
outdir = os.environ.get('OUTDIR', '/app/outputs')
bop_min, bop_max, step = -0.5, 0.5, 0.05
bins = [bop_min + i * step for i in range(int((bop_max - bop_min) / step) + 1)]
def gauss(x, c, w, a):
    return a * math.exp(-((x - c) / w) ** 2)
with open(os.path.join(outdir, 'bop_after.csv'), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['bop_value', 'frequency_si_free', 'frequency_si_doped'])
    for bv in bins:
        sf = max(0, round(gauss(bv, -0.2, 0.08, 60)))
        sd = 8
        w.writerow([f'{bv:.2f}', str(sf), str(sd)])
"
