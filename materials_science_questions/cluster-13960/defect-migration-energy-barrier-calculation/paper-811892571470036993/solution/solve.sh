#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/usr/bin/env bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_au_barriers.json ===
cat > "$OUTDIR/step_01_au_barriers.json" <<'JSONEOF'
{
  "impurity": "Au",
  "barrier_step1_2_eV": 0.07,
  "barrier_TS3_eV": 1.15,
  "delta_E_total_1_to_4_eV": -0.57
}
JSONEOF

# === solve block: step_02_co_barriers.json ===
cat > "$OUTDIR/step_02_co_barriers.json" <<'JSONEOF'
{
  "impurity": "Co",
  "barrier_step1_2_eV": 0.48,
  "barrier_TS3_eV": 1.15,
  "delta_E_total_1_to_4_eV": 0.45
}
JSONEOF
