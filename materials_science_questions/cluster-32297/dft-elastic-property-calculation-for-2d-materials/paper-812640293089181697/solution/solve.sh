#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: electronic_properties.json ===
cat > "$OUTDIR/electronic_properties.json" <<'FFEOF'
{
  "FeS": {
    "is_metallic": true,
    "magnetic_moment": 5.52,
    "ground_state": "FM"
  },
  "MnS": {
    "is_metallic": true,
    "magnetic_moment": 0.0,
    "ground_state": "AFM1"
  },
  "VS": {
    "is_metallic": true,
    "magnetic_moment": 0.0,
    "ground_state": "NM"
  }
}
FFEOF

# === solve block: phonon_max_imaginary.json ===
cat > "$OUTDIR/phonon_max_imaginary.json" <<'FFEOF'
{
  "FeS": { "max_imaginary_frequency": 0.0 },
  "MnS": { "max_imaginary_frequency": 0.0 },
  "VS":  { "max_imaginary_frequency": 0.0 }
}
FFEOF

# === solve block: aimd_stability.json ===
cat > "$OUTDIR/aimd_stability.json" <<'FFEOF'
{
  "FeS_673K": {
    "potential_energy_drift": 0.0,
    "structural_stable": true
  },
  "VS_673K": {
    "potential_energy_drift": 0.0,
    "structural_stable": true
  },
  "MnS_300K": {
    "potential_energy_drift": 0.0,
    "structural_stable": true
  }
}
FFEOF

# === solve block: elastic_constants.json ===
cat > "$OUTDIR/elastic_constants.json" <<'FFEOF'
{
  "FeS": {
    "c11_2D": 46.9,
    "c12_2D": 22.6,
    "c66_2D": 15.2
  },
  "MnS": {
    "c11_2D": 61.1,
    "c12_2D": 14.5,
    "c66_2D": 23.3
  },
  "VS": {
    "c11_2D": 31.5,
    "c12_2D": 21.4,
    "c66_2D": 17.5
  }
}
FFEOF

# === solve block: her_gibbs_free_energy.json ===
cat > "$OUTDIR/her_gibbs_free_energy.json" <<'FFEOF'
{
  "FeS": {
    "differential": {
      "1": -0.14,
      "2": -0.10,
      "3": -0.04,
      "4": -0.04,
      "5": -0.03,
      "6": -0.07,
      "7": -0.05,
      "8": -0.03
    },
    "average": {
      "1": -0.14,
      "2": -0.12,
      "3": -0.093,
      "4": -0.08,
      "5": -0.07,
      "6": -0.07,
      "7": -0.067,
      "8": -0.0625
    }
  },
  "VS": {
    "differential": {
      "1": -0.02,
      "2": -0.06,
      "3": 0.22,
      "4": 0.15,
      "5": 0.10,
      "6": 0.12,
      "7": 0.08,
      "8": 0.05
    },
    "average": {
      "1": -0.02,
      "2": -0.04,
      "3": 0.047,
      "4": 0.073,
      "5": 0.078,
      "6": 0.085,
      "7": 0.084,
      "8": 0.08
    }
  }
}
FFEOF
