#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: migration_parameters.json ===
cat > /app/outputs/migration_parameters.json << 'EOF'
[
  {"cluster": "1He", "migration_barrier": 0.071, "migration_barrier_error": 0.007, "dissolution_energy": null, "dissolution_energy_error": null},
  {"cluster": "2He", "migration_barrier": 0.09, "migration_barrier_error": 0.01, "dissolution_energy": null, "dissolution_energy_error": null},
  {"cluster": "3He", "migration_barrier": 0.17, "migration_barrier_error": 0.01, "dissolution_energy": null, "dissolution_energy_error": null},
  {"cluster": "4He", "migration_barrier": 0.28, "migration_barrier_error": 0.02, "dissolution_energy": null, "dissolution_energy_error": null},
  {"cluster": "1He-1H", "migration_barrier": 0.21, "migration_barrier_error": 0.03, "dissolution_energy": 0.52, "dissolution_energy_error": 0.02},
  {"cluster": "1He-2H", "migration_barrier": 0.25, "migration_barrier_error": 0.03, "dissolution_energy": 0.51, "dissolution_energy_error": 0.04},
  {"cluster": "2He-1H", "migration_barrier": 0.23, "migration_barrier_error": 0.02, "dissolution_energy": 0.79, "dissolution_energy_error": 0.01},
  {"cluster": "2He-2H", "migration_barrier": 0.25, "migration_barrier_error": 0.04, "dissolution_energy": 0.77, "dissolution_energy_error": 0.08},
  {"cluster": "3He-1H", "migration_barrier": 0.40, "migration_barrier_error": 0.03, "dissolution_energy": 0.98, "dissolution_energy_error": 0.09}
]
EOF
