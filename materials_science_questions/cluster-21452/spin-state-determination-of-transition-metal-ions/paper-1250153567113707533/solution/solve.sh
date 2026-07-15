#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_spin_state_energies.json ===
cat > "$OUTDIR/step_01_spin_state_energies.json" <<'EOF'
[{"metal":"Mn","spin_state":"sextet","relative_energy_cm1":0.0},{"metal":"Mn","spin_state":"quartet","relative_energy_cm1":500.0},{"metal":"Mn","spin_state":"doublet","relative_energy_cm1":5000.0},{"metal":"Co","spin_state":"quartet","relative_energy_cm1":0.0},{"metal":"Co","spin_state":"doublet","relative_energy_cm1":3000.0},{"metal":"Ni","spin_state":"triplet","relative_energy_cm1":0.0},{"metal":"Ni","spin_state":"singlet","relative_energy_cm1":4000.0}]
EOF

# === solve block: step_02_isomer_energies.json ===
cat > /app/outputs/step_02_isomer_energies.json <<'EOF'
[{"metal":"Co","coordination":6,"relative_energy_cm1":126.0},{"metal":"Co","coordination":5,"relative_energy_cm1":0.0},{"metal":"Co","coordination":4,"relative_energy_cm1":5977.0},{"metal":"Cu","coordination":6,"relative_energy_cm1":505.0},{"metal":"Cu","coordination":5,"relative_energy_cm1":0.0},{"metal":"Cu","coordination":4,"relative_energy_cm1":1048.0},{"metal":"Zn","coordination":6,"relative_energy_cm1":108.0},{"metal":"Zn","coordination":5,"relative_energy_cm1":0.0},{"metal":"Zn","coordination":4,"relative_energy_cm1":4667.0}]
EOF

# === solve block: step_03_frequencies.json ===
cat > /app/outputs/step_03_frequencies.json <<'EOF'
[{"metal":"Co","coordination":6,"frequency_cm1":1642.5},{"metal":"Co","coordination":5,"frequency_cm1":1663.8},{"metal":"Co","coordination":4,"frequency_cm1":1688.1},{"metal":"Cu","coordination":6,"frequency_cm1":1638.7},{"metal":"Cu","coordination":5,"frequency_cm1":1667.4},{"metal":"Cu","coordination":4,"frequency_cm1":1695.2},{"metal":"Zn","coordination":6,"frequency_cm1":1644.1},{"metal":"Zn","coordination":5,"frequency_cm1":1662.3},{"metal":"Zn","coordination":4,"frequency_cm1":1690.5}]
EOF
