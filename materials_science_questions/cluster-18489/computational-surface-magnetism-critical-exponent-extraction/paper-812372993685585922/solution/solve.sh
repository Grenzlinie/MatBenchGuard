#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: bulk_spin_autocorr.csv ===
cat <<PYEOF > /tmp/gen_bulk_spin.py
import numpy as np
# tau > 1 to avoid log(1)=0; logspace from 1.1 to 100
start_power = np.log10(1.1)
tau = np.logspace(start_power, 2, 200)
# exact bulk magnetization exponent x_m = 1 - omega/2 with omega = (1+sqrt(5))/2
x_m = (3 - np.sqrt(5)) / 4
G = 1.0 / np.log(tau) ** (2 * x_m)
np.savetxt('$OUTDIR/bulk_spin_autocorr.csv', np.column_stack((tau, G)),
           delimiter=',', header='tau,G_bulk', comments='')
PYEOF
python3 /tmp/gen_bulk_spin.py
rm /tmp/gen_bulk_spin.py

# === solve block: surface_spin_autocorr.csv ===
cat <<'PYEOF' > /tmp/gen_surf_spin.py
import numpy as np
tau = np.logspace(-2, 2, 200)
x_m_s = 0.5
G = 1.0 / np.log(1 + tau) ** (2 * x_m_s)
np.savetxt('/app/outputs/surface_spin_autocorr.csv', np.column_stack((tau, G)),
           delimiter=',', header='tau,G_surf', comments='')
PYEOF
python3 /tmp/gen_surf_spin.py
rm /tmp/gen_surf_spin.py

# === solve block: bulk_energy_autocorr.csv ===
cat <<'PYEOF' > /tmp/gen_bulk_energy.py
import numpy as np
tau = np.logspace(0, 2, 200)   # tau from 1 to 100
eta_e = 2.2
G = 1.0 / ((tau + 1e-3) ** eta_e)
np.savetxt('/app/outputs/bulk_energy_autocorr.csv', np.column_stack((tau, G)),
           delimiter=',', header='tau,G_bulk_e', comments='')
PYEOF
python3 /tmp/gen_bulk_energy.py
rm /tmp/gen_bulk_energy.py

# === solve block: surface_energy_autocorr.csv ===
cat <<'PYEOF' > /tmp/gen_surf_energy.py
import numpy as np
tau = np.logspace(0, 2, 200)
eta_s = 2.5
G = 1.0 / ((tau + 1e-3) ** eta_s)
np.savetxt('/app/outputs/surface_energy_autocorr.csv', np.column_stack((tau, G)),
           delimiter=',', header='tau,G_surf_e', comments='')
PYEOF
python3 /tmp/gen_surf_energy.py
rm /tmp/gen_surf_energy.py
