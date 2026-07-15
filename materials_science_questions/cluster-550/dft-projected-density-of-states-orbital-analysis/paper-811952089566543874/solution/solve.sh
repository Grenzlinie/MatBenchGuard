#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: torsion_angles.json ===
cat > "$OUTDIR/torsion_angles.json" <<'FFEOF'
{
  "molecules": [
    {"name": "BP2T_L", "omega_deg": 30.0},
    {"name": "BP3T_H", "omega_deg": 5.0},
    {"name": "BP4T_L", "omega_deg": 30.0},
    {"name": "BP5T_H", "omega_deg": 5.0}
  ]
}
FFEOF

# === solve block: xps_shifts.json ===
cat > "$OUTDIR/xps_shifts.json" <<'FFEOF'
{
  "binding_energies": [
    {"molecule": "BP2T_L", "s2p3_2_eV": 161.4},
    {"molecule": "BP3T_H", "s2p3_2_eV": 161.9},
    {"molecule": "BP4T_L", "s2p3_2_eV": 161.3},
    {"molecule": "BP5T_H", "s2p3_2_eV": 161.8}
  ]
}
FFEOF

# === solve block: rairs_modes.json ===
cat > "$OUTDIR/rairs_modes.json" <<'FFEOF'
{
  "modes": [
    {"molecule": "BP3T_H", "frequency_cm-1": 1500.0, "intensity_arb": 1.0,  "label": "nu_a"},
    {"molecule": "BP3T_H", "frequency_cm-1": 1450.0, "intensity_arb": 1.0,  "label": "nu_b"},
    {"molecule": "BP3T_H", "frequency_cm-1": 1400.0, "intensity_arb": 1.0,  "label": "nu_c"},
    {"molecule": "BP3T_H", "frequency_cm-1": 1350.0, "intensity_arb": 1.0,  "label": "nu_d"},
    {"molecule": "BP4T_L", "frequency_cm-1": 1502.0, "intensity_arb": 1.21, "label": "nu_a"},
    {"molecule": "BP4T_L", "frequency_cm-1": 1471.0, "intensity_arb": 2.56, "label": "nu_b"},
    {"molecule": "BP4T_L", "frequency_cm-1": 1427.0, "intensity_arb": 1.07, "label": "nu_c"},
    {"molecule": "BP4T_L", "frequency_cm-1": 1353.0, "intensity_arb": 1.07, "label": "nu_d"}
  ]
}
FFEOF

# === solve finalize ===
# no further steps required
