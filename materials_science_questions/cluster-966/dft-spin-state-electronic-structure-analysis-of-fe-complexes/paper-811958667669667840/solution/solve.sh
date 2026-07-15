#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: formation_energies.json ===
cat > "$OUTDIR/formation_energies.json" <<'EOF'
{
  "E_rel_II": -0.23,
  "E_rel_IMa_vs_II": -0.10,
  "E_rot": -0.11,
  "E_MQ_vs_IQ": 0.09
}
EOF

# === solve block: absorption_peaks.json ===
cat > "$OUTDIR/absorption_peaks.json" <<'EOF'
{
  "IQ": [
    {"wavelength_nm": 274, "intensity": 1.0},
    {"wavelength_nm": 301, "intensity": 0.95},
    {"wavelength_nm": 347, "intensity": 0.85},
    {"wavelength_nm": 750, "intensity": 0.2}
  ],
  "II": [
    {"wavelength_nm": 350, "intensity": 0.7},
    {"wavelength_nm": 620, "intensity": 1.0}
  ],
  "IMa": [
    {"wavelength_nm": 350, "intensity": 0.8},
    {"wavelength_nm": 570, "intensity": 1.0}
  ],
  "IMb": [
    {"wavelength_nm": 350, "intensity": 0.8},
    {"wavelength_nm": 510, "intensity": 1.0}
  ],
  "IMIM": [
    {"wavelength_nm": 350, "intensity": 0.8},
    {"wavelength_nm": 480, "intensity": 1.0}
  ],
  "planar_stacked": [
    {"wavelength_nm": 400, "intensity": 1.0}
  ]
}
EOF

# === solve block: dipole_strength.json ===
cat > "$OUTDIR/dipole_strength.json" <<'EOF'
{
  "IQ": 13.9,
  "II": 30.0,
  "IMa": 37.0,
  "IMb": 38.4,
  "IMIM": 50.2,
  "planar_stacked": 47.7
}
EOF

# === solve block: stacking_energy.json ===
cat > "$OUTDIR/stacking_energy.json" <<'EOF'
{
  "planar_stacking_energy_eV": -3.58
}
EOF
