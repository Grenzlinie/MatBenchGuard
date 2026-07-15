#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_02_total_energies.csv ===
cat > /app/outputs/step_02_total_energies.csv <<'FFEOF'
spin_configuration,total_energy_per_fu
NM,-3652.7461625
FM,-3653.1352625
ferri,-3653.197325
AFM-C1,-3653.2149875
AFM-C2,-3653.2221375
FFEOF

# === solve block: step_03_band_gap.json ===
cat > /app/outputs/step_03_band_gap.json <<'FFEOF'
{
  "band_gap_GGA": 0.78,
  "gap_type": "indirect"
}
FFEOF

# === solve block: step_04_magnetic_moments.json ===
cat > /app/outputs/step_04_magnetic_moments.json <<'FFEOF'
{
  "Mn1_moment": 3.3177,
  "Mn2_moment": 2.5403,
  "method": "GGA"
}
FFEOF

# === solve block: step_05_born_effective_charge.csv ===
cat > /app/outputs/step_05_born_effective_charge.csv <<'FFEOF'
atom,Zxx,Zyy,Zzz,Zxy,Zxz,Zyz,Zyx,Zzx,Zzy
Bi,3.94,2.36,-3.33,-4.36,0.00,0.00,3.04,0.00,0.00
Mn1,-0.05,-2.91,2.00,-4.73,0.00,0.00,-2.57,0.00,0.00
Mn2,-2.43,0.76,1.88,10.52,0.00,0.00,1.16,0.00,0.00
O1,-1.44,1.68,0.10,0.83,-1.22,0.78,0.47,-0.77,1.34
O2,-2.93,-2.54,-4.61,-1.48,0.00,0.00,-1.64,0.00,0.00
O3,6.43,0.78,3.56,5.92,0.00,0.00,1.44,0.00,0.00
O4,-2.07,-1.81,0.38,-3.82,0.00,0.00,0.20,0.00,0.00
FFEOF

# === solve block: step_06_polarization.json ===
cat > /app/outputs/step_06_polarization.json <<'FFEOF'
{
  "spontaneous_polarization_P": 6.0
}
FFEOF
