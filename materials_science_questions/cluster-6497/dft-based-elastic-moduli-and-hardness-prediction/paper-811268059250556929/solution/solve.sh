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
python3 << PYEOF
import json
data = {
  "stability_pressure": 7.3,
  "bulk_modulus": 366,
  "shear_modulus": 256,
  "young_modulus": 622,
  "vickers_hardness": 46,
  "band_gap": 0.5
}
with open("$OUTDIR/results.json", "w") as f:
    json.dump(data, f)
PYEOF
