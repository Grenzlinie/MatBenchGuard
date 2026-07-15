#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies.json ===
cat > /app/outputs/formation_energies.json <<'FFEOF'
{
  "Ni": {
    "<100>": { "Ni-Ni": 3.2 },
    "<110>": { "Ni-Ni": 3.6 },
    "<111>": { "Ni-Ni": 4.0 }
  },
  "Ni3Fe": {
    "<100>": {
      "Ni-Ni": 2.5,
      "Ni-Fe": 2.8,
      "Fe-Ni": 3.1,
      "Fe-Fe": 3.3
    },
    "<110>": {
      "Ni-Ni": 3.0,
      "Ni-Fe": 3.4,
      "Fe-Fe": 3.7
    },
    "<111>": {
      "Fe-Ni": 3.8,
      "Fe-Fe": 4.1
    }
  },
  "Ni3Co": {
    "<100>": {
      "Ni-Co": 2.9,
      "Co-Co": 2.95,
      "Co-Ni": 3.2,
      "Ni-Ni": 3.5
    },
    "<110>": {
      "Ni-Co": 3.1,
      "Co-Co": 3.3,
      "Ni-Ni": 3.7
    },
    "<111>": {
      "Co-Co": 3.6,
      "Co-Ni": 3.9
    }
  }
}
FFEOF

# === solve block: migration_barriers.json ===
cat > /app/outputs/migration_barriers.json <<'FFEOF'
{
  "Ni": {
    "3D_<111>_to_<110>": 0.17,
    "3D_<100>_trans_rot": 0.14
  },
  "Ni3Co": {
    "1D_<110>_translation": 0.07,
    "3D_<111>_to_<110>": 0.08,
    "3D_<100>_trans_rot": 0.21
  },
  "Ni3Fe": {
    "3D_<111>_to_<110>": 0.12,
    "3D_<100>_trans_rot": 0.39
  }
}
FFEOF
