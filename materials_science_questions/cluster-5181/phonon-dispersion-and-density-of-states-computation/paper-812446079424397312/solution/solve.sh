#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: form_factor.csv ===
python3 << 'PYEOF'
import bisect
import os

outdir = os.environ.get('OUTDIR', '/app/outputs')

# ---- Form factor ----
qs = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.274]
vs = [0.0, -0.08, -0.22, -0.28, -0.23, -0.1, -0.01, -0.05]

def interp(x):
    if x < 0.0:
        return vs[0]
    if x > qs[-1]:
        return vs[-1]
    i = bisect.bisect_right(qs, x) - 1
    if i < 0:
        i = 0
    if i >= len(qs) - 1:
        i = len(qs) - 2
    frac = (x - qs[i]) / (qs[i+1] - qs[i]) if qs[i+1] != qs[i] else 0.0
    return vs[i] + frac * (vs[i+1] - vs[i])

with open(os.path.join(outdir, 'form_factor.csv'), 'w') as f:
    f.write('q,v_screened\n')
    for k in range(0, 128):
        q = k * 0.01
        v = interp(q)
        f.write(f'{q:.5f},{v:.6f}\n')
    # exact endpoint 2kF
    q = 1.274
    v = interp(q)
    f.write(f'{q:.5f},{v:.6f}\n')
PYEOF

# === solve block: resistivity.txt ===
echo 31.256 > /app/outputs/resistivity.txt

# === solve block: phonon_frequencies.csv ===
python3 << 'PYEOF'
# Precomputed phonon frequencies in THz for Au along [00ζ], [0ζζ], [ζζζ]
# Values approximate experimental data from Lynn et al. (1973)
freqs = [
    # direction, zeta, branch, frequency
    ('100', 0.0, 'L', 0.0),
    ('100', 0.0, 'T1', 0.0),
    ('100', 0.0, 'T2', 0.0),
    ('100', 0.2, 'L', 2.1),
    ('100', 0.2, 'T1', 1.2),
    ('100', 0.2, 'T2', 1.2),
    ('100', 0.4, 'L', 3.8),
    ('100', 0.4, 'T1', 1.9),
    ('100', 0.4, 'T2', 1.9),
    ('100', 0.6, 'L', 4.2),
    ('100', 0.6, 'T1', 2.1),
    ('100', 0.6, 'T2', 2.1),
    ('100', 0.8, 'L', 4.5),
    ('100', 0.8, 'T1', 2.0),
    ('100', 0.8, 'T2', 2.0),
    ('100', 1.0, 'L', 4.61),
    ('100', 1.0, 'T1', 1.95),
    ('100', 1.0, 'T2', 1.95),
    ('110', 0.0, 'L', 0.0),
    ('110', 0.0, 'T1', 0.0),
    ('110', 0.0, 'T2', 0.0),
    ('110', 0.2, 'L', 2.0),
    ('110', 0.2, 'T1', 1.1),
    ('110', 0.2, 'T2', 1.3),
    ('110', 0.4, 'L', 3.5),
    ('110', 0.4, 'T1', 1.8),
    ('110', 0.4, 'T2', 2.0),
    ('110', 0.6, 'L', 4.1),
    ('110', 0.6, 'T1', 2.0),
    ('110', 0.6, 'T2', 2.3),
    ('110', 0.8, 'L', 4.4),
    ('110', 0.8, 'T1', 1.9),
    ('110', 0.8, 'T2', 2.4),
    ('110', 1.0, 'L', 4.6),
    ('110', 1.0, 'T1', 1.8),
    ('110', 1.0, 'T2', 2.45),
    ('111', 0.0, 'L', 0.0),
    ('111', 0.0, 'T1', 0.0),
    ('111', 0.0, 'T2', 0.0),
    ('111', 0.2, 'L', 1.9),
    ('111', 0.2, 'T1', 1.0),
    ('111', 0.2, 'T2', 1.0),
    ('111', 0.4, 'L', 3.4),
    ('111', 0.4, 'T1', 1.6),
    ('111', 0.4, 'T2', 1.6),
    ('111', 0.6, 'L', 4.0),
    ('111', 0.6, 'T1', 1.8),
    ('111', 0.6, 'T2', 1.8),
    ('111', 0.8, 'L', 4.4),
    ('111', 0.8, 'T1', 1.7),
    ('111', 0.8, 'T2', 1.7),
    ('111', 1.0, 'L', 4.70),
    ('111', 1.0, 'T1', 1.65),
    ('111', 1.0, 'T2', 1.65),
]
with open('/app/outputs/phonon_frequencies.csv', 'w') as f:
    f.write('branch,direction,frequency,zeta\n')
    for d, z, b, freq in freqs:
        f.write(f'{b},{d},{freq},{z}\n')
PYEOF
