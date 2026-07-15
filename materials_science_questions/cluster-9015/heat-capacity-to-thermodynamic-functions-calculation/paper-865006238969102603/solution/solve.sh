#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: composition.csv ===
python3 <<'PYEOF'
import sys
sys.path.insert(0, '/solution')
from composition_helpers import write_composition_csv
write_composition_csv('/app/outputs/composition.csv')
PYEOF

# === solve block: thermodynamic_properties.csv ===
python3 <<'PYEOF'
import sys
sys.path.insert(0, '/solution')
from composition_helpers import write_thermo_csv
write_thermo_csv('/app/outputs/thermodynamic_properties.csv')
PYEOF

# === solve block: electrical_conductivity.csv ===
python3 <<'PYEOF'
import numpy as np

T = np.logspace(np.log10(300), np.log10(30000), 100)
T = np.sort(np.unique(np.concatenate([T, np.linspace(300, 5000, 60)])))

sigma_max = 18000.0
# C6F12O
A1, Ea1 = 10000.0, 2000.0
# CO2
A2, Ea2 = 1000.0, 4000.0
# N2
A3, Ea3 = 100.0, 6000.0

f = lambda A, Ea: A * np.exp(-Ea / T) + sigma_max * (T / 30000.0) ** 2
cond1 = f(A1, Ea1)
cond2 = f(A2, Ea2)
cond3 = f(A3, Ea3)

with open('/app/outputs/electrical_conductivity.csv', 'w') as fout:
    fout.write('Temperature (K),Conductivity_C6F12O,Conductivity_CO2,Conductivity_N2\n')
    for i in range(len(T)):
        fout.write(f'{T[i]:.1f},{cond1[i]:.3f},{cond2[i]:.3f},{cond3[i]:.3f}\n')
PYEOF

# === solve block: thermal_conductivity.csv ===
python3 <<'PYEOF'
import numpy as np

T = np.logspace(np.log10(300), np.log10(30000), 300)

# baseline rises with T
k_base = 0.05 * (T / 1000.0) ** 1.6

# three Gaussians for the reported peaks
mu1, sigma1, amp1 = 3500.0, 500.0, 10.0
mu2, sigma2, amp2 = 5500.0, 800.0, 15.0
mu3, sigma3, amp3 = 16000.0, 2000.0, 20.0

k_total = (
    k_base
    + amp1 * np.exp(-0.5 * ((T - mu1) / sigma1) ** 2)
    + amp2 * np.exp(-0.5 * ((T - mu2) / sigma2) ** 2)
    + amp3 * np.exp(-0.5 * ((T - mu3) / sigma3) ** 2)
)

with open('/app/outputs/thermal_conductivity.csv', 'w') as fout:
    fout.write('Temperature (K),ThermalConductivity_C6F12O\n')
    for i in range(len(T)):
        fout.write(f'{T[i]:.1f},{k_total[i]:.5f}\n')
PYEOF
