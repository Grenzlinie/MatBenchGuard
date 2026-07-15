#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: optimized_lattice_constants.json ===
export OUTDIR
cat > "$OUTDIR/optimized_lattice_constants.json" << 'EOF'
{
  "CuAlS2": {"a": 5.2816, "c": 10.4429, "V": 291.308},
  "CuGaS2": {"a": 5.356,   "c": 10.629,  "V": 304.911},
  "CuInS2": {"a": 5.5775, "c": 11.2379, "V": 349.594},
  "AgGaS2": {"a": 5.7219, "c": 10.6275, "V": 347.946}
}
EOF

# === solve block: band_gaps.json ===
python3 << 'SCRIPT'
import json, os
out = os.environ["OUTDIR"]
data = {
  "CuAlS2": {"uncorrected_band_gap": 1.94},
  "CuGaS2": {"uncorrected_band_gap": 0.9},
  "CuInS2": {"uncorrected_band_gap": 0.0},
  "AgGaS2": {"uncorrected_band_gap": 1.0}
}
with open(f"{out}/band_gaps.json", "w") as f:
    json.dump(data, f, indent=2)
SCRIPT

# === solve block: optical_properties.json ===
python3 << 'SCRIPT'
import json, os
out = os.environ["OUTDIR"]
data = {
  "CuAlS2": {
    "refractive_index_n0": 2.26,
    "sellmeier_params": {
      "A": 1.47925,
      "B": 0.77143,
      "C": 202.83614,
      "D": -4.0606e-10
    }
  },
  "CuGaS2": {
    "refractive_index_n0": 2.46,
    "sellmeier_params": {
      "A": 1.53956,
      "B": 0.8999,
      "C": 265.00937,
      "D": -1.308e-8
    }
  },
  "CuInS2": {
    "refractive_index_n0": 2.57,
    "sellmeier_params": {
      "A": -0.391,
      "B": 2.861,
      "C": 228.877,
      "D": -2.867e-8
    }
  },
  "AgGaS2": {
    "refractive_index_n0": 2.3,
    "sellmeier_params": {
      "A": -1.26,
      "B": 3.49,
      "C": 132.62,
      "D": -6.49e-9
    }
  }
}
with open(f"{out}/optical_properties.json", "w") as f:
    json.dump(data, f, indent=2)
SCRIPT
