#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

eval $(python3 -c "
import math
NA = 6.02214076e23
muB = 9.274009994e-21  # erg/G (CGS)
kB = 1.380649e-16      # erg/K
g = 2.0
S = 1.5
theta = -4.0
conc = 200.0e-6
mu_eff = g * math.sqrt(S*(S+1)) * muB
C_Fe = NA * mu_eff**2 / (3 * kB)
C_imp = conc * C_Fe
chi_s = 0.33e-4
chi_orb = 4.77e-4
chi_pure = chi_s + chi_orb
print(f'CHI_S={chi_s}')
print(f'CHI_ORB={chi_orb}')
print(f'CHI_PURE={chi_pure}')
print(f'C_IMP={C_imp}')
")

# === solve block: spin_orbital_susceptibility.json ===
export CHI_S=3.3e-5
export CHI_ORB=4.77e-4
export CHI_PURE=0.00051
export C_IMP=0.000375
cat > "$OUTDIR/spin_orbital_susceptibility.json" <<JSONEOF
{
  "chi_s": 3.3e-5,
  "chi_orb": 4.77e-4,
  "units": "emu/mol"
}
JSONEOF

# === solve block: total_susceptibility.csv ===
python3 -c "
import os
chi_pure = float(os.environ['CHI_PURE'])
C_imp = float(os.environ['C_IMP'])
theta = -4.0
with open('$OUTDIR/total_susceptibility.csv', 'w') as f:
    f.write('T(K),chi_pure(emu/mol),chi_imp(emu/mol),chi_total(emu/mol)' + chr(10))
    for T in range(0, 301, 10):
        chi_imp = C_imp / (T - theta)
        chi_total = chi_pure + chi_imp
        f.write(f'{T},{chi_pure},{chi_imp},{chi_total}' + chr(10))
"
