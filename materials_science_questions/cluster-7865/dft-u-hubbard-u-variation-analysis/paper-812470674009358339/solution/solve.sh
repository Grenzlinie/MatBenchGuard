#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: ni_u_scan.json ===
python3 -c "
import json, sys
sys.path.insert(0, '/solution')
from generate_scans import get_ni_scan
with open('/app/outputs/ni_u_scan.json', 'w') as f:
    json.dump(get_ni_scan(), f, indent=2)
"

# === solve block: co_u_scan.json ===
python3 -c "
import json, sys
sys.path.insert(0, '/solution')
from generate_scans import get_co_scan
with open('/app/outputs/co_u_scan.json', 'w') as f:
    json.dump(get_co_scan(), f, indent=2)
"

# === solve finalize ===
echo 'All scan files written.'
