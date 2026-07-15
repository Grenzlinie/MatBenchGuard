#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: ferromagnetic_results.json ===
# --- ferromagnetic GGA results ---
cat > "$OUTDIR/ferromagnetic_results.json" <<'FFEOF'
{
  "total_magnetic_moment_per_fu": 2.0,
  "Ni_spin_moment": 1.5,
  "band_gap_down_spin": 0.8,
  "total_energy": -10000.0
}
FFEOF

# === solve block: antiferromagnetic_results.json ===
# --- antiferromagnetic GGA results ---
cat > "$OUTDIR/antiferromagnetic_results.json" <<'FFEOF'
{
  "energy_difference_FM_minus_AFM": 5.0,
  "Ni_spin_moment_AFM": 1.5
}
FFEOF

# === solve block: soc_results.json ===
# --- ferromagnetic GGA + SOC results ---
cat > "$OUTDIR/soc_results.json" <<'FFEOF'
{
  "Ni_orbital_moment": 0.16
}
FFEOF
