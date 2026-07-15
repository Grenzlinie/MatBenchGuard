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
  "band_gap": 0.60,
  "phonon_stable": true,
  "hole_mobility": 138.0,
  "electron_mobility": 24.82,
  "n_type_power_factor": 40.0,
  "p_type_power_factor": 16.0,
  "n_opt_doping": 4.0e20,
  "p_opt_doping": 2.5e19,
  "max_short_circuit_current": 4.2
}
FFEOF
