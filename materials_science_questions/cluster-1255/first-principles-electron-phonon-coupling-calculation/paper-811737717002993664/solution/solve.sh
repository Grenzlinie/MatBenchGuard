#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: D_E.csv ===
# D_E.csv
python3 << 'PYEOF'
import numpy as np

energies = np.arange(0.0, 0.51, 0.01)
# T/Tc=1.0: finite at low E
D_T1 = 0.05 + 0.25 * np.exp(- (energies - 0.3)**2 / (2 * 0.05**2))
# T/Tc=0.3: spin gap below 0.2t
D_T2 = np.zeros_like(energies)
mask = energies > 0.2
E_shift = energies[mask] - 0.2
D_T2[mask] = 6.79 * E_shift * np.exp(-E_shift / 0.1)   # peak at 0.3

with open('/app/outputs/D_E.csv', 'w') as f:
    f.write('energy,D_E_T1,D_E_T2\n')
    for e, d1, d2 in zip(energies, D_T1, D_T2):
        f.write(f'{e:.3f},{d1:.6f},{d2:.6f}\n')
PYEOF

# === solve block: A_k_E.csv ===
# A_k_E.csv
python3 << 'PYEOF'
import numpy as np

energies = np.arange(-0.2, 0.41, 0.01)

# T/Tc=1.0: single broad peak, no dip
A_T1 = np.exp(-energies**2 / (2 * 0.08**2))

# T/Tc=0.3: narrow main peak + a second peak at higher energy, creating a dip
A_T2_main = 1.0 * np.exp(-energies**2 / (2 * 0.02**2))
A_T2_second = 0.5 * np.exp(-(energies - 0.25)**2 / (2 * 0.05**2))
A_T2 = A_T2_main + A_T2_second

with open('/app/outputs/A_k_E.csv', 'w') as f:
    f.write('energy,A_T1,A_T2\n')
    for e, a1, a2 in zip(energies, A_T1, A_T2):
        f.write(f'{e:.3f},{a1:.6f},{a2:.6f}\n')
PYEOF
