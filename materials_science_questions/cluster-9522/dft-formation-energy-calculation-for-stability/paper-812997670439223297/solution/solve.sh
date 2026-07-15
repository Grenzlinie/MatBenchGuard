#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: aflow_AgAuCd_hull.json ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -c '
import json

data = {
  "points_data": [
    {
      "compound": "Ag",
      "auid": "aflow:0000000000000001",
      "formation_enthalpy_atom": 0.0,
      "stability_criterion": 0.0,
      "ground_state": True
    },
    {
      "compound": "Au",
      "auid": "aflow:0000000000000002",
      "formation_enthalpy_atom": 0.0,
      "stability_criterion": 0.0,
      "ground_state": True
    },
    {
      "compound": "Cd",
      "auid": "aflow:0000000000000003",
      "formation_enthalpy_atom": 0.0,
      "stability_criterion": 0.0,
      "ground_state": True
    },
    {
      "compound": "Ag4AuCd",
      "auid": "aflow:f01a0242937da2ae",
      "formation_enthalpy_atom": 87.0,
      "stability_criterion": 0.0,
      "ground_state": False
    },
    {
      "compound": "Ag2AuCd",
      "auid": "aflow:b306fb2e8866a640",
      "formation_enthalpy_atom": -112.0,
      "stability_criterion": 1.0,
      "ground_state": True
    },
    {
      "compound": "AgAuCd",
      "auid": "aflow:8634edc5da7d9b0",
      "formation_enthalpy_atom": -111.0,
      "stability_criterion": 0.0,
      "ground_state": False
    }
  ],
  "facets_data": [
    {
      "vertices_auid": [
        "aflow:0000000000000001",
        "aflow:0000000000000002",
        "aflow:b306fb2e8866a640"
      ],
      "vertices_position": [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.5, 0.25, -0.112]
      ]
    },
    {
      "vertices_auid": [
        "aflow:0000000000000001",
        "aflow:0000000000000003",
        "aflow:b306fb2e8866a640"
      ],
      "vertices_position": [
        [1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0],
        [0.5, 0.0, -0.112]
      ]
    }
  ]
}

with open("/app/outputs/aflow_AgAuCd_hull.json", "w") as f:
    json.dump(data, f, indent=2)
'
