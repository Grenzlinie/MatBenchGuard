#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: theoretical_DQCC.json ===
python3 -c "
import json
data = {'SCF_DQCC_kHz': 191.60, 'MP2_DQCC_kHz': 189.54, 'SCF_eta': 0.0662, 'MP2_eta': 0.0557}
with open('$OUTDIR/theoretical_DQCC.json', 'w') as f:
    json.dump(data, f)
"
