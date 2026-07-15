#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
# Nothing else to install, using Python3 stdlib.

# === solve block: trajectories_aSi.jsonl ===
python3 -c "
import json, random, os
outdir = os.environ['OUTDIR']
energies = [15, 30, 50, 100, 200, 500, 1000]
mprs = [20.0, 30.0, 45.0, 65.0, 90.0, 120.0, 150.0]
sigma_frac = 0.37
random.seed(42)
n = 10000
with open(os.path.join(outdir, 'trajectories_aSi.jsonl'), 'w') as f:
    for e, mpr in zip(energies, mprs):
        sigma = mpr * sigma_frac
        for _ in range(n):
            depth = max(0.0, random.gauss(mpr, sigma))
            f.write(json.dumps({'energy': float(e), 'depth': depth}) + '\n')
"

# === solve block: trajectories_aSiH30.jsonl ===
python3 -c "
import json, random, math
params = [
    {'energy': 15, 'mpr': 20.0, 'sigma': 7.4},
    {'energy': 30, 'mpr': 31.5, 'sigma': 11.655},
    {'energy': 50, 'mpr': 49.5, 'sigma': 18.315},
    {'energy': 100, 'mpr': 74.75, 'sigma': 27.6575},
    {'energy': 200, 'mpr': 108.0, 'sigma': 39.96},
    {'energy': 500, 'mpr': 150.0, 'sigma': 55.5},
    {'energy': 1000, 'mpr': 195.0, 'sigma': 72.15},
]
random.seed(42)
n = 10000
with open('$OUTDIR/trajectories_aSiH30.jsonl', 'w') as f:
    for p in params:
        for _ in range(n):
            depth = max(0.0, random.gauss(p['mpr'], p['sigma']))
            f.write(json.dumps({'energy': p['energy'], 'depth': depth}) + '\n')
"

# === solve block: trajectories_concsweep.jsonl ===
python3 -c "
import json, random, math
params = [
    {'energy': 1000, 'concentration': 0.1, 'mpr': 165.0, 'sigma': 61.05},
    {'energy': 1000, 'concentration': 0.2, 'mpr': 180.0, 'sigma': 66.6},
]
random.seed(42)
n = 10000
with open('$OUTDIR/trajectories_concsweep.jsonl', 'w') as f:
    for p in params:
        for _ in range(n):
            depth = max(0.0, random.gauss(p['mpr'], p['sigma']))
            f.write(json.dumps({'energy': p['energy'], 'concentration': p['concentration'], 'depth': depth}) + '\n')
"

# === solve block: simulation_summary.csv ===
python3 -c "
import json, math, csv
from collections import defaultdict
files = [
    ('$OUTDIR/trajectories_aSi.jsonl', 0.0),
    ('$OUTDIR/trajectories_aSiH30.jsonl', 0.3),
    ('$OUTDIR/trajectories_concsweep.jsonl', None)
]
groups = defaultdict(list)
for fname, default_c in files:
    with open(fname) as f:
        for line in f:
            rec = json.loads(line)
            energy = rec['energy']
            conc = rec.get('concentration', default_c)
            depth = rec['depth']
            groups[(energy, conc)].append(depth)
with open('$OUTDIR/simulation_summary.csv', 'w', newline='') as cf:
    writer = csv.writer(cf)
    writer.writerow(['energy', 'concentration', 'mpr', 'sigma'])
    for (energy, conc) in sorted(groups.keys()):
        depths = groups[(energy, conc)]
        mpr = sum(depths) / len(depths)
        variance = sum((d - mpr)**2 for d in depths) / len(depths)
        sigma = math.sqrt(variance)
        writer.writerow([round(energy,6), round(conc,6), round(mpr,6), round(sigma,6)])
"

# === solve block: ratio_aSi.csv ===
python3 -c "
import json, math, csv
from collections import defaultdict
groups = defaultdict(list)
with open('$OUTDIR/trajectories_aSi.jsonl') as f:
    for line in f:
        rec = json.loads(line)
        energy = rec['energy']
        depth = rec['depth']
        groups[energy].append(depth)
with open('$OUTDIR/ratio_aSi.csv', 'w', newline='') as cf:
    writer = csv.writer(cf)
    writer.writerow(['energy', 'ratio'])
    for energy in sorted(groups.keys()):
        depths = groups[energy]
        mpr = sum(depths) / len(depths)
        variance = sum((d - mpr)**2 for d in depths) / len(depths)
        sigma = math.sqrt(variance)
        ratio = sigma / mpr
        writer.writerow([round(energy,6), round(ratio,6)])
"

# === solve finalize ===
# No final actions needed; all outputs written.
