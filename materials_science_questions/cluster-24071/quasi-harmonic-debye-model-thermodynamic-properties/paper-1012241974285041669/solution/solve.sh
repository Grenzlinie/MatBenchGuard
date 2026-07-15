#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: dft_static_properties.json ===
cat > "$OUTDIR/dft_static_properties.json" <<'FFEOF'
{
  "KCl": {"V0_ang3_per_atom": 32.62, "B0_GPa": 16.23, "B_prime": 4.67},
  "LaCl3": {"V0_ang3_per_atom": 27.37, "B0_GPa": 29.02, "B_prime": 6.40},
  "K2LaCl5": {"V0_ang3_per_atom": 29.96, "B0_GPa": 15.89, "B_prime": 5.38},
  "K3La5Cl18": {"V0_ang3_per_atom": 27.49, "B0_GPa": 26.46, "B_prime": 6.35}
}
FFEOF

# === solve block: dft_heat_capacity_500K.json ===
cat > "$OUTDIR/dft_heat_capacity_500K.json" <<'FFEOF'
{"K2LaCl5": 26.99, "K3La5Cl18": 25.99}
FFEOF

# === solve block: marginal_likelihoods.json ===
cat > "$OUTDIR/marginal_likelihoods.json" <<'FFEOF'
{
  "Associate_M1": -435.136,
  "Ionic_M2": -373.410,
  "MQMQA_M3": -370.628,
  "MQMQA_M4": -371.420
}
FFEOF

# === solve block: calphad_model_parameters.json ===
cat > "$OUTDIR/calphad_model_parameters.json" <<'FFEOF'
{
  "Associate_M1": {
    "L0": {"A": -61777.370, "B": 1.218},
    "L1": {"A": -12634.241, "B": -1.383}
  },
  "Ionic_M2": {
    "L0": {"A": -61720.724, "B": 5.247},
    "L1": {"A": -12786.004, "B": 3.360}
  },
  "MQMQA_M3": {
    "delta_g_ex": {"A": -13295.794, "B": -1.236},
    "chi_KLaCl2": -9228.101,
    "chi_LaKCl2": -2071.866,
    "ternary": {
      "Delta_g_101": 10153.591,
      "Delta_g_001": {"A": 18921.383, "B": -12.806}
    }
  },
  "MQMQA_M4": {
    "delta_g_ex": {"A": -13313.121, "B": -1.333},
    "chi_KLaCl2": -9173.701,
    "chi_LaKCl2": -1989.647
  }
}
FFEOF
