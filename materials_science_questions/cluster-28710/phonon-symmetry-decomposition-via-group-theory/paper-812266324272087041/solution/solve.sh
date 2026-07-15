#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: decomposition_results.json ===
python3 -c '
import json, os
outdir = os.environ.get("OUTDIR", "/app/outputs")
os.makedirs(outdir, exist_ok=True)
out = {
  "irrep_decomposition": {
    "A1": 7, "A2": 9, "B1": 7, "B2": 7, "E": 18
  },
  "total_modes": 66,
  "acoustic_modes": {"A2": 1, "E": 2},
  "optical_modes": {
    "IR_active": {"A2": 8},
    "Raman_active": {"A1": 7, "B1": 7, "B2": 7, "E": 17},
    "E_also_IR_active": True
  },
  "raman_tensor_forms": {
    "A1": [
      [1, 0, 0],
      [0, 1, 0],
      [0, 0, 2]
    ],
    "B1": [
      [1, 0, 0],
      [0, -1, 0],
      [0, 0, 0]
    ],
    "B2": [
      [0, 1, 0],
      [1, 0, 0],
      [0, 0, 0]
    ],
    "E": [
      [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0]
      ],
      [
        [0, 1, 0],
        [0, 0, 0],
        [1, 0, 0]
      ]
    ]
  }
}
with open(os.path.join(outdir, "decomposition_results.json"), "w") as f:
    json.dump(out, f, indent=2)
    f.write("\n")
'
