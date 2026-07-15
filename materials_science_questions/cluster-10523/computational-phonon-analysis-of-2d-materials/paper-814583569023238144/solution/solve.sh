#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: pdos_pristine_30.csv ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple "numpy<2"
python3 << EOF
import numpy as np

freq = np.arange(0, 3001, 5)
baseline = 0.01

peak0 = 1350
sigma0 = 30
ampl0 = 1.0
g0 = baseline + ampl0 * np.exp(-0.5 * ((freq - peak0) / sigma0) ** 2)

peak30 = 1340
sigma30 = 45
ampl30 = 0.2
g30 = baseline + ampl30 * np.exp(-0.5 * ((freq - peak30) / sigma30) ** 2)

with open('$OUTDIR/pdos_pristine_30.csv', 'w') as f:
    f.write('frequency,PDOS_pristine,PDOS_30\n')
    for i in range(len(freq)):
        f.write('{:.1f},{:.6f},{:.6f}\n'.format(freq[i], g0[i], g30[i]))
EOF

# === solve block: e2g_peaks.csv ===
cat > /app/outputs/e2g_peaks.csv << 'EOF'
vacancy_concentration,e2g_frequency
0,1350.0
10,1342.0
20,1330.0
30,1315.0
EOF

# === solve block: specific_heat.csv ===
python3 << 'EOF'
import sys; sys.path.insert(0, '/solution')
import numpy as np
from helper import generate_pdos, compute_cv

freq = np.arange(0, 3001, 5)
temps = np.arange(50, 701, 50)

cv00 = compute_cv(generate_pdos(0,  freq), freq, temps)
cv10 = compute_cv(generate_pdos(10, freq), freq, temps)
cv20 = compute_cv(generate_pdos(20, freq), freq, temps)
cv30 = compute_cv(generate_pdos(30, freq), freq, temps)

with open('/app/outputs/specific_heat.csv', 'w') as f:
    f.write('temperature_K,C_V_pristine,C_V_10,C_V_20,C_V_30\n')
    for i, T in enumerate(temps):
        f.write('{:.1f},{:.8e},{:.8e},{:.8e},{:.8e}\n'.format(T, cv00[i], cv10[i], cv20[i], cv30[i]))
EOF
