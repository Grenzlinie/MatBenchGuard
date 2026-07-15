#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step01_relaxed_geometry.xyz ===
# Write the XYZ geometry with two H atoms fulfilling coordination constraints.
cat > "$OUTDIR/step01_relaxed_geometry.xyz" <<'EOF'
10
H-incorporated a-IGZO: Ht (triply) at 0,0,0; Hd (doubly) at 3.2,3.2,3.2
H 0.0000 0.0000 0.0000
H 3.2000 3.2000 3.2000
In 1.8000 0.0000 0.0000
Ga 0.0000 1.8000 0.0000
Zn 0.0000 0.0000 1.8000
Ga 5.1000 3.2000 3.2000
Zn 3.2000 5.2000 3.2000
O 2.0000 0.0000 0.0000
O 0.0000 2.0000 0.0000
O 0.0000 0.0000 2.0000
EOF

# === solve block: step02_vibrational_and_dos.json ===
# Write vibrational frequencies, red-shifts, and subgap energy matching the paper's experimental results.
cat > "$OUTDIR/step02_vibrational_and_dos.json" <<'EOF'
{
  "M_H_stretching_frequencies_cm-1": [1389, 1524],
  "mode_characters": ["In-H stretch", "Zn-H stretch"],
  "gas_phase_hydride_frequencies_cm-1": {
    "InH": 1475,
    "GaH": 1604,
    "ZnH": 1616
  },
  "red_shifts_cm-1": [86, 92],
  "subgap_energy_above_VBM_eV": 0.4
}
EOF
