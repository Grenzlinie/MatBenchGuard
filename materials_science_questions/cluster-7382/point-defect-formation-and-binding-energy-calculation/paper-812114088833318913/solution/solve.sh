#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: table_ii.json ===
cat > "$OUTDIR/table_ii.json" <<'FFEOF'
[
  {
    "k": 2,
    "x_liq": 0.693,
    "F_x_liq": 0.250,
    "x_min": 2.48,
    "alpha": 0.207,
    "n_over_v_liq": 3.35,
    "V_v_liq_n": 3.07,
    "a": 102,
    "g_v_liq": 340,
    "C": 12.3
  },
  {
    "k": 3,
    "x_liq": 0.549,
    "F_x_liq": 0.385,
    "x_min": 2.02,
    "alpha": 0.168,
    "n_over_v_liq": 3.27,
    "V_v_liq_n": 3.14,
    "a": 89,
    "g_v_liq": 290,
    "C": 8.2
  },
  {
    "k": 6,
    "x_liq": 0.358,
    "F_x_liq": 0.583,
    "x_min": 1.42,
    "alpha": 0.118,
    "n_over_v_liq": 3.03,
    "V_v_liq_n": 3.38,
    "a": 60,
    "g_v_liq": 180,
    "C": 5.8
  },
  {
    "k": 10,
    "x_liq": 0.256,
    "F_x_liq": 0.697,
    "x_min": 1.10,
    "alpha": 0.0921,
    "n_over_v_liq": 2.78,
    "V_v_liq_n": 3.63,
    "a": 39,
    "g_v_liq": 110,
    "C": 5.2
  }
]
FFEOF
