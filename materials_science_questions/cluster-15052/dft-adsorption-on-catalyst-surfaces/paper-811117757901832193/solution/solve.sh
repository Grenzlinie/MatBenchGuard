#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: adsorption_energies.csv ===
cat > "$OUTDIR/adsorption_energies.csv" <<'FFEOF'
molecule,substrate,adsorption_energy_eV
H2O,perfect,-0.187
H2O,MV,-0.193
H2O,DV,-0.205
O2,perfect,-0.489
O2,MV,-0.489
O2,DV,-0.705
FFEOF

# === solve block: adsorption_heights.csv ===
cat > "$OUTDIR/adsorption_heights.csv" <<'FFEOF'
molecule,substrate,height_A
H2O,perfect,3.01
H2O,MV,2.42
H2O,DV,2.66
O2,perfect,2.80
O2,MV,2.94
O2,DV,3.02
FFEOF

# === solve block: charge_transfer.csv ===
cat > "$OUTDIR/charge_transfer.csv" <<'FFEOF'
molecule,substrate,delta_q_e
H2O,perfect,0.010
H2O,MV,0.120
H2O,DV,0.050
O2,perfect,-0.036
O2,MV,-0.030
O2,DV,0.010
FFEOF

# === solve block: midgap_states.json ===
python3 -c "
import json
data = {
  'midgap_states': [
    {'molecule': 'H2O', 'substrate': 'perfect', 'has_midgap_state': False},
    {'molecule': 'H2O', 'substrate': 'MV', 'has_midgap_state': False},
    {'molecule': 'H2O', 'substrate': 'DV', 'has_midgap_state': False},
    {'molecule': 'O2', 'substrate': 'perfect', 'has_midgap_state': True},
    {'molecule': 'O2', 'substrate': 'MV', 'has_midgap_state': True},
    {'molecule': 'O2', 'substrate': 'DV', 'has_midgap_state': True}
  ]
}
with open('$OUTDIR/midgap_states.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: O2_dissociation_barriers.csv ===
cat > "$OUTDIR/O2_dissociation_barriers.csv" <<'FFEOF'
substrate,barrier_eV
perfect,0.81
MV,0.59
FFEOF
