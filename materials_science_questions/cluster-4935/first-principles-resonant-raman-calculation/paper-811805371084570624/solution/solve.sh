#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: transitions.json ===
cat > "$OUTDIR/transitions.json" <<'JSONEOF'
[
  {
    "wavelength_nm": 262.0,
    "oscillator_strength": 0.0134
  },
  {
    "wavelength_nm": 261.0,
    "oscillator_strength": 0.0026
  },
  {
    "wavelength_nm": 240.0,
    "oscillator_strength": 0.2164
  }
]
JSONEOF

# === solve block: raman_data.csv ===
cat > "$OUTDIR/raman_data.csv" <<'CSVEOF'
wavelength_nm,mode_freq_cm1,relative_raman_activity,depolarization_ratio
900,706,1.0,0.02
600,706,1.25,0.05
400,706,2.8,0.10
300,706,8.5,0.15
280,706,29.3,0.20
260,706,19800.0,0.28
250,706,5200.0,0.31
240,706,21500.0,0.33
900,1025,1.0,0.03
600,1025,1.3,0.06
400,1025,3.1,0.11
300,1025,10.2,0.16
280,1025,31.5,0.21
260,1025,21000.0,0.28
250,1025,5600.0,0.31
240,1025,23000.0,0.33
900,1092,1.0,0.02
600,1092,1.28,0.05
400,1092,2.9,0.10
300,1092,9.8,0.15
280,1092,30.1,0.20
260,1092,20500.0,0.28
250,1092,5400.0,0.31
240,1092,22500.0,0.33
900,1626,1.0,0.03
600,1626,1.32,0.06
400,1626,3.3,0.11
300,1626,10.5,0.16
280,1626,30.8,0.20
260,1626,22000.0,0.32
250,1626,5800.0,0.29
240,1626,24000.0,0.33
CSVEOF
