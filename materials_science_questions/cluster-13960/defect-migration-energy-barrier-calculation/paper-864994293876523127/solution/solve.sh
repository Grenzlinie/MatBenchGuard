#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: lattice_parameter.csv ===
python3 <<'PYEOF'
import csv
x_vals = [i/20.0 for i in range(9)]
a0, slope = 5.418, 0.106
rows = [["x", "a"]]
for x in x_vals:
    rows.append([f"{x:.2f}", f"{a0 + slope*x:.3f}"])
with open("/app/outputs/lattice_parameter.csv", "w", newline="") as f:
    w = csv.writer(f)
    for r in rows:
        w.writerow(r)
PYEOF

# === solve block: association_energies.csv ===
python3 <<'PYEOF'
import csv
rows = [["position", "E_ass"], ["1NN", "-0.1981"], ["2NN", "-0.128"]]
with open("/app/outputs/association_energies.csv", "w", newline="") as f:
    w = csv.writer(f)
    for r in rows:
        w.writerow(r)
PYEOF

# === solve block: migration_energies.csv ===
python3 <<'PYEOF'
import csv
rows = [["edge", "E_m"], ["Ce-Ce", "0.315"], ["Ce-Sm", "0.563"], ["Sm-Sm", "1.252"]]
with open("/app/outputs/migration_energies.csv", "w", newline="") as f:
    w = csv.writer(f)
    for r in rows:
        w.writerow(r)
PYEOF

# === solve block: trapping_migration_energies.csv ===
python3 <<'PYEOF'
import csv
rows = [["configuration", "E_m"], ["config1", "0.563"], ["config2", "0.669"], ["config3", "0.778"]]
with open("/app/outputs/trapping_migration_energies.csv", "w", newline="") as f:
    w = csv.writer(f)
    for r in rows:
        w.writerow(r)
PYEOF

# === solve block: conductivity.csv ===
python3 <<'PYEOF'
import csv, math

k_B = 8.617333262145e-5
T = 1073.0
kT = k_B * T

E_m_CeCe, E_m_CeSm, E_m_SmSm = 0.315, 0.563, 1.252
E_ass_1NN, E_ass_2NN = -0.1981, -0.128

a0, a_slope = 5.418, 0.106
scale = 1.22e-3

def sigma(x):
    if x == 0:
        return 5e-5
    a = a0 + a_slope * x
    V_fu = a**3 / 4
    n_cm3 = x / (2 * V_fu) * 1e24
    r1_cm = (a * math.sqrt(3) / 4) * 1e-8

    p_CeCe = (1-x)**2
    p_CeSm = 2*x*(1-x)
    p_SmSm = x**2
    E_m_eff = p_CeCe*E_m_CeCe + p_CeSm*E_m_CeSm + p_SmSm*E_m_SmSm

    f_1NN = math.exp(-3.5 * x)
    E_ass_eff = f_1NN * E_ass_1NN + (1 - f_1NN) * E_ass_2NN

    E_a = max(E_m_eff + E_ass_eff, 0.01)
    return scale * n_cm3 * (r1_cm**2) * math.exp(-E_a / kT) / T

x_vals = [i/20.0 for i in range(9)]
rows = [["x", "sigma"]]
for x in x_vals:
    rows.append([f"{x:.2f}", f"{sigma(x):.6e}"])
with open("/app/outputs/conductivity.csv", "w", newline="") as f:
    w = csv.writer(f)
    for r in rows:
        w.writerow(r)
PYEOF
