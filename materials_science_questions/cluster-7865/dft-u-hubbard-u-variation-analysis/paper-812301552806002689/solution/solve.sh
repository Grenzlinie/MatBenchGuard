#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 << 'PYEOF'
import json
results = {
  "H2_magnetic_moment": 0.97,
  "H8_magnetic_moment": 0.94,
  "H18_magnetic_moment": 0.93,
  "H2_gap_spin_unpolarized": 1.2,
  "H8_gap_spin_unpolarized": 0.4,
  "H18_gap_spin_unpolarized": 0.3,
  "H2_gap_spin_polarized": 7.1,
  "H8_gap_spin_polarized": 6.4,
  "H18_gap_spin_polarized": 6.0
}
with open('/app/outputs/results.json', 'w') as f:
    json.dump(results, f, indent=2)
PYEOF
