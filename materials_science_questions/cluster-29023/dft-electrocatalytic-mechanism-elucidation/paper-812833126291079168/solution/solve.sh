#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 <<'PYEOF'
import json, os

data = {
    "systems": {
        "pristine": {
            "free_energy_steps": {
                "OER": [1.200, 1.450, 1.640, 0.630],
                "ORR": [-0.630, -1.640, -1.450, -1.200]
            },
            "overpotentials": {
                "ORR": 0.600,
                "OER": 0.410
            }
        },
        "on_graphene": {
            "free_energy_steps": {
                "OER": [1.200, 1.450, 1.640, 0.630],
                "ORR": [-0.630, -1.640, -1.450, -1.200]
            },
            "overpotentials": {
                "ORR": 0.600,
                "OER": 0.410
            }
        },
        "on_Ni111": {
            "free_energy_steps": {
                "OER": [1.000, 1.130, 2.020, 0.770],
                "ORR": [-0.770, -2.020, -1.130, -1.000]
            },
            "overpotentials": {
                "ORR": 0.460,
                "OER": 0.790
            }
        },
        "on_graphene_Ni111": {
            "free_energy_steps": {
                "OER": [0.920, 1.610, 1.170, 1.220],
                "ORR": [-1.220, -1.170, -1.610, -0.920]
            },
            "overpotentials": {
                "ORR": 0.310,
                "OER": 0.380
            }
        }
    }
}

out_path = os.environ.get("OUTDIR", "/app/outputs") + "/results.json"
with open(out_path, "w") as f:
    json.dump(data, f, indent=2)
print(f"Written {out_path}")
PYEOF
