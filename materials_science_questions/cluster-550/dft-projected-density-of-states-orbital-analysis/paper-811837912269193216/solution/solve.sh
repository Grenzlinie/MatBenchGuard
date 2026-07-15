#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: outputs.json ===
OUTDIR="${OUTDIR:-/app/outputs}"
cat > "$OUTDIR/outputs.json" <<'FFEOF'
{
  "B_prime": 5.61,
  "C11_GPa": 114.4,
  "C12_GPa": 47.8,
  "C44_GPa": 34.3,
  "bulk_modulus_B_GPa": 70.0,
  "lattice_constant_a_nm": 0.3471,
  "total_DOS_at_Fermi_level_N_EF_states_per_eV": 1.32
}
FFEOF
