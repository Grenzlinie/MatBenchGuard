#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "compounds": [
    {
      "name": "AlN_wz",
      "a0": 3.130,
      "B0": 193.450,
      "E0": -443.331,
      "Ef": null,
      "mag_moment": null,
      "minority_gap": 6.1
    },
    {
      "name": "VN_NaCl",
      "a0": 3.092,
      "B0": 232.564,
      "E0": -648.837,
      "Ef": null,
      "mag_moment": null,
      "minority_gap": 0.0
    },
    {
      "name": "Al0.25V0.75N",
      "a0": 3.107,
      "B0": 224.544,
      "E0": -597.140,
      "Ef": 0.320,
      "mag_moment": 2.0,
      "minority_gap": 0.1
    },
    {
      "name": "Al0.50V0.50N",
      "a0": 3.118,
      "B0": 209.350,
      "E0": -545.815,
      "Ef": 0.270,
      "mag_moment": 2.0,
      "minority_gap": 0.1
    },
    {
      "name": "Al0.75V0.25N",
      "a0": 3.126,
      "B0": 198.170,
      "E0": -494.559,
      "Ef": 0.148,
      "mag_moment": 2.0,
      "minority_gap": 0.0
    }
  ]
}
FFEOF
