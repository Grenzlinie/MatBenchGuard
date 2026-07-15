#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: reconstruction_energies.json ===
cat > "$OUTDIR/reconstruction_energies.json" << 'EOF'
{
  "materials": [
    {"material": "Si", "core_type": "alpha", "reconstruction_energy_eV": 0.92},
    {"material": "GaAs", "core_type": "alpha", "reconstruction_energy_eV": 0.43},
    {"material": "GaAs", "core_type": "beta", "reconstruction_energy_eV": 0.56},
    {"material": "AlP", "core_type": "alpha", "reconstruction_energy_eV": 0.47},
    {"material": "AlP", "core_type": "beta", "reconstruction_energy_eV": 0.87}
  ]
}
EOF

# === solve block: AlP_electronic_structure_results.json ===
cat > "$OUTDIR/AlP_electronic_structure_results.json" << 'EOF'
{
  "bulk_gap_eV": 1.04,
  "unreconstructed_beta_half_filled_band_present": true,
  "reconstructed_beta_bonding_antibonding_gap_eV": 0.15,
  "alpha_reconstructed_resonant_level_position_below_VBM_eV": 4.0
}
EOF
