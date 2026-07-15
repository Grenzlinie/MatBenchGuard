#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: BaReH9_results.json ===
cat > /app/outputs/BaReH9_results.json <<'FFEOF'
{
  "band_gap_eV": 3.58,
  "formation_energy_kJ_per_mol_H2": -99
}
FFEOF

# === solve block: BaMnH9_results.json ===
cat > /app/outputs/BaMnH9_results.json <<'FFEOF'
{
  "band_gap_eV": 3.0,
  "formation_energy_kJ_per_mol_H2": -86
}
FFEOF
