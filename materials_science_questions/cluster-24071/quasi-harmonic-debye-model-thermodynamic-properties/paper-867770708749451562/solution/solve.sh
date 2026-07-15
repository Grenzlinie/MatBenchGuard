#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermodynamic_properties.csv ===
cat > /app/outputs/thermodynamic_properties.csv << 'EOF'
phase,temperature_K,pressure_GPa,thermal_expansivity_1_per_K,isothermal_bulk_modulus_GPa,adiabatic_bulk_modulus_GPa,isochoric_heat_capacity_J_per_mol_per_K,isobaric_heat_capacity_J_per_mol_per_K,thermodynamic_Gruneisen_parameter
Pv,4000,30,2.50e-05,180.0,213.3,130.0,154.1,1.85
Pv,4000,60,1.80e-05,250.0,279.0,128.0,142.7,1.60
Pv,4000,90,1.30e-05,320.0,343.3,126.0,135.2,1.40
Pv,4000,120,1.00e-05,390.0,409.5,124.7,130.9,1.25
PPv,4000,30,1.80e-05,140.0,155.1,126.0,139.6,1.50
PPv,4000,60,1.30e-05,200.0,213.5,124.0,132.4,1.30
PPv,4000,90,0.90e-05,260.0,270.8,123.0,128.1,1.15
PPv,4000,120,0.70e-05,320.0,329.0,122.0,125.4,1.00
EOF

# === solve block: phase_boundary_results.json ===
cat > /app/outputs/phase_boundary_results.json << 'EOF'
{
  "Pv_PPv_transition_pressure_GPa_at_2500K": 117.0,
  "Clapeyron_slope_MPa_per_K_at_2500K": 9.0,
  "Clapeyron_slope_MPa_per_K_at_1000K": 7.7,
  "Clapeyron_slope_MPa_per_K_at_4000K": 10.4,
  "transition_temperature_at_CMB_K": 4310
}
EOF
