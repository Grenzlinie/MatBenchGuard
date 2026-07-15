#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: Si_bands.json ===
cat > "$OUTDIR/Si_bands.json" <<'FFEOF'
{
  "Gamma_to_Gamma": 3.28,
  "Gamma_to_X": 1.31,
  "Gamma_to_L": 2.11,
  "L_to_X": -0.80,
  "Eg": 1.13
}
FFEOF

# === solve block: Ge_bands.json ===
cat > "$OUTDIR/Ge_bands.json" <<'FFEOF'
{
  "Gamma_to_Gamma": 0.85,
  "Gamma_to_X": 1.09,
  "Gamma_to_L": 0.73,
  "L_to_X": 0.36,
  "Eg": 0.73
}
FFEOF

# === solve block: GaAs_bands.json ===
cat > "$OUTDIR/GaAs_bands.json" <<'FFEOF'
{
  "Gamma_to_Gamma": 1.42,
  "Gamma_to_X": 1.95,
  "Gamma_to_L": 1.75,
  "L_to_X": 0.20,
  "X_to_X_splitting": 0.33
}
FFEOF

# === solve block: AlAs_bands.json ===
cat > "$OUTDIR/AlAs_bands.json" <<'FFEOF'
{
  "Gamma_to_Gamma": 2.93,
  "Gamma_to_X": 2.03,
  "Gamma_to_L": 2.91,
  "L_to_X": -0.88,
  "X_to_X_splitting": 1.07
}
FFEOF
