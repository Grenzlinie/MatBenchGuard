#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: arrhenius_tof.csv ===
python3 << 'PYEOF'
import csv, math

T_vals = [248, 273, 298, 336, 386, 436]
Ea = 10.5               # kcal/mol
R = 0.001987            # kcal/(mol·K)
A = 1e6

with open('/app/outputs/arrhenius_tof.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Temperature (K)', 'TurnoverFrequency (s⁻¹)'])
    for T in T_vals:
        tof = A * math.exp(-Ea / (R * T))
        writer.writerow([T, f'{tof:.6e}'])
PYEOF

# === solve block: activation_energy_kcal.txt ===
echo '10.5' > "$OUTDIR/activation_energy_kcal.txt"

# === solve block: orders_simulation.csv ===
python3 -c "
import csv

# Order parameters
n_H2 = 0.75
n_C2H4 = -0.2
k = 0.001
P_C2H4_ref = 25.0
P_H2_ref = 100.0

rows = []
# H2 variations
for PH2 in [50.0, 100.0, 150.0]:
    TOF = k * (PH2 ** n_H2) * (P_C2H4_ref ** n_C2H4)
    rows.append([f'H2_{int(PH2)}', PH2, f'{TOF:.6e}'])
# C2H4 variations
for PC2H4 in [10.0, 25.0, 50.0]:
    TOF = k * (P_H2_ref ** n_H2) * (PC2H4 ** n_C2H4)
    rows.append([f'C2H4_{int(PC2H4)}', PC2H4, f'{TOF:.6e}'])

with open('$OUTDIR/orders_simulation.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['experiment_label', 'Pressure_Torr', 'TurnoverFrequency_s-1'])
    writer.writerows(rows)
"
