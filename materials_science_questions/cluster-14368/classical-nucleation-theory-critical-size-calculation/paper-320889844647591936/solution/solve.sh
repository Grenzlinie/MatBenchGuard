#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 -c "
import json

data = [
    {
        \"threshold\": \"rain\",
        \"volume_ratio\": 1.252,
        \"supersaturation\": 4.2,
        \"critical_radius_m\": 8.6e-8
    },
    {
        \"threshold\": \"cloud\",
        \"volume_ratio\": 1.38,
        \"supersaturation\": 7.9,
        \"critical_radius_m\": 6.4e-8
    },
    {
        \"threshold\": \"sensitive\",
        \"volume_ratio\": 1.42,
        \"supersaturation\": 9.9,
        \"critical_radius_m\": 5.9e-8
    }
]

with open(\"$OUTDIR/results.json\", \"w\") as f:
    json.dump(data, f, indent=2)
"
