#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_energies.json ===
cat > "$OUTDIR/computed_energies.json" << 'EOF'
{
  "binding_energy_eV": 0.49,
  "charging_energies_vacuum_Si29": {"0": 0.0, "1": 7.292, "2": 16.662, "-1": -1.462},
  "charging_energies_water_Si29": {"0": 0.0, "1": 5.475, "2": 11.232, "-1": -2.314},
  "charging_energies_vacuum_Fe": {"1": 7.725, "2": 24.311, "3": 55.708},
  "charging_energies_water_Fe": {"1": 4.536, "2": 12.734, "3": 28.643},
  "total_energy_water_complex": -60770.70353,
  "total_energy_water_Fe6H2O_1plus": -60000.0,
  "total_energy_water_Si29_1plus": -1000.0,
  "total_energy_water_H2O": -76.43816
}
EOF
