#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: formation_energies.json ===
python3 - <<'PYEOF'
import json
data = {
    "5/3": {"Ti_Co_RS": 0.09, "Ti_Co_CoO2": 0.22, "Ti_Ca": 2.07},
    "3/2": {"Ti_Co_RS": -0.06, "Ti_Co_CoO2": 0.60, "Ti_Ca": 1.91}
}
with open("%s/formation_energies.json" % "/app/outputs", "w") as f:
    json.dump(data, f)
PYEOF

# === solve finalize ===
echo "All artifacts written." >&2
