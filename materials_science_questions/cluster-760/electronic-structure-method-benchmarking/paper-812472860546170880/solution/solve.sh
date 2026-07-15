#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: benchmark_results.json ===
cat <<'FFEOF' > /app/outputs/benchmark_results.json
[
  {
    "functional": "APFD",
    "geometry_mae_pm": 97.0,
    "vibrational_mae_cm1": 13.52,
    "polarizability_mae_percent": 5.9,
    "ion_exchange_signed_error_kcalmol": 0.41,
    "interaction_energy_mae_kcalmol": -2.00,
    "delocalization_error_extremum_kcalmol": null,
    "torsion_barrier_signed_error_kcalmol": 2.22,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "B3LYP",
    "geometry_mae_pm": 60.0,
    "vibrational_mae_cm1": 22.41,
    "polarizability_mae_percent": 3.5,
    "ion_exchange_signed_error_kcalmol": -0.68,
    "interaction_energy_mae_kcalmol": 10.30,
    "delocalization_error_extremum_kcalmol": -7.52,
    "torsion_barrier_signed_error_kcalmol": 0.91,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "B3LYP-D3",
    "geometry_mae_pm": 44.0,
    "vibrational_mae_cm1": 23.13,
    "polarizability_mae_percent": 3.6,
    "ion_exchange_signed_error_kcalmol": -1.98,
    "interaction_energy_mae_kcalmol": 1.79,
    "delocalization_error_extremum_kcalmol": -7.49,
    "torsion_barrier_signed_error_kcalmol": 1.60,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "B97-D",
    "geometry_mae_pm": 133.0,
    "vibrational_mae_cm1": 16.94,
    "polarizability_mae_percent": 1.1,
    "ion_exchange_signed_error_kcalmol": 0.41,
    "interaction_energy_mae_kcalmol": -1.18,
    "delocalization_error_extremum_kcalmol": -10.09,
    "torsion_barrier_signed_error_kcalmol": -3.18,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "B97-D3",
    "geometry_mae_pm": 67.0,
    "vibrational_mae_cm1": 16.69,
    "polarizability_mae_percent": 0.7,
    "ion_exchange_signed_error_kcalmol": 1.07,
    "interaction_energy_mae_kcalmol": -0.52,
    "delocalization_error_extremum_kcalmol": -10.10,
    "torsion_barrier_signed_error_kcalmol": -2.57,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "HSE06",
    "geometry_mae_pm": 71.0,
    "vibrational_mae_cm1": 10.54,
    "polarizability_mae_percent": 5.7,
    "ion_exchange_signed_error_kcalmol": 0.55,
    "interaction_energy_mae_kcalmol": -1.04,
    "delocalization_error_extremum_kcalmol": -8.63,
    "torsion_barrier_signed_error_kcalmol": 1.01,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "M06-2X",
    "geometry_mae_pm": 53.0,
    "vibrational_mae_cm1": 17.01,
    "polarizability_mae_percent": 8.3,
    "ion_exchange_signed_error_kcalmol": -1.72,
    "interaction_energy_mae_kcalmol": 1.88,
    "delocalization_error_extremum_kcalmol": -3.12,
    "torsion_barrier_signed_error_kcalmol": 6.25,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "M06-HF",
    "geometry_mae_pm": 297.0,
    "vibrational_mae_cm1": 27.83,
    "polarizability_mae_percent": 9.6,
    "ion_exchange_signed_error_kcalmol": 1.22,
    "interaction_energy_mae_kcalmol": 3.99,
    "delocalization_error_extremum_kcalmol": 3.49,
    "torsion_barrier_signed_error_kcalmol": 10.4,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "M06-L",
    "geometry_mae_pm": 142.0,
    "vibrational_mae_cm1": 18.02,
    "polarizability_mae_percent": 6.8,
    "ion_exchange_signed_error_kcalmol": -2.06,
    "interaction_energy_mae_kcalmol": 3.09,
    "delocalization_error_extremum_kcalmol": -9.87,
    "torsion_barrier_signed_error_kcalmol": -0.53,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "MN15",
    "geometry_mae_pm": 58.0,
    "vibrational_mae_cm1": 20.91,
    "polarizability_mae_percent": 6.9,
    "ion_exchange_signed_error_kcalmol": 0.39,
    "interaction_energy_mae_kcalmol": -1.98,
    "delocalization_error_extremum_kcalmol": -4.38,
    "torsion_barrier_signed_error_kcalmol": 4.64,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "PBE0",
    "geometry_mae_pm": 72.0,
    "vibrational_mae_cm1": 12.22,
    "polarizability_mae_percent": 6.1,
    "ion_exchange_signed_error_kcalmol": 0.50,
    "interaction_energy_mae_kcalmol": -1.09,
    "delocalization_error_extremum_kcalmol": -6.65,
    "torsion_barrier_signed_error_kcalmol": 1.81,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "CAM-B3LYP",
    "geometry_mae_pm": 62.0,
    "vibrational_mae_cm1": 32.47,
    "polarizability_mae_percent": 7.2,
    "ion_exchange_signed_error_kcalmol": -0.64,
    "interaction_energy_mae_kcalmol": 6.92,
    "delocalization_error_extremum_kcalmol": -1.48,
    "torsion_barrier_signed_error_kcalmol": 6.53,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "CAM-B3LYP-D3",
    "geometry_mae_pm": 70.0,
    "vibrational_mae_cm1": 32.92,
    "polarizability_mae_percent": 7.2,
    "ion_exchange_signed_error_kcalmol": -1.95,
    "interaction_energy_mae_kcalmol": 2.15,
    "delocalization_error_extremum_kcalmol": -1.51,
    "torsion_barrier_signed_error_kcalmol": 7.31,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "LC-BLYP",
    "geometry_mae_pm": 188.0,
    "vibrational_mae_cm1": 100.66,
    "polarizability_mae_percent": 11.3,
    "ion_exchange_signed_error_kcalmol": -0.95,
    "interaction_energy_mae_kcalmol": 3.78,
    "delocalization_error_extremum_kcalmol": null,
    "torsion_barrier_signed_error_kcalmol": 12.8,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "LC-ωHPBE",
    "geometry_mae_pm": 89.0,
    "vibrational_mae_cm1": 32.49,
    "polarizability_mae_percent": 8.4,
    "ion_exchange_signed_error_kcalmol": -0.17,
    "interaction_energy_mae_kcalmol": 7.68,
    "delocalization_error_extremum_kcalmol": 1.46,
    "torsion_barrier_signed_error_kcalmol": 11.2,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "LC-ωPBE-D3",
    "geometry_mae_pm": 99.0,
    "vibrational_mae_cm1": 32.46,
    "polarizability_mae_percent": 10.8,
    "ion_exchange_signed_error_kcalmol": -1.34,
    "interaction_energy_mae_kcalmol": 1.55,
    "delocalization_error_extremum_kcalmol": null,
    "torsion_barrier_signed_error_kcalmol": 11.6,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "ωB97x-D",
    "geometry_mae_pm": 72.0,
    "vibrational_mae_cm1": 13.55,
    "polarizability_mae_percent": 7.7,
    "ion_exchange_signed_error_kcalmol": -0.37,
    "interaction_energy_mae_kcalmol": 2.37,
    "delocalization_error_extremum_kcalmol": 1.46,
    "torsion_barrier_signed_error_kcalmol": 6.47,
    "exciton_stability_delta_EST_kcalmol": null
  },
  {
    "functional": "DSD-PBEP86",
    "geometry_mae_pm": null,
    "vibrational_mae_cm1": null,
    "polarizability_mae_percent": null,
    "ion_exchange_signed_error_kcalmol": null,
    "interaction_energy_mae_kcalmol": null,
    "delocalization_error_extremum_kcalmol": null,
    "torsion_barrier_signed_error_kcalmol": null,
    "exciton_stability_delta_EST_kcalmol": null
  }
]
FFEOF
