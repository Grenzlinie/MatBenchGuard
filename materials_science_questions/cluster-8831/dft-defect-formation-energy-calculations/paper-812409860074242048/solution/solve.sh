#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: defect_energies.json ===
cat > "$OUTDIR/defect_energies.json" << 'JSONEOF'
{
  "E_Si64": -790.0,
  "E_Si65": -820.0,
  "E_Si63C": -779.8934,
  "E_Si64C": -810.0,
  "E_intermediate": -809.96325,
  "E_Si65_p2": -819.984,
  "E_Si63B_m1": -779.0,
  "E_Si64B_p1": -809.0,
  "E_f_Si_i": 3.7,
  "E_b_Ci": 1.45,
  "E_m_Ci": 0.5,
  "E_a": 3.05,
  "E_b_BSi": 0.22
}
JSONEOF
