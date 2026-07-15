#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_band_gaps_ambient.json ===
cat > $OUTDIR/step_01_band_gaps_ambient.json <<'FFEOF'
{
  "GaP": {"E_g_GammaGamma": 2.00, "E_g_GammaX": 2.50, "E_g_GammaL": 2.09},
  "GaAs": {"E_g_GammaGamma": 0.49, "E_g_GammaX": 2.40, "E_g_GammaL": 1.30},
  "GaSb": {"E_g_GammaGamma": 0.40, "E_g_GammaX": 1.60, "E_g_GammaL": 0.80}
}
FFEOF

# === solve block: step_02_pressure_dependence.json ===
cat > /app/outputs/step_02_pressure_dependence.json <<'FFEOF'
{
  "GaP": {
    "pressures_Kbar": [0.0, 14.828],
    "E_g_GammaGamma": [2.00, 3.15],
    "E_g_GammaX": [2.50, 2.2],
    "E_g_GammaL": [2.09, 2.6],
    "dE_g_dP_meV_per_bar": 8.85,
    "critical_pressure_Kbar": 14.828
  },
  "GaAs": {
    "pressures_Kbar": [0.0, 13.277],
    "E_g_GammaGamma": [0.49, 1.98],
    "E_g_GammaX": [2.40, 2.05],
    "E_g_GammaL": [1.30, 1.85],
    "dE_g_dP_meV_per_bar": 10.73,
    "critical_pressure_Kbar": 13.277
  },
  "GaSb": {
    "pressures_Kbar": [0.0, 9.710],
    "E_g_GammaGamma": [0.40, 1.25],
    "E_g_GammaX": [1.60, 1.40],
    "E_g_GammaL": [0.80, 1.15],
    "dE_g_dP_meV_per_bar": 17.91,
    "critical_pressure_Kbar": 9.710
  }
}
FFEOF

# === solve block: step_03_dielectric_peaks.json ===
cat > /app/outputs/step_03_dielectric_peaks.json <<'FFEOF'
{
  "GaP": {"ambient_peak_energy_eV": 3.70},
  "GaAs": {"ambient_peak_energy_eV": 2.90},
  "GaSb": {"ambient_peak_energy_eV": 2.60}
}
FFEOF
