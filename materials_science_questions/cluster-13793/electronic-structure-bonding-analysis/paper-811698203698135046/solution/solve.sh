#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "band_gap_undoped": 0.44,
  "band_gap_doped": 0.071,
  "net_charges_undoped": {
    "Co1": 0.58,
    "Co2": 0.56,
    "Ca": 1.2,
    "O": -0.79
  },
  "net_charges_doped": {
    "Cu": 0.53,
    "Co2": 0.54,
    "Ca": 1.18,
    "O": -0.78
  },
  "bond_orders_undoped": {
    "Co1-O": 0.31,
    "Co2-O": 0.26,
    "Ca-O": 0.15,
    "Co1-Co2": -0.36
  },
  "bond_orders_doped": {
    "Cu-O": 0.27,
    "Co2-O": 0.25,
    "Ca-O": 0.14,
    "Cu-Co2": -0.55
  }
}
FFEOF
