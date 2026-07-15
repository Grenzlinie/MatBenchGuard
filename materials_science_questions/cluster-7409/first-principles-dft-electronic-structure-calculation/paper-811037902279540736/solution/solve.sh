#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: electronic_structure_results.json ===
python3 << 'PYEOF'
import json

results = {
    "LiTi2O4": {
        "band_gap": 0.0,
        "o2p_valence_band_width": 5.03,
        "valence_to_conduction_separation": 2.26,
        "t2g_eg_splitting_observed": True
    },
    "Li4Ti5O12": {
        "band_gap": 2.52,
        "o2p_valence_band_width": 5.00,
        "valence_to_conduction_separation": 2.52,
        "t2g_eg_splitting_observed": True
    },
    "Li2Ti2O4": {
        "band_gap": 0.0,
        "o2p_valence_band_width": 4.78,
        "valence_to_conduction_separation": 2.37,
        "t2g_eg_splitting_observed": True
    },
    "Li7Ti5O12": {
        "band_gap": 0.0,
        "o2p_valence_band_width": 5.25,
        "valence_to_conduction_separation": 2.91,
        "t2g_eg_splitting_observed": True
    }
}

with open('/app/outputs/electronic_structure_results.json', 'w') as f:
    json.dump(results, f, indent=2)
print("electronic_structure_results.json written")
PYEOF

# === solve block: optical_properties_results.json ===
python3 << 'PYEOF'
import json

results = {
    "LiTi2O4": {
        "static_dielectric_constant": 25.49,
        "dielectric_peak_A_energy": 1.42,
        "dielectric_peak_B_energy": 7.31,
        "absorption_peak_energies": [5.58, 6.27, 6.70, 7.51, 8.05, 10.02]
    },
    "Li4Ti5O12": {
        "static_dielectric_constant": 3.34,
        "dielectric_peak_A_energy": None,
        "dielectric_peak_B_energy": 4.68,
        "absorption_peak_energies": [2.95, 3.64, 4.07, 4.88, 5.42, 7.39]
    },
    "Li2Ti2O4": {
        "static_dielectric_constant": 62.29,
        "dielectric_peak_A_energy": 1.69,
        "dielectric_peak_B_energy": 7.56,
        "absorption_peak_energies": [5.83, 6.52, 6.95, 7.76, 8.30, 10.27]
    },
    "Li7Ti5O12": {
        "static_dielectric_constant": 56.48,
        "dielectric_peak_A_energy": 1.56,
        "dielectric_peak_B_energy": 7.44,
        "absorption_peak_energies": [5.71, 6.40, 6.83, 7.64, 8.18, 10.15]
    }
}

with open('/app/outputs/optical_properties_results.json', 'w') as f:
    json.dump(results, f, indent=2)
print("optical_properties_results.json written")
PYEOF

# === solve finalize ===
# Oracle writes both artifacts; nothing to finalize
