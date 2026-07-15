#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: elastic_and_derived_moduli.json ===
cat > /app/outputs/elastic_and_derived_moduli.json << 'JSONEOF'
{
  "alpha": {
    "elastic_constants": {
      "C11": 426,
      "C44": 200,
      "C12": 114
    },
    "derived_moduli": {
      "B_VRH": 218,
      "G_VRH": 181,
      "E": 426,
      "Poisson_ratio": 0.175,
      "Vickers_hardness": 30.8
    }
  },
  "beta": {
    "elastic_constants": {
      "C11": 473,
      "C33": 426,
      "C44": 162,
      "C12": 124,
      "C13": 79
    },
    "derived_moduli": {
      "B_VRH": 214,
      "G_VRH": 172,
      "E": 407,
      "Poisson_ratio": 0.183,
      "Vickers_hardness": 28.5
    }
  }
}
JSONEOF
