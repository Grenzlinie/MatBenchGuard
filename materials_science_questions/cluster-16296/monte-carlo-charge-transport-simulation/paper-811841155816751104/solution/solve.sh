#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: eta_data.csv ===
python3 << 'PYEOF'
import csv, math

# analytic parameters from paper: symmetric anisotropic case
# m_x*/m_z* = m_y*/m_z* = 4, Gamma=0 => sin(K0)=1, delta_c^2 = 1
# mu_min = 1 + (1/(sqrt(2)*delta)) * (delta^2 - 1)^{1/2}
# eta_inv = ln(mu_min)

delta2_vals = []
for i in range(1, 101):
    d2 = 1.0 + 0.01 * i   # from 1.01 to 2.0
    delta = math.sqrt(d2)
    diff = d2 - 1.0
    mu_min = 1.0 + (1.0 / (math.sqrt(2.0) * delta)) * math.sqrt(diff)
    eta = math.log(mu_min)
    delta2_vals.append((round(d2, 6), round(eta, 12)))

with open('/app/outputs/eta_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['delta_squared', 'eta_inv'])
    for d2, eta in delta2_vals:
        writer.writerow([d2, eta])
PYEOF
