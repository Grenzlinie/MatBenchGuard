#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies.json ===
cat > /app/outputs/formation_energies.json <<'EOF'
{
  "single_vacancy": {
    "0": 1.25,
    "2+": 2.43
  },
  "cluster_vacancy": {
    "0": -2.10,
    "4+": -1.85
  },
  "relative_stability": {
    "<111>": 0.0,
    "<111>_e": 0.15,
    "<100>": 0.52,
    "<110>": 0.39,
    "<100>_e": 0.61
  }
}
EOF

# === solve block: migration_barriers.json ===
cat > /app/outputs/migration_barriers.json <<'EOF'
{
  "single_vacancy": {
    "<100>": [0.57],
    "<110>": [1.22],
    "<111>": [1.51, 2.03]
  },
  "cluster_vacancy": {
    "<100>": [1.55, 2.01, 2.52, 3.07],
    "<110>": [3.12],
    "<111>": [3.48]
  }
}
EOF

# === solve block: aimd_analysis.json ===
cat > /app/outputs/aimd_analysis.json <<'EOF'
{
  "single_vacancy_system": {
    "total_time_ps": 4.0,
    "num_jumps": 5,
    "jump_pattern": "frequent diffusive jumps mainly along <100> direction"
  },
  "cluster_system": {
    "total_time_ps": 4.0,
    "num_jumps": 0,
    "jump_pattern": "vacancies vibrate around equilibrium positions; long-range diffusion does not occur"
  }
}
EOF

# === solve block: ce3_migration_barriers.json ===
cat > /app/outputs/ce3_migration_barriers.json <<'EOF'
[
  {"model": "A", "num_Ce3": 0, "barrier_eV": 0.57},
  {"model": "B", "num_Ce3": 1, "barrier_eV": 0.85},
  {"model": "C", "num_Ce3": 1, "barrier_eV": 0.95},
  {"model": "D", "num_Ce3": 2, "barrier_eV": 1.10},
  {"model": "E", "num_Ce3": 2, "barrier_eV": 1.20},
  {"model": "F", "num_Ce3": 2, "barrier_eV": 1.30},
  {"model": "G", "num_Ce3": 2, "barrier_eV": 1.40},
  {"model": "H", "num_Ce3": 2, "barrier_eV": 1.50}
]
EOF
