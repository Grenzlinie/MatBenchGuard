#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: relaxed_params.json ===
cat > "${OUTDIR}/relaxed_params.json" <<'FFEOF'
{
  "u": 0.221,
  "v": 0.813,
  "units": "dimensionless"
}
FFEOF

# === solve block: partial_charges.json ===
cat > "${OUTDIR}/partial_charges.json" <<'FFEOF'
{
  "Hf1": {"s": 2.316, "p": 6.071, "d": 1.397, "f": 13.984},
  "Hf2": {"s": 2.303, "p": 6.084, "d": 1.314, "f": 13.977},
  "Co": {"s": 0.595, "p": 6.519, "d": 7.492, "f": 0.019},
  "units": "electrons"
}
FFEOF

# === solve block: efg_params.json ===
cat > "${OUTDIR}/efg_params.json" <<'FFEOF'
{
  "16c": {"V_ZZ": -0.4, "eta": 0.0, "site": "Hf1"},
  "48f": {"V_ZZ": -18.4, "eta": 0.43, "site": "Hf2"},
  "units": "V_ZZ in 10^17 V/cm^2"
}
FFEOF
