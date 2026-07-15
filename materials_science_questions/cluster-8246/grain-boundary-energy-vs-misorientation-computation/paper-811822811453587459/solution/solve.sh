#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: segregation_energies.json ===
python3 - <<'PYEOF'
import json

results = {
    "as_segregation_energy_meV": -100.0,
    "asplus_segregation_energy_meV": -33.0,
    "ga_segregation_energy_meV": 0.0,
    "as_relaxation_energy_gb_meV": 50.0,
    "as_relaxation_energy_bk_meV": 45.0,
    "asplus_relaxation_energy_gb_meV": 50.0,
    "ga_relaxation_energy_gb_meV": 50.0,
    "as_ionization_increase_meV": 80.0,
    "bulk_as_binding_energy_meV": 13.0,
    "interface_band_energy_meV": -10.0
}

with open("/app/outputs/segregation_energies.json", "w") as f:
    json.dump(results, f, indent=2)
PYEOF
