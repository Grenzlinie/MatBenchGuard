#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dos_features.json ===
cat > /app/outputs/dos_features.json <<'FFEOF'
{
  "feature_A": {"min_energy": -0.5, "max_energy": 2.5},
  "feature_B": {"min_energy": -1.5, "max_energy": -0.5},
  "feature_C": {"min_energy": -3.5, "max_energy": -1.5},
  "feature_D": {"min_energy": -7.0, "max_energy": -3.8}
}
FFEOF

# === solve block: tb_parameters.json ===
cat > /app/outputs/tb_parameters.json <<'FFEOF'
{
  "pp_sigma": 0.40,
  "pp_pi": -0.13,
  "pd_sigma": -1.73,
  "pd_pi": 0.78,
  "bare_energy_d_minus_p": 0.4
}
FFEOF
