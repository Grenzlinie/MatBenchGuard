#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: structural_properties.json ===
cat > /app/outputs/structural_properties.json <<'FFEOF'
{
  "InN": {"a": 4.9926, "B": 140.5343, "B_prime": 4.1757},
  "InP": {"a": 5.8814, "B": 67.7383, "B_prime": 4.3041},
  "InAs": {"a": 6.0898, "B": 56.5406, "B_prime": 4.0185},
  "InAs0.25N0.25P0.5": {"a": 5.7717, "B": 69.0549, "B_prime": 4.774},
  "InAs0.25N0.5P0.25": {"a": 5.5763, "B": 77.3433, "B_prime": 3.922},
  "InAs0.5N0.25P0.25": {"a": 5.8316, "B": 64.039, "B_prime": 3.8116}
}
FFEOF

# === solve block: band_gaps.json ===
cat > /app/outputs/band_gaps.json <<'FFEOF'
{
  "InN": {"E_g_direct": 0.79110, "E_g_indirect": 4.06859},
  "InP": {"E_g_direct": 1.66753, "E_g_indirect": 2.36479},
  "InAs": {"E_g_direct": 0.68182, "E_g_indirect": 2.19368},
  "InAs0.25N0.25P0.5": {"E_g_direct": 0.78529, "E_g_indirect": 2.99961},
  "InAs0.25N0.5P0.25": {"E_g_direct": 0.65339, "E_g_indirect": 3.11918},
  "InAs0.5N0.25P0.25": {"E_g_direct": 0.61100, "E_g_indirect": 2.97629}
}
FFEOF

# === solve block: quaternary_refractive_index.json ===
cat > /app/outputs/quaternary_refractive_index.json <<'FFEOF'
{
  "InAs0.25N0.25P0.5": 3.6,
  "InAs0.25N0.5P0.25": 3.69,
  "InAs0.5N0.25P0.25": 3.85
}
FFEOF
