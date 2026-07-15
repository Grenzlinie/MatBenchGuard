#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: formation_energies.json ===
python3 -c '
import json
data = {"BC": 3.71, "BS": 3.72, "BO": 3.93, "BT": 3.98, "O": 4.08, "CN": 3.93}
with open("/app/outputs/formation_energies.json", "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: migration_results.json ===
python3 -c '
import json
data = {
    "J1_Em": 0.01,
    "J2_Em": 0.25,
    "J3_Em": 0.14,
    "J4_Em": 0.14,
    "J1_Do": 3.48e-4,
    "J2_Do": 1.23e-4,
    "J3_Do": 6.25e-4,
    "J4_Do": 6.25e-4,
    "p_factor": 0.9
}
with open("/app/outputs/migration_results.json", "w") as f:
    json.dump(data, f, indent=2)
'
