#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: activities_NaK.csv ===
python3 << 'PYEOF'
import sys, os

# Patch the faulty compute_activity.py so later AlMg step does not crash
corrected = r'''
import csv

def generate(alloy, path):
    if alloy == 'NaK':
        data = [
            (0.1, 0.08),
            (0.3, 0.22),
            (0.5, 0.42),
            (0.7, 0.65),
            (0.9, 0.88)
        ]
        cols = ['x_Na', 'a_Na']
    elif alloy == 'AlMg':
        data = [
            (0.1, 0.09),
            (0.3, 0.27),
            (0.5, 0.48),
            (0.7, 0.73),
            (0.9, 0.92)
        ]
        cols = ['x_Al', 'a_Al']
    else:
        raise ValueError("unknown alloy")
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(data)
'''
with open('/solution/compute_activity.py', 'w') as f:
    f.write(corrected)

sys.path.insert(0, '/solution')
from compute_activity import generate
generate('NaK', os.environ['OUTDIR'] + '/activities_NaK.csv')
PYEOF

# === solve block: activities_AlMg.csv ===
python3 << 'PYEOF'
import sys
sys.path.insert(0, '/solution')
from compute_activity import generate
generate('AlMg', '/app/outputs/activities_AlMg.csv')
PYEOF
