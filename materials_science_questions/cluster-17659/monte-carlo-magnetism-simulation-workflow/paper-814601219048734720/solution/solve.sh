#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
# No packages needed; use python3 stdlib only.

# === solve block: edwards_entropy.csv ===
python3 <<'PYEOF'
import sys
sys.path.insert(0, '/solution')
from helper import write_edwards_entropy_csv
write_edwards_entropy_csv('/app/outputs/edwards_entropy.csv')
PYEOF

# === solve block: edwards_temperature.json ===
python3 <<'PYEOF'
import sys
sys.path.insert(0, '/solution')
from helper import write_edwards_temperature_json
write_edwards_temperature_json('/app/outputs/edwards_temperature.json')
PYEOF

# === solve block: edwards_structure.csv ===
python3 <<'PYEOF'
import sys
sys.path.insert(0, '/solution')
from helper import write_edwards_structure_csv
write_edwards_structure_csv('/app/outputs/edwards_structure.csv')
PYEOF

# === solve block: dynamic_structure.csv ===
python3 <<'PYEOF'
import sys
sys.path.insert(0, '/solution')
from helper import write_dynamic_structure_csv
write_dynamic_structure_csv('/app/outputs/dynamic_structure.csv')
PYEOF

# === solve block: dynamic_temperature.json ===
python3 <<'PYEOF'
import sys
sys.path.insert(0, '/solution')
from helper import write_dynamic_temperature_json
write_dynamic_temperature_json('/app/outputs/dynamic_temperature.json')
PYEOF
