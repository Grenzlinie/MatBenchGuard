#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: localization_distance_s.txt ===
python3 <<'PYEOF'
import math

m_e   = 9.10938356e-28   # g
e     = 4.8032047e-10    # esu
hbar  = 1.054571817e-27  # erg*s
sigma = 0.37              # dyn/cm
E_V_cm = 3000.0
E_statV_cm = E_V_cm / 299.792458

s = math.sqrt(2 * math.pi * sigma * hbar**2 / (m_e * e**2 * E_statV_cm**2))
with open('/app/outputs/localization_distance_s.txt', 'w') as f:
    f.write(f'{s}\n')
PYEOF

# === solve block: phase_boundary_A.txt ===
python3 <<'PYEOF'
import math

sigma = 0.37               # dyn/cm
A = 4 * (1 - math.sqrt(3.0/4.0)) * math.pi**2 * sigma / math.log(2.0 / (12.0**0.25))
with open('/app/outputs/phase_boundary_A.txt', 'w') as f:
    f.write(f'{A}\n')
PYEOF
