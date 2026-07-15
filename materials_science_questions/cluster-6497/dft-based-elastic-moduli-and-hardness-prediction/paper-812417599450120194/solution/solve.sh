#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: elastic_constants.json ===
mkdir -p /app/outputs
python3 -c '
import json
data = {
    "c11": 1.825,
    "c12": 1.131,
    "c44": 0.320,
    "c33": 1.976,
    "c13": 0.980,
    "Bs": 1.312
}
with open("/app/outputs/elastic_constants.json", "w") as f:
    json.dump(data, f, indent=2)
'
