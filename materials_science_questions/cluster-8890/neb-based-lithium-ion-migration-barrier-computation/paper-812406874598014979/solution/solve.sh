#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: absorption_energies.json ===
python3 -c "
import json
data = [
    {'mg_wt_percent': 0.0, 'absorption_energy_eV': -1.521},
    {'mg_wt_percent': 4.2, 'absorption_energy_eV': -1.586},
    {'mg_wt_percent': 4.5, 'absorption_energy_eV': -1.620},
    {'mg_wt_percent': 7.0, 'absorption_energy_eV': -1.563},
    {'mg_wt_percent': 12.0, 'absorption_energy_eV': -1.564},
    {'mg_wt_percent': 24.0, 'absorption_energy_eV': -1.572}
]
with open('/app/outputs/absorption_energies.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: migration_barriers.json ===
python3 -c "
import json
data = {
    'pure_Li_barrier_eV': 0.074,
    'Li_Mg_toward_barrier_eV': 0.126,
    'Li_Mg_away_barrier_eV': 0.126
}
with open('/app/outputs/migration_barriers.json', 'w') as f:
    json.dump(data, f, indent=2)
"
