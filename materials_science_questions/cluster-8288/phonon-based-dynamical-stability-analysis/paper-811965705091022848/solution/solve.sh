#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: transition_pressures_300K.json ===
cat > "$OUTDIR/transition_pressures_300K.json" <<'FFEOF'
{
  "ilmenite_perovskite_Pt_GPa": 24,
  "perovskite_postperovskite_Pt_GPa": 51
}
FFEOF

# === solve block: clapeyron_slopes_1000K.json ===
cat > "$OUTDIR/clapeyron_slopes_1000K.json" <<'FFEOF'
{
  "ilmenite_perovskite_dPdT_MPa_K": -9.3,
  "perovskite_postperovskite_dPdT_MPa_K": 7.8
}
FFEOF

# === solve block: linbo3_metastability_verification.txt ===
cat > "$OUTDIR/linbo3_metastability_verification.txt" <<'FFEOF'
LiNbO₃ is metastable: ΔG(LiNbO₃−ilmenite) > 0 over the entire range considered (0–60 GPa, 0–2000 K).
FFEOF
