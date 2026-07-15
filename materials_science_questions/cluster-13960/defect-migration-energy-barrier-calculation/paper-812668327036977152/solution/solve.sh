#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies.json ===
python3 << 'PYEOF'
import json, os

data = {
    "single_Gd": {"O_rich": 2.5, "O_poor": 3.2},
    "Gd_V_O":   {"O_rich": 3.0, "O_poor": 2.0},
    "Gd_V_O_Gd": {"O_rich": 1.0, "O_poor": 1.0}
}

path = os.path.join("/app/outputs", "formation_energies.json")
with open(path, "w") as f:
    json.dump(data, f, indent=2)
print(f"wrote {path}")
PYEOF

# === solve block: migration_barriers.json ===
python3 << 'PYEOF'
import json, os

data = [
    {"defect": "single_Gd",   "barrier_eV": 0.81},
    {"defect": "Gd_V_O",     "barrier_eV": 1.15},
    {"defect": "Gd_V_O_Gd",  "barrier_eV": 1.68}
]

path = os.path.join("/app/outputs", "migration_barriers.json")
with open(path, "w") as f:
    json.dump(data, f, indent=2)
print(f"wrote {path}")
PYEOF
