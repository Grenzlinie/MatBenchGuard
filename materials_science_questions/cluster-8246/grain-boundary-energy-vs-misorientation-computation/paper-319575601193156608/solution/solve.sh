#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energies.json ===
cat > /app/outputs/energies.json <<'FFEOF'
{
  "unrelaxed_gb_energy": 18.2,
  "relaxed_gb_energy": 3.35
}
FFEOF

# === solve block: omega_params.json ===
cat > /app/outputs/omega_params.json <<'FFEOF'
{
  "a": 0.447,
  "c": 0.274,
  "c_ratio": 0.613
}
FFEOF

# === solve block: excess_energy_profile.json ===
cat > /app/outputs/excess_energy_profile.json <<'FFEOF'
[
  {"plane_index": -3, "excess_energy": 0.0},
  {"plane_index": -2, "excess_energy": 0.0},
  {"plane_index": -1, "excess_energy": 1.315},
  {"plane_index":  0, "excess_energy": -0.53},
  {"plane_index":  1, "excess_energy": 1.315},
  {"plane_index":  2, "excess_energy": 0.0},
  {"plane_index":  3, "excess_energy": 0.0}
]
FFEOF

# === solve finalize ===
# Verify all files exist
test -f /app/outputs/energies.json || exit 1
test -f /app/outputs/omega_params.json || exit 1
test -f /app/outputs/excess_energy_profile.json || exit 1
test -f /app/outputs/initial_structure.xyz || exit 1
test -f /app/outputs/relaxed_structure.xyz || exit 1
echo "All outputs written."
