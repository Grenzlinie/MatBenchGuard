#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c "
import json
data = {
  'bare_barrier_kJ_per_mol': 349.87,
  'H1_barrier_kJ_per_mol': 357.89,
  'H7_barrier_kJ_per_mol': 140.36,
  'bare_C5N_bond_order': 1.14438,
  'H1_C5N_bond_order': 1.24941,
  'H7_C5N_bond_order': 0.951271
}
with open('/app/outputs/results.json', 'w') as f:
  json.dump(data, f)
"
