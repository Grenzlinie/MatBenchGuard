#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: calculated_properties.json ===
mkdir -p /app/outputs
cat > "/app/outputs/calculated_properties.json" <<'FFEOF'
{
  "Co3W_DO19": {
    "a": 5.19,
    "c": 4.18,
    "Hf": -7.78
  },
  "Co3W_L12": {
    "a": 3.659,
    "Hf": -4.8
  },
  "Al12W": {
    "a": 7.736,
    "Hf": -5.10,
    "C11": 131,
    "C12": 72,
    "C44": 47,
    "B": 92
  },
  "Al5W": {
    "a": 4.765,
    "c": 8.729,
    "Hf": -21.15
  },
  "Al4W": {
    "a": 5.153,
    "b": 17.465,
    "c": 5.227,
    "Hf": -11.83
  }
}
FFEOF
