#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_bulk_and_defect_formation.json ===
python3 - <<'PYEOF'
import json
data = {
  "bulk_lattice_constant_A": 5.433,
  "bulk_band_gap_eV": 1.15,
  "defect_formation_energies": {
    "(CN)_Si_0": 3.0,
    "C_Si_0": 2.0,
    "(NSi)_Si_0": 1.61
  },
  "charge_transition_levels": {
    "(CN)_Si_0_to_minus1": 0.98
  }
}
with open("/app/outputs/step_01_bulk_and_defect_formation.json", "w") as f:
    json.dump(data, f, indent=2)
print("step_01 written")
PYEOF

# === solve block: step_02_main_results.json ===
python3 - <<'PYEOF'
import json
data = {
  "decomposition_energy_eV": 0.61,
  "migration_barrier_eV": 0.68,
  "dW_factor_percent": 5.0,
  "zpl_values_meV": {
    "supercell_216": 809.0,
    "supercell_512": 820.0,
    "supercell_1000": 824.0
  },
  "extrapolated_zpl_meV": 828.0,
  "radiative_lifetime_us": 4.18
}
with open("/app/outputs/step_02_main_results.json", "w") as f:
    json.dump(data, f, indent=2)
print("step_02 written")
PYEOF
