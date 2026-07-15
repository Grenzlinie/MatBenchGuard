#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 << 'EOF'
import json
data = {
  'materials': ['MoC', 'WC', 'MoN', 'WN'],
  'supercells': ['1x1', '2x2', '3x3', '4x4'],
  'surface_energies': {
    'MoC': {
      '1x1': {'gamma_rel': 0.77, 'units': 'J/m2'},
      '2x2': {'gamma_rel': 0.67, 'units': 'J/m2'},
      '3x3': {'gamma_rel': 0.70, 'units': 'J/m2'},
      '4x4': {'gamma_rel': 0.67, 'units': 'J/m2'}
    },
    'WC': {
      '1x1': {'gamma_rel': 0.66, 'units': 'J/m2'},
      '2x2': {'gamma_rel': 0.59, 'units': 'J/m2'},
      '3x3': {'gamma_rel': 0.62, 'units': 'J/m2'},
      '4x4': {'gamma_rel': 0.61, 'units': 'J/m2'}
    },
    'MoN': {
      '1x1': {'gamma_rel': -0.77, 'units': 'J/m2'},
      '2x2': {'gamma_rel': -0.75, 'units': 'J/m2'},
      '3x3': {'gamma_rel': -0.67, 'units': 'J/m2'},
      '4x4': {'gamma_rel': -0.79, 'units': 'J/m2'}
    },
    'WN': {
      '1x1': {'gamma_rel': -1.57, 'units': 'J/m2'},
      '2x2': {'gamma_rel': -1.35, 'units': 'J/m2'},
      '3x3': {'gamma_rel': -1.81, 'units': 'J/m2'},
      '4x4': {'gamma_rel': -1.83, 'units': 'J/m2'}
    }
  },
  'imaginary_frequencies_MoC': {
    '1x1': False,
    '2x2': True
  },
  'geometric_parameters': {
    'MoC': {
      'd_MC_surface': 0.18,
      'd_MC_subsurface': 0.05,
      'alpha_surface': 10,
      'alpha_subsurface': 10,
      'units': {'distance': 'angstrom', 'angle': 'deg'}
    },
    'WC': {
      'd_MC_surface': 0.17,
      'd_MC_subsurface': 0.05,
      'alpha_surface': 10,
      'alpha_subsurface': 12,
      'units': {'distance': 'angstrom', 'angle': 'deg'}
    },
    'MoN': {
      'd_MC_surface': 0.07,
      'd_MC_subsurface': 0.05,
      'alpha_surface': 13,
      'alpha_subsurface': 12,
      'units': {'distance': 'angstrom', 'angle': 'deg'}
    },
    'WN': {
      'd_MC_surface': 0.32,
      'd_MC_subsurface': 1.24,
      'alpha_surface': 13,
      'alpha_subsurface': 37,
      'units': {'distance': 'angstrom', 'angle': 'deg'}
    }
  },
  'bulk_energy_diff': {
    'MoC': {'Delta_E': 0.40, 'units': 'eV/f.u.'},
    'WC': {'Delta_E': 0.69, 'units': 'eV/f.u.'},
    'MoN': {'Delta_E': 0.62, 'units': 'eV/f.u.'},
    'WN': {'Delta_E': 0.81, 'units': 'eV/f.u.'}
  }
}
with open('/app/outputs/results.json', 'w') as f:
    json.dump(data, f, indent=2)
EOF
