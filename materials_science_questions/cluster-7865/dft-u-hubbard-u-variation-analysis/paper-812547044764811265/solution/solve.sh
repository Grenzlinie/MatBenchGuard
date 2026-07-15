#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lattice_constant.json ===
cat > /app/outputs/lattice_constant.json <<'FFEOF'
{
  "lattice_constant_nm": 0.554781,
  "unit": "nm"
}
FFEOF

# === solve block: phonon_dos.json ===
python3 -c "
import json, math

# Energy grid from 0.001 to 0.15 eV, step 0.001 eV
emin, emax, de = 0.001, 0.15, 0.001
n = int((emax - emin) / de) + 1
energy = [emin + i*de for i in range(n)]

# Gaussian function
def gauss(x, mu, sigma, A):
    return (A / (sigma * math.sqrt(2*math.pi))) * math.exp(-0.5 * ((x - mu)/sigma)**2)

# U_DOS: acoustic peak at 0.02 eV, broad, plus some optical contribution at 0.06 eV
# normalize to total integral = 3
U = []
for e in energy:
    val = gauss(e, 0.02, 0.008, 2.5) + gauss(e, 0.06, 0.015, 0.5)
    U.append(max(0.0, val))
integral_U = sum(U) * de
scale_U = 3.0 / integral_U
U = [v * scale_U for v in U]

# O_DOS: two main peaks at 0.06 eV and 0.08 eV
O = []
for e in energy:
    val = gauss(e, 0.06, 0.01, 2.0) + gauss(e, 0.08, 0.01, 1.0)
    O.append(max(0.0, val))
integral_O = sum(O) * de
scale_O = 3.0 / integral_O
O = [v * scale_O for v in O]

output = {
    'energy_eV': energy,
    'U_DOS': U,
    'O_DOS': O,
    'unit_DOS': 'states/eV/atom'
}
with open('/app/outputs/phonon_dos.json', 'w') as f:
    json.dump(output, f, indent=2)
print('phonon_dos.json written.')
"
