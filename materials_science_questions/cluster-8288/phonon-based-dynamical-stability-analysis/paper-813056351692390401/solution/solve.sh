#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

# Create output directory
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: results.json ===
cat > $OUTDIR/results.json << 'EOFJSON'
{
  "energies": {
    "1T'": {
      "surface_energy_asymptote_J_per_m2": 0.005,
      "cleaving_energy_asymptote_J_per_m2": 0.288,
      "binding_energy_asymptote_eV": 22.28,
      "vdw_energy_asymptote_J_per_m2": 0.47
    },
    "2H": {
      "surface_energy_asymptote_J_per_m2": 0.183,
      "cleaving_energy_asymptote_J_per_m2": 0.304,
      "binding_energy_asymptote_eV": 22.04,
      "vdw_energy_asymptote_J_per_m2": 0.36
    },
    "3R": {
      "surface_energy_asymptote_J_per_m2": 0.233,
      "cleaving_energy_asymptote_J_per_m2": 0.351,
      "binding_energy_asymptote_eV": 22.86,
      "vdw_energy_asymptote_J_per_m2": 0.37
    }
  },
  "bandgap_2H": [
    {"layer": 1, "bandgap_eV": 2.219},
    {"layer": 2, "bandgap_eV": 1.707},
    {"layer": 3, "bandgap_eV": 1.532},
    {"layer": 4, "bandgap_eV": 1.472},
    {"layer": 5, "bandgap_eV": 1.452},
    {"layer": 6, "bandgap_eV": 1.445},
    {"layer": 7, "bandgap_eV": 1.442},
    {"layer": 8, "bandgap_eV": 1.441},
    {"layer": 10, "bandgap_eV": 1.441},
    {"layer": 12, "bandgap_eV": 1.441},
    {"layer": 15, "bandgap_eV": 1.441},
    {"layer": 20, "bandgap_eV": 1.441}
  ],
  "optical": {
    "1T'": {
      "eps1_0_fit_coeffs": [15.967, 17.158, 4.25],
      "n_0_fit_coeffs": [3.991, 3.338, 3.278],
      "eps1_inf_fit_coeffs": [0.552, -0.363, 25.419],
      "n_inf_fit_coeffs": [0.729, -0.228, 29.029],
      "absorption_fit_coeffs": [2.360, 1.558, 3.60],
      "reflectivity_fit_coeffs": [0.440, -0.320, 2.952]
    },
    "2H": {
      "eps1_0_fit_coeffs": [5.580, 5.512, 2.44],
      "n_0_fit_coeffs": [2.330, 1.392, 2.401],
      "eps1_inf_fit_coeffs": [0.552, -0.362, 27.178],
      "n_inf_fit_coeffs": [0.735, -0.221, 30.181],
      "absorption_fit_coeffs": [2.725, 1.656, 3.973],
      "reflectivity_fit_coeffs": [0.492, -0.312, 3.30]
    },
    "3R": {
      "eps1_0_fit_coeffs": [12.565, 15.117, 2.758],
      "n_0_fit_coeffs": [3.588, 3.176, 2.416],
      "eps1_inf_fit_coeffs": [0.640, -0.272, 21.539],
      "n_inf_fit_coeffs": [0.791, -0.164, 24.048],
      "absorption_fit_coeffs": [1.797, 1.262, 3.220],
      "reflectivity_fit_coeffs": [0.392, -0.306, 2.866]
    }
  }
}
EOFJSON
