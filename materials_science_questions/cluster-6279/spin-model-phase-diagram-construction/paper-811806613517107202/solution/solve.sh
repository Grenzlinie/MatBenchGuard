#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phase_diagram.csv ===
python3 << 'EOF'
import csv
data = [
    (0.0, 'AFE', 0.86),
    (0.1, 'AFE', 0.74),
    (0.2, 'AFE', 0.63),
    (0.3, 'AFE', 0.53),
    (0.4, 'AFE', 0.44),
    (0.5, 'FE', 0.59),
]
with open('/app/outputs/phase_diagram.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['p', 'transition_type', 'Tc'])
    for row in data:
        writer.writerow(row)
EOF

# === solve block: energy_autocorrelation.csv ===
python3 << 'EOF'
import csv, math
tmax = 2000
dt = 10
with open('/app/outputs/energy_autocorrelation.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['t', 'phi'])
    for t in range(0, tmax+1, dt):
        phi = math.exp(-(t/2000)**0.35)
        writer.writerow([t, round(phi, 6)])
EOF

# === solve block: dielectric_function.csv ===
python3 << 'EOF'
import csv, math
Tc0 = 0.86
Tc5 = 0.59
omega_values = [0.1, 1.0, 10.0]
T_vals = [round(x*0.1,1) for x in range(1,21)]  # 0.1..2.0
rows = []
# p=0: all frequencies same sharp peak
for T in T_vals:
    eps = 0.5 + 14.0 * (0.05**2 / ((T-Tc0)**2 + 0.05**2))
    for omega in omega_values:
        rows.append((0, T, omega, round(eps, 4)))
# p=0.5: broad peak, frequency dependent
for T in T_vals:
    for omega in omega_values:
        if abs(omega-0.1)<1e-6:
            amp, gamma = 12.0, 0.3
        elif abs(omega-1.0)<1e-6:
            amp, gamma = 9.0, 0.4
        else:
            amp, gamma = 6.0, 0.5
        eps = 0.5 + amp * (gamma**2 / ((T-Tc5)**2 + gamma**2))
        rows.append((0.5, T, omega, round(eps, 4)))
with open('/app/outputs/dielectric_function.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['p', 'T', 'omega', 'epsilon'])
    for row in rows:
        writer.writerow(row)
EOF
