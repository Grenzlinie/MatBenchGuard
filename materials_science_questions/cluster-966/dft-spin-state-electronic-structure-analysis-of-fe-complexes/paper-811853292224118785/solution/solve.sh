#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: relative_energies.json ===
python3 <<'PYEOF'
import json

entries = [
    {"complex": "FeCl(BCP8)", "conformer": "αααα‑in", "spin": "HS", "relative_energy_cm-1": 0.0},
    {"complex": "FeCl(BCP8)", "conformer": "αααα‑out", "spin": "HS", "relative_energy_cm-1": 649.0},
    {"complex": "FeCl(BCP8)", "conformer": "αβαβ", "spin": "HS", "relative_energy_cm-1": 2746.0},
    {"complex": "FeCl(BCP8)", "conformer": "αααα‑in", "spin": "LS", "relative_energy_cm-1": 1307.0},
    {"complex": "FeCl(BCP8)", "conformer": "αααα‑out", "spin": "LS", "relative_energy_cm-1": 2075.0},
    {"complex": "FeCl(BCP8)", "conformer": "αβαβ", "spin": "LS", "relative_energy_cm-1": 3605.0},
    {"complex": "MnCl(BCP8)", "conformer": "αααα‑in", "spin": "HS", "relative_energy_cm-1": 0.0},
    {"complex": "MnCl(BCP8)", "conformer": "αααα‑out", "spin": "HS", "relative_energy_cm-1": 1719.0},
    {"complex": "MnCl(BCP8)", "conformer": "αβαβ", "spin": "HS", "relative_energy_cm-1": 3475.0}
]

with open("/app/outputs/relative_energies.json", "w") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)
PYEOF
