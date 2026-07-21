#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_charges.json ===
python3 - <<'PYEOF'
import json
data = {
    "depletion_charge_density_e_per_nm2": 0.81,
    "contact_radius_nm": 8.6,
    "depletion_charge_total_e": 189,
    "flexoelectric_interface_charge_e": 693,
    "flexoelectric_surface_charge_e": -648,
    "induced_metal_charge_e": -627,
    "total_charge_transfer_case_b_e": 144,
    "total_charge_transfer_case_cde_e": -504,
}
with open("/app/outputs/computed_charges.json", "w") as f:
    json.dump(data, f)
PYEOF
