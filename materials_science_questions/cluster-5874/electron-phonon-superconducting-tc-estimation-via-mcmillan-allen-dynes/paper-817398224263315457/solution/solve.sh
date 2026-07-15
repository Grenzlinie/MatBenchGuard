#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_phonon_stability.txt ===
cat > /app/outputs/step_01_phonon_stability.txt <<'EOF'
No imaginary frequencies found.
EOF

# === solve block: step_02_epc_properties.json ===
cat > /app/outputs/step_02_epc_properties.json <<'EOF'
{
  "total_EPC_lambda": 1.47,
  "logavg_phonon_freq_omega_log": 188.0,
  "Tc_McMillan": 21.0,
  "Tc_Eliashberg": 21.7,
  "gap_6K": 5.0
}
EOF

# === solve block: step_03_eliasberg_spectral_function.json ===
python3 /solution/generate_eliashberg.py /app/outputs/step_03_eliasberg_spectral_function.json
