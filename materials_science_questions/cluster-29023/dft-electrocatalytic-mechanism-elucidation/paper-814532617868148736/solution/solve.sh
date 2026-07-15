#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: adsorption_energies.json ===
python3 -c '
import json
data = {
    "surfaces": [
        {"type": "with_O2", "E_ads_eV": -0.74},
        {"type": "without_O2", "E_ads_eV": -0.54}
    ]
}
with open("/app/outputs/adsorption_energies.json", "w") as f:
    json.dump(data, f, indent=2)
print("Written adsorption_energies.json")
'
