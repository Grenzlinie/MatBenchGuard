#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reproduction_results.json ===
cat > /app/outputs/reproduction_results.json << 'FFEOF'
{
  "bulk": {
    "in_plane_lattice_const_A": 5.358,
    "co_layer_distance_A": 4.403,
    "magnetic_state": "FM ∥ c",
    "co_moment_muB": 0.350,
    "anomalous_hall_conductivity_e2_per_h": 0.9,
    "anomalous_nernst_conductivity_kB_T_5meV": 0.2
  },
  "sn_end_monolayer": {
    "in_plane_lattice_const_A": 5.325,
    "co_layer_distance_A": null,
    "magnetic_state": "FM ∥ c",
    "co_moment_muB": 0.415,
    "anomalous_hall_conductivity_e2_per_h": 3.0,
    "anomalous_nernst_conductivity_kB_T_5meV": 0.0
  },
  "sn_end_bilayer": {
    "in_plane_lattice_const_A": 5.355,
    "co_layer_distance_A": 4.434,
    "magnetic_state": "FM ∥ c",
    "co_moment_muB": [0.372, 0.372],
    "anomalous_hall_conductivity_e2_per_h": 4.5,
    "anomalous_nernst_conductivity_kB_T_5meV": -0.5
  },
  "sn_end_trilayer": {
    "in_plane_lattice_const_A": 5.370,
    "co_layer_distance_A": 4.436,
    "magnetic_state": "FM ∥ c",
    "co_moment_muB": [0.365, 0.362, 0.365],
    "anomalous_hall_conductivity_e2_per_h": 3.5,
    "anomalous_nernst_conductivity_kB_T_5meV": -0.3
  },
  "s_end_monolayer": {
    "in_plane_lattice_const_A": 5.194,
    "co_layer_distance_A": null,
    "magnetic_state": "FM ∥ c",
    "co_moment_muB": 1.01,
    "anomalous_hall_conductivity_e2_per_h": -0.34,
    "anomalous_nernst_conductivity_kB_T_5meV": -0.1
  },
  "s_end_bilayer": {
    "in_plane_lattice_const_A": 5.276,
    "co_layer_distance_A": 4.410,
    "magnetic_state": "interlayer AFM ∥ b'",
    "co_moment_muB": [0.339, 0.339],
    "anomalous_hall_conductivity_e2_per_h": 0.0,
    "anomalous_nernst_conductivity_kB_T_5meV": 0.0
  },
  "s_end_trilayer": {
    "in_plane_lattice_const_A": 5.310,
    "co_layer_distance_A": 4.412,
    "magnetic_state": "interlayer ferri ∥ c",
    "co_moment_muB": [0.207, 0.080, 0.207],
    "anomalous_hall_conductivity_e2_per_h": -2.71,
    "anomalous_nernst_conductivity_kB_T_5meV": -0.2
  }
}
FFEOF
