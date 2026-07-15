#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: theoretical_gms.json ===
python3 -c "import json; P_sigma=0.4; P_alpha=0.5; gms=(P_sigma**2 - P_alpha**2)/(1-P_sigma**2); gms_percent=gms*100; json.dump({'GMS_percent': gms_percent}, open('/app/outputs/theoretical_gms.json','w'))"
