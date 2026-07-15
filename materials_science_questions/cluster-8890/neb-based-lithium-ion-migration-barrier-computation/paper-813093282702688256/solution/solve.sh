#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: migration_barriers.json ===
python3 -c 'import json; json.dump({"Ti_I3+": 0.480, "Ti_II3+": 0.595, "Ti_III3+": 0.636, "All-Ti4+": 0.602}, open("/app/outputs/migration_barriers.json","w"))'
