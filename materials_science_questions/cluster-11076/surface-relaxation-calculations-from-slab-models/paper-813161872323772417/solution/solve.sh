#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_04_results.json ===
python3 - << PYEOF
import json

data = {
    "bulk": {
        "Ba_moment": 0.12,
        "C_moment": 1.48
    },
    "surfaces": [
        {
            "name": "001",
            "Ba_moment": 0.11,
            "C_moment": 1.54,
            "half_metallic": True,
            "majority_gap": 1.67
        },
        {
            "name": "111-Ba",
            "Ba_moment": 0.06,
            "half_metallic": True,
            "majority_gap": 1.2
        },
        {
            "name": "111-C",
            "C_moment": 2.08,
            "half_metallic": True,
            "majority_gap": 1.8
        }
    ],
    "interfaces": [
        {
            "name": "Ba-Sn",
            "Ba_moment": 0.071,
            "C_moment": 1.48,
            "half_metallic": False
        },
        {
            "name": "Ba-Se",
            "Ba_moment": 0.070,
            "C_moment": 1.48,
            "half_metallic": False
        },
        {
            "name": "C-Sn",
            "Ba_moment": 0.12,
            "C_moment": 0.286,
            "half_metallic": False
        },
        {
            "name": "C-Se",
            "Ba_moment": 0.12,
            "C_moment": 1.881,
            "half_metallic": False
        }
    ]
}

with open("$OUTDIR/step_04_results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
