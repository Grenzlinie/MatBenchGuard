#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -c '
import json

data = {
    "mo_sse_gaN": {
        "lattice_constant_A": 3.228,
        "interface_distance_A": 2.931,
        "formation_energy_meV_per_Ang2": -29.59,
        "band_gap_eV": 1.479,
        "cbm_vs_vacuum_eV": -4.25,
        "vbm_vs_vacuum_eV": -5.729,
        "carrier_mobilities": [
            {
                "direction": "armchair",
                "carrier_type": "electron",
                "effective_mass": 0.57,
                "deformation_potential_eV": -7.35,
                "elastic_modulus_N_per_m": 224.87,
                "mobility_cm2_V_s": 275.86
            },
            {
                "direction": "armchair",
                "carrier_type": "hole",
                "effective_mass": -1.84,
                "deformation_potential_eV": 0.65,
                "elastic_modulus_N_per_m": 224.87,
                "mobility_cm2_V_s": 3476.81
            },
            {
                "direction": "zigzag",
                "carrier_type": "electron",
                "effective_mass": 0.56,
                "deformation_potential_eV": -7.39,
                "elastic_modulus_N_per_m": 223.67,
                "mobility_cm2_V_s": 276.27
            },
            {
                "direction": "zigzag",
                "carrier_type": "hole",
                "effective_mass": -1.69,
                "deformation_potential_eV": 0.66,
                "elastic_modulus_N_per_m": 223.67,
                "mobility_cm2_V_s": 3651.83
            }
        ],
        "charge_transfer_e": 0.107,
        "potential_drop_eV": 7.03,
        "optical_absorption_peaks": [
            {
                "wavelength_nm": 127,
                "absorption_coefficient_cm1": 1580000.0
            },
            {
                "wavelength_nm": 425,
                "absorption_coefficient_cm1": 274000.0
            },
            {
                "wavelength_nm": 536,
                "absorption_coefficient_cm1": 186000.0
            }
        ]
    },
    "mo_sse_alN": {
        "lattice_constant_A": 3.228,
        "interface_distance_A": 2.683,
        "formation_energy_meV_per_Ang2": -25.73,
        "band_gap_eV": 1.420,
        "cbm_vs_vacuum_eV": -4.26,
        "vbm_vs_vacuum_eV": -5.68,
        "carrier_mobilities": [
            {
                "direction": "armchair",
                "carrier_type": "electron",
                "effective_mass": 0.64,
                "deformation_potential_eV": -5.54,
                "elastic_modulus_N_per_m": 226.92,
                "mobility_cm2_V_s": 384.51
            },
            {
                "direction": "armchair",
                "carrier_type": "hole",
                "effective_mass": -3.91,
                "deformation_potential_eV": 1.11,
                "elastic_modulus_N_per_m": 226.92,
                "mobility_cm2_V_s": 280.27
            },
            {
                "direction": "zigzag",
                "carrier_type": "electron",
                "effective_mass": 0.64,
                "deformation_potential_eV": -4.53,
                "elastic_modulus_N_per_m": 227.03,
                "mobility_cm2_V_s": 575.08
            },
            {
                "direction": "zigzag",
                "carrier_type": "hole",
                "effective_mass": -3.28,
                "deformation_potential_eV": 1.11,
                "elastic_modulus_N_per_m": 227.03,
                "mobility_cm2_V_s": 334.44
            }
        ],
        "charge_transfer_e": 0.158,
        "potential_drop_eV": 2.23,
        "optical_absorption_peaks": [
            {
                "wavelength_nm": 125,
                "absorption_coefficient_cm1": 1424000.0
            },
            {
                "wavelength_nm": 412,
                "absorption_coefficient_cm1": 395000.0
            },
            {
                "wavelength_nm": 528,
                "absorption_coefficient_cm1": 205000.0
            }
        ]
    }
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: results.json ===
echo "Written by preamble"
