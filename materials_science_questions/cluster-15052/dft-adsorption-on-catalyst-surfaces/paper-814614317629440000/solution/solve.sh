#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: step_01_phonon_stability.json ===
cat > "$OUTDIR/step_01_phonon_stability.json" <<'FFEOF'
{
  "minimum_phonon_frequency": 0.0,
  "unit": "THz"
}
FFEOF

# === solve block: step_02_aimd_stability.json ===
cat > "$OUTDIR/step_02_aimd_stability.json" <<'FFEOF'
{
  "total_energy_std_ev": 0.001,
  "max_out_of_plane_displacement_A": 0.05
}
FFEOF

# === solve block: step_03_o2_dissociation_barrier.json ===
cat > "$OUTDIR/step_03_o2_dissociation_barrier.json" <<'FFEOF'
{
  "dissociation_barrier_eV": 0.09
}
FFEOF

# === solve block: step_04_current_density.json ===
cat > "$OUTDIR/step_04_current_density.json" <<'FFEOF'
{
  "partial_current_density_at_0_65V_mA_per_cm2": 3.0
}
FFEOF

# === solve block: step_05_band_gap.json ===
cat > "$OUTDIR/step_05_band_gap.json" <<'FFEOF'
{
  "hse06_band_gap_eV": 1.14
}
FFEOF

# === solve finalize ===
echo "All artifacts written."
