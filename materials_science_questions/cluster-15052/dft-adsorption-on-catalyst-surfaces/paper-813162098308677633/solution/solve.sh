#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{
  "Eads_CO_CrPc": -1.10,
  "Eads_O2_CrPc": -2.30,
  "Eads_CO_MnPc": -1.60,
  "Eads_O2_MnPc": -1.80,
  "Eads_CO_FePc": -2.10,
  "Eads_O2_FePc": -1.20,
  "E_coad_CrPc": -0.16,
  "Ea_LH_TS1": 0.55,
  "Ea_LH_TS2": 0.14,
  "Ea_ER_TS": 0.46
}
EOF

# === solve finalize ===
echo "All reference artifacts written."
