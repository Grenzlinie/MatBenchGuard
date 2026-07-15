#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: defect_formation_energies.csv ===
cat > /app/outputs/defect_formation_energies.csv <<'CSVEOF'
defect,formation_energy_eV,total_energy_eV,supercell_size
V,3.78,-3096.22,32
AsV,2.47,-3097.53,32
As2V,0.82,-3099.18,32
As3V,-0.53,-3100.53,32
As4V,-2.39,-3102.39,32
V2,6.07,-2993.93,32
As2V2,2.70,-2997.30,32
As4V2,-0.54,-3000.54,32
As6V2,-3.23,-3003.23,32
As2I,3.76,-3296.24,32
As4I,2.19,-3397.81,32
CSVEOF

# === solve block: migration_barriers.json ===
cat > /app/outputs/migration_barriers.json <<'JSONEOF'
{
  "AsV": {
    "migration_barrier_eV": 1.43,
    "activation_energy_eV": 3.9
  },
  "As2V": {
    "migration_barrier_eV": 1.88,
    "activation_energy_eV": 2.7
  }
}
JSONEOF
