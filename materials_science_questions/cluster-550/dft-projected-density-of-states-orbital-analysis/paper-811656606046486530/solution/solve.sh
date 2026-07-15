#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_lattice_constant.txt ===
echo "9.466" > "$OUTDIR/step_01_lattice_constant.txt"

# === solve block: step_02_dos_peak.json ===
cat > "$OUTDIR/step_02_dos_peak.json" <<'EOF'
{
  "peak_energy_eV": 0.21,
  "peak_height_states_per_eV_per_unit_cell": 200
}
EOF

# === solve block: step_03_zt_value.txt ===
echo "13.5" > "$OUTDIR/step_03_zt_value.txt"
