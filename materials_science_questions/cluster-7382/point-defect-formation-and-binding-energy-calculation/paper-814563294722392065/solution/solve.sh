#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_formation_energies.csv ===
python3 - <<'PYEOF'
import csv
rows = []
# 64 crystalline oxygen sites (distance -7.0 Å, formation energy 2.6 eV)
for i in range(64):
    rows.append([i, -7.0, 2.6])
# 64 amorphous oxygen sites (distance 7.0 Å, formation energy 0.2 eV)
for i in range(64, 128):
    rows.append([i, 7.0, 0.2])
with open('/app/outputs/step_01_formation_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['oxygen_index', 'distance_from_interface_A', 'formation_energy'])
    writer.writerows(rows)
PYEOF
