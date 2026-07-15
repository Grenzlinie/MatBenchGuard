#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_band_gap.json ===
python3 -c "
import json
data = {
    'BP_GDYO_band_gap_ev': 0.15,
    'bulk_BP_band_gap_ev': 0.30
}
with open('$OUTDIR/step_01_band_gap.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: step_02_migration_barriers.json ===
python3 -c "
import json
data = {
    'BP_GDYO_barrier_ev': 0.21,
    'defect_free_BP_edge_barrier_ev': 0.39,
    'edge_reconstructed_BP_barrier_ev': 0.83
}
with open('$OUTDIR/step_02_migration_barriers.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: step_03_adsorption_energies.json ===
python3 -c "
import json
data = {
    'BP_phase_adsorption_ev': -2.50,
    'GDYO_adsorption_ev': -2.16,
    'defect_free_BP_adsorption_ev': -1.96,
    'edge_reconstructed_BP_adsorption_ev': -1.50
}
with open('$OUTDIR/step_03_adsorption_energies.json', 'w') as f:
    json.dump(data, f, indent=2)
"
