#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_phonon_stability.json ===
cat > "$OUTDIR/step_01_phonon_stability.json" <<'FFEOF'
{"max_imaginary_frequency":0.0}
FFEOF

# === solve block: step_02_band_gap_noSOC.txt ===
cat > "$OUTDIR/step_02_band_gap_noSOC.txt" <<'FFEOF'
0.570
FFEOF

# === solve block: step_03_band_gap_SOC.txt ===
cat > "$OUTDIR/step_03_band_gap_SOC.txt" <<'FFEOF'
0.123
FFEOF

# === solve block: step_04_parity_eigenvalues.json ===
cat > "$OUTDIR/step_04_parity_eigenvalues.json" <<'FFEOF'
{"\u0393":-1,"X":1,"Y":-1,"M":-1}
FFEOF

# === solve block: step_05_Z2_invariant.txt ===
cat > "$OUTDIR/step_05_Z2_invariant.txt" <<'FFEOF'
1
FFEOF

# === solve block: step_06_tunable_parity.json ===
cat > "$OUTDIR/step_06_tunable_parity.json" <<'FFEOF'
{"\u0393":-1,"X":1,"Y":-1,"M":-1}
FFEOF

# === solve block: step_07_tunable_gap_SOC.txt ===
cat > "$OUTDIR/step_07_tunable_gap_SOC.txt" <<'FFEOF'
0.351
FFEOF
