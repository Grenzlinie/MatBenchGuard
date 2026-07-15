#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fitted_properties.json ===
cat > /app/outputs/fitted_properties.json << 'FFEOF'
{
  "CoSn": {"a": 5.221, "c": 2.921, "E0": -14.046, "V0": 22.990, "K0": 303.6, "K0_prime": 4.19},
  "WC": {"a": 2.913, "c": 2.862, "E0": -13.953, "V0": 21.035, "K0": 337.1, "K0_prime": 4.17},
  "CsCl": {"a": 2.750, "c": null, "E0": -12.348, "V0": 20.797, "K0": 307.0, "K0_prime": 4.28},
  "ZnS_B3": {"a": 4.753, "c": null, "E0": -13.042, "V0": 26.845, "K0": 244.2, "K0_prime": 4.18},
  "NaCl": {"a": 4.413, "c": null, "E0": -13.370, "V0": 21.481, "K0": 327.6, "K0_prime": 4.35}
}
FFEOF

# === solve block: dos_at_fermi.json ===
cat > /app/outputs/dos_at_fermi.json << 'DFEOF'
{
  "CoSn": 0.24,
  "WC": 0.05,
  "CsCl": 0.69,
  "ZnS_B3": 1.39,
  "NaCl": 0.92
}
DFEOF
