#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: table_data.json ===
cat > /app/outputs/table_data.json <<'FFEOF'
{
  "(10,10)": {
    "50K": {"a": 59.22, "b": 0.17, "c": -8.44},
    "300K": {"a": 65.36, "b": 0.63, "c": -8.39},
    "600K": {"a": 67.98, "b": 1.02, "c": -8.32},
    "900K": {"a": 74.22, "b": 1.52, "c": -8.26}
  },
  "(8,8)": {
    "50K": {"epsilon0": -0.0036},
    "300K": {"epsilon0": -0.009},
    "600K": {"epsilon0": -0.0154},
    "900K": {"epsilon0": -0.0194}
  },
  "(12,12)": {
    "50K": {"epsilon0": -0.0050},
    "300K": {"epsilon0": -0.0101},
    "600K": {"epsilon0": -0.0156},
    "900K": {"epsilon0": -0.0181}
  },
  "(17,0)": {
    "50K": {"epsilon0": -0.0073},
    "300K": {"epsilon0": -0.0150},
    "600K": {"epsilon0": -0.0179},
    "900K": {"epsilon0": -0.0232}
  }
}
FFEOF
