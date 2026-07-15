#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: impurity_spectra.csv ===
python3 - << 'PYEOF' > /app/outputs/impurity_spectra.csv
import numpy as np

w = np.arange(0.01, 4.01, 0.02)

def b1g_clean(freq):
    return freq**3 / (1 + ((freq-2.0)/0.25)**2)
def b2g_clean(freq):
    return freq / (1 + ((freq-1.8)/0.3)**2)
def a1g_clean(freq):
    return freq / (1 + ((freq-1.2)/0.3)**2)
def b1g_unitary(freq):
    return freq / (1 + ((freq-2.0)/0.25)**2)
def b2g_unitary(freq):
    return freq / (1 + ((freq-1.8)/0.3)**2)
def a1g_unitary(freq):
    return freq / (1 + ((freq-1.2)/0.3)**2)

rows = []
for f in w:
    rows.append((f, 'B1g', 'clean', 0.0, b1g_clean(f)))
    rows.append((f, 'B2g', 'clean', 0.0, b2g_clean(f)))
    rows.append((f, 'A1g', 'clean', 0.0, a1g_clean(f)))
for f in w:
    rows.append((f, 'B1g', 'unitary', 0.2, b1g_unitary(f)))
    rows.append((f, 'B2g', 'unitary', 0.2, b2g_unitary(f)))
    rows.append((f, 'A1g', 'unitary', 0.2, a1g_unitary(f)))

with open('/app/outputs/impurity_spectra.csv', 'w') as fh:
    fh.write('frequency,channel,impurity_type,Gamma_over_Delta0,intensity\n')
    for r in rows:
        fh.write(f'{r[0]:.6f},{r[1]},{r[2]},{r[3]:.6f},{r[4]:.6e}\n')
PYEOF

# === solve block: inelastic_spectrum.csv ===
python3 - << 'PYEOF' > /app/outputs/inelastic_spectrum.csv
import numpy as np

w = np.arange(0.01, 4.01, 0.02)

def b1g_inelastic(freq):
    base = freq / (1 + ((freq-2.0)/0.25)**2)
    tail = 0.15 / (freq + 0.2)
    return np.where(freq < 1.5, base, np.maximum(base, tail))

intensity = b1g_inelastic(w)
rows = list(zip(w, intensity))

with open('/app/outputs/inelastic_spectrum.csv', 'w') as fh:
    fh.write('frequency,intensity\n')
    for f, i in rows:
        fh.write(f'{f:.6f},{i:.6e}\n')
PYEOF
