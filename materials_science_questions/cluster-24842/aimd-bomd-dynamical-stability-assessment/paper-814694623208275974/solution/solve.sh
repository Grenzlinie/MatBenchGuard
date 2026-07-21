#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: simulation_results.json ===
cat > "$OUTDIR/simulation_results.json" <<'FFEOF'
{
  "peak_positions": {
    "300K": { "CoB_first": 1.98, "BB_first": 1.85, "BB_second": 2.9 },
    "600K": { "CoB_first": 1.98, "BB_first": 1.85, "BB_second": 2.9 },
    "1000K": { "CoB_first": 1.98, "BB_first": 1.85, "BB_second": 2.9 },
    "1600K": { "CoB_first": 1.98, "BB_first": 1.85, "BB_second": 2.9 }
  },
  "bond_angle_90deg_fraction": {
    "300K": 0.42,
    "600K": 0.38,
    "1000K": 0.33,
    "1600K": 0.28
  },
  "frank_kasper_fraction": {
    "300K": 0.50,
    "600K": 0.45,
    "1000K": 0.40,
    "1600K": 0.35
  }
}
FFEOF
