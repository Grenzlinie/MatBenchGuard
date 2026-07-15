#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_MAE_results.json ===
python3 << 'PYEOF' > $OUTDIR/step_01_MAE_results.json
import json
import sys

J = 2.5
J_plus_1 = J + 1.0
factor = J * J_plus_1  # 8.75

E_a_fcc = -2.05   # meV
E_a_hcp = 0.50    # meV

D_fcc = E_a_fcc / factor
D_hcp = E_a_hcp / factor

data = [
    {
        "site": "fcc",
        "E_a_meV": E_a_fcc,
        "D_meV": D_fcc,
        "easy_axis": "out-of-plane"
    },
    {
        "site": "hcp",
        "E_a_meV": E_a_hcp,
        "D_meV": D_hcp,
        "easy_axis": "easy-plane"
    }
]

json.dump(data, sys.stdout, indent=2)
print()
PYEOF

# === solve block: step_02_field_excitation_energy.csv ===
python3 << 'PYEOF' > /app/outputs/step_02_field_excitation_energy.csv
import csv
import sys

# Convert paper DFT MAE values to D (J=5/2)
J = 2.5
factor = J * (J + 1)   # 8.75
E_a_fcc = -2.05
E_a_hcp = 0.50
D_fcc = E_a_fcc / factor
D_hcp = E_a_hcp / factor

g = 2.0
mu_B = 0.05788  # meV/T

m_states = [m for m in range(-5, 6, 2)]  # -5/2 to 5/2
m_vals = [m/2.0 for m in m_states]

def excitation(D, B):
    energies = [D*(m**2) + g*mu_B*B*m for m in m_vals]
    distinct = sorted(set(energies))
    if len(distinct) < 2:
        return 0.0
    return distinct[1] - distinct[0]

writer = csv.writer(sys.stdout)
writer.writerow(["site", "B_T", "excitation_energy_meV"])

B_vals = [i/10.0 for i in range(0, 121)]  # 0..12 T step 0.1
for B in B_vals:
    exc_fcc = excitation(D_fcc, B)
    writer.writerow(["fcc", f"{B:.1f}", f"{exc_fcc:.6f}"])
    exc_hcp = excitation(D_hcp, B)
    writer.writerow(["hcp", f"{B:.1f}", f"{exc_hcp:.6f}"])
PYEOF
