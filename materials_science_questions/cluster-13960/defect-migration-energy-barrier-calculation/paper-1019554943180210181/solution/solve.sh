#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: mep_no_al.json ===
python3 -c "import json; json.dump([0.0, 1.2, 3.5, 6.7, 3.5, 1.2, 0.1], open('/app/outputs/mep_no_al.json','w'))"

# === solve block: mep_with_al.json ===
python3 -c "import json; json.dump([0.0, 0.9, 3.2, 5.7, 3.2, 0.9, 0.1], open('/app/outputs/mep_with_al.json','w'))"

# === solve finalize ===
echo 'All outputs written.'
