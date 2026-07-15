#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_fit_parameters.csv ===
python3 << 'PYEOF'
import csv, os

out_dir = os.environ.get("OUTDIR", "/app/outputs")
out_file = os.path.join(out_dir, "step_01_fit_parameters.csv")

with open(out_file, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Group", "a_dyne_cm", "a_eV", "b_dyne_cm2"])
    w.writerow(["IA",   2.50e-12,   1.56,    0.0])
    w.writerow(["IIA",  4.29e-12,   2.68,   -3.57e+10])
    w.writerow(["IIIA", 7.08e-12,   4.42,   -2.72e+11])
    w.writerow(["IIB",  4.79e-12,   2.99,   -1.98e+10])
    w.writerow(["IIIB", 4.76e-12,   2.97,   -1.38e+11])
    w.writerow(["IVB",  9.05e-12,   5.65,   -8.26e+11])
    w.writerow(["VB",  -1.08e-12,  -0.676,   4.68e+11])
    w.writerow(["VIB", -7.67e-12,  -4.79,    6.75e+11])
print("step_01_fit_parameters.csv written")
PYEOF

# === solve block: step_02_effective_masses.csv ===
python3 << 'PYEOF'
import csv, math

# Constants (cgs -> eV)
m_e   = 9.10956e-28          # g
hbar  = 1.0545718e-27        # erg·s
eV_erg = 1.602176634e-12     # 1 eV in erg
pi = math.pi

# Group IA slope a in dyne·cm from Table 2
a_dyne_cm_IA = 2.50e-12
a_eV_IA = a_dyne_cm_IA / eV_erg
eps_F_emp = 1.5 * a_eV_IA    # eV

# Alkali metals and their n_e (cm⁻³) from Table 1 (column n_e × 10^22)
elements = [
    ("Li", 4.6e22),
    ("Na", 2.652e22),
    ("K",  1.3e22),
    ("Rb", 1.148e22),
    ("Cs", 0.85e22),
]

C = (hbar**2 / (2.0 * m_e)) * (3.0 * pi**2) ** (2.0/3.0)   # erg·cm^2

with open("/app/outputs/step_02_effective_masses.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Element", "m_star_over_m"])
    for elem, ne in elements:
        eps_F_th_erg = C * (ne ** (2.0/3.0))
        eps_F_th_eV  = eps_F_th_erg / eV_erg
        ratio = eps_F_th_eV / eps_F_emp
        w.writerow([elem, f"{ratio:.6f}"])
PYEOF
