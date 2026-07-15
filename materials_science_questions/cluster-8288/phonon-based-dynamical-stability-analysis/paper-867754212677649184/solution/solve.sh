#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dos_and_band_analysis.json ===
cat > "$OUTDIR/dos_and_band_analysis.json" <<'EOF'
{
  "vhs_energy_relative_to_fermi_meV": 70.0,
  "dos_at_fermi_states_per_eV_formula_unit": 7.34,
  "vhs_present_at_L_point": true
}
EOF

# === solve block: phonon_frequencies.json ===
cat > "$OUTDIR/phonon_frequencies.json" <<'EOF'
{
  "minimum_phonon_frequency_cm-1": 20.0,
  "imaginary_modes_present": false
}
EOF
