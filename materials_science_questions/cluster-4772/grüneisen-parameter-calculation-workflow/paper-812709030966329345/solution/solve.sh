#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 << 'PYEOF'
import json

# Silicon Carbide (SiC)
Y_SiC = 4.4e11
eta = 2
P_M_SiC = Y_SiC / (6 * eta)               # Pa
rho_SiC = 3.2e3
M_SiC = 41e-3                            # kg/mol
vol_per_mol_SiC = M_SiC / rho_SiC        # m^3/mol
factor = (1 + 1/(12*eta))**3
U0_J_per_mol_SiC = P_M_SiC * vol_per_mol_SiC * factor
U0_kJ_per_mol_SiC = U0_J_per_mol_SiC / 1000.0

# Silicon (Si)
Y_Si = 4.0e10
P_M_Si = Y_Si / (6 * eta)                # Pa
rho_Si = 2.3e3
M_Si = 28.06e-3                          # kg/mol
vol_per_mol_Si = M_Si / rho_Si           # m^3/mol
U0_J_per_mol_Si = P_M_Si * vol_per_mol_Si * factor
U0_kJ_per_mol_Si = U0_J_per_mol_Si / 1000.0

results = {
    "SiC": {
        "P_M_Pa": P_M_SiC,
        "U0_kJ_per_mol": U0_kJ_per_mol_SiC
    },
    "Si": {
        "P_M_Pa": P_M_Si,
        "U0_kJ_per_mol": U0_kJ_per_mol_Si
    }
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(results, f, indent=2)
PYEOF
