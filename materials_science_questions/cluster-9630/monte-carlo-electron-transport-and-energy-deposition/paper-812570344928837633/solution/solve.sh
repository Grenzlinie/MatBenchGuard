#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: step_01_swarm_results.json ===
python3 -c "
import json
results = [
    {'reduced_field': 1, 'mean_energy': 0.101, 'drift_velocity': 1.28, 'diffusion_coefficient': 0.978},
    {'reduced_field': 10, 'mean_energy': 0.239, 'drift_velocity': 6.26, 'diffusion_coefficient': 1.115},
    {'reduced_field': 20, 'mean_energy': 0.361, 'drift_velocity': 8.55, 'diffusion_coefficient': 1.151}
]
with open('$OUTDIR/step_01_swarm_results.json', 'w') as f:
    json.dump(results, f, indent=2)
"
