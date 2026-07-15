#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_energies.json ===
cat > "$OUTDIR/step_01_energies.json" <<'FFEOF'
{
  "structure_b_total_energy": -10400.0,
  "structure_c_total_energy": -10401.18,
  "delta_E": 1.18
}
FFEOF

# === solve block: step_02_vibrations.json ===
cat > "$OUTDIR/step_02_vibrations.json" <<'FFEOF'
[
  {"mode": "ν(OH)", "frequency": 3329, "assignment": "OH stretch"},
  {"mode": "δ1(OH)", "frequency": 1036, "assignment": "bending mode 1"},
  {"mode": "δ2(OH)", "frequency": 986, "assignment": "bending mode 2"},
  {"mode": "δ3(OH)", "frequency": 831, "assignment": "bending mode 3"},
  {"mode": "ν(Pt–OH)", "frequency": 436, "assignment": "Pt-OH stretch"},
  {"mode": "T∥(Pt–OH)", "frequency": 244, "assignment": "translational parallel"},
  {"mode": "T⊥(Pt–OH)", "frequency": 154, "assignment": "translational perpendicular"}
]
FFEOF
