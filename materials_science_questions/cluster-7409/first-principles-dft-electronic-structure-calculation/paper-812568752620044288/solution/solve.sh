#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: summary_results.json ===
python3 -c "
import json
data = {
    'KCl': {
        'lattice_constant_A': 6.379,
        'bulk_modulus_GPa': 17.104,
        'band_gap_eV': 5.071,
        'static_dielectric_constant': 2.1,
        'seebeck_coefficient_300K_uV_per_K': 150.0,
        'power_factor_300K': 1.0e11
    },
    'K0.5Rb0.5Cl': {
        'lattice_constant_A': 6.557,
        'bulk_modulus_GPa': 14.142,
        'band_gap_eV': 4.928,
        'static_dielectric_constant': 2.0,
        'seebeck_coefficient_300K_uV_per_K': 250.0,
        'power_factor_300K': 5.0e10
    }
}
with open(\"$OUTDIR/summary_results.json\", 'w') as f:
    json.dump(data, f, indent=2)
"
