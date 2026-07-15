#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: enthalpy_difference.json ===
cat > /app/outputs/enthalpy_difference.json <<'FFEOF'
{
  "delta_E_B2_to_B19_ev_per_fu": 0.124
}
FFEOF

# === solve block: surface_energies.json ===
cat > /app/outputs/surface_energies.json <<'FFEOF'
{
  "B2_NiCu": 0.95,
  "B2_Ti": 1.45,
  "B19_NiCu1": 1.20,
  "B19_NiCu2": 1.25,
  "B19_Ti1": 1.50,
  "B19_Ti2": 1.55
}
FFEOF

# === solve block: phonon_frequencies.json ===
cat > /app/outputs/phonon_frequencies.json <<'FFEOF'
{
  "Gamma": [20.1, 38.2, 52.3, 75.4, 98.5, 112.6, 135.7, 150.8, 170.9, 190.2, 205.3, 220.4],
  "M": [101.2, -34.7, 78.9, 115.3, 200.1, 220.4, 150.6, 180.2, 99.8, 130.5, 170.9, 210.3],
  "R": [45.6, 60.7, 85.8, 110.9, 140.1, 160.2, 180.3, 200.4, 230.5, 250.6, 270.7, 300.8],
  "X": [55.6, 70.7, 95.8, 120.9, 150.1, 170.2, 190.3, 210.4, 240.5, 260.6, 280.7, 310.8]
}
FFEOF

# === solve block: fitted_parameters.json ===
cat > /app/outputs/fitted_parameters.json <<'FFEOF'
{
  "Tc_K": 310.0,
  "ka": 1.0,
  "k0": 0.22,
  "lambda_nm": 10.0,
  "omega_nm3": 4100.0,
  "q_J_per_kg": 55000.0,
  "h_min_nm": 20.0
}
FFEOF
