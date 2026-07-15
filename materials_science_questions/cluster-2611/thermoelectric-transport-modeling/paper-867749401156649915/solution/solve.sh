#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: magneto_thermopower.csv ===
python3 << 'PYEOF'
import sys, math, csv, os
sys.path.insert(0, '/solution')
from helper import compute_fermi_energy_and_k, compute_thermopower

n_total = 1.0e12  # cm^-2
n_spin = n_total / 2.0
ef_up, ef_down, _, _ = compute_fermi_energy_and_k(n_spin)

tau = 1.0e-10  # s
s = 0.7
T = 4.0

B_vals = [round(i*0.1,1) for i in range(-30, 31, 5)]  # -3.0 .. 3.0 step 0.5
out_path = os.path.join('/app/outputs', 'magneto_thermopower.csv')
with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['B_field', 'spin', 'Qxx', 'Qyx'])
    for B in B_vals:
        for spin, ef in [('up', ef_up), ('down', ef_down)]:
            Qxx, Qyx = compute_thermopower(ef, B, tau, s, T)
            writer.writerow([f"{B:.1f}", spin, f"{Qxx:.6e}", f"{Qyx:.6e}"])
PYEOF

# === solve block: power_factor.csv ===
python3 << 'PYEOF'
import sys, math, csv, os
sys.path.insert(0, '/solution')
from helper import compute_fermi_energy_and_k, compute_power_factor

tau = 1.0e-9
s = 0.7
T = 1.0

n_list = [1e11, 2e11, 5e11, 1e12, 2e12, 5e12, 1e13]  # total cm^-2
out_path = os.path.join('/app/outputs', 'power_factor.csv')
with open(out_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['carrier_density', 'spin', 'power_factor'])
    for n_total in n_list:
        n_spin = n_total / 2.0
        ef_up, ef_down, kf_up, kf_down = compute_fermi_energy_and_k(n_spin)
        pf_up = compute_power_factor(ef_up, kf_up, tau, s, T)
        pf_down = compute_power_factor(ef_down, kf_down, tau, s, T)
        writer.writerow([f"{n_total:.0e}", 'up', f"{pf_up:.6e}"])
        writer.writerow([f"{n_total:.0e}", 'down', f"{pf_down:.6e}"])
PYEOF
