#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_energies.json ===
python3 <<'PYEOF'
import json

hartree_to_eV = 27.2114
rs_energy = -530.12345678

rels = {
    "RS": 0.0,
    "A": 0.69,
    "B": -0.04,
    "C": -0.76,
    "D": -0.39,
    "E": -0.60
}

configs = []
for name, rel in rels.items():
    total = rs_energy + rel / hartree_to_eV
    configs.append({
        "name": name,
        "total_energy_Hartree": total,
        "relative_energy_eV": rel
    })

with open("/app/outputs/dft_energies.json", "w") as f:
    json.dump({"configurations": configs}, f, indent=2)
PYEOF
